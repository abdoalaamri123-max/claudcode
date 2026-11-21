/**
 * بوصلتك الداخلية — الأنشطة التفاعلية المباشرة.
 *
 * صفحة الطالب:   رابط تطبيق الويب كما هو (يمسحه الطلبة من رمز QR مرة واحدة).
 * لوحة المحاضر:  رابط تطبيق الويب + ?v=board&k=<ADMIN_KEY>
 *
 * المحاضر يفعّل النشاط من اللوحة، فتنتقل جوالات الطلبة إليه تلقائيًا.
 * الخطوات في ملف "طريقة-التشغيل.md".
 */

// غيّر هذا المفتاح قبل النشر (حروف إنجليزية وأرقام فقط).
const ADMIN_KEY = 'change-me';

const SHEET_NAME = 'answers';
const HEADER = ['time', 'session', 'activity', 'client', 'college', 'gender', 'data'];
const ACTS = ['jobs', 'discover', 'lead', 'help', 'exam', 'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'share', 'card'];
const HEARTBEAT_SECONDS = 75; // يُعدّ الجوال متصلًا إن سأل عن النشاط خلال هذه المدة
const COLLEGES = ['eng', 'it', 'bus', 'other'];
const GENDERS = ['m', 'f'];

/** شغّل هذه الدالة مرة واحدة من المحرّر: تنشئ جدول النتائج وتمنح الصلاحيات. */
function setup() {
  const sheet = getSheet_();
  const p = PropertiesService.getScriptProperties();
  if (!p.getProperty('SESSION')) newSession_();
  Logger.log('جدول النتائج: ' + sheet.getParent().getUrl());
}

function doGet(e) {
  const p = (e && e.parameter) || {};
  if (p.v === 'board') {
    if (p.k !== ADMIN_KEY) {
      return HtmlService.createHtmlOutput('<p dir="rtl" style="font-family:sans-serif;font-size:20px;padding:24px">رابط اللوحة يحتاج مفتاح المحاضر الصحيح.</p>');
    }
    const t = HtmlService.createTemplateFromFile('Board');
    t.studentUrl = ScriptApp.getService().getUrl();
    t.key = ADMIN_KEY;
    return t.evaluate()
      .setTitle('بوصلتك الداخلية · لوحة النتائج')
      .addMetaTag('viewport', 'width=device-width, initial-scale=1');
  }
  return HtmlService.createHtmlOutputFromFile('Student')
    .setTitle('بوصلتك الداخلية')
    .addMetaTag('viewport', 'width=device-width, initial-scale=1, maximum-scale=1');
}

/* ---------------- state ---------------- */

/** ما يسأل عنه جوال الطالب كل بضع ثوانٍ: النشاط المفعّل والجلسة. ويسجّل أن الجوال متصل. */
function getState(client) {
  if (validClient_(client)) CacheService.getScriptCache().put('hb:' + client, '1', HEARTBEAT_SECONDS);
  return state_();
}

/** أول ما يفعله جوال الطالب: يسجّل انضمامه إلى الجلسة مرة واحدة. */
function join(client) {
  if (!validClient_(client)) throw new Error('bad_client');
  const cache = CacheService.getScriptCache();
  const state = state_();
  cache.put('hb:' + client, '1', HEARTBEAT_SECONDS);
  const k = 'j:' + state.session + ':' + client;
  if (!cache.get(k)) {
    const sheet = getSheet_();
    const lock = LockService.getScriptLock();
    lock.waitLock(15000);
    try { sheet.appendRow([new Date(), state.session, 'join', client, '', '', '']); } finally { lock.releaseLock(); }
    cache.put(k, '1', 21600);
  }
  return state;
}

function validClient_(c) { return typeof c === 'string' && /^[A-Za-z0-9-]{8,40}$/.test(c); }

function state_() {
  const cache = CacheService.getScriptCache();
  const hit = cache.get('STATE');
  if (hit) return JSON.parse(hit);
  const p = PropertiesService.getScriptProperties();
  const state = { act: p.getProperty('ACT') || '', session: p.getProperty('SESSION') || '' };
  cache.put('STATE', JSON.stringify(state), 20);
  return state;
}

function setActivity(key, act) {
  checkKey_(key);
  if (act && ACTS.indexOf(act) < 0) throw new Error('bad_activity');
  PropertiesService.getScriptProperties().setProperty('ACT', act || '');
  CacheService.getScriptCache().remove('STATE');
  return state_();
}

function startNewSession(key) {
  checkKey_(key);
  newSession_();
  PropertiesService.getScriptProperties().setProperty('ACT', '');
  CacheService.getScriptCache().remove('STATE');
  return state_();
}

function newSession_() {
  const id = Utilities.formatDate(new Date(), 'Asia/Muscat', 'yyyyMMdd-HHmmss');
  PropertiesService.getScriptProperties().setProperty('SESSION', id);
  return id;
}

/* ---------------- answers ---------------- */

/** يستقبل إجابة طالب واحد في نشاط واحد. لا يُخزَّن أي اسم أو بريد. */
function submit(payload) {
  payload = payload || {};
  const act = String(payload.act || '');
  if (ACTS.indexOf(act) < 0) throw new Error('bad_activity');
  const client = String(payload.client || '');
  if (!validClient_(client)) throw new Error('bad_client');
  const data = validate_(act, payload.data);
  const college = act === 'discover' && COLLEGES.indexOf(payload.college) >= 0 ? payload.college : '';
  const gender = act === 'discover' && GENDERS.indexOf(payload.gender) >= 0 ? payload.gender : '';

  const session = state_().session || newSession_();
  const sheet = getSheet_();
  const lock = LockService.getScriptLock();
  lock.waitLock(15000);
  try {
    sheet.appendRow([new Date(), session, act, client, college, gender, data]);
  } finally {
    lock.releaseLock();
  }
  return { ok: true };
}

function validate_(act, d) {
  const isIdx = function (x) { return Number.isInteger(x) && x >= 0 && x <= 5; };
  switch (act) {
    case 'jobs':
      if (!/^[ab]$/.test(d)) throw new Error('bad_data');
      return d;
    case 'lead': case 'help': case 'exam':
      if (!/^[abc]$/.test(d)) throw new Error('bad_data');
      return d;
    case 'discover':
      if (!/^[abc]{12}$/.test(d)) throw new Error('bad_data');
      return d;
    case 'share':
      if (!d || !isIdx(d.v)) throw new Error('bad_data');
      return JSON.stringify({ v: d.v });
    case 'card':
      if (!d || !Array.isArray(d.top) || d.top.length !== 2 || !d.top.every(isIdx) || d.top[0] === d.top[1] || !isIdx(d.grow)) throw new Error('bad_data');
      return JSON.stringify({ top: d.top, grow: d.grow });
    case 'c1': case 'c2': case 'c3': case 'c4': case 'c5': case 'c6':
      if (!d || !Array.isArray(d.v) || d.v.length !== 2 || !d.v.every(isIdx) || d.v[0] === d.v[1]) throw new Error('bad_data');
      return JSON.stringify({ v: d.v.slice().sort() });
  }
  throw new Error('bad_activity');
}

/** للوحة المحاضر: عدد المنضمين والمتصلين، وآخر إجابة لكل جوال في النشاط المطلوب (إن طُلب). */
function getResults(key, act) {
  checkKey_(key);
  if (act && ACTS.indexOf(act) < 0) throw new Error('bad_activity');
  const state = state_();
  const sheet = getSheet_();
  const last = sheet.getLastRow();
  const rows = last < 2 ? [] : sheet.getRange(2, 1, last - 1, HEADER.length).getValues();
  const byClient = {}, joined = {};
  for (const r of rows) {
    if (String(r[1]) !== state.session) continue;
    const a = String(r[2]);
    if (a === 'join') { joined[String(r[3])] = 1; continue; }
    if (a !== act) continue;
    byClient[String(r[3])] = [String(r[4]), String(r[5]), String(r[6])];
    joined[String(r[3])] = 1;
  }
  const ids = Object.keys(joined);
  let online = 0;
  const cache = CacheService.getScriptCache();
  for (let i = 0; i < ids.length; i += 500) {
    online += Object.keys(cache.getAll(ids.slice(i, i + 500).map(function (c) { return 'hb:' + c; }))).length;
  }
  const out = Object.keys(byClient).map(function (k) { return byClient[k]; });
  return { session: state.session, act: state.act, rows: out, joined: ids.length, online: online, at: new Date().toISOString() };
}

function checkKey_(key) {
  if (key !== ADMIN_KEY) throw new Error('not_allowed');
}

function getSheet_() {
  const props = PropertiesService.getScriptProperties();
  const id = props.getProperty('SHEET_ID');
  let ss;
  if (id) {
    ss = SpreadsheetApp.openById(id);
  } else {
    ss = SpreadsheetApp.create('بوصلتك الداخلية · نتائج الأنشطة');
    props.setProperty('SHEET_ID', ss.getId());
  }
  let sheet = ss.getSheetByName(SHEET_NAME);
  if (!sheet) {
    sheet = ss.getSheets().length === 1 && ss.getSheets()[0].getLastRow() === 0 ? ss.getSheets()[0] : ss.insertSheet();
    sheet.setName(SHEET_NAME);
    sheet.appendRow(HEADER);
    sheet.setFrozenRows(1);
  }
  return sheet;
}
