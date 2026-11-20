# 🔬 Research Gap Finder & Hypothesis Generator

<div align="center">

**An AI Agent skill for systematic literature analysis, research gap identification, and hypothesis generation**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Claude Code](https://img.shields.io/badge/Claude-Code-orange.svg)](https://claude.com/claude-code)
[![Status](https://img.shields.io/badge/Status-Production--Ready-brightgreen.svg)]()

</div>

---

## 🌟 Overview

**Research Gap Finder** is a specialized AI Agent skill that automatically analyzes scientific literature to identify research gaps and generate scientifically rigorous, testable hypotheses with multi-dimensional quality assessments.

### 🎯 What It Does

- 🔍 **Systematic Gap Analysis** - Identifies methodological, theoretical, application, and interdisciplinary research gaps
- 💡 **Intelligent Hypothesis Generation** - Creates testable hypotheses with innovation, feasibility, and impact scoring
- 📊 **Multi-Format Output** - Generates comprehensive Markdown reports and structured JSON data
- 🎓 **Flexible Analysis Modes** - Quick scan (5-10 min), Standard (15-20 min), or Comprehensive (30+ min)

---

## ✨ Key Features

### 🔬 Systematic Research Gap Identification
- **Methodological Gaps**: Sample limitations, measurement constraints, design boundaries
- **Theoretical Gaps**: Incomplete frameworks, unexplained phenomena, contradictions
- **Application Gaps**: Translation barriers, population restrictions, scale-up challenges
- **Interdisciplinary Opportunities**: Cross-domain applications, technology transfer

### 💡 Multi-Dimensional Hypothesis Quality Assessment
- **Innovation Score** (1-5): Originality and creativity evaluation
- **Feasibility Score** (1-5): Technical and resource viability assessment
- **Impact Score** (1-5): Scientific and practical value prediction
- **Priority Ranking**: High/Medium/Low categorization for research planning

### 🌐 Flexible Input Support
- **Single PDF Papers**: Deep analysis of individual research articles
- **Multiple Papers**: Comparative literature synthesis
- **Text Abstracts**: Quick analysis from summaries
- **Field Analysis**: Domain-wide research evaluation

---

## 🚀 Quick Start

### Installation

1. **Clone this repository** to your Claude skills directory:
```bash
git clone https://github.com/LengFeng00/research-gap-finder.git ~/.claude/skills/research-gap-finder
```

2. **Verify installation**:
```bash
ls ~/.claude/skills/research-gap-finder/
```

Expected output:
```
SKILL.md  README.md  examples/  references/  templates/
```

### Basic Usage

Simply start using the skill in your Claude Code conversations:

```
User: [Upload research paper PDF]
User: "Analyze this paper and find research gaps"

AI: [Activates Research Gap Finder skill]
AI: [Comprehensive analysis with gaps and hypotheses]
```

### Example Workflows

**Single Paper Analysis**:
```
"Analyze this cancer research paper and identify research gaps"
```

**Literature Review**:
```
"Compare these three papers on machine learning and find common research gaps"
```

**Research Planning**:
```
"I'm planning a PhD in renewable energy. What are the research gaps?"
```

---

## 📁 Project Structure

```
research-gap-finder/
├── SKILL.md                              # Main skill definition
├── README.md                             # This file
├── LICENSE                               # MIT License
├── .gitignore                            # Git ignore rules
│
├── examples/
│   └── test-scenarios.md                 # Test cases and validation examples
│
├── references/
│   └── hypothesis-scoring-guide.md       # Quality assessment framework
│
└── templates/
    └── analysis-report-template.md      # Output format template
```

---

## 📊 Example Output

### Research Gap Analysis Report

```markdown
# Research Gap Analysis & Hypothesis Generation

## Executive Summary
Identified 12 research gaps across methodological, theoretical, and
application domains. Generated 8 prioritized hypotheses with quality
assessments.

## Key Research Gaps

### 🔬 Methodological Gap: Incomplete Functional Annotation
**Severity**: HIGH
60-80% of dispensable genes lack functional annotation, limiting
biological interpretation and breeding applications.

### 💡 Top Hypothesis: ML-Based Function Prediction
**Innovation**: 5/5 | **Feasibility**: 3/5 | **Impact**: 5/5

"Deep learning models can predict functions for uncharacterized
dispensable genes using sequence features and genomic context."

**Suggested Methodology**:
- Multi-task deep learning with protein language models
- Transfer learning from general protein models
- Experimental validation of top predictions

## Priority Recommendations
1. ✅ Immediate: Environmental adaptation study ($500K-$1M)
2. ✅ High-Impact: ML function prediction platform ($2M-$3M)
3. ✅ Practical: Genomic selection integration ($300K-$700K)
```

---

## 🎓 Use Cases

### 👨‍🔬 For Researchers
- **Literature Reviews**: Systematic gap identification for review articles
- **Grant Writing**: Strong justification based on identified gaps
- **Research Planning**: Data-driven hypothesis generation for projects

### 🌱 For PhD Students
- **Topic Selection**: Identify understudied areas with high impact potential
- **Thesis Planning**: Generate testable hypotheses aligned with expertise
- **Literature Analysis**: Comprehensive understanding of research landscape

### 🏢 For Research Institutions
- **Strategic Planning**: Identify high-impact research directions
- **Resource Allocation**: Prioritize research based on feasibility and impact
- **Collaboration Opportunities**: Discover interdisciplinary connections

### 🧪 For Industry R&D
- **Technology Assessment**: Evaluate research gaps in target domains
- **Innovation Pipeline**: Generate ideas for R&D projects
- **Competitive Intelligence**: Understand research landscape and opportunities

---

## 🛠️ Technical Details

### Analysis Frameworks

**Gap Identification Systematic Frameworks**:
- Methodological limitation analysis
- Theoretical contradiction detection
- Application barrier assessment
- Interdisciplinary opportunity mapping

**Hypothesis Quality Assessment**:
- Multi-dimensional scoring (innovation, feasibility, impact)
- Priority ranking algorithm
- Risk assessment framework
- Success metric definition

### Output Formats

**Markdown Report** (Human-readable):
- Executive summary
- Detailed gap analysis
- Prioritized hypotheses
- Strategic recommendations

**JSON Data** (Machine-readable):
- Structured gap classifications
- Quantified hypothesis assessments
- Metadata and provenance
- Integration-ready format

---

## 🧪 Testing

Run the test scenarios to validate installation:

```bash
# View test scenarios
cat ~/.claude/skills/research-gap-finder/examples/test-scenarios.md

# Test with Claude Code
claude "Analyze this abstract: [paste abstract]"
```

### Sample Test Cases

1. **Single Paper Analysis**: Cancer detection ML research
2. **Multiple Papers Comparison**: Drug discovery approaches
3. **Literature Review**: Renewable energy storage
4. **PhD Planning**: Climate change adaptation
5. **Grant Proposal**: Personalized medicine

---

## 📈 Performance Metrics

- **Quick Scan**: 5-10 minutes (3-5 gaps, 2-3 hypotheses)
- **Standard Analysis**: 15-20 minutes (5-10 gaps, 3-5 hypotheses)
- **Comprehensive**: 30+ minutes (10-20 gaps, 5-10 hypotheses)

**Quality Assurance**:
- ✅ All hypotheses are scientifically testable
- ✅ Innovation scores reflect genuine novelty
- ✅ Feasibility assessments consider realistic constraints
- ✅ Impact predictions are justified with reasoning

---

## 🤝 Contributing

Contributions are welcome! Areas for improvement:

- 🌐 **Multi-language Support**: Add support for non-English literature
- 📊 **Visualization**: Add gap and hypothesis visualization tools
- 🔗 **Integration**: Connect with literature databases (PubMed, arXiv)
- 🤖 **ML Enhancement**: Improve function prediction accuracy
- 📱 **Web Interface**: Develop standalone web application

### Development Setup

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

---

## 📚 Documentation

- **[SKILL.md](SKILL.md)** - Complete technical specification
- **[Hypothesis Scoring Guide](references/hypothesis-scoring-guide.md)** - Quality assessment framework
- **[Test Scenarios](examples/test-scenarios.md)** - Validation examples
- **[Report Template](templates/analysis-report-template.md)** - Output format reference

---

## 🗺️ Roadmap

### Version 1.1 (Q2 2026)
- [ ] Enhanced ML function prediction
- [ ] Integration with literature databases
- [ ] Interactive web interface
- [ ] Multi-language PDF support

### Version 2.0 (Q4 2026)
- [ ] Real-time collaboration features
- [ ] Advanced visualization dashboards
- [ ] API for programmatic access
- [ ] Community database of gaps and hypotheses

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- Built for **Claude Code** by Anthropic
- Inspired by systematic review methodologies
- Developed with the global scientific research community

---

## 📞 Contact & Support

- **Issues**: [GitHub Issues](https://github.com/LengFeng00/research-gap-finder/issues)
- **Discussions**: [GitHub Discussions](https://github.com/LengFeng00/research-gap-finder/discussions)
- **Email**: lengfeng@example.com

---

## ⭐ Show Your Support

If you find this skill useful, please consider:
- ⭐ Starring the repository
- 🍴 Forking for your own use
- 📢 Sharing with colleagues
- 💡 Contributing improvements

---

<div align="center">

**Built with ❤️ for the global scientific research community**

[⬆ Back to Top](#-research-gap-finder--hypothesis-generator)

</div># research-gap-finder
