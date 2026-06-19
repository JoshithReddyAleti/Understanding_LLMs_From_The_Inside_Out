# 🧠 Understanding LLMs From The Inside Out

> **Episode 1 of the [AI Engineering Roadmap 2026](https://www.linkedin.com/newsletters/ai-engineering-roadmap-2026-7467249724752908288/) Newsletter Series**
>
> *"You can't engineer something you don't understand."*

---

<div align="center">

![Beginner Friendly](https://img.shields.io/badge/Level-Beginner%20Friendly-22C55E?style=flat-square)
![No Code Required](https://img.shields.io/badge/Code-Optional-3776AB?style=flat-square)
![Reading Time](https://img.shields.io/badge/Reading%20Time-30%20min-F59E0B?style=flat-square)
![Episode](https://img.shields.io/badge/Episode-1%20of%2010-534AB7?style=flat-square)

**[📖 Newsletter](https://www.linkedin.com/newsletters/ai-engineering-roadmap-2026-7467249724752908288/) · [🗺️ Full Roadmap](docs/ROADMAP.md) · [🧠 Concepts](docs/CONCEPTS.md) · [➡️ Episode 2](https://github.com/YOUR_USERNAME/Python_For_AI_What_Actually_Matters)**

</div>

---

## 🎯 What Is This?

Before you build AI systems, you need to understand what's actually happening inside them.

Most people use ChatGPT every day without knowing:
- Why it sometimes confidently gives wrong answers
- Why the same question gets different answers each time
- Why it "forgets" what you said 100 messages ago
- Why it can write poetry but struggles with `9.11 vs 9.9`

This episode answers all of that — from the ground up.

**No fluff. No hype. Just the actual mechanics.**

---

## 🔑 The One Sentence That Explains Everything

> **An LLM predicts the next most likely token, given everything before it.**

That's it. Every capability, every failure, every quirk — it all comes from that one sentence.

The rest of this repo is just unpacking what that means.

---

## 📚 What You'll Learn

By the end of this episode, you will be able to explain:

- ✅ What a token is and why it matters
- ✅ How LLMs are trained (in plain English)
- ✅ What a context window is and why it has limits
- ✅ What temperature does and when to use it
- ✅ Why LLMs hallucinate (and why that's unavoidable)
- ✅ The difference between a model and a product
- ✅ Why LLMs are bad at maths but great at language
- ✅ What embeddings are (and why they power search)
- ✅ What fine-tuning vs prompting actually means
- ✅ Why "more parameters = smarter" isn't the full story

---

## 🗂️ What's In This Repo

```
Understanding_LLMs_From_The_Inside_Out/
│
├── docs/
│   ├── CONCEPTS.md          # Deep-dive on every concept in this episode
│   ├── GLOSSARY.md          # Every AI term defined clearly, no jargon
│   ├── ROADMAP.md           # Full 10-episode AI Engineering Roadmap 2026
│   ├── MISCONCEPTIONS.md    # The most common wrong beliefs about LLMs
│   └── INTERVIEW_PREP.md    # How to talk about LLMs in interviews
│
├── notebooks/
│   ├── 01_tokenisation.ipynb      # See how text becomes tokens
│   ├── 02_temperature.ipynb       # See how temperature changes outputs
│   └── 03_context_window.ipynb    # See what happens at the context limit
│
├── examples/
│   ├── token_counter.py           # Count tokens in any text
│   ├── temperature_demo.py        # Same prompt, different temperatures
│   └── context_limit_demo.py      # What happens when context fills up
│
├── visuals/
│   ├── llm_architecture.md        # Text diagram of how LLMs work
│   ├── token_flow.md              # How text → tokens → prediction works
│   └── training_vs_inference.md   # Training vs using a model
│
├── .env.example
├── requirements.txt
└── README.md
```

---

## 🧩 The Core Concepts — Quick Reference

### 1. Tokens (Not Words)
LLMs don't see words. They see **tokens** — chunks of text that are sometimes words, sometimes parts of words, sometimes punctuation.

```
"Hello, world!"  →  ["Hello", ",", " world", "!"]   = 4 tokens
"unhappiness"    →  ["un", "happiness"]              = 2 tokens
"ChatGPT"        →  ["Chat", "G", "PT"]              = 3 tokens
```

Why does this matter?
- Every API call is priced per token
- Context windows are measured in tokens, not words
- Unusual words cost more tokens than common words

**Rule of thumb:** 1 token ≈ 0.75 words in English

---

### 2. How Training Works (Plain English)

```
Step 1: Feed the model billions of text documents from the internet
Step 2: Hide the last word of every sentence
Step 3: Ask the model to predict what word comes next
Step 4: Compare prediction to actual word
Step 5: Adjust model weights to make better predictions
Step 6: Repeat 100 billion times
```

That's it. No one told the model grammar rules, facts about the world, or how to reason. It learned all of that as a side effect of predicting text really well.

---

### 3. The Context Window

The context window is the model's working memory — everything it can "see" at once.

```
┌──────────────────────────────────────────┐
│            CONTEXT WINDOW                │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ │
│  │  System  │ │  Chat    │ │  Your    │ │
│  │  Prompt  │ │  History │ │  Query   │ │
│  └──────────┘ └──────────┘ └──────────┘ │
│                              ↑           │
│                         Model reads ALL  │
│                         of this to       │
│                         generate ONE     │
│                         response         │
└──────────────────────────────────────────┘
```

When the context fills up:
- The model can't "remember" earlier parts of the conversation
- It doesn't summarise — it literally can't see what's outside the window
- This is why long conversations degrade in quality

---

### 4. Temperature — The Creativity Dial

Temperature controls how "random" the model's predictions are.

| Temperature | Behaviour | Best For |
|---|---|---|
| 0.0 | Always picks most likely token | Classification, routing, structured output |
| 0.3 | Mostly predictable, slight variation | Summarisation, Q&A |
| 0.7 | Balanced | General conversation |
| 1.0 | Creative, sometimes surprising | Brainstorming, creative writing |
| 2.0 | Chaotic, often incoherent | Never use this |

**Key insight:** For routing decisions (Episode 3), use `temperature=0`. For creative tasks, use `temperature=0.7–1.0`.

---

### 5. Why LLMs Hallucinate

Hallucination is not a bug. It's a feature of how LLMs work.

The model was trained to produce fluent, confident text. It was not trained to say "I don't know." When it doesn't have good signal for the answer, it does what it always does — produces the most statistically likely continuation of the text.

That continuation might sound correct but be completely wrong.

**This is why validation matters** (Episode 3 — the entire validation layer exists because of this).

**Engineering solutions:**
- RAG — give the model the actual facts (Episode 5)
- Structured outputs — constrain what it can say (Episode 3)
- Verification layers — check outputs against ground truth

---

### 6. The Difference Between a Model and a Product

| Model | Product |
|---|---|
| GPT-4o (the weights) | ChatGPT (the app) |
| Claude Sonnet | Claude.ai |
| Llama 3 | Ollama, Perplexity, etc. |

The model is the raw intelligence. The product is the system built around it — with memory, tools, guardrails, a UI, and a business model.

**This roadmap teaches you to build the product layer.**

---

### 7. Parameters — What They Actually Are

"GPT-4 has 1.7 trillion parameters" — but what does that mean?

Parameters are numbers. Specifically, they're the numbers inside the neural network that get adjusted during training. After training, they're frozen — they encode everything the model "knows."

More parameters generally means:
- Better at complex reasoning
- More expensive to run
- Slower inference
- Higher API cost

But parameter count alone doesn't determine quality — training data, training method, and fine-tuning all matter just as much.

---

## 🔬 Interactive Examples

### Token Counter (`examples/token_counter.py`)
```bash
python examples/token_counter.py "What is a large language model?"
# Output: 8 tokens | Estimated cost: $0.000008 at $0.01/1K tokens
```

### Temperature Demo (`examples/temperature_demo.py`)
```bash
python examples/temperature_demo.py --prompt "The sky is" --temperatures 0.0 0.5 1.0
# Runs the same prompt 3 times with different temperatures
# Shows how output changes
```

### Context Window Demo (`examples/context_limit_demo.py`)
```bash
python examples/context_limit_demo.py
# Fills a context window progressively and shows degradation
```

---

## ❌ The 10 Biggest Misconceptions About LLMs

See [`docs/MISCONCEPTIONS.md`](docs/MISCONCEPTIONS.md) for the full breakdown. Here are the top 3:

**1. "LLMs understand language like humans do."**
They don't. They model statistical relationships between tokens. The appearance of understanding is a side effect of doing that extremely well at scale.

**2. "A bigger model is always better."**
Not for your use case. A well-prompted small model often outperforms a poorly-prompted large one — and costs 10x less.

**3. "LLMs have opinions and feelings."**
They produce text that sounds like opinions and feelings, because that's what they were trained on. The text is real. The underlying experience is not.

---

## 🎤 How to Talk About LLMs in Interviews

If an interviewer asks "explain how LLMs work", most candidates say:

> *"They're trained on lots of data and they predict the next word."*

A strong candidate says:

> *"LLMs are transformer-based models trained via next-token prediction on large text corpora. The training process adjusts billions of parameters to minimise prediction loss across the dataset. At inference time, the model uses the full context window — everything in the conversation so far — to produce a probability distribution over possible next tokens, then samples from that distribution based on the temperature setting. The key engineering implication is that outputs are probabilistic, not deterministic, which is why production systems need validation and structured output enforcement."*

See [`docs/INTERVIEW_PREP.md`](docs/INTERVIEW_PREP.md) for more.

---

## ⚡ Quick Start (Optional Code)

```bash
git clone https://github.com/YOUR_USERNAME/Understanding_LLMs_From_The_Inside_Out.git
cd Understanding_LLMs_From_The_Inside_Out

python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt

cp .env.example .env
# Add your OpenAI API key to .env

python examples/token_counter.py "Hello, world!"
```

---

## 📚 Recommended Reading (Free)

| Resource | Why It's Worth It |
|---|---|
| [Attention Is All You Need](https://arxiv.org/abs/1706.03762) | The original transformer paper — read the abstract at minimum |
| [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/) | Best visual explanation of transformers that exists |
| [Andrej Karpathy — Let's build GPT](https://www.youtube.com/watch?v=kCc8FmEb1nY) | 2 hours that will change how you think about LLMs |
| [Tokenizer explorer (tiktokenizer.vercel.app)](https://tiktokenizer.vercel.app) | See tokenisation live in your browser |

---

## 🗺️ Where This Fits in the Roadmap

| Episode | Topic | Status |
|---|---|---|
| **1** | **What is an LLM really?** | **← You are here** |
| 2 | Python for AI — what actually matters | [View repo →](https://github.com/YOUR_USERNAME/Python_For_AI_What_Actually_Matters) |
| 3 | Tool calling, APIs & validation | [View repo →](https://github.com/YOUR_USERNAME/Building_AI_Project_Blueprint_for_Beginners) |
| 4–10 | Coming soon | [Subscribe →](https://www.linkedin.com/newsletters/ai-engineering-roadmap-2026-7467249724752908288/) |

---

## 📬 Subscribe to the Newsletter

This repo is Episode 1 of the **AI Engineering Roadmap 2026** — a LinkedIn newsletter that walks you step by step through becoming an AI engineer in 2026.

Each episode gets you:
- A real GitHub project (like this one)
- A LinkedIn carousel breaking down the concept
- A deep-dive concept guide
- Interview prep for that topic

**[→ Subscribe here. It's free.](https://www.linkedin.com/newsletters/ai-engineering-roadmap-2026-7467249724752908288/)**

---

<div align="center">

**If this helped you understand LLMs better, give it a ⭐**

*It helps other learners find this resource.*

[LinkedIn Newsletter](https://www.linkedin.com/newsletters/ai-engineering-roadmap-2026-7467249724752908288/) · [Episode 2 →](https://github.com/YOUR_USERNAME/Python_For_AI_What_Actually_Matters) · [Episode 3 →](https://github.com/YOUR_USERNAME/Building_AI_Project_Blueprint_for_Beginners)

</div>
