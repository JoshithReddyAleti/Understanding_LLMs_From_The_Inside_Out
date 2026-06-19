# 🧠 Concepts Deep Dive — Episode 1

> Everything you need to understand LLMs at an engineering level.
> Read this alongside the README. These are the explanations that go deeper.

---

## 1. The Transformer Architecture (Plain English)

Before LLMs, the best language models read text left to right, one word at a time. That meant they had to "remember" context from earlier — and they weren't very good at it.

The transformer changed everything by processing **all tokens in the input simultaneously** and using a mechanism called **attention** to decide which tokens matter most for each prediction.

**Attention in one sentence:**
> When predicting the next token, attention lets the model look at every previous token and decide how much to "pay attention" to each one.

Example:
> "The trophy didn't fit in the suitcase because **it** was too big."

What does "it" refer to — the trophy or the suitcase? Humans know it's the trophy. The attention mechanism lets the model figure this out by looking at the relationship between "it" and all other words in the sentence simultaneously.

---

## 2. Pre-training vs Fine-tuning vs Prompting

These three things are often confused. Here's the clear version:

### Pre-training
The expensive, one-time process of training a model from scratch on billions of documents. This is what OpenAI and Anthropic do. Costs tens of millions of dollars. Produces the base model.

### Fine-tuning
Taking a pre-trained model and training it further on a smaller, specific dataset. Used to make the model better at a specific task (e.g., medical Q&A, code completion, following instructions).

This is what turns a base model into an instruction-following assistant like ChatGPT.

### Prompting
Sending text to an already-trained model and getting a response. No weights change. You're just using the model as-is and guiding its behaviour through the text you provide.

**As an AI engineer, you'll mostly work with prompting.** Fine-tuning is for when prompting isn't enough — and it usually is enough.

```
Pre-training    → Months, $millions, done by labs
Fine-tuning     → Days/weeks, $thousands, done by companies
Prompting       → Seconds, cents, done by engineers
                                         ↑
                                    That's you
```

---

## 3. Embeddings — The Foundation of Modern AI

An embedding is a list of numbers that represents meaning.

The key property: **things with similar meanings have similar embeddings.**

```
"cat"  → [0.2, 0.8, 0.1, 0.9, ...]  (1536 numbers)
"dog"  → [0.3, 0.7, 0.2, 0.8, ...]  (similar numbers — similar meaning)
"car"  → [0.9, 0.1, 0.7, 0.2, ...]  (different numbers — different meaning)
```

Why this matters for AI engineering:
- **Semantic search** — find documents by meaning, not keywords
- **RAG** (Episode 5) — embed your documents, then find the relevant ones for each query
- **Recommendation** — find similar items by comparing embedding distances
- **Classification** — train a simple classifier on top of embeddings

You don't need to build embeddings yourself. Every major LLM provider has an embeddings API:
```python
from openai import OpenAI
client = OpenAI()
response = client.embeddings.create(
    input="What is a large language model?",
    model="text-embedding-3-small"
)
embedding = response.data[0].embedding  # List of 1536 floats
```

---

## 4. RLHF — Why ChatGPT Feels Different From a Base Model

A base model just predicts text. Ask it "what is 2+2?" and it might respond:

> "What is 2+2? What is 3+3? What is 4+4?" (continuing the pattern of math questions)

That's because it was trained on text that looks like that. It doesn't know it's supposed to answer questions.

**RLHF (Reinforcement Learning from Human Feedback)** is the process that turns a base model into an assistant:

1. Generate many responses to a question
2. Have humans rank them from best to worst
3. Train a reward model to predict human preferences
4. Use that reward model to fine-tune the LLM to produce higher-ranked responses

The result: a model that is helpful, follows instructions, and (usually) declines harmful requests.

This is why ChatGPT, Claude, and Gemini all feel like assistants rather than raw text generators.

---

## 5. The Probability Distribution — What Actually Happens at Inference

When a model generates text, it doesn't pick one token. It calculates a **probability distribution** over all possible next tokens — then samples from it.

Example for the prompt "The capital of France is":

```
"Paris"     → 94.2% probability
"Lyon"      →  1.8% probability
"a"         →  0.9% probability
"located"   →  0.7% probability
(50,000 other tokens) → remaining %
```

With temperature=0, it always picks "Paris".
With temperature=1, it samples — usually "Paris", but occasionally something else.
With temperature=2, the distribution flattens and randomness explodes.

This is why:
- The same prompt gives different answers at temperature > 0
- Setting temperature=0 makes outputs deterministic (same prompt = same answer)
- Routing and classification tasks should always use temperature=0

---

## 6. Why LLMs Fail at Simple Maths

`9.11 > 9.9` — most LLMs get this wrong and say 9.11 is bigger.

Why? Because:
1. Numbers are tokenised in non-intuitive ways (`9.11` might be `["9", ".", "1", "1"]`)
2. The model was trained to predict text, not to compute
3. In training data, "9.11" appeared in contexts like version numbers, dates, Bible verses — contexts where 9.11 *does* come "after" 9.9 in some sense
4. The model is pattern-matching, not reasoning mathematically

This is exactly why the calculator tool in Episode 3 exists. **Don't let LLMs do maths. Give them a calculator.**

---

## 7. System Prompts — The Invisible Layer

Every time you use ChatGPT, Claude, or Gemini, there's a system prompt you don't see. It's set by the company and shapes everything about how the model behaves.

Structure of an LLM API call:
```
System prompt:  "You are a helpful assistant. Be concise. Never discuss competitors."
User message:   "What's the best AI tool for X?"
                  ↓
           Model sees BOTH and responds accordingly
```

As an AI engineer, the system prompt is one of your most powerful tools:
- Set the persona ("You are a customer support agent for...")
- Set the output format ("Always respond in JSON with keys: answer, confidence, source")
- Set the constraints ("Never reveal internal system information")
- Set the context ("The user is a beginner Python developer")

In Episode 3's `prompts/` folder, you can see exactly how system and user prompts are used for routing and response generation.

---

## 8. Tokens and Pricing — The Economics of LLMs

Every API call costs money based on tokens. Understanding this helps you build cost-efficient systems.

**How pricing works:**
- Input tokens (your prompt) cost less than output tokens (the response)
- Longer prompts = higher cost
- More requests = higher cost

**Rough estimates (varies by model and provider):**
```
gpt-4o-mini:    ~$0.15 per 1M input tokens   ← good for learning
gpt-4o:         ~$5.00 per 1M input tokens   ← use sparingly
claude-haiku:   ~$0.25 per 1M input tokens   ← fast and cheap
claude-sonnet:  ~$3.00 per 1M input tokens   ← balanced
```

**Practical implications for Episode 3:**
- The routing call uses `max_tokens=20` because you only need one word back
- The response call uses `max_tokens=500` because you need a full answer
- Always set `max_tokens` — never leave it unlimited in production

---

## 9. Context Window — The Full Picture

The context window isn't just your messages. It includes everything:

```
┌─────────────────────────────────────────────────────────┐
│ CONTEXT WINDOW (e.g., 128,000 tokens for GPT-4o)        │
│                                                          │
│  ┌────────────────────────────────────────────────────┐  │
│  │ System Prompt (~500 tokens)                        │  │
│  ├────────────────────────────────────────────────────┤  │
│  │ Conversation History (~5,000 tokens per exchange)  │  │
│  ├────────────────────────────────────────────────────┤  │
│  │ Retrieved Documents / RAG context (~10,000 tokens) │  │
│  ├────────────────────────────────────────────────────┤  │
│  │ Tool outputs (~2,000 tokens)                       │  │
│  ├────────────────────────────────────────────────────┤  │
│  │ Current user message (~100 tokens)                 │  │
│  └────────────────────────────────────────────────────┘  │
│                                                          │
│  Max response: whatever tokens are left                  │
└─────────────────────────────────────────────────────────┘
```

In production systems you have to manage the context window deliberately:
- Summarise old conversation history
- Limit retrieved document length
- Monitor context usage per request
- Have a strategy for when context fills up

This becomes critical in Episodes 5 (RAG) and 6 (Memory).

---

*Back to [README](../README.md) · [Glossary](GLOSSARY.md) · [Misconceptions](MISCONCEPTIONS.md)*
