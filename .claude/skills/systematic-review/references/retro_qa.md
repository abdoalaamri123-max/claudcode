# Retrospective Extraction QA — Reference (Phase 7c companion)

*Companion to SKILL.md Phase 7c (v8.1). This file holds the full check catalogue, the coverage-status vocabulary, the intake-probe details, the tier-capability table, and the worksheet template — the material Phase 7c references by name. Where this file and SKILL.md conflict, SKILL.md governs. Everything here is subject to the Hard Rules of the skill: the model performs no arithmetic; flag, never fix; every gate is researcher-owned; a value without an anchor is not a value.*

---

## 1. Capability-tier task table (full form)

| Task | Tier A (anchors + layers + hashes) | Tier B (PDFs, layers regenerated) | Tier C (no sources) |
|---|---|---|---|
| Machine verification of claimed anchors (`anchor_verification.py`) | ✓ | — (no anchors were claimed) | ✗ impossible |
| Retrospective anchoring (values → candidate anchors) | ✓ (for values whose claimed anchors fail) | ✓ (primary activity) | ✗ impossible |
| `SUPPORTED / CONTRADICTED / DERIVED? / NOT_LOCATED` classification | ✓ | ✓ | ✗ impossible |
| Blind Extractor-B fallback (independent re-extraction from source) | ✓ | ✓ | ✗ impossible — dies at Tier C |
| SCH — schema & structure checks | ✓ | ✓ | ✓ |
| CON — internal-consistency checks | ✓ | ✓ | ✓ |
| PRF — proofreading checks | ✓ | ✓ | ✓ |
| COV — coverage matrix | ✓ | ✓ | ✓ (against the retrospective TDPL only) |
| Table-vs-text conflict capture (both values under QUERY) | ✓ | ✓ | ✗ (no text to compare) |
| Evidence-backed Gate R3 sign-off | ✓ | ✓ | ✗ — the researcher verifies against their own copies; every deliverable states that no cell was verified against a source |

**Tier B upgrade path:** the open-access web-retrieval rung of the researcher's-files fallback ladder (Phase 3) is a *partial* upgrade from Tier C: it enables retrospective anchoring against the retrieved text layer, but the anchors are **page-less** relative to the researcher's own PDF (pagination rarely matches) and are logged as degraded candidate anchors with the retrieved file's own hash.

---

## 2. Intake-probe detail (`.xlsx` pathology checklist)

Run on every sheet during Step 7c.3, item 2. Every hit is **reported**, never silently normalised.

| Probe | What it detects | Why it matters for QA |
|---|---|---|
| Merged ranges | `worksheet.merged_cells.ranges` | A merged header spreads one label over many columns; naive parsing attributes values to the wrong data point |
| Hidden sheets / rows / columns | `sheet_state`, `row_dimensions[].hidden`, `column_dimensions[].hidden` | Hidden content is still data; scoping without it silently narrows the audit |
| Formula count (two-pass load) | `openpyxl` pass 1 `data_only=False` (formulas), pass 2 `data_only=True` (cached values) | A formula cell's displayed value may be stale if the file was edited outside Excel; both faces are recorded |
| Date auto-coercion | Cells typed as datetime where the column is not a date field | Excel famously converts strings like `1-2` or gene-symbol-like tokens to dates |
| Lost leading zeros | Numeric cells in columns that are identifiers by the schema mapping | `0042` → `42` corrupts IDs |
| Scientific-notation strings | Text cells matching `\d+(\.\d+)?E[+-]\d+` | A long numeric ID displayed and saved as `1.23E+15` |
| Decimal commas | Numeric-looking strings with `,` as the decimal separator | Locale artifacts; `3,4` parsed as 34 or 3.4 depending on parser — a failed parse is a flag, never a guess |
| Escaped control characters | `_x0001_`-style OOXML escapes in strings | Paste artifacts from PDFs; PRF family cross-references these |

**Values-only substrate rule:** every sheet is snapshotted to a values-only CSV (cached values, UTF-8, RFC-4180 quoting), hashed, and that CSV is what every check family reads. The `.xlsx` itself is opened only by the intake probes; it is never the substrate, and it is never written to.

---

## 3. Check catalogue (full)

Every check is an executed, version-pinned script. Every numeric flag shows its arithmetic inline. A failed parse is a flag (`PARSE_FAIL`), never a guess. No check runs before Gate R1 (an unconfirmed column meaning manufactures false flags).

### SCH — schema & structure

| ID | Check |
|---|---|
| SCH-01 | Key integrity: every row resolves to a `record_id` (Step 4.0, incl. the citation-hash deviation) and the confirmed row unit; collisions and blanks flagged |
| SCH-02 | ID integrity: duplicate `record_id × row-unit` combinations flagged (may be legitimate — e.g., two informants — routed as convention questions, not errors) |
| SCH-03 | Controlled vocabularies: columns the retrospective TDPL declares categorical are checked against their observed value set; singleton variants (`RCT` vs `rct` vs `R.C.T.`) flagged |
| SCH-04 | Whitespace: leading/trailing/multiple internal spaces, non-breaking spaces |
| SCH-05 | Encoding: mojibake sequences, mixed encodings, OOXML control-character escapes |
| SCH-06 | Structural absences: the canonical Phase 7b fields the legacy sheet never had (`record_id`, `dp_id`, `status`, quote/anchors, `conversion_needed`, versions) recorded as ABSENT-BY-DESIGN — reported once, never per-row "failures" |
| SCH-07 | Orphan rows: rows whose citation matches no study in the definitive included-studies list (or, under "spreadsheet rows are definitive", rows whose citation matches no other row's — possible fragment duplicates) |

### CON — internal consistency

| ID | Check |
|---|---|
| CON-01 | Group sums vs n: per-arm and per-subgroup counts sum to the stated total; per-arm variant runs wherever arm columns are mapped. Tolerance: **exact** (default) |
| CON-02 | Analysed ≤ randomised, per arm and total |
| CON-03 | Events ≤ n, per arm |
| CON-04 | Percentage recomputation with the **implied-denominator technique**: recompute claimed % from mapped numerator/denominator; if it diverges beyond tolerance (default **±0.1 pp**), also solve for the denominator (and numerator) the claimed % implies, and present it as an **adjudicable hypothesis**, e.g., `claimed 35.2% with 29/88 = 33.0% (Δ 2.2 pp); 29/x = 35.2% ⇒ x ≈ 82 — was the denominator the analysed n (82), not the randomised n (88)?` |
| CON-05 | CI brackets estimate: lower ≤ point ≤ upper; degenerate (zero-width) intervals flagged |
| CON-06 | SD positivity; separator anomalies (an "SD" column holding `3.4-6.1`-style ranges or `12,3` decimal-comma strings → `PARSE_FAIL` flag, never coercion) |
| CON-07 | Mean within stated range (and within instrument bounds where the conventions registry records them) |
| CON-08 | Same-study cross-row agreement: rows sharing `record_id` compared on study-level fields (n, design, country…); divergences phrased *"may be a legitimate per-informant difference"* and routed as convention questions |
| CON-09 | Eligibility-window checks: dates/ages/durations against the protocol's stated windows, where mapped |
| CON-10 | Unit-of-analysis audit: cluster/crossover/multi-arm signals in the data (e.g., arms sharing a comparator) without a corresponding flag column |
| CON-11 | `conversion_needed` audit: cells that look like conversions already performed (a mean+SD row citing a paper the anchoring shows reported median+IQR) — flagged *"method must be named and re-executed at analysis"*; the QA never redoes or verifies the arithmetic |

### PRF — proofreading

| ID | Check |
|---|---|
| PRF-01 | Spelling/typos in free-text fields — **cosmetic** class |
| PRF-02 | PDF-paste hyphenation artifacts (`depres- sion`), soft hyphens, ligature residue — cosmetic unless inside a value-bearing cell |
| PRF-03 | Control-character artifacts (cross-referenced to SCH-05) |
| PRF-04 | **Value-bearing** anomalies: any PRF hit inside a numeric or categorical cell is tagged `CONFIRM-VS-SOURCE` and cross-referenced to its CON flag; its correction proposal cannot be accepted from proofreading evidence alone |

### COV — coverage

One matrix: confirmed studies × retrospective-TDPL data points. Status vocabulary:

| Status | Meaning |
|---|---|
| `LOCATED` | A value is present for this study × data point |
| `MISSING_REQUIRED` | The data point is `required: true` in the confirmed retrospective TDPL and no value exists |
| `MISSING_CONDITIONAL` | Required only under a condition that **is** triggered for this study, and absent |
| `NA_CONDITION_NOT_TRIGGERED` | Conditional data point whose condition does not apply to this study — not a gap |
| `LOCATED_NA_NOTED` | The extractor explicitly recorded NA/not reported — a decision, not an omission |
| `QUERY_R1` | Coverage cannot be classified until a pending Gate R1 confirmation resolves (also the **conservative branch** under the proceed-provisional protocol: an undecided required-ness resolves here, never to `MISSING_REQUIRED`) |
| `NA_CONVENTION_PENDING` | Classification awaits a proposed conventions-registry rule the researcher has not yet approved |

---

## 4. Standing parser rules (verbatim from Phase 7c, for script authors)

1. **A failed parse is a flag, never a guess.** No coercion, no "best effort" numeric extraction, no locale inference. The cell's raw content goes into the flag.
2. **Composite-cell micro-grammars belong in the conventions registry.** When a column systematically packs multiple values into one cell (`14.2 (6.1) [n=41]`), the format is proposed to the researcher as a conventions-registry entry (category `rounding_and_units` or `other`, Step 7b.3 schema); only after approval does a parser for that registered grammar run — and the parser's version is pinned and logged like any other script.

---

## 5. Per-study worksheet template (risk-ordered)

```
STUDY: {record_id} — {citation}          TIER {A|B|C} BANNER LINE
════════════════════════════════════════════════════════════════
SECTION 1 — RESOLVE FIRST (blocking)
  [ ] {dp}: NOT_LOCATED — value "{v}" not found in source
  [ ] {dp}: QUERY — table says "{v1}", text says "{v2}" (both captured)
  [ ] {dp}: CONTRADICTED (CRITICAL) — sheet "{v}"; source "{v_src}"
      at {candidate anchor}
SECTION 2 — CONSISTENCY FLAGS
  [ ] {check-ID}: {flag with arithmetic shown}
      route: {transcription | convention | tdpl_defect | upstream}
SECTION 3 — CLEAN-FIELD CHECKBOXES (100% human verification)
  [ ] {dp} = "{v}"   {Tier A/B: anchor or candidate anchor}
                     {Tier C: "verify against your own copy of the paper"}
════════════════════════════════════════════════════════════════
Silent passes on this study: {enumerated check IDs}
Machine-check coverage gaps on this study: {patterns not matched}
```

At Tier C, Section 3's instruction routes verification to the researcher's own copies for **every** field — the checkbox is their attestation, and the report repeats that no cell was machine-verified against a source.

---

## 6. Deliverable ordering and sign-off questions (Gate R3 support)

The seven deliverables and their order are normative in SKILL.md Step 7c.6. The **gap report's sign-off questions** (deliverable 1) are, at minimum:

1. "These inputs were requested and not provided: {list}. Confirm the QA proceeds without them at Tier {X}, with that tier's limits."
2. "The included-studies source is {definitive list | 'spreadsheet rows are definitive'}. Confirm — and, in the latter case, confirm you accept the detection-blindness limitation (a study extracted into no row cannot be detected)."
3. "The confirmed scope is {rows/columns/studies}. Rows outside it will not be audited. Confirm."
4. "Temperature for this run is {0 | platform-controlled}. Confirm you accept the sampling-honesty note where platform-controlled."

The **key issues summary** (deliverable 7) must end with a *"what remains human work"* paragraph: applying accepted corrections to the researcher's copy; the Tier-C source verifications; any `UPSTREAM_SPECIFICATION_FLAG` decisions; and the Gate R3 sign-off itself.
