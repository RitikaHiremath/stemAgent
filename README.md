# Stem Agent

A stem agent that starts with no prior configuration and evolves a specialized system prompt for a JetBrains-style AI coding assistant through iterative self-reflection.

Like a stem cell, the agent begins undifferentiated. It observes a class of tasks, attempts them with a minimal prompt, reflects on what went wrong, and rewrites itself round by round until it converges on a specialized configuration.

---

## Architecture

```
                        +----------+
                        |  LEARN   |  Reads task examples, writes initial system prompt
                        +----+-----+
                             |
                             v
                   +---------+---------+
              +--->|       TRY         |  Runs current system prompt on all 7 tasks
              |    +---------+---------+
              |              |
              |              v
              |    +---------+---------+
              |    |      SCORE        |  LLM-as-judge rates each output 0-1 (3x averaged)
              |    +---------+---------+
              |              |
              |              v
              |    +---------+---------+
              |    |      DECIDE       |  Stop if converged or max rounds hit
              |    +---------+---------+
              |         |        |
              |      continue   stop
              |         |        |
              |         v        v
              |    +---------+  [specialized_agent.json]
              |    |  REFLECT |  Identify specific gaps in the current prompt
              |    +---------+
              |         |
              |         v
              |    +---------+
              +----+  IMPROVE |  Rewrite prompt to fix identified gaps
                   +---------+
```

---

## Results

| Round | Score | What changed |
|-------|-------|--------------|
| 1 (stem) | 0.752 | Initial prompt, no specialization |
| 2 | 0.829 | Added guidance on context and actionable examples |
| 3 | 0.781 | Oscillation — prompt over-corrected |
| 4 (specialized) | 0.805 | Stabilized with security and brevity focus |

**Net improvement: +0.053 (0.752 → 0.805)**

The oscillation between rounds 2 and 3 is expected — prompt improvements are not monotonic, and the LLM judge has inherent variance even when averaged. The agent stopped at round 4 due to the max iterations safeguard.

---

## Project Structure

```
stemAgent/
├── main.py              Orchestration loop — runs LEARN then the TRY/SCORE/DECIDE/REFLECT/IMPROVE cycle
├── config.py            Model names, MAX_ITERATIONS, MIN_SCORE_DELTA
├── requirements.txt
│
├── benchmark/
│   ├── __init__.py
│   └── tasks.py         7 task examples covering: SQL injection review, SRP refactoring,
│                        CI debugging, dataclass vs namedtuple, performance, pedagogy,
│                        and commit message formatting. Authored to cover distinct skill
│                        dimensions where a generic prompt is likely to fail.
│
└── nodes/
    ├── __init__.py
    ├── learn.py          LEARN  — derives an initial system prompt from the task examples
    ├── try_node.py       TRY    — runs the current system prompt against all 7 examples
    ├── score.py          SCORE  — LLM-as-judge, each output scored 3x and averaged
    ├── reflect.py        REFLECT — identifies specific gaps in the current prompt
    ├── improve.py        IMPROVE — rewrites the prompt to address those gaps
    └── decide.py         DECIDE  — stops if delta < MIN_SCORE_DELTA or max rounds hit
```

---

## Setup

```bash
pip install -r requirements.txt
export OPENAI_API_KEY="your-key-here"
python main.py
```

The final specialized agent config (evolved system prompt + full score history)
is saved to `specialized_agent.json` after each run.

---

## Acknowledgements

Code developed with assistance from Claude (Anthropic) as a pair-programming tool. All architectural decisions, domain choices, task design, and experimental analysis are my own.