# notspoonfed

A local-first, AI-powered learning system that transforms study material into structured, question-driven learning experiences.

> **Status:** Early development — Day 3 of a 100-day build.

## What is notspoonfed?

notspoonfed is an experimental learning platform built around a simple idea:

**Don't just summarize study material — learn it through questions.**

The long-term goal is to allow a learner to upload lecture notes or PDFs and turn them into structured learning material containing:

* concise notes
* important concepts
* conceptual questions
* answers and explanations
* difficulty levels
* concept-level practice
* weakness detection
* targeted follow-up questions
* revision and mastery tracking

The first version is being built as a **fully local application**, allowing the core AI features to run without paid API credits.

---

## Current Pipeline

As of Day 3:

```text
Lecture Notes
      │
      ▼
Python Backend
      │
      ▼
Prompt / Grounding
      │
      ▼
Ollama
      │
      ▼
Qwen3:4b
      │
      ▼
Structured JSON
      │
      ▼
Pydantic Validation
      │
      ▼
LearningMaterial
      │
      ├── Topic
      ├── Summary
      ├── Key Points
      └── Questions
            ├── Question
            ├── Answer
            ├── Explanation
            ├── Difficulty
            └── Concept
```

---

## Tech Stack

Current:

* **Python**
* **Ollama**
* **Qwen3:4b**
* **Pydantic**

Planned technologies will be introduced incrementally as the project grows.

The project intentionally starts small rather than implementing the complete architecture from the beginning.

---

## Project Structure

```text
notspoonfed/
├── backend/
│   ├── ai_service.py
│   ├── schemas.py
│   ├── test_ai.py
│   ├── test_notes.py
│   └── requirements.txt
│
├── data/
│
├── docs/
│   └── progress.md
│
├── uploads/
│
├── .gitignore
└── README.md
```

The frontend, database, PDF processing, retrieval system and other components will be introduced later.

---

# Development Progress

## Day 1 — Local AI Foundation

### Goal

Establish communication between Python and a locally running language model.

### Completed

* Created the initial project structure.
* Created a Python virtual environment.
* Installed the Ollama Python client.
* Configured **Qwen3:4b** as the initial local language model.
* Connected Python to Ollama.
* Successfully sent prompts from Python to the local model.
* Confirmed that AI generation works without paid API credits.

### Initial Pipeline

```text
Python
   ↓
Ollama
   ↓
Qwen3:4b
   ↓
AI Response
```

### Key Learning

The language model is not part of the Python application itself.

Python acts as the application layer while Ollama runs and serves the local model.

---

## Day 2 — Structured Learning Material

### Goal

Move from unrestricted text generation to predictable structured educational output.

### Completed

* Added `schemas.py`.
* Created Pydantic models for learning material.
* Added a `Question` model.
* Added a `LearningMaterial` model.
* Created `ai_service.py`.
* Implemented `generate_learning_material()`.
* Used the Pydantic JSON schema to request structured output from Qwen.
* Validated model responses using Pydantic.
* Generated structured learning material from CS topics.
* Added concept identification for individual questions.

### Data Model

```text
LearningMaterial
│
├── topic
├── summary
├── key_points[]
│
└── questions[]
      │
      ├── question
      ├── answer
      ├── explanation
      ├── difficulty
      └── concept
```

### Example

Input:

```text
Operator Precedence
```

Output structure:

```text
Topic
Summary
Key Points

Question 1
├── Answer
├── Explanation
├── Difficulty
└── Concept

Question 2
...

Question 3
...
```

### Key Learning

Structured output guarantees the **shape of the response**, not necessarily its correctness.

For example, the model can successfully produce:

```json
{
  "difficulty": "hard"
}
```

while the generated question may not actually be difficult.

Content quality and structural validity are separate problems.

---

## Day 3 — Grounding AI in Lecture Notes

### Goal

Generate learning material using supplied lecture notes instead of relying entirely on the model's internal knowledge.

### Completed

* Added `generate_from_notes()`.
* Added `test_notes.py`.
* Implemented multiline lecture-note input.
* Added an `END` command for terminating input.
* Added empty-input validation.
* Used supplied notes as the primary source for generation.
* Tested grounding with lexical-analysis notes.
* Tested grounding with deliberately restricted semaphore notes.
* Confirmed that generated questions remained within the supplied concepts.

### Grounded Pipeline

```text
Lecture Notes
      ↓
generate_from_notes()
      ↓
Grounded Prompt
      ↓
Qwen3:4b
      ↓
Structured Response
      ↓
Pydantic
      ↓
LearningMaterial
```

### Grounding Test

The model was supplied only with:

```text
A semaphore is an integer synchronization variable.

The two atomic operations on a semaphore are wait and signal.

A binary semaphore can take values 0 and 1.
```

The generated material remained focused on:

* semaphore definition
* `wait`
* `signal`
* binary semaphore values

It did not introduce unrelated operating-system concepts.

### Input Validation

The CLI now protects the generation pipeline from empty input:

```python
if not notes.strip():
    print("No notes provided.")
```

This handles inputs containing:

* no text
* spaces
* blank lines
* tabs

without unnecessarily calling the language model.

### Key Learning

Day 3 introduced the concept of **grounding**.

Instead of asking:

```text
What do you know about semaphores?
```

the system is moving toward:

```text
Here is the learner's source material.
Teach using this material.
```

This distinction will become important when lecture PDFs and retrieval are introduced later.

---

# Current Limitations

notspoonfed is currently an early prototype.

It does **not** yet include:

* PDF ingestion
* automatic text extraction
* embeddings
* semantic retrieval
* persistent database storage
* adaptive question generation
* answer evaluation
* weakness detection
* spaced repetition
* frontend/UI
* user accounts
* cloud deployment

Local generation can also currently be slow because complete structured responses are generated synchronously before being displayed.

These limitations are intentional at this stage.

The current priority is building and understanding the core learning pipeline before optimizing or scaling it.

---

# Long-Term Direction

The intended learning flow is:

```text
Upload Learning Material
          ↓
Extract & Understand Concepts
          ↓
Generate Structured Learning Material
          ↓
Question-Based Learning
          ↓
Student Attempts Question
          ↓
Evaluate Understanding
          ↓
Detect Weak Concept / Misconception
          ↓
Generate Targeted Similar Question
          ↓
Track Mastery
          ↓
Schedule Revision
```

Future learning modes may include:

**Learn · Practice · Recall · Exam**

The eventual goal is not simply to create another AI PDF summarizer.

The goal is to build a system that continuously asks:

> **What does the learner understand, what are they getting wrong, and what should they practice next?**

---

# 100-Day Build

notspoonfed is being developed incrementally over 100 days.

The philosophy of the build is:

```text
Build
  ↓
Understand
  ↓
Test
  ↓
Improve
  ↓
Repeat
```

Features are intentionally being introduced gradually so that the architecture evolves alongside an understanding of how each component works.

Detailed development notes are maintained in:

```text
docs/progress.md
```

---

## Running the Current Prototype

### 1. Clone the repository

```bash
git clone https://github.com/Redvey/notspoonfed.git
cd notspoonfed/backend
```

### 2. Create a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Install and run Ollama

Make sure Ollama is installed and the required model is available:

```bash
ollama pull qwen3:4b
```

Start Ollama if necessary:

```bash
ollama serve
```

### 5. Run topic-based generation

In another terminal:

```bash
cd ~/notspoonfed/backend
source .venv/bin/activate
python test_ai.py
```

### 6. Run note-grounded generation

```bash
python test_notes.py
```

Paste lecture notes and enter:

```text
END
```

on a new line when finished.

---

## License

No license has been selected yet.

---

## Development Status

```text
Day 01  ██████████  Local AI connection
Day 02  ██████████  Structured output
Day 03  ██████████  Note-grounded generation
Day 04  ░░░░░░░░░░  Next milestone
...
Day 100 ░░░░░░░░░░
```

**Current milestone: Day 3 / 100**
