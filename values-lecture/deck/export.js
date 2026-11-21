// Export the deck to a PDF with the real fonts embedded (Tajawal, Reem Kufi, Amiri).
// Usage: node export.js <deckRoot> <out.pdf> <fonts.css> <lucideIconsDir> [slideIndexesToScreenshot] [shotDir]
const {chromium} = require('/opt/node-tools/node_modules/playwright');
const fs = require('fs'), path = require('path');
const [root, out, fontsCss, iconsDir, shots, shotDir] = process.argv.slice(2);
const deck = JSON.parse(fs.readFileSync(root + '/project/deck.json', 'utf8'));
const ICON = {Book: 'book', Chart: 'chart-column', Globe: 'globe', GraduationCap: 'graduation-cap', Home: 'house', Lightbulb: 'lightbulb', Star: 'star', Trust: 'handshake', Users: 'users'};
const icon = n => fs.readFileSync(path.join(iconsDir, ICON[n] + '.svg'), 'utf8')
  .replace(/<!--[\s\S]*?-->/g, '').replace('width="24"', 'width="100%"').replace('height="24"', 'height="100%"');
const base = [
  '* { margin: 0 } body { font: 32px/1.2 sans-serif; background: #fff }',
  'body > section { width: 1920px !important; height: 1080px !important; overflow: hidden !important; box-sizing: border-box !important; position: relative; isolation: isolate; break-after: page }',
  'aside { display: none !important } h1 { font-size: 96px; font-weight: 600 } h2 { font-size: 64px; font-weight: 600 } h3 { font-size: 44px; font-weight: 600 }',
  'p, li, h1, h2, h3 { overflow-wrap: break-word; text-wrap: pretty } x-shape, x-icon { display: block }',
  'x-shape[kind="diamond"] { clip-path: polygon(50% 0, 100% 50%, 50% 100%, 0 50%) } x-shape[kind="ellipse"] { border-radius: 50% }',
  'x-icon svg { width: 100%; height: 100%; display: block }',
  '.fragment { opacity: 1 !important } section { direction: ltr !important }',
  '*, *::before, *::after { animation-duration: 0s !important; animation-delay: 0s !important; transition: none !important }',
  '@page { size: 1920px 1080px; margin: 0 }'
].join('\n');
let html = '<!doctype html><html><head><meta charset="utf-8"><style>' + fs.readFileSync(fontsCss, 'utf8') + base +
  '</style><style>' + fs.readFileSync(root + '/project/deck.css', 'utf8') + '</style></head><body>';
for (const id of deck.order) {
  html += fs.readFileSync(path.join(root, 'project/slides', id + '.html'), 'utf8')
    .replace(/<x-icon name="([A-Za-z]+)"([^>]*)><\/x-icon>/g, (m, n, a) => '<x-icon name="' + n + '"' + a + '>' + icon(n) + '</x-icon>');
}
html += '</body></html>';
(async () => {
  const b = await chromium.launch();
  const pg = await b.newPage({viewport: {width: 1920, height: 1080}});
  await pg.setContent(html, {waitUntil: 'load'});
  await pg.evaluate(() => document.fonts.ready);
  const missing = await pg.evaluate(() => ['Tajawal', 'Reem Kufi', 'Amiri'].filter(f => !document.fonts.check('700 40px "' + f + '"', 'قيم')));
  console.log('slides', deck.order.length, 'fonts not loaded:', JSON.stringify(missing));
  await pg.pdf({path: out, width: '1920px', height: '1080px', printBackground: true});
  if (shots) {
    const secs = await pg.$$('body > section');
    for (const i of shots.split(',').map(Number)) await secs[i].screenshot({path: shotDir + '/x' + i + '.png'});
  }
  await b.close();
})();
