# Task examples for the AI Chat Assistant specialization domain.
# Each example is a realistic user message sent to a JetBrains AI chat assistant.
# Authored to cover distinct skill dimensions: security, architecture, debugging,
# language choice, performance, pedagogy, and communication style.

TASK_EXAMPLES = [
    {
        "input": (
            "This function works but my code review got rejected. Why might that be?\n\n"
            "def get_user(id):\n"
            "    return db.execute('SELECT * FROM users WHERE id=' + str(id))"
        ),
        "ideal": (
            "Identifies SQL injection clearly. Explains why it fails code review. "
            "Shows the parameterised fix. Does not just say 'use an ORM'."
        ),
    },
    {
        "input": (
            "I have a class with 600 lines and 40 methods. "
            "My tech lead says it violates SRP. What does that mean and where do I start?"
        ),
        "ideal": (
            "Explains Single Responsibility Principle concretely. "
            "Gives a practical first step to identify splits. Does not rewrite their class."
        ),
    },
    {
        "input": (
            "My unit test passes locally but fails in CI. "
            "The test checks a sorted list."
        ),
        "ideal": (
            "Diagnoses non-deterministic ordering as the likely cause. "
            "Suggests asserting on sets or sorted output explicitly. Asks for the test if needed."
        ),
    },
    {
        "input": (
            "Should I use a dataclass or a named tuple for a read-only point "
            "with x, y coordinates in Python?"
        ),
        "ideal": (
            "Gives a clear recommendation with reasoning. "
            "Covers immutability, memory, unpacking. Does not say 'it depends' without committing."
        ),
    },
    {
        "input": (
            "How do I make this faster? It's taking 3 seconds on 10k rows.\n"
            "for row in rows:\n    result.append(process(row))"
        ),
        "ideal": (
            "Asks what process() does before guessing. "
            "Mentions list comprehension, vectorisation, parallelism as options. "
            "Does not over-engineer."
        ),
    },
    {
        "input": "Explain what a memory leak is to a junior developer who just joined the team.",
        "ideal": (
            "Clear analogy, no jargon. Practical example in a common language. "
            "Actionable — tells them what to watch for."
        ),
    },
    {
        "input": (
            "Write a commit message for: fixed the bug where null pointer exception "
            "was thrown when user had no profile picture set"
        ),
        "ideal": (
            "Follows conventional commits format. Imperative mood. "
            "Specific about what changed and why. Under 72 chars."
        ),
    },
]
