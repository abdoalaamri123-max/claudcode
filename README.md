# مهارات البحث العلمي والتحليل الإحصائي لـ Claude Code

مهارات مجانية مفتوحة المصدر (رخصة MIT) منسوخة من GitHub إلى `.claude/skills/`، وتُحمَّل تلقائياً عند فتح هذا المستودع في Claude Code.

## تحليل الاستبانات والمقاييس (التربية / علم النفس / القياس)
| المهارة | الوصف | المصدر |
|---|---|---|
| `questionnaire-analysis` | الصدق والثبات (α، CR، AVE)، EFA/CFA، SEM، الوساطة والتعديل، تقارير APA — SPSS/AMOS/R | [maydengximin-sketch/questionnaire-analysis-skill](https://github.com/maydengximin-sketch/questionnaire-analysis-skill) |
| `statistical-consultant` | مستشار إحصائي: فحص جودة البيانات والافتراضات واختيار الاختبار وكتابة النتائج | [TerryFYL/claude-statistical-analysis-skill](https://github.com/TerryFYL/claude-statistical-analysis-skill) |

## التحليل الإحصائي — من [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills)
| المهارة | الوصف |
|---|---|
| `statistical-analysis` | اختيار الاختبار، فحص الافتراضات، أحجام الأثر، التقرير |
| `statistical-power` | حساب حجم العينة والقوة الإحصائية |
| `experimental-design` | تصميم التجارب والدراسات قبل جمع البيانات |
| `exploratory-data-analysis` | التحليل الاستكشافي للبيانات |
| `statsmodels` | الانحدار OLS/GLM، النماذج المختلطة، ARIMA |
| `pymc` | الإحصاء البايزي والنماذج الهرمية |
| `scikit-survival` | تحليل البقاء |
| `scikit-learn` | تعلّم الآلة |
| `seaborn`، `scientific-visualization` | رسوم بيانية إحصائية جاهزة للنشر |

## البحث العلمي والكتابة — من K-Dense-AI
| المهارة | الوصف |
|---|---|
| `literature-review` | مراجعات منهجية ونطاقية وسردية |
| `citation-management` | إدارة المراجع (OpenAlex، PubMed، Google Scholar) |
| `research-lookup` | جمع الأدلة العلمية الحديثة |
| `hypothesis-generation` | صياغة الأسئلة والفرضيات |
| `scientific-writing` | كتابة المخطوطات العلمية ومراجعتها |
| `scientific-critical-thinking` | تقييم الادعاءات وجودة الأدلة |
| `peer-review` | إعداد تقارير التحكيم |

## ملاحظات
- كل مهارة تحتفظ بملف رخصتها الأصلي (MIT).
- غُيّر اسم مهارة TerryFYL إلى `statistical-consultant` لتجنّب التعارض مع `statistical-analysis`.
- بعض المهارات تحتاج حزم Python أو R (مثل statsmodels وpymc وlavaan) مثبّتة لتنفيذ التحليل.

---

# مهارات الوصول إلى المجلات والبحوث العلمية

## Google Scholar — من [cookjohn/gs-skills](https://github.com/cookjohn/gs-skills) (MIT)
تعمل عبر متصفح Chrome (أداة chrome-devtools MCP).
| المهارة | الوصف |
|---|---|
| `gs-search` | البحث في Google Scholar |
| `gs-advanced-search` | بحث متقدم (مؤلف، مجلة، سنوات) |
| `gs-cited-by` | تتبّع الأبحاث التي استشهدت بورقة |
| `gs-fulltext` | روابط النص الكامل (PDF، DOI، Unpaywall) — **استُبدلت روابط Sci-Hub بـ Unpaywall** |
| `gs-export` | تصدير المراجع إلى Zotero / BibTeX |
| `gs-navigate-pages` | التنقّل بين صفحات النتائج |

## Semantic Scholar
| المهارة | الوصف | المصدر |
|---|---|---|
| `s2-cli` | الاستشهادات والمراجع والبحث في أكثر من 200 مليون ورقة | [huggingface/s2-cli](https://github.com/huggingface/s2-cli) (Apache-2.0) |
| `s2-paper-triage`، `s2-trace-citations`، `s2-expand-references` | فرز الأوراق وتتبّع شبكة الاستشهادات | [zongmin-yu/semantic-scholar-skills](https://github.com/zongmin-yu/semantic-scholar-skills) (MIT) |

## arXiv
| المهارة | الوصف | المصدر |
|---|---|---|
| `arxiv-mcp-server` | بحث وقراءة أوراق arXiv (تحتاج خادم MCP، انظر أدناه) | [blazickjp/arxiv-mcp-server](https://github.com/blazickjp/arxiv-mcp-server) (Apache-2.0) |

## البحث متعدد المصادر (Scopus، Web of Science، OpenAlex، Crossref، PubMed...)
| المهارة | المصادر | المصدر |
|---|---|---|
| `thesis-retrieval` | OpenAlex، CrossRef، Semantic Scholar، PubMed، **Scopus**، **Web of Science** + فلترة حسب الربع | [Xun477/thesis-retrieval](https://github.com/Xun477/thesis-retrieval) (MIT) |
| `paper-search-pro` | OpenAlex، Semantic Scholar، CrossRef، PubMed، arXiv، OpenReview + تصدير استراتيجيات بحث لـ Scopus/WoS | [O0000-code/paper-search-pro](https://github.com/O0000-code/paper-search-pro) (Apache-2.0) |
| `paper-search` | arXiv، Semantic Scholar، Google Scholar، IEEE، PubMed، WoS + قاعدة JCR | [TCMzhoutong/paper-search](https://github.com/TCMzhoutong/paper-search) (MIT) |
| `nature-academic-search` | CrossRef، PubMed، arXiv، OpenAlex، ClinicalTrials + التحقق من المراجع | [wp-a/nature-academic-search](https://github.com/wp-a/nature-academic-search) (MIT) |
| `paper-lookup` | 18 واجهة: PubMed، OpenAlex، Crossref، CORE، DOAJ، Unpaywall... | K-Dense-AI (MIT) |
| `database-lookup` | قواعد بيانات علمية عامة | K-Dense-AI (MIT) |

## المجلات والتحميل القانوني والمراجع
| المهارة | الوصف | المصدر |
|---|---|---|
| `journal-finder` | اقتراح مجلات مع التحقق من الفهرسة والربع (JCR) والرسوم | [utkugrhn-source/journal-finder-skill](https://github.com/utkugrhn-source/journal-finder-skill) (MIT) |
| `venue-templates` | قوالب المجلات والمؤتمرات | K-Dense-AI (MIT) |
| `paper-download` | تحميل PDF بالـ DOI من مصادر الوصول المفتوح أولاً | [jxtse/auto-paper-harvester](https://github.com/jxtse/auto-paper-harvester) (MIT) |
| `pyzotero` | إدارة مكتبة Zotero | K-Dense-AI (MIT) |

## خوادم MCP اختيارية (تُضاف يدوياً)
```bash
claude mcp add arxiv -- uvx arxiv-mcp-server
```
```bash
claude mcp add scopus -e SCOPUS_API_KEY=مفتاحك -- uvx scopus-mcp
```
مفتاح Scopus مجاني من https://dev.elsevier.com ويعمل كاملاً من شبكة جامعة مشتركة في Scopus.

## مفاتيح API (اختيارية ومجانية)
| المتغير | الجهة |
|---|---|
| `SCOPUS_API_KEY` | Elsevier Developer Portal |
| `S2_API_KEY` | Semantic Scholar API |
| `WOS_API_KEY` | Clarivate Developer Portal (Web of Science Starter API) |

## مهارات لم تُنسخ
- [cookjohn/wos-skills](https://github.com/cookjohn/wos-skills) — Web of Science عبر المتصفح: **بدون رخصة** فلا يجوز نسخها؛ يمكنك تثبيتها بنفسك.
- [saidsurucu/literature-review-skills](https://github.com/saidsurucu/literature-review-skills) — 21 مصدراً عبر Chrome: **بدون رخصة**.
- استُبعدت المهارات المعتمدة على Sci-Hub لأنها تنتهك حقوق النشر.

---

# خريطة الطريق: من الفكرة إلى النشر في مجلة Scopus Q1

كل مرحلة مع المهارات المتاحة في هذا المستودع. الأسماء بين `` هي أسماء المهارات في `.claude/skills/`.

| # | المرحلة | المهارات |
|---|---|---|
| 1 | **اختيار الموضوع والفجوة البحثية** | `research-gap-finder`، `idea-novelty-auditor`، `hypothesis-generation`، `scientific-critical-thinking` |
| 2 | **البحث في قواعد البيانات** (Scopus، WoS، Scholar، arXiv) | `thesis-retrieval`، `paper-search-pro`، `paper-search`، `paper-lookup`، `gs-search`، `gs-advanced-search`، `gs-cited-by`، `s2-trace-citations`، `arxiv-mcp-server` |
| 3 | **مراجعة الأدبيات** | `literature-review`، `problem-driven-literature-review`، `read-paper-to-notes`، `systematic-review` (PRISMA 2020)، `meta-analysis-systematic-review` |
| 4 | **تصميم الدراسة والمنهجية** | `experimental-design`، `statistical-power` (حجم العينة)، `paper-strategist` |
| 5 | **جمع البيانات وتحليلها** | `questionnaire-analysis`، `statistical-consultant`، `statistical-analysis`، `statsmodels`، `pymc`، `exploratory-data-analysis`، `statistical-rigor-helper` |
| 6 | **الجداول والأشكال** | `scientific-visualization`، `seaborn`، `table-checker`، `figure-checker`، `graphical-abstract` |
| 7 | **كتابة المخطوطة** (IMRaD) | `paper-writing`، `paper-composer`، `scientific-writing`، `paper-argument-reconstructor`، `experiment-section-auditor` |
| 8 | **التدقيق اللغوي والمراجع** | `paper-polisher`، `manuscript-copyeditor`، `citation-auditor`، `citation-management`، `pyzotero`، `gs-export` |
| 9 | **إرشادات التقارير** | `guideline-select` (يختار الإرشاد المناسب)، `consort-check`، `prisma-check`، `strobe-check`، `stard-check`، `tripod-check`، `spirit-check`، `care-check`، `arrive-check`، `qualitative-check`، `checklist-check`، `flow-diagram` |
| 10 | **اختيار المجلة** (Q1، النطاق، الفهرسة) | `journal-finder`، `journal-selector`، `journal-scope-review`، `presubmission-inquiry` |
| 11 | **التحكيم الذاتي قبل الإرسال** | `paper-redteam` (يحاكي "المحكّم رقم 2")، `review-simulator`، `peer-review-check`، `peer-review`، `submission-screener` |
| 12 | **تجهيز الإرسال** | `journal-reformatter`، `venue-templates`، `journal-submission-checklist`، `cover-letter`، `cover-letter-writer`، `authorship-credit` (CRediT)، `reviewer-recommender` |
| 13 | **الرد على المحكّمين** | `reviewer-response-rebuttal`، `write-response-letter`، `revision-responder` |
| 14 | **بعد القبول** | `proof-checker`، `post-publication-corrector`، `research-disseminator` |

## مصادر المهارات الجديدة
| المستودع | الرخصة | المهارات |
|---|---|---|
| [yaotingsun/academic-publishing-skills](https://github.com/yaotingsun/academic-publishing-skills) | Apache-2.0 | 18 مهارة لدورة النشر (اختيار المجلة، خطاب التغطية، الرد على المحكّمين، البروفات...) |
| [JointTex/reporting-guidelines](https://github.com/JointTex/reporting-guidelines) | MIT | 12 مهارة لإرشادات CONSORT وPRISMA وSTROBE وغيرها |
| [yujie-jason-zhang/polish_skill](https://github.com/yujie-jason-zhang/polish_skill) | MIT | الأصالة، المراجعة الموجّهة بالمشكلة، التدقيق، قراءة الأوراق |
| [LengFeng00/research-gap-finder](https://github.com/LengFeng00/research-gap-finder) | MIT | الفجوة البحثية |
| [AngelChen-HC/systematic-review-skill](https://github.com/AngelChen-HC/systematic-review-skill) | Apache-2.0 | المراجعة المنهجية PRISMA 2020 |
| [maydengximin-sketch](https://github.com/maydengximin-sketch) | MIT | التحليل البعدي، الرد على المحكّمين |
| [lishix520/academic-paper-skills](https://github.com/lishix520/academic-paper-skills) | MIT | تخطيط الورقة وكتابتها |
| [SNL-UCSB/paper-writing-skill](https://github.com/SNL-UCSB/paper-writing-skill) | MIT | مبادئ تحرير كل قسم |
| [xf686/Meet-Reviewer-2](https://github.com/xf686/Meet-Reviewer-2) | MIT | التحكيم الذاتي العدائي |
| [narcoco/peer-review-check](https://github.com/narcoco/peer-review-check) | MIT | فحص ذاتي وفق معايير Elsevier |
| [CaoYongshengcys/journal-scope-review](https://github.com/CaoYongshengcys/journal-scope-review) | MIT | توافق المخطوطة مع نطاق المجلة |
| [jiahanwang0411/cover-letter-skill](https://github.com/jiahanwang0411/cover-letter-skill) | MIT | خطاب التغطية (وفق إرشادات Wiley) |
| [meiling-huang/write-response-letter](https://github.com/meiling-huang/write-response-letter) | MIT | خطاب الرد على المحكّمين |
| [LightFury333/graphical-abstract-skill](https://github.com/LightFury333/graphical-abstract-skill) | MIT | الملخص الرسومي |

## أدوات مفيدة لم تُنسخ
- [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) (57 ألف نجمة): مسار كامل بحث ← كتابة ← تحكيم ← مراجعة. رخصتها **CC BY-NC 4.0** (غير تجارية) وتعتمد على بنية مشتركة كبيرة، فالأفضل تثبيتها كإضافة من مستودعها مباشرة.
- **كشف المجلات المفترسة (Predatory):** [sustainet-guardian/aletheia-probe](https://github.com/sustainet-guardian/aletheia-probe) و[stop-predatory-journals](https://github.com/stop-predatory-journals/stop-predatory-journals.github.io). وتحقّق دائماً من فهرسة المجلة وربعها مباشرة في Scopus Sources وSCImago (SJR).

## تنبيه مهم
هذه المهارات تساعد في التخطيط والتحليل والصياغة والتدقيق، لكنها لا تغني عن جهد الباحث وأمانته العلمية: تحقّق من كل مرجع ورقم، واتّبع سياسة المجلة في الإفصاح عن استخدام الذكاء الاصطناعي.
