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
const ACTS = ['jobs', 'discover', 'lead', 'help', 'exam', 'conflict', 'share', 'card'];
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

/** ما يسأل عنه جوال الطالب كل بضع ثوانٍ: النشاط المفعّل والجلسة. */
function getState() {
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
  return getState();
}

function startNewSession(key) {
  checkKey_(key);
  newSession_();
  PropertiesService.getScriptProperties().setProperty('ACT', '');
  CacheService.getScriptCache().remove('STATE');
  return getState();
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
  if (!/^[A-Za-z0-9-]{8,40}$/.test(client)) throw new Error('bad_client');
  const data = validate_(act, payload.data);
  const college = act === 'discover' && COLLEGES.indexOf(payload.college) >= 0 ? payload.college : '';
  const gender = act === 'discover' && GENDERS.indexOf(payload.gender) >= 0 ? payload.gender : '';

  const session = getState().session || newSession_();
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
    case 'conflict': {
      if (!d || !Number.isInteger(d.c) || d.c < 1 || d.c > 6) throw new Error('bad_data');
      if (!Array.isArray(d.v) || d.v.length !== 2 || !d.v.every(isIdx) || d.v[0] === d.v[1]) throw new Error('bad_data');
      if (d.v.indexOf(d.p) < 0) throw new Error('bad_data');
      const t = String(d.t || '').replace(/[\u0000-\u001F\u007F]/g, ' ').replace(/\s+/g, ' ').trim().slice(0, 140);
      return JSON.stringify({ c: d.c, v: d.v, p: d.p, t: t });
    }
  }
  throw new Error('bad_activity');
}

/** للوحة المحاضر: آخر إجابة لكل جوال في نشاط واحد من الجلسة الحالية. */
function getResults(key, act) {
  checkKey_(key);
  if (ACTS.indexOf(act) < 0) throw new Error('bad_activity');
  const state = getState();
  const sheet = getSheet_();
  const last = sheet.getLastRow();
  const rows = last < 2 ? [] : sheet.getRange(2, 1, last - 1, HEADER.length).getValues();
  const byClient = {};
  for (const r of rows) {
    if (String(r[1]) !== state.session || String(r[2]) !== act) continue;
    byClient[String(r[3])] = [String(r[4]), String(r[5]), String(r[6])];
  }
  const out = Object.keys(byClient).map(function (k) { return byClient[k]; });
  return { session: state.session, act: state.act, rows: out, at: new Date().toISOString() };
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
