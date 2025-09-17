# Claude Code Writing Squad

A multi-agent writing system designed to iteratively process and refine text through specialized editing agents. Each agent focuses on a specific aspect of writing improvement, working together to produce polished, professional content.

## Overview

This system processes text through a series of specialized agents, each with a specific role in improving different aspects of writing quality. The agents work in sequence, with each agent's output becoming the input for the next agent in the pipeline.

## Agent Configurations

### Core Editing Agents

#### 1. [Basic Typo Reviewer](./agents/basic-typo-reviewer.md)
**Purpose**: Surface-level corrections  
**Function**: Corrects typos, spelling mistakes, punctuation, capitalization, and spacing while preserving the author's voice and meaning.

#### 2. [UK English Standardiser](./agents/uk-english-standardiser.md)
**Purpose**: Regional language standardization  
**Function**: Converts text to UK English standards, including spelling, vocabulary, punctuation, and formatting while maintaining meaning and tone.

#### 3. [Flow and Polish](./agents/flow-and-polish.md)
**Purpose**: Structural flow and readability  
**Function**: Improves logical progression, readability, and consistency of tone while ensuring smooth transitions between sections.

#### 4. [Headings](./agents/headings.md)
**Purpose**: Document structure  
**Function**: Generates, reviews, and refines subheadings to create clear, logical sections that support readability and comprehension.

#### 5. [Proofreader](./agents/proofreader.md)
**Purpose**: Fact verification and source linking  
**Function**: Verifies facts and statistics, corrects inaccuracies, and inserts precise inline Markdown links for claims requiring sources.

#### 6. [Add Sources](./agents/add-sources.md)
**Purpose**: Source integration  
**Function**: Integrates reliable sources by inserting inline Markdown links at factual claims while preserving document structure and tone.

#### 7. [SEO Reviewer](./agents/seo-reviewer.md)
**Purpose**: Search engine optimization  
**Function**: Applies minimal, high-precision edits to improve organic search performance without altering flow, voice, or narrative structure.

## Processing Flow

The recommended processing order is:

1. **Basic Typo Reviewer** - Clean up surface-level errors
2. **UK English Standardiser** - Standardize to UK English
3. **Flow and Polish** - Improve readability and logical flow
4. **Headings** - Structure the document with clear headings
5. **Proofreader** - Verify facts and add sources
6. **Add Sources** - Enhance source integration
7. **SEO Reviewer** - Final SEO optimization

## Usage

### Manual Processing
Each agent configuration can be used individually by copying the prompt from the respective markdown file and applying it to your text.

### Automated Processing
Use the `process_text.py` script to automatically process text through the entire agent pipeline:

```bash
python3 process_text.py
```

This script will:
1. Read text from `input.md`
2. Process it through each agent in sequence
3. Save the final result to `output.md`
4. Save intermediate results for review

## File Structure

```
Claude-Code-Writing-Squad/
├── README.md                           # This file
├── agents/                             # Agent configuration files
│   ├── basic-typo-reviewer.md
│   ├── uk-english-standardiser.md
│   ├── flow-and-polish.md
│   ├── headings.md
│   ├── proofreader.md
│   ├── add-sources.md
│   └── seo-reviewer.md
├── process_text.py                     # Automated processing script
├── input.md                           # Input text file
└── output.md                          # Final processed output
```

## Agent Characteristics

- **Autonomous Operation**: All agents work independently without requiring user approval
- **Meaning Preservation**: Each agent maintains the original intent and message
- **Collaborative Design**: Agents are designed to work together in sequence
- **Markdown Focus**: All agents handle Markdown formatting appropriately
- **Direct Output**: Agents return processed text without commentary or explanations

## Getting Started

1. Place your text in `input.md`
2. Run `python3 process_text.py`
3. Review the processed output in `output.md`
4. Check intermediate files if you need to see the progression through each agent

## Contributing

When adding new agents or modifying existing ones:
- Ensure agents work autonomously without user interaction
- Maintain compatibility with Markdown formatting
- Preserve meaning and authorial intent
- Follow the established pattern of direct text output
- Update this README with any new agents or changes to the processing flow
