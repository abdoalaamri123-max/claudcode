/**
 * بوصلتك الداخلية — جمع نتائج "اكتشف قيمك" مباشرة.
 *
 * صفحة الطالب:   رابط تطبيق الويب كما هو.
 * لوحة المحاضر:  رابط تطبيق الويب + ?v=board&k=<ADMIN_KEY>
 *
 * الخطوات في ملف "طريقة-التشغيل.md".
 */

// غيّر هذا المفتاح قبل النشر (حروف إنجليزية وأرقام فقط).
// من يعرفه يفتح لوحة النتائج ويبدأ جلسة جديدة.
const ADMIN_KEY = 'change-me';

const SHEET_NAME = 'responses';
const N_ITEMS = 12;
const COLLEGES = ['eng', 'it', 'bus', 'other'];
const GENDERS = ['m', 'f'];

/** شغّل هذه الدالة مرة واحدة من المحرّر: تنشئ جدول النتائج وتمنح الصلاحيات. */
function setup() {
  const sheet = getSheet_();
  if (!PropertiesService.getScriptProperties().getProperty('SESSION')) newSession_();
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
    .setTitle('اكتشف قيمك')
    .addMetaTag('viewport', 'width=device-width, initial-scale=1, maximum-scale=1');
}

/** يستقبل إجابات طالب واحد. لا يُخزَّن أي اسم أو بريد. */
function submit(payload) {
  const answers = String((payload && payload.answers) || '');
  if (!new RegExp('^[abc]{' + N_ITEMS + '}$').test(answers)) throw new Error('bad_answers');
  const college = COLLEGES.indexOf(payload.college) >= 0 ? payload.college : '';
  const gender = GENDERS.indexOf(payload.gender) >= 0 ? payload.gender : '';

  const sheet = getSheet_();
  const session = PropertiesService.getScriptProperties().getProperty('SESSION') || newSession_();
  const lock = LockService.getScriptLock();
  lock.waitLock(15000);
  try {
    sheet.appendRow([new Date(), session, college, gender, answers]);
  } finally {
    lock.releaseLock();
  }
  return { ok: true };
}

/** للوحة المحاضر: إجابات الجلسة الحالية فقط. */
function getResults(key) {
  checkKey_(key);
  const session = PropertiesService.getScriptProperties().getProperty('SESSION') || '';
  const sheet = getSheet_();
  const last = sheet.getLastRow();
  const rows = last < 2 ? [] : sheet.getRange(2, 1, last - 1, 5).getValues();
  const out = [];
  for (const r of rows) {
    if (String(r[1]) !== session) continue;
    const a = String(r[4]);
    if (a.length !== N_ITEMS) continue;
    out.push([String(r[2]), String(r[3]), a]);
  }
  return { session: session, rows: out, at: new Date().toISOString() };
}

/** يبدأ جلسة جديدة دون حذف أي صف: اللوحة تعرض الجلسة الحالية وحدها. */
function startNewSession(key) {
  checkKey_(key);
  return newSession_();
}

function newSession_() {
  const id = Utilities.formatDate(new Date(), 'Asia/Muscat', 'yyyyMMdd-HHmmss');
  PropertiesService.getScriptProperties().setProperty('SESSION', id);
  return id;
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
    ss = SpreadsheetApp.create('بوصلتك الداخلية · نتائج اكتشف قيمك');
    props.setProperty('SHEET_ID', ss.getId());
    const first = ss.getSheets()[0];
    first.setName(SHEET_NAME);
    first.appendRow(['time', 'session', 'college', 'gender', 'answers']);
    first.setFrozenRows(1);
  }
  return ss.getSheetByName(SHEET_NAME);
}
