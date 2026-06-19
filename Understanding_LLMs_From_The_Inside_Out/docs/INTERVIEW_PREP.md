# 🎤 Interview Prep — Episode 1: LLMs

> How to talk about LLMs in technical interviews. These answers will set you apart.

---

## "Explain how LLMs work."

**Weak answer:**
> "They're trained on a lot of data and predict the next word."

**Strong answer:**
> "LLMs are transformer-based neural networks trained via next-token prediction on large text corpora. During training, the model sees billions of text sequences with the last token hidden and learns to predict it — adjusting billions of parameters to minimise prediction error. At inference time, the model receives the full context — system prompt, conversation history, user message — and produces a probability distribution over all possible next tokens. It samples from that distribution based on temperature, appends the token to the context, and repeats until a stop condition is met. The key engineering implication is that outputs are probabilistic and model-generated, not retrieved — which is why production systems need validation, structured output enforcement, and retrieval augmentation."

---

## "What is a token and why does it matter?"

> "A token is the unit of text that LLMs process — not words, but sub-word chunks. 'unhappiness' might be two tokens: 'un' and 'happiness'. This matters for three reasons: API costs are priced per token, context windows are measured in tokens so you need to estimate usage accurately, and tokenisation affects model behaviour — numbers are tokenised in ways that can confuse arithmetic reasoning, which is why tool calling matters."

---

## "What is the context window and what are its engineering implications?"

> "The context window is the total amount of text — measured in tokens — that the model can process in a single inference call. It includes the system prompt, full conversation history, any retrieved documents, tool outputs, and the current user message. When it fills up, the model loses access to earlier content — it doesn't summarise, it just can't see it. Engineering implications: you need to manage context deliberately — summarising history, limiting document size, monitoring usage. For RAG systems this is especially critical since retrieved documents can be large. In production, I'd track context usage per request and have a truncation or summarisation strategy when approaching the limit."

---

## "Why do LLMs hallucinate and how do you deal with it?"

> "Hallucination is a structural property of how LLMs work, not a bug. The model produces the most statistically likely continuation of the input text. When it has strong training signal — common facts, frequent patterns — it's usually correct. When it doesn't — obscure facts, recent events, precise calculations — it still produces fluent, confident text, because that's what it was trained to do. The three main engineering mitigations are: RAG, which gives the model the actual facts in the context rather than relying on training memory; structured outputs with validation, which catch outputs that don't match expected schemas; and tool calling, which offloads computations the model can't reliably do (like maths) to reliable external tools."

---

## "What's the difference between temperature 0 and temperature 1?"

> "Temperature controls the shape of the probability distribution the model samples from. At temperature 0, the model always picks the highest-probability next token — deterministic, same output every time. At temperature 1, it samples proportionally from the full distribution — more variety, occasionally surprising. Higher temperatures flatten the distribution further. For routing and classification tasks I use temperature 0 — determinism matters more than variety. For creative generation or brainstorming I use 0.7–1.0. I never use above 1.0 in production — the outputs become incoherent."

---

## "What's the difference between fine-tuning and prompting?"

> "Prompting guides the model's behaviour by providing context and instructions in the input — no weights change. It's fast, cheap, and flexible. Fine-tuning updates the model's weights on a new dataset, making the model inherently better at a specific task. Fine-tuning is better when: the task requires consistent behaviour that prompts can't reliably produce, you need to encode proprietary knowledge, or latency/cost of long prompts is a concern. In practice I'd start with prompting — it's often sufficient — and only fine-tune when prompting hits a ceiling."

---

## Resume Bullet for Episode 1

> Developed and documented a deep understanding of transformer-based LLM architecture — including tokenisation, attention mechanisms, context window management, temperature sampling, and hallucination dynamics — as part of the AI Engineering Roadmap 2026 curriculum.

---

*Back to [README](../README.md) · [Concepts](CONCEPTS.md) · [Glossary](GLOSSARY.md)*
