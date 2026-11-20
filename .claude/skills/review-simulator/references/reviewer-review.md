# Reviewer Review

Read this for the reviewer role. Each simulated reviewer evaluates the science, does not rewrite the paper, and writes for two readers: the editor (to help decide) and the author (to help improve). The purpose is to help the authors strengthen the manuscript and help the editor publish something useful. Be nice: show professional courtesy and treat the authors the way you would want to be treated. Constructive, evidence-based, specific.

## Read for the whole first

Read the manuscript through once before picking at details, and answer the big questions: is the research question important, is the claim novel, are the conclusions supported by the data, is the work credible, and is it a fit for this journal. Carry that overall impression into the detailed pass.

## The five evaluation criteria

Assess the manuscript against these five high-level axes, calibrated to the target journal. The eight detailed dimensions below are how you judge them.

- **Originality:** the real increment over existing work, not a restatement of the known.
- **Scientific importance:** how much the finding matters, and the strength of the "so what" for the field.
- **Interdisciplinary readership:** whether the work is of interest and accessible to readers beyond the immediate subfield (weighted heavily by broad-scope journals).
- **Technical soundness (does the scientific argument hold up):** whether the design, methods, and statistics are appropriate and the data actually support the claims. The three central tests are: is anything overclaimed, are the statistical methods appropriate to the data and study design, and is every conclusion supported by the data. Treat a failure of any of these as a major comment. (Judged in detail in dimensions 3 and 5.)
- **Readability:** whether the writing, structure, and display items are clear enough for the intended, and often non-specialist, reader.

## The eight assessment dimensions

1. **Question and novelty.** Is the research question clear and important? What is the real increment over existing work (not an empty "no one has done this before")? Novelty expectations vary by journal taste: calibrate to the target journal, and note that some journals (for example Scientific Reports and some methods or data-analysis journals) explicitly do not require methodological novelty, only a clear and correct description. Judge against this journal's stated bar, not a universal one.
2. **Methods and reproducibility.** Does the design answer the question? Are sample size, controls, and randomization sound? Are methods detailed enough to reproduce, with reagents, software, parameters, and code? Flag missing steps, absent parameters, or anomalies in key analysis methods. For proteomics specifically, scrutinize DIA-MS acquisition parameters, spectral-library and search settings, FDR control, quantification and batch correction, and pre-statistics data processing.
3. **Statistics.** Is the test appropriate to the data type and design? Multiple-comparison correction where needed? Assumptions met? Is n adequate? Any over-reliance on p-values?
4. **Results and display items.** Do the figures and tables support the text's claims? Are numbers consistent across text, figures, and tables? Any over-processing or selective presentation? Any signs of image splicing or anomalies (check labels too)? **Anomalous or counterintuitive results need an explanation:** where a result runs against expectation, ask the authors to account for it. Examples: a small overlap between RNA and protein identifications (possibly different datasets or clinical-parameter differences that should be stated); or a cancer study showing mostly down-regulated proteins when tumors versus normal tissue would usually show increases, which warrants justification.
5. **Conclusions, claim precision, and over-interpretation (critical).** Does every conclusion trace to a specific result? Is the main claim stated precisely: for instance "biomarker" should specify diagnostic versus prognostic, and a term like "proteogenomics" should be used accurately. Is the evidence sufficient for the specific claim: calling differentially expressed proteins "biomarkers" after only a differential-expression analysis is insufficient and typically needs validation experiments. Flag causal claims beyond the data, generalization beyond the sample, and overstatement like "proves" or "first-ever". Also check the authors have made the study's importance clear.
6. **Logic and clarity.** Is the argument coherent and the structure complete and connected (introduction, methods, results, discussion)? Point out logic gaps or under-supported reasoning. Is it clear enough for a future reader? If you misread something, that usually means it is unclear, so recommend the authors clarify rather than blaming them.
7. **Citations.** Do claims that need support carry citations? Are original sources cited rather than secondary ones? Is any key work in the field missing? (Deep citation checking is `citation-auditor`'s job; here, flag gaps.)
8. **Compliance.** Ethics approval and consent, data and code availability, competing interests, reporting standards.

## Guiding principles for major comments

The core tests for a major comment are **accuracy, reproducibility, and scientificity**: is the main message accurate and precisely stated, could the work be reproduced from what is written, and does the experimental design and analysis scientifically support the stated conclusion. A major comment is one that affects one of these.

## Flagging issues by type

As well as marking each comment must-fix versus suggestion, tag it by type where it applies, so the author can triage:

- **Unsupported claim:** a statement not backed by the paper's own data or a citation.
- **Technical flaw:** a problem in design, method, statistics, or data handling.
- **Evidence-chain gap:** a break in the chain from data to result to conclusion, where a step does not follow.
- **Readability barrier:** a point a non-specialist reader would struggle to follow.

## Structure of a reviewer report

1. **Opening paragraph.** A brief 3 to 4 sentence summary of the paper (what material, what methods, what conclusions) can help, though it is optional, since the authors summarize the work in their abstract. Then state the main strengths and, if there are serious problems, the main weaknesses, followed by a concise overall recommendation. Use a transition sentence to lead into the detail, for example: "Several weaknesses in the data analysis and presentation need to be addressed prior to publication. These are described in detail below."
2. **Major comments.** The core issues affecting the credibility of the conclusions, judged by accuracy, reproducibility, and scientificity. Numbered, specific, actionable, located.
3. **Minor comments.** Method-description gaps and parameter details, figure correctness and labels, data-analysis choices, and format, wording, numbers, and language expression. Numbered.

Comments may be ordered by where they appear in the manuscript or by importance; pick one and be consistent. Mark each comment must-fix versus suggestion, and make sure the detailed comments are consistent with the overall recommendation (do not recommend acceptance while listing fatal flaws). Some journals also ask for a confidential note to the editor and a recommendation; in the report, give a recommendation (accept / minor revision / major revision / reject) and, where useful, a short editor-only note that states priority and concerns candidly but still with evidence.

## Simulating 2 to 3 reviewers

Produce distinct reports, not three copies of one. Give each reviewer a slightly different emphasis (for example one focused on methods and statistics, one on novelty and framing, one on clarity and completeness), as a real panel would vary. Each still covers the dimensions but weights them differently.

## Principles

Disagree with evidence, not attitude; acknowledge what is done well, not only what is wrong; match a comment's depth to the issue's severity; do not turn the review into "how I would have written it"; state uncertainty honestly; keep comments consistent with your recommendation. Never leave an empty verdict ("not novel", "poorly written") without a specific, actionable reason.
