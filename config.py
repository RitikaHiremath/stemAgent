import os

MODEL      = "gpt-4o"
MODEL_MINI = "gpt-4o-mini"

MAX_ITERATIONS  = 4
MIN_SCORE_DELTA = 0.05

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
