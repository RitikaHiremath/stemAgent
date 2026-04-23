from openai import OpenAI
from config import MODEL, OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)


def try_prompt(system_prompt: str, examples: list) -> list:
    outputs = []
    for ex in examples:
        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user",   "content": ex["input"]},
            ],
            temperature=0.2,
        )
        out = response.choices[0].message.content.strip()
        outputs.append({"input": ex["input"], "ideal": ex["ideal"], "output": out})
        print(f"  [TRY] '{ex['input'][:60]}...' → {len(out)} chars")
    return outputs
