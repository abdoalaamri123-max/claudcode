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
