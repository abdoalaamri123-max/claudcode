# Research Gap Finder - Installation & Usage Guide

## Overview

The **Research Gap Finder** skill helps AI Agents systematically analyze scientific literature to identify research gaps and generate scientifically rigorous hypotheses with quality assessments.

## Installation

The skill is already installed in your Claude skills directory:
```
~/.claude/skills/research-gap-finder/
```

## Quick Start

### Basic Usage

Simply upload a research paper (PDF) or provide an abstract and ask for analysis:

```
User: "Can you analyze this paper and identify research gaps?"
User: "Find research gaps in this literature"
User: "Generate hypotheses based on these papers"
User: "Evaluate the progress in this research area"
```

### Input Types Supported

1. **Single PDF Paper**: Deep dive into one research paper
2. **Multiple Papers**: Comparative analysis across studies
3. **Text Abstracts**: Quick analysis of paper summaries
4. **Literature Collection**: Comprehensive field analysis

## Features

### 🔍 Systematic Gap Identification
- Methodological limitations
- Theoretical contradictions
- Application gaps
- Interdisciplinary opportunities

### 💡 Intelligent Hypothesis Generation
- Testable and scientifically valid hypotheses
- Multi-dimensional quality assessment:
  - Innovation Score (1-5)
  - Feasibility Score (1-5)
  - Impact Score (1-5)
  - Overall Priority Ranking

### 📊 Comprehensive Output
- Structured Markdown reports
- JSON-formatted data for programmatic use
- Priority rankings and strategic recommendations

### ⚙️ Flexible Analysis Modes
- **Quick Scan** (5-10 min): Overview of major gaps
- **Standard Analysis** (15-20 min): Detailed gap identification
- **Comprehensive** (30+ min): Extensive analysis with interdisciplinary insights

## Example Workflows

### Example 1: Single Paper Analysis
```
User: Uploads paper.pdf
User: "Analyze this paper and find research gaps"

Skill Output:
- Executive summary of main findings
- 5-7 research gaps categorized by type
- 3-5 prioritized hypotheses with quality scores
- Suggested next steps and methodology recommendations
```

### Example 2: Comparative Literature Analysis
```
User: Uploads paper1.pdf, paper2.pdf, paper3.pdf
User: "Compare these papers and identify common research gaps"

Skill Output:
- Cross-study synthesis of findings
- Recurring limitations across papers
- Convergent and divergent research directions
- Meta-analysis opportunities and field evolution insights
```

### Example 3: Research Planning
```
User: "I'm planning a PhD in machine learning for healthcare. What are the research gaps?"

Skill Output:
- Current state of the field analysis
- Priority research directions ranked by feasibility and impact
- Hypotheses suitable for doctoral research scope
- Resource requirements and collaboration opportunities
```

## Output Formats

### Markdown Report (Human-Readable)
- Executive summary
- Detailed gap analysis
- Prioritized hypotheses with quality assessments
- Strategic recommendations

### JSON Data (Machine-Readable)
```json
{
  "analysis_metadata": {...},
  "research_gaps": [...],
  "hypotheses": [...],
  "priority_rankings": [...]
}
```

## Customization Options

### Analysis Depth
Specify your preferred analysis level:
- "Quick scan" for overview
- "Standard analysis" (default) for detailed review
- "Comprehensive analysis" for in-depth exploration

### Focus Areas
Request specific types of analysis:
- "Focus on methodological gaps"
- "Emphasize interdisciplinary opportunities"
- "Prioritize clinically relevant gaps"

### Output Preferences
- "Give me both report and JSON output"
- "Focus on high-impact hypotheses only"
- "Include detailed feasibility assessments"

## Best Practices

### For Optimal Results
1. **Provide clear input**: High-quality PDFs or complete abstracts
2. **Specify context**: Mention your research area and constraints
3. **Indicate depth**: Choose appropriate analysis mode for your needs
4. **Follow up**: Use generated hypotheses as starting points for deeper literature review

### Quality Assurance
- All hypotheses require validation with domain experts
- Innovation scores should be evaluated against your expertise
- Feasibility assessments should consider your specific resources
- Impact predictions should be validated with stakeholder input

### Ethical Considerations
- Review suggested research for ethical implications
- Ensure proposed methods align with institutional standards
- Consider societal impact of research directions
- Evaluate inclusivity and diversity in research design

## Troubleshooting

**Issue**: "Too many hypotheses generated"
**Solution**: Filter by high feasibility scores and your expertise area

**Issue**: "Hypotheses seem too obvious"
**Solution**: Request comprehensive analysis mode for deeper insights

**Issue**: "Limited gap identification"
**Solution**: Provide more diverse papers or specify particular research aspects

**Issue**: "Feasibility scores don't match my resources"
**Solution**: Provide context about your available resources and constraints

## Advanced Features

### Temporal Analysis
Track how research questions evolve over time and identify persistent vs. emerging gaps.

### Interdisciplinary Mapping
Identify opportunities to apply methods from adjacent fields to your research area.

### Collaboration Suggestions
Get recommendations for potential collaborations based on identified gaps.

### Field Evolution Insights
Understand the trajectory of research areas and predict future directions.

## Limitations

- Does not replace expert domain knowledge
- Hypotheses require literature validation
- Feasibility assessments are estimates
- Impact predictions are speculative

## Support & Enhancement

For questions or improvement suggestions, refer to the skill documentation:
- SKILL.md: Complete skill specification
- references/hypothesis-scoring-guide.md: Quality assessment framework
- templates/analysis-report-template.md: Output format reference

---

**Version**: 1.0
**Last Updated**: 2026-03-22
**Compatibility**: Claude Code with PDF reading capability