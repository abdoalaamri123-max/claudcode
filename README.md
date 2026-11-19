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
