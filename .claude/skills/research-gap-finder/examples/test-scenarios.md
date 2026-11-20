# Test Scenarios for Research Gap Finder

## Scenario 1: Single Paper Analysis (Quick Test)

**Input**: Abstract of a machine learning paper
```
Title: "Deep Learning for Cancer Detection from Medical Images"

Abstract: "We developed a convolutional neural network (CNN) approach for detecting
cancer from medical images with 95% accuracy. Our method was tested on 10,000
images from a single hospital. Limitations include lack of external validation
and limited diversity in patient population. Future work should focus on
multi-center validation and integration with clinical workflows."
```

**Expected Output**:
- Identification of gaps: external validation, population diversity, clinical integration
- 2-3 hypotheses addressing these gaps
- Quality assessments with innovation/feasibility/impact scores
- Priority rankings

**Test Command**: "Analyze this abstract and find research gaps for cancer detection ML"

---

## Scenario 2: Multiple Papers Comparison

**Input**: Two papers on the same topic with different approaches

**Paper 1**: "Drug Discovery Using Traditional Methods"
**Paper 2**: "AI-Based Drug Discovery: A New Approach"

**Expected Output**:
- Comparative analysis of methodological approaches
- Identification of gaps between traditional and AI methods
- Hypotheses combining strengths of both approaches
- Interdisciplinary opportunities

**Test Command**: "Compare these two drug discovery approaches and find research gaps"

---

## Scenario 3: Literature Review in Specific Field

**Input**: User request for field analysis
```
User: "I'm interested in renewable energy storage research. What are the main
research gaps in battery technology for grid-scale applications?"
```

**Expected Output**:
- Overview of current battery technology landscape
- Identification of technical and application gaps
- Prioritized hypotheses for grid-scale storage
- Feasibility assessments considering current technology

**Test Command**: "Find research gaps in grid-scale battery storage technology"

---

## Scenario 4: PhD Research Planning

**Input**: Student planning doctoral research
```
User: "I'm starting a PhD in climate change adaptation. Can you help identify
research gaps and suggest hypotheses for doctoral-level research?"
```

**Expected Output**:
- Analysis suitable for PhD scope (3-5 year timeline)
- Feasible hypotheses with moderate resource requirements
- Innovation appropriate for doctoral contribution
- Strategic recommendations for research program

**Test Command**: "Suggest PhD-level research hypotheses in climate adaptation"

---

## Scenario 5: Grant Proposal Development

**Input**: Researcher preparing grant application
```
User: "I'm writing a grant on personalized medicine. Help me identify compelling
research gaps and high-impact hypotheses for funding consideration."
```

**Expected Output**:
- High-impact hypotheses with strong innovation scores
- Feasibility assessments suitable for grant timelines
- Impact predictions emphasizing scientific and practical value
- Strategic alignment with funding priorities

**Test Command**: "Generate high-impact hypotheses for personalized medicine grant"

---

## Quality Assessment Checklist

For each test scenario, verify:

### Output Completeness
- [ ] All identified gaps are categorized (methodological, theoretical, etc.)
- [ ] Each hypothesis has clear rationale
- [ ] Quality scores provided (innovation, feasibility, impact)
- [ ] Priority rankings included
- [ ] Strategic recommendations offered

### Output Quality
- [ ] Hypotheses are testable and scientifically sound
- [ ] Innovation scores reflect genuine novelty
- [ ] Feasibility assessments are realistic
- [ ] Impact predictions are justified
- [ ] Recommendations are actionable

### Format Compliance
- [ ] Markdown report is well-structured
- [ ] JSON output is properly formatted (if requested)
- [ ] Template sections are properly filled
- [ ] References to scoring framework are accurate

### User Experience
- [ ] Analysis depth appropriate for request
- [ ] Output length suitable for complexity
- [ ] Recommendations are relevant to user context
- [ ] Language is clear and accessible

---

## Testing Procedure

1. **Start with Scenario 1** (simplest test)
2. **Verify basic functionality** works correctly
3. **Progress to more complex scenarios**
4. **Test edge cases** (very short/long inputs, mixed quality sources)
5. **Validate output quality** against checklist
6. **Document any issues** or improvements needed

## Expected Performance

- **Quick Scan**: 5-10 minutes processing time
- **Standard Analysis**: 15-20 minutes processing time
- **Comprehensive Analysis**: 30+ minutes processing time

**Output Quality**: All hypotheses should be scientifically valid and clearly connected to identified research gaps.

---

Use these scenarios to validate the skill's performance across different use cases and complexity levels.