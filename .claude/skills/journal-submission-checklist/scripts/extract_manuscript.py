#!/usr/bin/env python3
"""Extract plain text from a manuscript for checklist assessment.

Supports: .pdf, .docx, .txt, .md. Prints text to stdout.
Usage: python extract_manuscript.py <path> [--max-chars N]

Install deps on first use if missing:
    pip install pdfplumber python-docx --break-system-packages
"""
import sys, argparse, os

def from_pdf(path):
    try:
        import pdfplumber
    except ImportError:
        os.system("pip install pdfplumber --break-system-packages -q")
        import pdfplumber
    out = []
    n_pages = 0
    with pdfplumber.open(path) as pdf:
        n_pages = len(pdf.pages)
        for i, page in enumerate(pdf.pages, 1):
            out.append(f"\n----- page {i} -----\n")
            out.append(page.extract_text() or "")
    text = "\n".join(out)
    # Scanned/image-only PDFs return almost no extractable text. Warn (non-fatal) so the
    # caller knows the assessment would be empty and OCR is needed, rather than silently
    # producing a report that flags everything as missing.
    body = text.replace("----- page", "").strip()
    if n_pages and len(body) < 100 * n_pages:
        sys.stderr.write(
            "WARNING: very little text extracted from this PDF "
            f"(~{len(body)} chars over {n_pages} page(s)). It may be scanned or image-only. "
            "Run OCR first (e.g. `ocrmypdf in.pdf out.pdf`) or supply a text/docx version, "
            "otherwise the checklist assessment will have nothing to read.\n"
        )
    return text

def from_docx(path):
    try:
        from docx import Document
    except ImportError:
        os.system("pip install python-docx --break-system-packages -q")
        from docx import Document
    doc = Document(path)
    parts = [p.text for p in doc.paragraphs]
    for tbl in doc.tables:
        for row in tbl.rows:
            parts.append(" | ".join(c.text for c in row.cells))
    return "\n".join(parts)

def from_text(path):
    with open(path, encoding="utf-8", errors="ignore") as f:
        return f.read()

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("path")
    ap.add_argument("--max-chars", type=int, default=0,
                    help="truncate output to this many chars (0 = no limit)")
    args = ap.parse_args()
    ext = os.path.splitext(args.path)[1].lower()
    if ext == ".pdf":
        text = from_pdf(args.path)
    elif ext == ".docx":
        text = from_docx(args.path)
    elif ext in (".txt", ".md", ".markdown"):
        text = from_text(args.path)
    else:
        sys.exit(f"Unsupported extension: {ext}. Use pdf/docx/txt/md.")
    if args.max_chars and len(text) > args.max_chars:
        text = text[:args.max_chars] + f"\n...[truncated at {args.max_chars} chars]..."
    sys.stdout.write(text)

if __name__ == "__main__":
    main()
