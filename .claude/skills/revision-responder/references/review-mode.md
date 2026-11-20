# Review Mode

Read this when the user wants an existing response letter checked, audited, or improved rather than drafted. The job is to act as a careful pre-submission reader of the response letter: does it do what a good response letter must, and does the revised manuscript actually contain what the letter claims?

## Inputs

1. **The revised manuscript** (the version that goes with this letter).
2. **The response letter** to audit.

If the manuscript is missing you can still assess structure, tone, coverage, and format, but you cannot verify that claimed changes exist, so say that verification was not possible and flag it.

## What to check

Grade the letter against the good-response-letter standard, and verify claims against the manuscript.

**Standard (structure and craft):**
- Opens with a brief thank you to the editor and reviewers.
- Each comment is repeated exactly, with no paraphrasing, followed immediately by the response.
- Every claimed change is traceable: either the revised text is quoted (italics or block quote) or, under Nature Portfolio / Scientific Reports pointer style, the letter points precisely to where the change now sits. A precise pointer counts as satisfying this; do not flag a correctly pointer-styled letter for "not quoting".
- Responses are separated by reviewer and editor for clarity.
- Formatted for readability. Long is acceptable; hard to follow is not.

**Coverage:**
- Every editor and reviewer comment has a response. Count comments against responses and name any that are missing.
- Any point not acted on has a brief, reasonable rationale rather than silence.

**Verification against the manuscript (the core of the audit):**
- For each claimed change, open the cited location in the revised manuscript and confirm the change is actually there and matches what the response says. Mark each as verified, mismatched (letter and manuscript disagree), or not found (claimed location has no such change).
- Flag any location reference that is vague enough that you cannot check it.
- Never invent a verification you did not perform; if you could not locate something, say "could not verify", not "verified".

**Tone:**
- Soft, collaborative, professional. Flag anything combative, dismissive, or defensive, and anything that blames a reviewer for misunderstanding.
- Where the letter disagrees with a reviewer, check that it does so respectfully and with an explained, evidence-based rationale.

## Outputs

Produce two artifacts.

**1. Summary.** A short narrative (a paragraph or a few) giving the overall assessment: is the letter submission-ready, and if not, what are the highest-impact fixes? Lead with the most serious issues (missing responses, unverifiable or false claims, combative tone), then lesser ones. Be candid but constructive; the goal is to help the letter pass.

**2. Point-by-point evaluation checklist.** One row per numbered comment, so the author sees exactly where each response stands:

```
## Per-comment evaluation

| Comment | Responded? | Verified in manuscript | Tone | Notes / fixes |
|---------|-----------|------------------------|------|---------------|
| E.1  | yes | verified            | ok       | Clear; matches p.14. |
| R1.1 | yes | verified            | ok       | Good, concise. |
| R1.2 | yes | mismatch            | ok       | Letter says Fig 2 updated; manuscript shows no change to Fig 2. Reconcile. |
| R1.3 | yes | not found           | ok       | Cites "Sec 3.4 lines 300-310" but that text is unchanged. Check location. |
| R2.1 | no  | n/a                 | n/a      | No response found. Add one. |
| R2.2 | yes | verified            | combative| Rephrase: "the reviewer is wrong" -> explain the evidence respectfully. |
```

Verification vocabulary: `verified`, `mismatch`, `not found`, `could not verify`, `n/a`. Any value other than `verified` needs a note with the specific fix. Close with a one-line readiness verdict (for example: "3 issues to resolve before submission: one missing response, one mismatch, one location to correct").

This per-comment table is the Review-mode deliverable; pair it with the summary above.
