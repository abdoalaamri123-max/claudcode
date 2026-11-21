"""Replace flex `row-reverse` with `row` + `justify-content:flex-end` and reverse the children in the file.

The Slides editor does not store row-reverse: it reorders children and packs them to the left.
Writing the children in visual (left-to-right) order with flex-end gives the same picture in the
browser and keeps right-aligned rows on the right in the editor.

Usage: python3 derev.py <slides-dir> [--check]
"""
import os, re, sys

CLASSES = {'row', 'eb', 'band', 'opt', 'bar-row', 'key', 'trow', 'prog'}
VOID = {'br', 'img', 'hr', 'input', 'meta', 'link', 'source', 'wbr'}
TOKEN = re.compile(r'<!--.*?-->|<(/?)([a-zA-Z][\w:-]*)((?:[^>"\']|"[^"]*"|\'[^\']*\')*?)(/?)>', re.S)


class El:
    def __init__(self, name, start):
        self.name, self.start, self.kids, self.end = name, start, [], ''


def parse(src):
    root = El('#root', '')
    stack, pos = [root], 0
    for m in TOKEN.finditer(src):
        if m.start() > pos:
            stack[-1].kids.append(src[pos:m.start()])
        tok = m.group(0)
        pos = m.end()
        if tok.startswith('<!--'):
            stack[-1].kids.append(tok)
            continue
        closing, name, selfclose = m.group(1), m.group(2).lower(), m.group(4)
        if closing:
            while len(stack) > 1 and stack[-1].name != name:
                stack.pop()  # tolerate unclosed tags
            if len(stack) > 1:
                stack[-1].end = tok
                stack.pop()
            continue
        el = El(name, tok)
        stack[-1].kids.append(el)
        if not selfclose and name not in VOID:
            stack.append(el)
    if pos < len(src):
        stack[-1].kids.append(src[pos:])
    return root


def ser(n):
    if isinstance(n, str):
        return n
    return n.start + ''.join(ser(k) for k in n.kids) + n.end


def classes(start):
    m = re.search(r'\sclass="([^"]*)"', start)
    return set(m.group(1).split()) if m else set()


def style(start):
    m = re.search(r'\sstyle="([^"]*)"', start)
    return m.group(1) if m else ''


changed = []


def fix(n):
    if isinstance(n, str):
        return
    for k in n.kids:
        fix(k)
    st = style(n.start)
    inline_rev = re.search(r'flex-direction\s*:\s*row-reverse', st)
    by_class = bool(classes(n.start) & CLASSES) and not re.search(r'flex-direction\s*:', st)
    if not (inline_rev or by_class):
        return
    elems = [k for k in n.kids if not isinstance(k, str)]
    texts = [k for k in n.kids if isinstance(k, str) and k.strip() and not k.strip().startswith('<!--')]
    if texts:
        raise SystemExit('text directly inside a reversed row: %r in %s' % (texts[0][:40], n.start[:80]))
    if len(elems) > 1:
        # keep the whitespace pattern, reverse only the element order
        it = iter(reversed(elems))
        n.kids = [next(it) if not isinstance(k, str) else k for k in n.kids]
    if inline_rev:
        new = re.sub(r'flex-direction\s*:\s*row-reverse', 'flex-direction:row', st)
        if not re.search(r'justify-content\s*:', new):
            new = new.rstrip('; ') + '; justify-content:flex-end'
        n.start = n.start.replace('style="%s"' % st, 'style="%s"' % new, 1)
    changed.append(n.start[:60])


def main():
    d = sys.argv[1]
    total = 0
    for f in sorted(os.listdir(d)):
        if not f.endswith('.html'):
            continue
        p = os.path.join(d, f)
        src = open(p, encoding='utf-8').read()
        tree = parse(src)
        assert ser(tree) == src, 'round trip failed for ' + f
        changed.clear()
        fix(tree)
        out = ser(tree)
        total += len(changed)
        if out != src and '--check' not in sys.argv:
            open(p, 'w', encoding='utf-8').write(out)
        print('%-18s %d rows' % (f, len(changed)))
    print('total', total)


main()
