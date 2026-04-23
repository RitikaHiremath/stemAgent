import json
from openai import OpenAI
from config import MODEL_MINI, OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

REFLECT_PROMPT = """Current system prompt:
{system_prompt}

Results from this round:
{summary}

List up to 4 specific gaps — what is the system prompt failing to instruct
the assistant to do? Be concrete, not generic.

Return only JSON: {{"gaps": ["gap1", "gap2", ...]}}"""


def reflect(outputs: list, system_prompt: str) -> list:
    summary = "\n".join(
        f"- Input: {o['input'][:80]}\n  Ideal: {o['ideal']}\n  Got: {o['output'][:120]}"
        for o in outputs
    )
    response = client.chat.completions.create(
        model=MODEL_MINI,
        messages=[
            {"role": "system", "content": "You are a strict evaluator. Return only JSON."},
            {"role": "user",   "content": REFLECT_PROMPT.format(
                system_prompt=system_prompt, summary=summary
            )},
        ],
        temperature=0.0,
        response_format={"type": "json_object"},
    )
    gaps = json.loads(response.choices[0].message.content).get("gaps", [])
    print(f"[REFLECT] Gaps: {gaps}")
    return gaps
