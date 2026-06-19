"""
examples/temperature_demo.py
==============================
AI Engineering Roadmap 2026 · Episode 1

See how temperature changes LLM outputs.
Same prompt. Different temperatures. Different results.

Usage:
  python examples/temperature_demo.py
  python examples/temperature_demo.py --prompt "The best programming language is"
  python examples/temperature_demo.py --runs 5

What this teaches:
  - Temperature 0 = deterministic (same answer every time)
  - Temperature 1 = creative and varied
  - When to use each in real systems
"""

import os
import sys
import argparse
import time

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def call_llm_at_temperature(prompt: str, temperature: float, model: str = "gpt-4o-mini") -> str:
    """Call the LLM at a specific temperature and return the response."""
    try:
        from openai import OpenAI
        from dotenv import load_dotenv
        load_dotenv()

        client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "Be concise. Respond in 1-2 sentences maximum."},
                {"role": "user", "content": prompt}
            ],
            temperature=temperature,
            max_tokens=100,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"[Error: {e}]"


def run_temperature_demo(prompt: str, temperatures: list, runs: int = 3) -> None:
    """Run the same prompt at multiple temperatures and show the differences."""

    print("\n" + "=" * 70)
    print("  TEMPERATURE DEMO — AI Engineering Roadmap 2026, Episode 1")
    print("=" * 70)
    print(f"\n  Prompt: \"{prompt}\"")
    print(f"  Runs per temperature: {runs}")
    print(f"  Model: gpt-4o-mini\n")

    for temp in temperatures:
        label = {
            0.0: "Deterministic (use for routing, classification)",
            0.3: "Mostly predictable (use for summaries, Q&A)",
            0.7: "Balanced (use for general conversation)",
            1.0: "Creative (use for brainstorming, writing)",
            1.5: "Very random (rarely useful in production)",
        }.get(temp, f"Temperature {temp}")

        print(f"  ── Temperature {temp} — {label}")
        print(f"  {'─' * 60}")

        for i in range(runs):
            response = call_llm_at_temperature(prompt, temperature=temp)
            print(f"  Run {i+1}: {response}")
            time.sleep(0.5)  # Avoid rate limiting

        print()

    print("=" * 70)
    print("\n  Key takeaways:")
    print("  → At temperature 0, all runs should return identical output")
    print("  → At temperature 1+, each run varies — sometimes significantly")
    print("  → For Episode 3's routing layer, we use temperature=0")
    print("    (we need deterministic classification, not creativity)")
    print("=" * 70 + "\n")


def main():
    parser = argparse.ArgumentParser(
        description="See how temperature affects LLM output."
    )
    parser.add_argument(
        "--prompt",
        default="Complete this sentence: The most important skill for an AI engineer is",
        help="The prompt to test"
    )
    parser.add_argument(
        "--temperatures",
        nargs="+",
        type=float,
        default=[0.0, 0.7, 1.0],
        help="Temperatures to test (e.g., --temperatures 0.0 0.5 1.0)"
    )
    parser.add_argument(
        "--runs",
        type=int,
        default=3,
        help="Number of runs per temperature"
    )

    args = parser.parse_args()

    run_temperature_demo(
        prompt=args.prompt,
        temperatures=args.temperatures,
        runs=args.runs
    )


if __name__ == "__main__":
    main()
