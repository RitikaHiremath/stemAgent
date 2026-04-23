import json
from openai import OpenAI
from config import MODEL_MINI, OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

SCORE_PROMPT = """Rate this AI assistant output from 0.0 to 1.0.

Task: {input}
What a good response looks like: {ideal}
Actual output: {output}

Return only JSON: {{"score": <float>, "reason": "<one sentence>"}}"""


def score_single(o: dict) -> float:
    """Score one output 3 times and average to reduce judge noise."""
    trials = []
    for _ in range(3):
        response = client.chat.completions.create(
            model=MODEL_MINI,
            messages=[
                {"role": "system", "content": "You are a strict evaluator. Return only JSON."},
                {"role": "user", "content": SCORE_PROMPT.format(
                    input=o["input"], ideal=o["ideal"], output=o["output"]
                )},
            ],
            temperature=0.0,
            response_format={"type": "json_object"},
        )
        raw = json.loads(response.choices[0].message.content)
        trials.append(float(raw.get("score", 0.5)))
    return round(sum(trials) / len(trials), 3)


def score(outputs: list) -> float:
    scores = []
    for o in outputs:
        s = score_single(o)
        scores.append(s)
        print(f"  [SCORE] {s:.3f} — '{o['input'][:50]}...'")

    avg = round(sum(scores) / len(scores), 3)
    print(f"[SCORE] Average: {avg:.3f}")
    return avg