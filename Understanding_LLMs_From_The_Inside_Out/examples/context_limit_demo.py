"""
examples/context_limit_demo.py
================================
AI Engineering Roadmap 2026 · Episode 1

Demonstrate what happens as the context window fills up.

This script:
  1. Starts a conversation with a unique piece of information
  2. Gradually fills the context with unrelated content
  3. Tests whether the model still remembers the original information

What this teaches:
  - The context window has a hard limit
  - Models can lose track of early content in very long contexts
  - This is why memory management is an engineering challenge (Episode 6)

Usage:
  python examples/context_limit_demo.py
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def run_context_demo():
    """Show context window effects in a simple, visual way."""

    try:
        from openai import OpenAI
        from dotenv import load_dotenv
        load_dotenv()
        client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
    except Exception as e:
        print(f"\n[Setup required] {e}")
        print("Add your OPENAI_API_KEY to .env and run again.\n")
        _show_concept_explanation()
        return

    print("\n" + "=" * 65)
    print("  CONTEXT WINDOW DEMO — AI Engineering Roadmap 2026, Ep 1")
    print("=" * 65)

    # Step 1: Plant a unique piece of information
    secret_word = "SAFFRON42"
    conversation = [
        {
            "role": "system",
            "content": "You are a helpful assistant. Answer concisely."
        },
        {
            "role": "user",
            "content": f"Remember this secret code for later: {secret_word}. Confirm you have it."
        }
    ]

    print(f"\n  Step 1: Planting a secret code: {secret_word}")
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=conversation,
        max_tokens=50,
    )
    reply = response.choices[0].message.content
    conversation.append({"role": "assistant", "content": reply})
    print(f"  Model: {reply[:80]}")

    # Step 2: Add increasing amounts of filler content
    filler = (
        "The history of computing spans decades, beginning with mechanical calculators "
        "in the 19th century. Early computers filled entire rooms and required teams of "
        "engineers to operate. The invention of the transistor revolutionised electronics. "
        "Moore's Law predicted doubling of transistors every two years. The rise of the "
        "internet transformed how humans communicate and share information globally. "
    ) * 20  # Repeat to add volume

    test_points = [0, 5, 20, 50]

    for filler_count in test_points:
        # Add filler to conversation
        if filler_count > 0:
            filler_segment = filler[:filler_count * 200]
            conversation.append({
                "role": "user",
                "content": f"Here is some background reading: {filler_segment}"
            })
            conversation.append({
                "role": "assistant",
                "content": "Understood, I've read the background information."
            })

        # Test recall
        conversation_copy = conversation + [{
            "role": "user",
            "content": "What was the secret code I gave you at the very beginning of our conversation?"
        }]

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=conversation_copy,
            max_tokens=50,
            temperature=0,
        )
        recall_response = response.choices[0].message.content
        correct = secret_word in recall_response

        tokens_used = response.usage.total_tokens

        print(f"\n  After {filler_count:2} filler blocks ({tokens_used:,} tokens used):")
        print(f"  Model said: {recall_response[:80]}")
        print(f"  Correct recall: {'✅ YES' if correct else '❌ NO — context degradation!'}")

    print("\n" + "=" * 65)
    print("\n  Key Engineering Lessons:")
    print("  → Context window = working memory. It is limited.")
    print("  → The model doesn't 'forget' — it literally can't see")
    print("    content that's pushed outside the window.")
    print("  → In production: summarise history, limit document size,")
    print("    monitor token usage per request.")
    print("  → Episode 6 covers memory architecture in detail.\n")


def _show_concept_explanation():
    """Show the concept without running the demo."""
    print("\n" + "=" * 65)
    print("  CONTEXT WINDOW — Concept Explanation")
    print("=" * 65)
    print("""
  Imagine the context window as a physical notepad with 128,000
  character spaces.

  At the start of a conversation:
  ┌─────────────────────────────────────────┐
  │ System prompt      [500 chars used]     │
  │ User: "Remember SAFFRON42"  [30 chars]  │
  │ [127,470 chars remaining]               │
  └─────────────────────────────────────────┘

  After 50 messages of filler:
  ┌─────────────────────────────────────────┐
  │ [earlier content pushed off the top]   │
  │ ... message 30 ...                      │
  │ ... message 31 ...                      │
  │ ... message 50 ...                      │
  │ User: "What was the secret code?"       │
  └─────────────────────────────────────────┘

  The model can no longer see "Remember SAFFRON42" because it
  was pushed outside the window.

  It doesn't summarise. It doesn't archive. It simply can't
  see what's no longer in the window.

  This is why Episode 6 covers memory architecture.
""")


if __name__ == "__main__":
    run_context_demo()
