"""Builds bosla-single.gs: one Apps Script file that holds the server code and both pages.

Edit Code.gs, Student.html and Board.html, then run:  python3 build_single.py
"""
import json
import pathlib

here = pathlib.Path(__file__).parent
code = (here / 'Code.gs').read_text(encoding='utf-8')
student = (here / 'Student.html').read_text(encoding='utf-8')
board = (here / 'Board.html').read_text(encoding='utf-8')

URL_SLOT = '<?!= JSON.stringify(studentUrl) ?>'
KEY_SLOT = '<?!= JSON.stringify(key) ?>'
assert URL_SLOT in board and KEY_SLOT in board

old_board = """    const t = HtmlService.createTemplateFromFile('Board');
    t.studentUrl = ScriptApp.getService().getUrl();
    t.key = ADMIN_KEY;
    return t.evaluate()"""
new_board = """    const html = BOARD_HTML
      .replace(BOARD_URL_SLOT, JSON.stringify(ScriptApp.getService().getUrl()))
      .replace(BOARD_KEY_SLOT, JSON.stringify(ADMIN_KEY));
    return HtmlService.createHtmlOutput(html)"""
old_student = "  return HtmlService.createHtmlOutputFromFile('Student')"
new_student = "  return HtmlService.createHtmlOutput(STUDENT_HTML)"
assert old_board in code and old_student in code
code = code.replace(old_board, new_board).replace(old_student, new_student)

header = """/**
 * ملف واحد: الصقه وحده في Code.gs داخل مشروع Apps Script جديد، ولا تحتاج إلى ملفات HTML.
 * (مولَّد آليًا من Code.gs وStudent.html وBoard.html بالأمر: python3 build_single.py)
 */

"""
pages = (
    "\n\n/* ================= الصفحتان (لا تعدّل ما تحت هذا السطر يدويًا) ================= */\n\n"
    f"const BOARD_URL_SLOT = {json.dumps(URL_SLOT)};\n"
    f"const BOARD_KEY_SLOT = {json.dumps(KEY_SLOT)};\n"
    f"const STUDENT_HTML = {json.dumps(student, ensure_ascii=False)};\n"
    f"const BOARD_HTML = {json.dumps(board, ensure_ascii=False)};\n"
)
(here / 'bosla-single.gs').write_text(header + code + pages, encoding='utf-8')
print('bosla-single.gs', len(header + code + pages), 'chars')
