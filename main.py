import json
from benchmark.tasks import TASK_EXAMPLES
from nodes.learn   import learn
from nodes.try_node import try_prompt
from nodes.score   import score
from nodes.reflect import reflect
from nodes.improve import improve
from nodes.decide  import decide


def run():
    # ── LEARN: understand the task class from examples ────────────────────
    system_prompt = learn(TASK_EXAMPLES)
    scores = []
    gaps   = []

    for iteration in range(1, 10):  # hard cap at 9; decide() stops earlier
        print(f"\n{'='*50}\n[ROUND {iteration}]\n{'='*50}")

        # ── TRY: run current prompt on all examples ───────────────────────
        outputs = try_prompt(system_prompt, TASK_EXAMPLES)

        # ── SCORE: judge output quality ───────────────────────────────────
        round_score = score(outputs)
        scores.append(round_score)
        print(f"\n[DECIDE] Round {iteration} score: {round_score:.3f} | history: {scores}")

        # ── DECIDE: stop or continue? ─────────────────────────────────────
        stop, reason = decide(scores, iteration)
        if stop:
            print(f"[DECIDE] Stopping — {reason}")
            break

        # ── REFLECT: what did the prompt get wrong? ───────────────────────
        gaps = reflect(outputs, system_prompt)

        # ── IMPROVE: rewrite the prompt to fix the gaps ───────────────────
        system_prompt = improve(system_prompt, gaps)

    # ── SUMMARY ───────────────────────────────────────────────────────────
    print("\n" + "=" * 60)
    print("  STEM AGENT — EVOLUTION SUMMARY")
    print("=" * 60)
    print(f"  Rounds taken:  {len(scores)}")
    print(f"  Score history: {[f'{s:.3f}' for s in scores]}")
    if len(scores) >= 2:
        print(f"  Improvement:   {scores[-1] - scores[0]:+.3f}  "
              f"({scores[0]:.3f} → {scores[-1]:.3f})")
    print("=" * 60)

    result = {
        "task_class":         "AI Chat Assistant Specialization",
        "final_system_prompt": system_prompt,
        "score_history":      scores,
        "final_gaps":         gaps,
        "rounds_taken":       len(scores),
    }
    with open("specialized_agent.json", "w") as f:
        json.dump(result, f, indent=2)
    print("\nSpecialized agent saved → specialized_agent.json")


if __name__ == "__main__":
    run()
