# MCP Submission Checklist — Assessment Report

> Template for Molecular & Cellular Proteomics (ASBMB). Fill every `{{ }}` slot.
> Only include the checklist sections that apply to this manuscript (see routing).
> Legend: ✅ Covered · ⚠️ Partial · ❌ Missing · ➖ N/A · 👤 Author-only
> MCP requires a **page number** next to each satisfied item, so record where the evidence sits.

**Manuscript:** {{title / filename}}
**Corresponding author:** {{name}}
**Assessed on:** {{YYYY-MM-DD}}
**Acquisition / study type detected:** {{e.g. DIA discovery on human FFPE tissue}}

---

## 0. Which MCP checklists apply
| Checklist | Applies? | Basis |
|---|---|---|
| Peptide & Protein Identification (base) | {{yes/no}} | {{}} |
| DIA | {{yes/no}} | {{}} |
| Targeted MS (MRM/PRM/SRM) | {{yes/no}} | {{}} |
| Glycomic | {{yes/no}} | {{}} |
| Clinical Proteomics | {{yes/no}} | {{}} |

**Blank forms to fill:** {{list the applicable MCP/ASBMB checklists to download from the MCP author guidelines, https://www.mcponline.org/}}

### Top action items
1. {{highest-priority gap}}
2. {{...}}
3. {{...}}

---

## Reporting convention
For each item: **Status** · **Page/section** (where it is, or "add to Methods") · **Note / draft**.
Only render the sections whose checklist applies. Use the field IDs from
`references/mcp-checklist-fields.md`.

---

## §A. Peptide & Protein Identification (base)  *(include if applies)*

### A1. Experimental Design and Statistical Rationale
| Item | Status | Page | Note / draft |
|---|---|---|---|
| Subsection header present | {{}} | {{}} | {{}} |
| Sample size n per experiment (number, not range) | {{}} | {{}} | {{}} |
| Rationale for n | {{}} | {{}} | {{}} |
| Controls (number + type) | {{}} | {{}} | {{}} |
| Replicates: biological/process/technical + rationale | {{}} | {{}} | {{}} |
| Inclusion/exclusion criteria | {{}} | {{}} | {{}} |
| Statistical methods described | {{}} | {{}} | {{}} |
| Statistical methods justified | {{}} | {{}} | {{}} |

### A2. Search Parameters and Acceptance Criteria
| Item | Status | Page | Note |
|---|---|---|---|
| Peak-list software + version | {{}} | {{}} | {{}} |
| Search engine + version | {{}} | {{}} | {{}} |
| Database/library + version | {{}} | {{}} | {{}} |
| In-house DB source + software | {{}} | {{}} | {{}} |
| # entries searched | {{}} | {{}} | {{}} |
| Protease specificity | {{}} | {{}} | {{}} |
| Missed/non-specific cleavages | {{}} | {{}} | {{}} |
| Fixed modifications | {{}} | {{}} | {{}} |
| Variable modifications | {{}} | {{}} | {{}} |
| Precursor mass tolerance | {{}} | {{}} | {{}} |
| Fragment mass tolerance | {{}} | {{}} | {{}} |
| Contaminants excluded (PMF) | {{}} | {{}} | {{}} |
| Threshold score/expectation value | {{}} | {{}} | {{}} |
| Threshold justified | {{}} | {{}} | {{}} |
| FDR + how calculated | {{}} | {{}} | {{}} |

### A3–A6. Results/Supplemental (Identification, PTMs, Protein inference, Quantification)
{{one line per applicable item with status + page; mark PTM/inference/quant blocks N/A if not present}}

### A7. Raw data submission
- Deposited: {{status}} — repository + accession: {{PXD… / MassIVE / jPOST}} — {{reviewer creds go in cover letter}}

---

## §B. DIA  *(include if applies)*
Sub-tracks: spectrum-centric and/or peptide-centric (include only those used).
{{tables mirroring B1–B7 from the reference file, with Status / Page / Note per item}}

---

## §C. Targeted MS  *(include if applies)*
- **Tier level:** {{1/2/3 — detected basis}}
{{tables for Sections I–V (C1–C5), Status / Page / Note per item}}

---

## §D. Glycomic  *(include if applies)*
{{tables for Sections I–III (D1–D3), Status / Page / Note per item}}

---

## §E. Clinical Proteomics  *(include if applies)*
- **Ethics/IRB approval statement (mandatory):** {{status}} — {{approval body + number if found}}
{{tables for E1–E6, Status / Page / Note per item}}

---

## Appendix — Draft text ready to paste
- **Experimental Design and Statistical Rationale (subsection):** {{draft}}
- **Search parameters block:** {{draft from software/versions/DB found}}
- **Data availability / repository statement:** {{draft with PXD placeholder}}
- **Ethics/IRB statement (if clinical):** {{draft}}
- **Cover-letter note:** repository reviewer username/password + Tier level (if targeted).
