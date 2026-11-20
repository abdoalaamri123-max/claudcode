---
name: research-gap-finder
description: Analyze scientific literature to identify research gaps and generate testable hypotheses. Use when users upload research papers (PDF), ask to "find research gaps", "generate hypotheses", "analyze literature", or "evaluate field progress". Automatically triggers for scientific paper analysis, literature review synthesis, and hypothesis generation tasks. Works with single papers, multiple papers, or text abstracts.
compatibility: Requires PDF reading capability (Read tool with PDF support), optional web access for citation lookup
---

# Research Gap Finder & Hypothesis Generator

A specialized skill for identifying research gaps and generating scientifically rigorous hypotheses from academic literature.

## Core Capabilities

This skill helps you:
- **Identify Research Gaps**: Methodological limitations, unexplored variables, theoretical contradictions, technical application gaps, interdisciplinary opportunities
- **Generate Testable Hypotheses**: Create scientifically valid, innovative, and impactful research hypotheses
- **Analyze Literature Depth**: From quick scans to comprehensive analysis
- **Evaluate Field Progress**: Assess the current state and future directions of research domains

## Analysis Process

### Phase 1: Input Analysis (5-10 minutes)

#### For Single Papers:
1. **Extract Key Information**
   - Research questions and objectives
   - Methodology and experimental design
   - Main findings and conclusions
   - Acknowledged limitations
   - Future work suggestions

2. **Identify Explicit Limitations**
   - Sample size and population constraints
   - Methodological boundaries
   - Technical limitations
   - Scope restrictions

#### For Multiple Papers:
1. **Synthesize Across Studies**
   - Common methodological approaches
   - Recurring limitations across studies
   - Contradictory findings
   - Temporal evolution of research
   - Geographic/cultural variations

### Phase 2: Gap Identification (5-10 minutes)

Use these systematic frameworks:

#### Methodology Gaps
- Measurement limitations (accuracy, precision, validity)
- Sample constraints (size, diversity, representativeness)
- Design limitations (correlation vs. causation, short-term vs. long-term)
- Technical constraints (equipment, computational power, analytical methods)

#### Theoretical Gaps
- Incomplete theoretical frameworks
- Unexplained phenomena
- Contradictory theoretical predictions
- Missing mediators or moderators
- Over-simplified models

#### Application Gaps
- Laboratory findings not translated to real-world settings
- Missing population subgroups
- Geographic or cultural limitations
- Scale-up challenges
- Integration with existing systems

#### Interdisciplinary Gaps
- Opportunities to apply methods from other fields
- Untapped theoretical frameworks from adjacent disciplines
- Cross-domain research opportunities
- Technology transfer possibilities

### Phase 3: Hypothesis Generation (5-10 minutes)

For each identified gap, generate hypotheses using this framework:

#### Hypothesis Structure
```
Hypothesis: [Clear, testable statement]

Rationale:
- Based on: [Existing evidence + identified gap]
- Novelty: [What makes this innovative]
- Testability: [How it can be experimentally validated]

Quality Assessment:
- Innovation Score (1-5): [Originality and creativity]
- Feasibility Score (1-5): [Practical implementation considerations]
- Impact Score (1-5): [Potential scientific and practical value]
- Overall Priority: [High/Medium/Low]
```

#### Hypothesis Quality Criteria

**1. Testability (Required)**
- Clearly defined variables
- Measurable outcomes
- Achievable experimental design
- Realistic resource requirements

**2. Innovation Scoring**
- 1 = Incremental improvement on existing work
- 2 = New application of established methods
- 3 = Novel combination of existing approaches
- 4 = Significant methodological or theoretical advance
- 5 = Paradigm-shifting research direction

**3. Feasibility Assessment**
- Technical feasibility: Available methods and tools
- Resource feasibility: Time, budget, expertise requirements
- Ethical feasibility: IRB approval, safety considerations
- Practical feasibility: Sample access, equipment availability

**4. Impact Prediction**
- Scientific impact: Contribution to fundamental knowledge
- Practical impact: Real-world applications and benefits
- Societal impact: Potential for positive change
- Field impact: Influence on future research directions

## Output Format

### Executive Summary (Markdown Report)
```markdown
# Research Gap Analysis & Hypothesis Generation

## Document Information
- **Input**: [Paper titles or abstract]
- **Analysis Date**: [Date]
- **Analysis Depth**: [Standard/Comprehensive]

## Key Findings Summary
[Brief overview of main gaps and opportunities]

## Detailed Analysis

### 1. Research Gaps Identified
[Methodological, theoretical, application, interdisciplinary gaps]

### 2. Hypotheses Generated
[Ranked list with quality assessments]

### 3. Priority Recommendations
[Top 3-5 most promising research directions]

### 4. Next Steps
[Experimental design suggestions, collaboration opportunities, funding priorities]
```

### Structured Data (JSON)
```json
{
  "analysis_metadata": {
    "input_type": "single_paper|multiple_papers|abstract",
    "analysis_depth": "standard|comprehensive",
    "date": "ISO date",
    "papers_analyzed": ["paper1", "paper2"]
  },
  "research_gaps": [
    {
      "category": "methodological|theoretical|application|interdisciplinary",
      "description": "Gap description",
      "severity": "high|medium|low",
      "evidence_base": ["supporting citations"]
    }
  ],
  "hypotheses": [
    {
      "statement": "Testable hypothesis",
      "rationale": "Scientific justification",
      "quality_assessment": {
        "innovation_score": 1-5,
        "feasibility_score": 1-5,
        "impact_score": 1-5,
        "overall_priority": "high|medium|low"
      },
      "suggested_methodology": "Experimental approach"
    }
  ],
  "priority_rankings": ["hypothesis_ids in priority order"]
}
```

## Usage Guidelines

### Standard Analysis Mode (Default)
- Processing time: 15-20 minutes
- Output: 5-10 research gaps, 3-5 prioritized hypotheses
- Depth: Methodological and theoretical gap analysis
- Use for: Literature reviews, grant proposal background, research planning

### Comprehensive Analysis Mode (Opt-in)
- Processing time: 30+ minutes
- Output: 10-20 research gaps, 5-10 prioritized hypotheses
- Depth: Includes interdisciplinary gaps and extensive literature synthesis
- Use for: Major grant applications, PhD research planning, lab strategy development

### Quick Scan Mode (Opt-in)
- Processing time: 5-10 minutes
- Output: 3-5 major gaps, 2-3 top hypotheses
- Depth: Focus on explicit limitations and obvious gaps
- Use for: Initial literature exploration, meeting preparation

## Best Practices

### Input Preparation
- For PDFs: Ensure high-quality, readable text
- For multiple papers: Organize by relevance or theme
- For abstracts: Include complete abstracts with key findings

### Interpretation Guidelines
- Prioritize hypotheses with high innovation AND feasibility scores
- Look for gaps that appear across multiple papers
- Consider your own expertise and resources when evaluating feasibility
- Validate hypotheses against existing literature before experimental design

### Quality Assurance
- All hypotheses must be testable with current or near-future technology
- Innovation scores should be justified with specific reasoning
- Feasibility assessments should consider realistic resource constraints
- Impact predictions should balance scientific and practical value

## Advanced Features

### Comparative Analysis
When analyzing multiple papers, the skill will:
- Identify convergence and divergence in findings
- Detect methodological trends across studies
- Highlight replication opportunities
- Suggest meta-analysis approaches

### Field Evolution Tracking
For temporal analysis:
- Trace how research questions have evolved
- Identify solved vs. persistent problems
- Detect emerging trends and technologies
- Predict future research directions

### Interdisciplinary Mapping
- Identify relevant methods from adjacent fields
- Suggest theoretical framework imports
- Highlight technology transfer opportunities
- Propose collaboration opportunities

## Limitations and Considerations

### Scope Boundaries
- Does not replace expert domain knowledge
- Hypotheses require validation with literature search
- Feasibility assessments are estimates, not guarantees
- Impact predictions are speculative and should be treated as such

### Quality Dependencies
- Output quality depends on input paper quality
- Requires accurate PDF text extraction
- Assumes papers report limitations honestly
- May miss gaps requiring specialized domain expertise

### Ethical Considerations
- Consider ethical implications of suggested research
- Ensure hypotheses align with responsible research practices
- Evaluate potential societal impacts of research directions
- Consider inclusion and diversity in research design

## Troubleshooting

### Common Issues

**Problem**: Too many hypotheses generated
**Solution**: Filter by high feasibility scores and alignment with expertise

**Problem**: Hypotheses seem too obvious
**Solution**: Request comprehensive analysis mode for deeper insights

**Problem**: Limited gap identification
**Solution**: Provide more diverse papers or specify particular research aspects

**Problem**: Feasibility scores seem inaccurate
**Solution**: Provide context about available resources and expertise

## Example Workflow

```
User: "Analyze this paper and find research gaps"

[Skill activation: Standard analysis mode]

1. Extract paper details (methods, findings, limitations)
2. Apply systematic gap identification framework
3. Generate 5-7 hypotheses with quality assessments
4. Produce both markdown report and JSON output
5. Rank by priority and suggest next steps

Output: Comprehensive analysis with prioritized hypotheses
```

---

**Remember**: This skill augments but does not replace human scientific expertise. Always validate hypotheses with domain experts and extensive literature review before committing significant research resources.