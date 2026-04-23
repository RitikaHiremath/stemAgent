from openai import OpenAI
from config import MODEL_MINI, OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

IMPROVE_PROMPT = """Current system prompt:
{system_prompt}

These gaps were identified:
{gaps}

Rewrite the system prompt to fix all these gaps.
Keep it under 200 words. Be specific and direct."""


def improve(system_prompt: str, gaps: list) -> str:
    response = client.chat.completions.create(
        model=MODEL_MINI,
        messages=[{"role": "user", "content": IMPROVE_PROMPT.format(
            system_prompt=system_prompt,
            gaps="\n".join(f"- {g}" for g in gaps),
        )}],
        temperature=0.2,
    )
    new_prompt = response.choices[0].message.content.strip()
    print(f"[IMPROVE] New system prompt ({len(new_prompt)} chars)")
    return new_prompt
