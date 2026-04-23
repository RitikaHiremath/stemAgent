from config import MAX_ITERATIONS, MIN_SCORE_DELTA


def decide(scores: list, iteration: int) -> tuple:
    if iteration >= MAX_ITERATIONS:
        return True, f"max iterations ({MAX_ITERATIONS}) reached"

    if len(scores) >= 2:
        delta = scores[-1] - scores[-2]
        print(f"[DECIDE] Delta: {delta:+.3f} (threshold: {MIN_SCORE_DELTA})")
        # Only stop if improvement is positive but tiny (converged upward)
        # A negative delta means we got worse — keep trying
        if 0 <= delta < MIN_SCORE_DELTA:
            return True, f"converged (delta {delta:+.3f})"

    return False, "continuing"