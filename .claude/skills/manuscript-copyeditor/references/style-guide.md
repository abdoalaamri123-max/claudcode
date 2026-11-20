# Style Guide

Read this for the full rule set behind each pass in `SKILL.md`, organized from macro decisions to micro typography. Apply in this order before any submission or revision round. Most rules here are field-standard conventions; a few are a coherent house style rather than a universal requirement — see `SKILL.md`'s "A note on house style vs. hard rules" for which is which, and let a stated author preference or the target journal's own guidelines override the default where they conflict.

---

## 1. Global Decisions

Make these decisions before editing begins. They govern the entire manuscript.

### Choose one spelling convention and hold it

Pick British or American English and apply it consistently throughout. Journals run automated checks; inconsistencies are a common reviewer complaint. Convention is determined by the **publisher family**, not simply by country of publication.

| Style | Publisher / Journal family | Example journals |
|---|---|---|
| **British** | Nature Portfolio (Springer Nature) | *Nature*, *Nature Methods*, *Nature Biotechnology*, *Nature Communications*, *Nature Protocols* |
| **British** | BMJ Publishing Group | *BMJ*, *Gut*, *Thorax* |
| **British** | The Lancet (Elsevier) | *Lancet*, *Lancet Oncology* |
| **British** | EMBO Press | *EMBO Journal*, *Molecular Systems Biology* |
| **American** | Cell Press (Elsevier) | *Cell*, *Molecular Cell*, *Cell Reports*, *Cell Systems*, *Cancer Cell* |
| **American** | AAAS | *Science*, *Science Advances*, *Science Translational Medicine* |
| **American** | ASBMB | *JBC*, *MCP*, *JLR* |
| **American** | ACS Publications | *JACS*, *ACS Nano*, *Analytical Chemistry* |
| **American** | ACS / ASMS | *JPR*, *Journal of Proteome Research* |
| **American** | PNAS / NAS | *PNAS* |
| **Flexible** | eLife Sciences | *eLife* — accepts both; internal consistency required |

Two overrides that apply regardless of chosen style:
- **IUPAC nomenclature** takes precedence for chemical terms: always "sulfur", "aluminium".
- **Gene and protein names** follow HGNC/MGI — they are globally standardised and do not change between US/UK variants.

### Four suffix patterns

| Rule | British ending | American ending | British | American |
|---|---|---|---|---|
| **1. -re / -er** | -re | -er | centre, fibre | center, fiber |
| **2. -our / -or** | -our | -or | colour, tumour, behaviour | color, tumor, behavior |
| **3. -ise / -ize** | -ise (preferred) | -ize | realise, organise | realize, organize |
| **4. -ll- / -l-** | double-l before suffix | single-l | signalling, modelling | signaling, modeling |

**Note (on -ise vs -ize):** both forms are acceptable in British English. Oxford University Press and many UK scientific journals prefer -ize ("Oxford spelling"). Whichever you choose, apply it to all verbs.

### Quick reference: common scientific terms

| British | American |
|---|---|
| signalling | signaling |
| tumour | tumor |
| colour | color |
| behaviour | behavior |
| favourable | favorable |
| organisation | organization |
| realise | realize |
| centre | center |

### Full reference table

| Category | American | British |
|---|---|---|
| **Biomedical terms** | tumor | tumour |
| | fiber | fibre |
| | edema | oedema |
| | estrogen | oestrogen |
| | fetal | foetal |
| | anemia | anaemia |
| | leukemia | leukaemia |
| | esophagus | oesophagus |
| | hemoglobin | haemoglobin |
| | hemorrhage | haemorrhage |
| | hematoxylin | haematoxylin |
| | diarrhea | diarrhoea |
| | pediatric | paediatric |
| | orthopedic | orthopaedic |
| | anesthesia | anaesthesia |
| **-ize / -ise verbs** | analyze | analyse |
| | characterize | characterise |
| | normalize | normalise |
| | optimize | optimise |
| | utilize | utilise |
| | standardize | standardise |
| | visualize | visualise |
| | summarize | summarise |
| **-or / -our** | color | colour |
| | behavior | behaviour |
| | labor | labour |
| | favor | favour |
| **-er / -re** | center | centre |
| | fiber | fibre |
| | meter | metre |
| **Past tense** | learned | learnt |
| | burned | burnt |
| | dreamed | dreamt |
| **Double consonants** | modeling | modelling |
| | labeling | labelling |
| | traveled | travelled |
| | focused | focussed |
| **Noun / verb pairs** | practice (both) | practice (n.) / practise (v.) |
| | license (both) | licence (n.) / license (v.) |
| **Other common terms** | program | programme |
| | catalog | catalogue |
| | gray | grey |
| | aluminum | aluminium |
| | sulfur | sulphur* |

**IUPAC exception:** \*IUPAC recommends **"sulfur"** in all scientific writing regardless of regional style. Similarly, use **"aluminium"** (IUPAC), not "aluminum", even in American-style manuscripts.

### No invented data, and nothing new added

Never fabricate numbers or citations while copyediting. If a value is uncertain, mark it explicitly:

> `[CHECK: confirm n=XX from Table S1]`

Flag all marked items for author verification before submission.

Two directions this rule cuts, both absolute:

- **Never changed:** facts, data (numbers, units, effect sizes), citations, and specialized/proper expressions (gene and protein names, method and reagent names, established technical terms). A smoother-sounding synonym is never a valid reason to swap out a precise term of art — "knockdown" and "knockout" are not interchangeable for readability, and neither is a specific reagent or instrument name for a generic description of it. The same holds, more easily overlooked, for degree/magnitude words during fluency polishing: "attenuated" and "blocked", "decreased" and "abolished", "some" and "most" describe different amounts of effect, not interchangeable phrasings of the same claim — never swap toward the stronger or weaker word for smoother flow, only within a genuinely equivalent degree.
- **Never added:** a **result** the manuscript did not report, a **mechanism** the manuscript did not propose, a **statistical-significance claim** ("significantly," "a significant difference") where the original made no such claim, or a **citation** the manuscript did not already contain. This is the most common failure mode when "polishing" a sentence for flow — filling a gap left by a cut hedge or a trimmed qualifier with something that sounds plausible rather than leaving the claim exactly as strong (or weak) as it was.

### Abbreviation strategy

Decide the abbreviation list before drafting. Global rules:

1. **Define on first use:** full term, then abbreviation in parentheses — "deep visual proteomics (DVP)".
2. **Re-define in the abstract** — the abstract is read independently of the main text.
3. **Minimum frequency threshold:** abbreviate only if the term appears **≥ 2 times** in the main text; otherwise spell out every time.
4. **Never abbreviate in headings** (unless the abbreviation is more recognisable than the full term, e.g., DNA, RNA, LC-MS/MS).
5. **One abbreviation per concept; one concept per abbreviation.**
6. **Units are not abbreviations** — do not define μm, kDa, etc.

### Abbreviation audit template

Run before submission. Every abbreviation must have `Occurrences (full) ≥ 1` in the section where it first appears.

| Abbreviation | Full Term | First defined | Occurrences (full) | Occurrences (abbrev) | Notes |
|---|---|---|---|---|---|
| DVP | deep visual proteomics | Abstract | 1 | 14 | Re-defined in Intro |
| DIA | data-independent acquisition | Methods | 0 | 9 | Standard field term |
| TMA | tissue microarray | Abstract | 1 | 22 | |

**How to audit:** use "Find & Replace" count or a script. Flag any row where `Occurrences (full) = 0` — the abbreviation is used but never defined.

---

## 2. Paragraph Level

### Open with the finding, not the context

The first sentence must carry information. Never open with a broad contextual statement.

| Avoid | Prefer |
|---|---|
| "In recent years, spatial proteomics has gained attention…" | "Deep Visual Proteomics resolves protein abundance at single-cell resolution within intact tissue." |
| "With the advancement of mass spectrometry…" | "Label-free DIA quantified 4,400 proteins from 50-cell laser-captured regions." |

### Hedging — one hedge per claim

Use calibrated hedges. Stacking multiple hedges weakens rather than strengthens a claim.

| Strength | Expressions |
|---|---|
| Strong | "demonstrates", "shows", "establishes" — use only when data directly prove |
| Moderate | "indicates", "suggests", "is consistent with" — for interpretations |
| Weak | "may reflect", "could indicate", "raises the possibility" — for speculative claims |

- **Wrong:** "These findings may possibly suggest that there could be…"
- **Right:** "These findings suggest a role for BRD4 in immune evasion."

A hedge is a claim-strength decision, not a wording nicety: never raise or lower it to make prose flow better without confirming that's what the evidence supports. If unsure which tier a claim belongs in, flag it rather than picking one.

### Connective discipline

**The connective test:** delete the connector and re-read both sentences. If the argument still holds, cut the connector. Restore it only if logical flow breaks without it.

| Connector | When to cut | When to keep |
|---|---|---|
| "Furthermore," | When the next sentence continues naturally | When genuinely adding a logically separate point |
| "Therefore," | When causality is already implied | When the conclusion would be missed |
| "However," | When contrast is obvious | When the reader might miss the pivot |
| "Notably," | Almost always — shows rather than tells | Rarely justified |
| "Interestingly," | Always — cut unconditionally | Never |

---

## 3. Sentence Level

### Vary sentence length

Mix short and long sentences within a paragraph. A run of similarly-sized sentences flattens emphasis and dulls the reader.

**Why it matters:** short sentences land hard. They isolate a key finding or conclusion so the reader cannot miss it. Longer sentences, by contrast, are better suited to explanation, qualification, or building an argument across multiple related ideas before arriving at a point.

| Pattern | Effect | Verdict |
|---|---|---|
| All long | Dense; buries emphasis | ✗ Avoid |
| All short | Choppy; reads like a list | ✗ Avoid |
| Mixed | Rhythm guides the reader; emphasis is controlled | ✓ Preferred |

**How to apply:**
1. After drafting a paragraph, count sentence lengths roughly.
2. If three or more consecutive sentences are similar in length, break one up or merge two.
3. Reserve the shortest sentence in any paragraph for the single most important claim.

| Flat (uniform) | Varied |
|---|---|
| "DVP integrates laser capture microdissection with mass spectrometry. It enables single-cell proteomics in intact tissue. It was applied here to skin biopsies. We quantified 3200 proteins per region." | "DVP integrates laser capture microdissection with mass spectrometry to enable single-cell proteomics in intact tissue. Applied here to skin biopsies, it quantified 3200 proteins per region. That is a fourfold gain over prior methods." |

**Tip:** read the paragraph aloud. A flat rhythm sounds monotonous; a varied one has a natural pace. If you find yourself taking the same breath interval at every period, the sentences are too uniform.

### Voice and tense by section

| Section        | Convention     | Example                                                         |
| -------------- | -------------- | --------------------------------------------------------------- |
| Methods        | Passive past   | "Samples were digested with trypsin at 37 °C for 16 hours."     |
| Results        | Passive past   | "Proteins were quantified using DIA-NN 1.9."                    |
| Interpretation | Active present | "These results suggest a tumor-intrinsic resistance mechanism." |
| Figure legends | Passive past   | "Data are shown as mean ± SD (n = 3)."                          |

### Parallel structure

Ensure all items in a list are grammatically parallel.

- **Wrong:** "We collected samples, the processing was done overnight, and data analysis."
- **Right:** "We collected samples, processed them overnight, and analyzed the data."

### No ambiguous "this"

Always specify what "this" refers to — never leave it as a bare pronoun.

- **Ambiguous:** "This was unexpected."
- **Clear:** "This discrepancy between DVP and bulk proteomics was unexpected."

### No em-dash — use hyphen instead (house style)

Never use em-dash (—). Replace with:

| Replacement | Use case | Example |
|---|---|---|
| **Comma** | Brief parenthetical | "The method, originally developed for tissue sections, scales to single cells." |
| **Semicolon** | Two linked independent clauses | "Sensitivity improved threefold; specificity remained unchanged." |
| **Parentheses** | Asides, clarifications | "Protein identifications (n = 3200) exceeded the previous benchmark." |
| **Period** | When in doubt | Split into two sentences. |

Regular hyphen (-) remains correct for compound adjectives and prefixes: "laser-captured regions", "data-independent acquisition."

This is the clearest house-style item in this guide, not a universal rule — many journals and style guides permit or even favor em-dashes. Apply it as the default; drop it if the author states otherwise or the manuscript already uses em-dashes consistently.

---

## 4. Word Level

### Quantify; do not qualify

Use numbers, not vague qualifiers.

| Vague | Precise |
|---|---|
| significantly improved sensitivity | identified 3200 proteins from 200 cells (vs. 1100 previously) |
| a large proportion of patients | 68% of patients (n = 138 of 202) |
| the majority of proteins | 74% of quantified proteins (3256 of 4400) |
| several replicates | three biological replicates, each with two technical replicates |

Only substitute a number that is actually in the manuscript or its source data; never invent one to make a vague qualifier concrete. Where the qualifier is all the draft gives you, flag it for the author to supply the figure rather than guessing.

### Avoid over-nominalization

Do not turn verbs into noun clusters.

- "the quantification of protein abundance changes" → "quantifying how protein abundance changes"
- "the optimization of sample preparation protocols" → "optimizing sample preparation"

### Shorten noun-phrase verbs

| Verbose | Concise |
|---|---|
| performed an analysis of | analyzed |
| made an assessment of | assessed |
| conducted a comparison of | compared |
| showed an increase in | increased |
| is indicative of | indicates |
| in order to | to |
| due to the fact that | because |
| at this point in time | now |

### First mention rules

**Genes — full name at first mention, symbol in parentheses:**
- Correct: "titin (*Ttn*) is the largest protein in the sarcomere. *Ttn* mutations are associated with…"
- Wrong: using the symbol before defining it

**Proteins — write the complete protein name at first mention:**

| Wrong | Correct |
|---|---|
| ABCA1 was significantly upregulated… | ATP Binding Cassette Subfamily A Member 1 (ABCA1) was significantly upregulated… |
| We quantified BRCA1 levels… | We quantified breast cancer type 1 susceptibility protein (BRCA1) levels… |

### Authoritative nomenclature databases

| Organism | Authority | Resource |
|---|---|---|
| Human | HUGO Gene Nomenclature Committee | [HGNC](https://www.genenames.org) |
| Mouse | The Jackson Laboratory (MGI) | [MGI](https://www.informatics.jax.org) |
| All organisms | NCBI Entrez Gene | [Entrez Gene](https://www.ncbi.nlm.nih.gov/gene) |
| Functional annotation | Gene Ontology Project | [GO](https://geneontology.org) |

If a gene or protein's official name/symbol isn't stated in the manuscript and can't be confidently inferred, flag it rather than guessing which authority's nomenclature applies.

### Do not use slash notation for alternative names

A slash is ambiguous — it can mean a ratio, a complex, alternative names, or different subunits.

| Wrong | Correct |
|---|---|
| Oct4/Pou5f1 | Pou5f1 (also known as Oct4) — one name throughout |
| ERK1/2 (one isoform) | ERK1 or ERK2 — specify the exact isoform |
| p16/CDKN2A | CDKN2A (also known as p16) |

**Warning:** ERK1/2, SMAD2/3 are acceptable **only** when referring to both isoforms collectively and made explicit: "ERK1 and ERK2 (hereafter ERK1/2)."

### Citation format with "et al."

When a source has **more than two authors**, use the first author's surname + "et al." (roman). Do not list remaining authors.

| Authors | Correct |
|---|---|
| 1 author | Smith (2020) |
| 2 authors | Smith and Jones (2020) |
| 3+ authors | Smith et al. (2020) |

Rules:
- "et al." is roman — not italic.
- Period after "al." only; no period after "et".
- No comma between surname and "et al.": `Smith et al.`, not `Smith, et al.`
- Parenthetical: comma after "et al." before the year — `(Smith et al., 2020)`.
- Disambiguation when two works shorten identically: `(Smith, Jones, et al., 2020)` vs `(Smith, Lee, et al., 2020)`.

Examples:
> Ren et al. (2017) investigated the usage of social media devices among college students in Shanghai.
> Protein abundance was profiled across 440 tissue cores (Sun et al., 2024).

This is a prose-punctuation check, distinct from `citation-auditor`'s job of confirming the citation is the *right, real* paper with correct metadata — apply both where a manuscript needs both.

### Citation selection and placement

**Cite the earliest supporting work.**
Prioritise the original paper that first established or demonstrated the claim, not the most recent review or the most-cited paper. If multiple landmark papers exist, cite in chronological order.

- Correct: cite the 1953 Watson & Crick paper when referring to the double helix, not a 2020 review.
- Wrong: citing a review in place of the primary source because it is easier to find.

**Placement — after a noun or at the end of a sentence.**
Citations may follow a specific noun (the entity being referenced) or the full sentence. Both positions are acceptable; choose based on what is being supported.

| Position | Example |
|---|---|
| After noun | "The DVP workflow (Smith et al., 2020) enables single-cell proteomics." |
| End of sentence | "Single-cell proteomics resolves tumour heterogeneity at protein level (Smith et al., 2020)." |

**Maximum five references per claim.**
Do not pile up a long list of citations to appear comprehensive. If more than five papers support a claim, select the most seminal ones. Excessive citation lists slow reading and dilute emphasis.

- Acceptable: (Smith et al., 2018; Jones et al., 2019; Lee et al., 2021)
- Too many: (A et al., 2010; B et al., 2012; C et al., 2014; D et al., 2016; E et al., 2018; F et al., 2020; G et al., 2022)

Trimming an over-long citation list is a style edit, not a content edit: never drop the single reference actually supporting the specific claim, and never trim without checking which of the piled-up citations is load-bearing (that check is `citation-auditor`'s territory if it's unclear).

**Period placement — always outside the parenthesis.**
The sentence period comes after the closing parenthesis, never before it.

| Wrong | Correct |
|---|---|
| `0000. (Fig. 1)` | `0000 (Fig. 1).` |
| `increased significantly. (Smith et al., 2020)` | `increased significantly (Smith et al., 2020).` |
| `as shown. (Table 2)` | `as shown (Table 2).` |

**Warning:** this rule applies universally: figures, tables, supplementary data, and literature citations all follow the same pattern — parenthesis first, period last.

### Special cases in gene / protein nomenclature

| Case | Rule | Example |
|---|---|---|
| Point mutation | Gene italic + superscript mutation roman | *KRAS*^G12D^, *TP53*^R248W^ |
| Knockout | Superscript −/− after italic gene | *Brca1*^−/−^ mice |
| Transgenic | Tg() notation | Tg(*Kras*^G12D^) |
| Fusion gene | Both names italic, hyphen between | *BCR-ABL1* |
| microRNA | Roman, lowercase, hyphenated number | miR-21, miR-155 |
| lncRNA | Italic, uppercase (human) | *MALAT1*, *HOTAIR* |
| Protein complex | Roman, no italic | mTORC1, RISC, PRC2 |
| Signalling pathway | Roman, by convention | Wnt, Notch, Hedgehog, NF-κB |

---

## 5. Formatting & Typography

### Alignment — left-align, not justified

Always set paragraph alignment to **left-aligned (ragged right)**. Do not use full justification (both edges flush).

**Why not justified:**
- Justified text forces the word processor to insert variable whitespace between words to fill each line. The gaps are irregular and visually distracting.
- It becomes impossible to verify spacing: one space or two? A stray double-space hides cleanly in a justified block but is visible immediately in left-aligned text.
- Readability studies consistently show ragged-right text reduces eye strain for continuous reading.

| Setting | Effect | Verdict |
|---|---|---|
| Left-aligned (ragged right) | Consistent word spacing; uneven right margin | ✓ Preferred |
| Justified (both edges flush) | Variable word spacing; rivers of whitespace | ✗ Avoid |

**Tip:** most journal submission systems re-flow text into their own template anyway. Write and review in left-aligned; let the typesetter handle final layout.

### Number formatting

**Rule 1 — Spell out one through twenty.**
Use words for integers 1–20; Arabic numerals for 21 and above.

| Wrong | Correct |
|---|---|
| 3 replicates | three replicates |
| 5 patients | five patients |
| 21 samples | 21 samples |

Exception: always use numerals when a number is directly followed by a unit — "3 μg", "5 hours", "20 cells" — regardless of magnitude.

**Rule 2 — Thousands (1000–9999): no comma.**

| Wrong | Correct |
|---|---|
| 3,200 proteins | 3200 proteins |
| 1,100 cells | 1100 cells |

**Rule 3 — Ten thousand and above: comma every three digits.**

| Wrong | Correct |
|---|---|
| 30000 reads | 30,000 reads |
| 100000 cells | 100,000 cells |

**Quick rule:** fewer than 5 digits → no comma. Five or more digits → comma from the right in groups of three.
`3200` (4 digits) · `30,000` (5 digits)

### Oxford comma (serial comma)

Always use the Oxford comma before the final "and" or "or" in a list of three or more items.

- **Correct:** "We measured proliferation, apoptosis, and migration."
- **Wrong:** "We measured proliferation, apoptosis and migration."

**Why it matters:**
"We thank our collaborators, John Smith and Jane Doe." — ambiguous (are John and Jane the collaborators?)
"We thank our collaborators, John Smith, and Jane Doe." — three distinct parties, unambiguous.

### SI units — number + space + symbol

Always insert a space between the numeral and the unit symbol. Unit symbols are not abbreviations: no period, never pluralised.

| Wrong | Correct |
|---|---|
| 4°C | 4 °C |
| 37°C | 37 °C |
| 100μl | 100 μL |
| 10mM | 10 mM |
| 280nm | 280 nm |
| 50kDa | 50 kDa |

**Temperature:**

| Format | Rule |
|---|---|
| **4 °C** | Numeral + space + °C. ° and C written together, no space between them. |
| **310 K** | Numeral + space + K. Never "°K" — Kelvin has no degree symbol. |
| **−20 °C** | Negative: use proper minus sign (−, U+2212), not a hyphen. |

**Common units in proteomics / biology:**

| Quantity | Symbol | Example | Notes |
|---|---|---|---|
| Temperature | °C, K | 37 °C, 310 K | No °K |
| Time | hour(s), minute(s), second(s) | 1 hour, 2 hours, 30 minutes | Spell out in full; never h, min, s, hrs, mins |
| Volume | L, mL, μL | 200 μL, 1 mL | Always uppercase L |
| Mass | kg, mg, μg, ng | 10 μg, 500 ng | |
| Concentration (molar) | mol/l, mmol/l, μmol/l | 10 mmol/l | Or mM, μM — journal-dependent |
| Concentration (mass) | mg/mL, μg/μL | 1 mg/mL | |
| Length | m, mm, μm, nm | 10 μm, 280 nm | |
| Molecular mass | Da, kDa | 50 kDa | Not "kd" or "KDa" |
| Centrifugation | × g | 1,000 × g | Not "rpm" for biological centrifugation |
| Amount of substance | mol, mmol, nmol, pmol | 5 pmol | |

**Time units — always spell out in full:**

| Wrong | Correct |
|---|---|
| 0.5 h | 0.5 hour |
| 16 h | 16 hours |
| 30 min | 30 minutes |
| 2 hrs | 2 hours |

Singular vs plural: `1 hour`, `2 hours`, `0.5 hour` (fraction less than one takes singular).

**SI prefixes:**

| Prefix | Symbol | Factor |
|---|---|---|
| mega | M | 10⁶ |
| kilo | k | 10³ |
| milli | m | 10⁻³ |
| micro | μ | 10⁻⁶ |
| nano | n | 10⁻⁹ |
| pico | p | 10⁻¹² |
| femto | f | 10⁻¹⁵ |

### Exceptions — no space before symbol

**Percent (%):** no space between numeral and symbol.

| Wrong | Correct |
|---|---|
| 15 % | 15% |
| 74 % of proteins | 74% of proteins |

**Foot (′) and inch (″):** no space; values written together.

| Format    | Example |
| --------- | ------- |
| Feet only | 6′      |
| Combined  | 4′5″    |

**Note:** prefer SI in scientific manuscripts: convert feet/inches to metres or centimetres.

### Spell out unit names; do not abbreviate

When a unit is written as a word (not a symbol), spell it out fully. Abbreviated unit words with a period are not acceptable.

| Wrong | Correct |
|---|---|
| 4 ft. | 4 feet |
| 6 in. | 6 inches |
| 10 lbs. | 10 pounds |

SI unit *symbols* (μL, nm, kDa) are not abbreviations — they require no period. This is a separate rule.

### Gene names — always italic

*Italic*, species-dependent capitalisation. Never bold.

| Species | Format | Examples |
|---|---|---|
| Human | *Italic*, all uppercase | *TP53*, *BRCA1*, *EGFR* |
| Mouse / Rat | *Italic*, first letter uppercase, rest lowercase | *Trp53*, *Brca1*, *Egfr* |
| Zebrafish | *Italic*, all lowercase | *tp53*, *egfr* |
| Drosophila | *Italic*, all lowercase (dominant alleles: first letter uppercase) | *p53*, *Notch* |
| S. cerevisiae | *Italic*, all uppercase | *CDC28*, *TRP1* |

**Tip (italic = gene; roman = protein):** "*TP53* encodes the tumor suppressor protein TP53."

### Latin phrases — italic vs roman

**Common Latin abbreviations are roman.** They are used so frequently they are no longer treated as foreign words.

| Abbreviation | Full form | Italic? | Notes |
|---|---|---|---|
| et al. | *et alii* | ✗ Roman | No period after "et"; period after "al." only |
| i.e. | *id est* | ✗ Roman | "That is"; followed by comma: `(i.e., X)` |
| e.g. | *exempli gratia* | ✗ Roman | "For example"; followed by comma: `(e.g., X)` |
| *etc.* | *et cetera* | ✓ Italic | Italic by convention; avoid in scientific prose — prefer "and so on" |
| vs. | *versus* | ✗ Roman | Scientific writing: `vs.`; legal case names: `v.` (italic) |

**Complete Latin phrases remain italic** — they have no direct English equivalent.

| Phrase | Italic? | Example |
|---|---|---|
| in vitro | ✓ | "cells were cultured *in vitro*" |
| in vivo | ✓ | "*in vivo* tumor growth was measured" |
| ex vivo | ✓ | "*ex vivo* stimulation of splenocytes" |
| in situ | ✓ | "*in situ* hybridization" |
| de novo | ✓ | "*de novo* protein synthesis" |
| per se | ✓ | "not the method *per se*, but its application" |
| a priori | ✓ | "*a priori* hypothesis" |

**Decision rule:** has a standard English replacement ("that is", "for example") → **roman**. No natural English equivalent (*in vitro*, *de novo*) → **italic**.

### Statistical and analytical terms

| Term | Rule | Correct | Wrong |
|---|---|---|---|
| ***P*-value** | *P* uppercase, italic | *P* = 0.032; *P* < 0.05 | p-value, p = 0.032 |
| ***t*-test** | *t* lowercase, italic | *t*-test, Student's *t*-test | T-test, t test |
| ***m/z*** | Entire term italic | *m/z* range 350–1250 Th | m/z, M/Z |

Examples in context:
> The *m/z* range was set to 350–1250 Th.
> Differences were considered significant at *P* < 0.05 (paired *t*-test).

### Gene and protein capitalisation by species

| Species | Gene | Protein |
|---|---|---|
| Human | *ABCA1* — italic, all caps | ABCA1 — roman, all caps |
| Mouse | *Abca1* — italic, first letter cap | Abca1 — roman, first letter cap |

### Statistical symbols

| Symbol | Rule |
|---|---|
| *P* in *P*-value | Uppercase |
| *t* in *t*-test | Lowercase |
| *m/z* | All lowercase, italic |

### Unit symbols

| Symbol | Correct | Wrong |
|---|---|---|
| Litre | L, mL, μL | l, ml, μl |
| Kilodalton | kDa | KDa, kd, KD |
| Degree Celsius | °C | oc, 0C |
| Kelvin | K | °K |

### Greek letters — Unicode required

Always use the true Unicode character. Latin substitutes render incorrectly in typesetting and are rejected by journal submission systems.

| Character | Unicode | Wrong substitute | Context |
|---|---|---|---|
| μ (micro sign) | U+00B5 | u, mc | μm, μL, μg |
| α | U+03B1 | a | α-helix, α-tubulin |
| β | U+03B2 | b | β-actin, β-sheet |
| γ | U+03B3 | g | γ-H2AX, IFN-γ |
| ° (degree) | U+00B0 | o, 0 | °C |
| ± | U+00B1 | +/- | mean ± SD |
| × | U+00D7 | x | 1,000 × g |
| − (minus sign) | U+2212 | hyphen - | −20 °C |

**How to insert:**

| Tool | Method |
|---|---|
| Microsoft Word | Insert → Symbol; Alt+code (Windows); Character Viewer (Mac) |
| LaTeX | `\mu`, `\alpha`, `\times`, `\pm` — correct by default |
| Google Docs | Insert → Special characters |
| Mac | `⌃⌘Space` — Character Viewer |
| Windows | `Win+.` — emoji/symbol picker |

---

## 6. Voice Authenticity and Overclaim Check

A different kind of pass from §1-5: not a mechanical formatting rule, but a read for whether the *voice* is credible and the *claims* are proportionate to the evidence. Every fix here still obeys the "No invented data, and nothing new added" rule in §1: rephrase to a more natural, proportionate, correctly-hedged version of the *same* claim — never quietly drop what was claimed, and never strengthen or invent something to fill the gap left by cutting a hyped-up or padded phrase.

### AI-flavor markers (a watch list, not a ban list)

Several words and patterns have become disproportionately common in LLM-assisted or LLM-generated prose. Flag **density and pattern** — several clustering in a short span, or one word repeated mechanically as filler — not any single instance in isolation, since most of these are also completely ordinary formal scientific vocabulary on their own.

| Category | Examples | What to watch for |
|---|---|---|
| Stock transitional filler | "It is worth noting that," "It is important to note that," "Furthermore," "Moreover," "Additionally" | Used as connective glue on every paragraph rather than because a genuinely separate point follows — see §2 connective discipline |
| Generic praise-verbs | "underscores," "highlights," "showcases," "sheds light on," "paves the way for," "unveils," "elucidates," "delves into," "navigates," "boasts," "harnesses," "leverages" (as a verb) | Used repeatedly as filler rather than because it is the one precise word for the claim |
| Empty descriptors | "robust," "comprehensive," "holistic," "intricate," "multifaceted," "meticulous," "commendable," "pivotal," "crucial" | Applied generically rather than because the specific finding earns that specific weight |
| Formulaic structure | Repeated tricolon lists ("X, Y, and Z") across consecutive sentences; every paragraph opening with the same templated pattern ("This study demonstrates...", "Our findings reveal...") | Mechanical repetition of a structure rather than variation (see §3 sentence-length variation) |
| Overly smooth abstraction | A sentence that "explains" a finding in general terms with no specific number, comparison, or mechanism anchoring it | A known LLM tendency: plausible-sounding but information-free |

**How to apply:** fix by making the sentence more specific and concrete, tying it back to an actual number or finding *already in the manuscript* — never by inventing a specificity that wasn't there. If the only fix available would require new information, flag it instead of leaving in the vague filler.

### Exaggerated claims

| Word/phrase | Only justified when | Red flag |
|---|---|---|
| unprecedented / groundbreaking / revolutionary | Genuinely first-of-its-kind, with cited prior work showing nothing comparable existed | Used as a generic intensifier with no comparison to prior work |
| novel | The specific element that is new is named | Applied to a routine or incremental extension of an established method |
| paradigm-shifting / game-changing | Reserved for the rare claim the actual result truly supports at that scale | Used to describe an ordinary incremental finding |
| proves / demonstrates conclusively | A controlled, adequately powered, direct test | A single study, a small *n*, or an observational association |

**How to apply:** match the fix to the hedging-calibration table in §2 — replace the hype word with the calibrated strength (strong / moderate / weak) the actual evidence supports, don't just delete it and leave the claim's strength ambiguous.

### Causal overreach

The most common, most consequential overclaim in observational science: causal language implies a controlled or mechanistic test, and correlational or observational data only license associative language.

| Study design | Causal language ("causes," "drives," "leads to," "results in") | Correct framing |
|---|---|---|
| RCT / controlled intervention with a manipulated variable | Justified | "X reduced Y" |
| Knockout/rescue or other manipulate-and-measure experiment | Justified, for the manipulated relationship | "Loss of X reduced Y" |
| Cohort / cross-sectional / observational association | Not justified | "X was associated with Y" |
| Retrospective or registry-based study | Not justified | "X was linked to Y" |

Flag causal language mismatched to the study design even where the mismatch predates this pass (the manuscript already read that way) — this is a legitimate finding to surface, not something this skill introduced. Swapping the verb ("causes" → "is associated with") is a pure wording fix, squarely in scope, exactly like hedging calibration; but if it's genuinely unclear whether the design supports causal wording, flag it for the author rather than deciding unilaterally.

### Unnatural collocations

Word pairings a field expert would not produce — often a translation- or LLM-tell, distinct from the mechanical over-nominalization already covered in §4.

| Unnatural | Natural |
|---|---|
| "make a deep dive into" | "examine in detail" |
| "give a comprehensive elucidation of" | "explain" |
| "conduct an investigation into the intricate mechanism of" | "investigate the mechanism of" |
| "plays a pivotal role in orchestrating" | "regulates" (or the actual named role) |
| "serves as a testament to" | usually just delete — rarely adds information |
| "stands as a cornerstone of" | usually just delete, or state the actual relationship |

**How to apply:** read the sentence aloud (same test as §3's rhythm tip). If a phrase sounds like it is translating a concept rather than stating it plainly, or reads like marketing copy rather than a specific technical claim, replace it with the plain equivalent — removing padding, never adding new specificity that wasn't in the original.
