# تعليمات دائمة لهذا المستودع

المستخدم باحث يريد النشر في مجلات محكّمة مصنّفة Scopus Q1. يحتوي `.claude/skills/` على نحو 89 مهارة للبحث العلمي والتحليل الإحصائي والنشر. خريطة المراحل كاملة في `README.md`.

## كيف تعمل في كل محادثة
- حدّد المرحلة التي يطلبها المستخدم، ثم حمّل المهارة المناسبة بأداة Skill قبل أن تبدأ العمل، حتى لو لم يذكر المستخدم اسم المهارة. وإذا احتاجت المهمة أكثر من مهارة فاستخدمها بالتتابع.
- أخبر المستخدم في سطر واحد بالمهارة التي استخدمتها.
- ردّ بالعربية ما لم يطلب المستخدم لغة أخرى. اكتب النصوص المعدّة للنشر بالإنجليزية الأكاديمية إلا إذا طُلب غير ذلك.

## اختيار المهارة حسب المهمة
| المهمة | المهارات |
|---|---|
| فكرة أو موضوع أو فجوة بحثية | `research-gap-finder`، `idea-novelty-auditor`، `hypothesis-generation` |
| البحث عن أوراق (Scopus، WoS، Scholar، arXiv) | `thesis-retrieval`، `paper-search-pro`، `paper-lookup`، `gs-search`، `gs-cited-by`، `s2-trace-citations` |
| مراجعة الأدبيات أو مراجعة منهجية أو تحليل بعدي | `literature-review`، `problem-driven-literature-review`، `systematic-review`، `meta-analysis-systematic-review` |
| قراءة ورقة وتلخيصها | `read-paper-to-notes` |
| تصميم الدراسة وحجم العينة | `experimental-design`، `statistical-power` |
| استبانات ومقاييس (الصدق، الثبات، EFA، CFA، SEM) | `questionnaire-analysis` |
| تحليل إحصائي عام | `statistical-consultant`، `statistical-analysis`، `statistical-rigor-helper`، `statsmodels`، `pymc` |
| الرسوم البيانية والجداول | `scientific-visualization`، `seaborn`، `table-checker`، `figure-checker`، `graphical-abstract` |
| كتابة المخطوطة | `paper-writing`، `scientific-writing`، `paper-argument-reconstructor` |
| التدقيق اللغوي | `manuscript-copyeditor`، `paper-polisher` |
| المراجع والاستشهادات | `citation-auditor`، `citation-management`، `pyzotero` |
| إرشادات كتابة التقارير | `guideline-select`، ثم `*-check` المناسبة |
| اختيار المجلة | `journal-finder`، `journal-selector`، `journal-scope-review` |
| فحص المخطوطة قبل الإرسال | `submission-screener`، `review-simulator`، `peer-review-check`، `paper-redteam` |
| تجهيز الإرسال | `cover-letter-writer`، `journal-reformatter`، `journal-submission-checklist`، `authorship-credit`، `reviewer-recommender` |
| الرد على المحكّمين | `revision-responder`، `reviewer-response-rebuttal`، `write-response-letter` |
| بعد القبول | `proof-checker`، `research-disseminator`، `post-publication-corrector` |
| ترجمة نص بحثي عربي إلى الإنجليزية | `anthropic-skills:arabic-research-translation` |

## قواعد النزاهة
- لا تخترع مراجع أو بيانات أو نتائج أو أسماء محررين. تحقّق من كل مرجع عبر قواعد البيانات.
- لا تستخدم Sci-Hub ولا أي مصدر يخالف حقوق النشر. استخدم الوصول المفتوح (Unpaywall، OpenAlex) أو اشتراك جامعة المستخدم.
- تحقّق من فهرسة المجلة وربعها من Scopus Sources أو SCImago، ونبّه المستخدم إلى المجلات المفترسة.
- ذكّر المستخدم بسياسة المجلة في الإفصاح عن استخدام الذكاء الاصطناعي.
