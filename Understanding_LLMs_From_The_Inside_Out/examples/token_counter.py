"""
examples/token_counter.py
==========================
AI Engineering Roadmap 2026 · Episode 1

See how your text is tokenised and estimate API costs.

Usage:
  python examples/token_counter.py "Hello, world!"
  python examples/token_counter.py "What is a large language model?"
  python examples/token_counter.py --file my_prompt.txt

What this teaches:
  - Tokens are not words
  - Different text types tokenise very differently
  - API costs are directly tied to token count
  - Always estimate token usage before scaling
"""

import sys
import argparse
import os


def count_tokens(text: str, model: str = "gpt-4o") -> dict:
    """
    Count tokens in text using tiktoken (OpenAI's tokeniser).

    Args:
        text: The text to tokenise
        model: The model whose tokeniser to use

    Returns:
        dict with token_count, tokens list, and cost estimates
    """
    try:
        import tiktoken
        enc = tiktoken.encoding_for_model(model)
        tokens = enc.encode(text)
        token_list = [enc.decode([t]) for t in tokens]

        # Cost estimates (as of 2025, approximate)
        costs = {
            "gpt-4o-mini (input)":   len(tokens) / 1_000_000 * 0.15,
            "gpt-4o (input)":        len(tokens) / 1_000_000 * 5.00,
            "claude-haiku (input)":  len(tokens) / 1_000_000 * 0.25,
            "claude-sonnet (input)": len(tokens) / 1_000_000 * 3.00,
        }

        return {
            "text": text,
            "model": model,
            "token_count": len(tokens),
            "word_count": len(text.split()),
            "char_count": len(text),
            "tokens": token_list,
            "ratio": round(len(tokens) / max(len(text.split()), 1), 2),
            "cost_estimates": costs,
        }

    except ImportError:
        # Fallback if tiktoken not installed: rough estimate
        word_count = len(text.split())
        estimated_tokens = int(word_count / 0.75)
        return {
            "text": text,
            "model": "estimated (tiktoken not installed)",
            "token_count": estimated_tokens,
            "word_count": word_count,
            "char_count": len(text),
            "tokens": ["(install tiktoken for exact breakdown)"],
            "ratio": 1.33,
            "cost_estimates": {
                "gpt-4o-mini (input)": estimated_tokens / 1_000_000 * 0.15,
            },
            "note": "Run: pip install tiktoken for exact tokenisation"
        }


def print_results(result: dict) -> None:
    """Pretty-print tokenisation results."""
    print("\n" + "=" * 60)
    print("  TOKEN ANALYSIS")
    print("=" * 60)
    print(f"\n  Text:        {result['text'][:60]}{'...' if len(result['text']) > 60 else ''}")
    print(f"  Characters:  {result['char_count']:,}")
    print(f"  Words:       {result['word_count']:,}")
    print(f"  Tokens:      {result['token_count']:,}")
    print(f"  Ratio:       {result['ratio']} tokens per word")

    print(f"\n  Token breakdown:")
    for i, token in enumerate(result['tokens'][:20]):
        print(f"    {i+1:2}. {token!r}")
    if len(result['tokens']) > 20:
        print(f"    ... and {len(result['tokens']) - 20} more")

    print(f"\n  Cost estimates (input tokens only):")
    for model, cost in result['cost_estimates'].items():
        print(f"    {model:<30} ${cost:.8f}")

    print("\n  Key insight:")
    print("  Tokens ≠ words. Unusual words, code, and numbers")
    print("  often use more tokens than you'd expect.")
    print("=" * 60 + "\n")


def demo_comparisons() -> None:
    """Show how different text types tokenise differently."""
    examples = [
        ("Common English", "The quick brown fox jumps over the lazy dog"),
        ("Technical terms", "Transformer architecture with multi-head self-attention"),
        ("Numbers", "The temperature is 98.6 degrees Fahrenheit at 37.0 Celsius"),
        ("Code", "def calculate_percentage(value, total): return (value / total) * 100"),
        ("Unusual words", "supercalifragilisticexpialidocious antidisestablishmentarianism"),
        ("Simple question", "What is 25% of 480?"),
    ]

    print("\n" + "=" * 60)
    print("  TOKENISATION COMPARISON")
    print("  Seeing how different text types use tokens differently")
    print("=" * 60)

    for label, text in examples:
        result = count_tokens(text)
        print(f"\n  {label}:")
        print(f"    Text:   {text[:50]}")
        print(f"    Words:  {result['word_count']}  |  Tokens: {result['token_count']}  |  Ratio: {result['ratio']}")

    print("\n" + "=" * 60)
    print("  Notice: code and technical terms use more tokens per word.")
    print("  This affects cost — prompt design matters.\n")


def main():
    parser = argparse.ArgumentParser(
        description="Count tokens and estimate API costs for any text."
    )
    parser.add_argument("text", nargs="?", help="Text to analyse")
    parser.add_argument("--file", help="Read text from a file")
    parser.add_argument("--demo", action="store_true", help="Run comparison demo")
    parser.add_argument("--model", default="gpt-4o", help="Model tokeniser to use")

    args = parser.parse_args()

    if args.demo:
        demo_comparisons()
        return

    if args.file:
        with open(args.file, "r") as f:
            text = f.read()
    elif args.text:
        text = args.text
    else:
        # Interactive mode
        print("\nToken Counter — AI Engineering Roadmap 2026, Episode 1")
        print("Enter text to analyse (or 'demo' for comparison examples):\n")
        text = input("> ").strip()
        if text.lower() == "demo":
            demo_comparisons()
            return

    result = count_tokens(text, model=args.model)
    print_results(result)


if __name__ == "__main__":
    main()
