# Nature Submission Forms — Assessment Report

> Template. Fill every `{{ }}` slot. Keep the section order. One row per form field.
> Legend: ✅ Covered · ⚠️ Partial · ❌ Missing · ➖ N/A · 👤 Author-only (verify manually)

**Manuscript:** {{title / filename}}
**Corresponding author:** {{name}}
**Assessed on:** {{YYYY-MM-DD}}
**Detected study type:** {{e.g. Life sciences — human tissue proteomics}}

---

## 0. Coverage summary

| Form | ✅ | ⚠️ | ❌ | ➖ | 👤 |
|---|---|---|---|---|---|
| Reporting Summary | {{n}} | {{n}} | {{n}} | {{n}} | {{n}} |
| Editorial Policy Checklist | {{n}} | {{n}} | {{n}} | {{n}} | {{n}} |

### Top action items (things to fix before submission)
1. {{highest-priority gap, e.g. "No Code availability statement — custom QuPath extension needs a GitHub/Zenodo link"}}
2. {{...}}
3. {{...}}

---

## Part A — Editorial Policy Checklist

For each field: **Status** · **Evidence** (quote ≤15 words + location) · **Suggested form answer / action**.

### 2. Competing interests
- **Status:** {{}}
- **Evidence:** {{quote + where}}
- **Suggested answer:** {{which declaration to select; draft wording if missing}}

### 3. Authorship
- Author-list agreement — {{status}} — {{note}}
- No LLM as author — {{status}} — {{any AI-use disclosure found?}}
- Inclusion & Ethics statement — {{status}} — {{}}

### 4. Data availability
- Data availability statement — {{status}} — {{evidence}} — {{action}}
- Mandated accession codes — {{status}} — {{which option; list PXD/GEO/PDB accessions found}}

### 5. Code availability
- **Status:** {{}}
- **Evidence:** {{GitHub/Zenodo links, versions, license}}
- **Suggested answer:** {{draft a Code availability statement if missing}}

### 6. Data presentation (mostly verify in figures)
- {{per-item notes; flag any figure legend missing error-bar/box-plot definitions}}

### 7. Image integrity
- **Status:** 👤 — {{reminder tailored to figure types present}}

### 8. Additional policy considerations
Applicability scan: {{list which of the 7 categories apply and which do not}}
For each that applies, one block:
#### {{category name}}
- **Status:** {{}} — **Evidence:** {{}} — **Action:** {{}}

### 9. Certification
- 👤 Author to sign and date.

---

## Part B — Reporting Summary

### 2. Statistics (10 items)
| # | Item | Status | Evidence / note |
|---|---|---|---|
| 1 | Exact sample size n + unit | {{}} | {{}} |
| 2 | Distinct vs repeated measurements | {{}} | {{}} |
| 3 | Test(s) + one/two-sided | {{}} | {{}} |
| 4 | Covariates | {{}} | {{}} |
| 5 | Assumptions/corrections | {{}} | {{}} |
| 6 | Central tendency + variation | {{}} | {{}} |
| 7 | Test statistic, CI, effect size, df, exact P | {{}} | {{}} |
| 8 | Bayesian priors/MCMC | {{}} | {{}} |
| 9 | Hierarchical/complex designs | {{}} | {{}} |
| 10 | Effect-size estimates + method | {{}} | {{}} |

### 3. Software and code
- **Data collection:** {{status}} — draft: "{{list acquisition/instrument software + versions}}"
- **Data analysis:** {{status}} — draft: "{{list analysis tools + versions + repo links; flag any missing version/link}}"

### 4. Data
- **Data availability:** {{status}} — {{cross-reference Part A; note any gaps}}

### 5. Human participants (if applicable)
- Sex and gender — {{status}} — {{}}
- Race/ethnicity/socially relevant groupings — {{status}} — {{}}
- Population characteristics — {{status}} — {{}}
- Recruitment — {{status}} — {{}}
- Ethics oversight — {{status}} — {{approval body + number if found}}

### 6. Field-specific reporting
- **Recommended track:** {{Life sciences / Behavioural & social / Ecological}} — rationale: {{}}
- **Sample size:** {{status}} — {{}}
- **Data exclusions:** {{status}} — {{}}
- **Replication:** {{status}} — {{}}
- **Randomization:** {{status}} — {{}}
- **Blinding:** {{status}} — {{}}
(If a non-life-sciences track applies, list that track's fields instead.)

### 7. Materials, systems & methods
Involvement scan:
| Item | Involved? | Basis |
|---|---|---|
| Antibodies | {{yes/no}} | {{}} |
| Eukaryotic cell lines | {{yes/no}} | {{}} |
| Palaeontology & archaeology | {{yes/no}} | {{}} |
| Animals & other organisms | {{yes/no}} | {{}} |
| Clinical data | {{yes/no}} | {{}} |
| Dual use research of concern | {{yes/no}} | {{}} |
| Plants | {{yes/no}} | {{}} |
| ChIP-seq | {{yes/no}} | {{}} |
| Flow cytometry | {{yes/no}} | {{}} |
| MRI-based neuroimaging | {{yes/no}} | {{}} |

For each **involved** item, a deep-dive block with the sub-fields from the reference file:
#### {{item}}
- {{sub-field}}: {{status}} — {{evidence}} — {{draft/action}}

---

## Appendix — Draft statements ready to paste
Collect the strongest drafts here so the author can copy them straight into the manuscript/form:
- **Data availability:** {{draft}}
- **Code availability:** {{draft}}
- **Competing interests:** {{draft}}
- **Ethics oversight:** {{draft}}
- **Software (data collection / analysis):** {{draft}}
