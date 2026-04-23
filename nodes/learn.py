from openai import OpenAI
from config import MODEL_MINI, OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

LEARN_PROMPT = """You are designing a system prompt for an AI coding assistant.

Here are example tasks and what good responses look like:
{examples}

Write a concise system prompt (under 150 words) that would make the assistant
perform well on all these tasks. Be specific about tone, format, and behaviour."""


def learn(task_examples: list) -> str:
    print("\n[LEARN] Understanding the task class...")
    example_str = "\n\n".join(
        f"Input: {e['input']}\nIdeal: {e['ideal']}"
        for e in task_examples[:3]
    )
    response = client.chat.completions.create(
        model=MODEL_MINI,
        messages=[{"role": "user", "content": LEARN_PROMPT.format(examples=example_str)}],
        temperature=0.2,
    )
    prompt = response.choices[0].message.content.strip()
    print(f"[LEARN] Initial system prompt ({len(prompt)} chars)")
    return prompt
