# ❌ The Biggest Misconceptions About LLMs

> Correcting the wrong beliefs that hold most beginners back.
> If you've thought any of these — you're not alone. Most people have.

---

## Misconception 1: "LLMs understand language like humans do"

**What people believe:** The model reads your message, understands it, and thinks of a response.

**What actually happens:** The model maps your tokens to a high-dimensional vector space, runs them through dozens of transformer layers with attention operations, and produces a probability distribution over the next token. It does this billions of times fast, for every token in its response.

There is no "understanding" in the human sense. There is extraordinarily sophisticated pattern matching, at a scale that produces behaviour that *looks like* understanding.

**Why this matters for engineering:** If you think the model "understands," you'll trust it too much. Knowing it's sophisticated pattern matching explains why validation, structured outputs, and tool calling exist — and why they matter.

---

## Misconception 2: "More parameters always means a better model"

**What people believe:** GPT-4 has more parameters than GPT-3.5, so GPT-4 is always better.

**The reality:** Parameter count is one factor among many. What also matters:
- Quality and diversity of training data
- Training techniques (RLHF, DPO, Constitutional AI)
- Fine-tuning approach
- Context length
- Inference optimisations

A smaller, well-trained, well-aligned model often outperforms a larger but poorly-trained one. And for specific tasks, a fine-tuned small model often beats a large general model.

**Practical implication:** Don't default to the biggest, most expensive model. Test cheaper models first. You'll often be surprised.

---

## Misconception 3: "LLMs have opinions, feelings, and consciousness"

**What people believe:** When Claude says "I find that interesting," it means it.

**The reality:** LLMs produce text that represents opinions and feelings because they were trained on human text that contains opinions and feelings. The text output is real. Whether there's any underlying experience is an open philosophical question — but for engineering purposes, treat it as sophisticated text generation.

**Why this matters:** Don't anthropomorphise your tools. It leads to overtrusting outputs ("the AI said it was confident") and underengineering your systems ("the AI seems to understand the task").

---

## Misconception 4: "If I ask the model to be accurate, it will be"

**What people believe:** "Please be accurate and don't hallucinate" will reduce hallucinations.

**The reality:** Instruction following is one capability. Factual accuracy is another. Asking for accuracy helps somewhat at the margins, but the model can't access facts it doesn't have. If it doesn't know something, it will produce a plausible-sounding answer regardless of your instructions.

**The engineering fix:** RAG (Episode 5) — give the model the facts in the context window, so it doesn't have to retrieve them from training memory.

---

## Misconception 5: "LLMs are just search engines"

**What people believe:** It's basically Google but you can ask questions.

**What's actually different:**
- Search engines retrieve existing documents. LLMs generate new text.
- Search engines don't reason or synthesise. LLMs can combine information in novel ways.
- Search engines are deterministic. LLMs are probabilistic.
- Search engines have no context window. LLMs maintain conversational context.

**What's similar:** Both have retrieval problems. Neither has perfect accuracy. Both can mislead you.

---

## Misconception 6: "The system prompt is private and secure"

**What people believe:** Users can't see or manipulate the system prompt.

**The reality:** System prompts are not cryptographically secure. Prompt injection attacks — where malicious user input tries to override or reveal the system prompt — are a real attack vector. The model can sometimes be coaxed into repeating the system prompt if asked cleverly.

**Engineering implication:** Don't put secrets in system prompts. Design systems that are safe even if the system prompt is revealed.

---

## Misconception 7: "The model remembers our previous conversations"

**What people believe:** "I've been talking to ChatGPT for months, it knows me."

**The reality:** Without explicit memory features, each conversation starts completely fresh. The model has no memory of previous sessions. What feels like memory in products like ChatGPT is usually:
- Conversation history injected into the context window
- Explicit memory features that store and retrieve past information
- Fine-tuning on your past data (rare, expensive)

**Engineering implication:** If your system needs memory, you have to build it — the model won't provide it. This is Episode 6.

---

## Misconception 8: "A longer prompt is always better"

**What people believe:** The more context I give, the better the output.

**The reality:** Up to a point, more context helps. But:
- Very long prompts can cause "lost in the middle" — the model pays less attention to information in the middle of the context
- More tokens = higher cost
- More tokens = slower response
- Irrelevant context can confuse the model

**Best practice:** Give the model exactly what it needs. No more, no less. The routing prompt in Episode 3 is 20 lines — not 200.

---

## Misconception 9: "Temperature 0 means the model will always be correct"

**What people believe:** Setting temperature=0 removes randomness, so outputs are reliable.

**The reality:** Temperature=0 makes outputs **deterministic** — the same prompt always gives the same output. But if that deterministic output is wrong, you get the same wrong answer every time.

Temperature controls randomness, not accuracy. A model at temperature=0 will still hallucinate — it'll just hallucinate the same thing every time.

**The fix:** Validation (Episode 3), RAG (Episode 5), tool calling (Episode 3).

---

## Misconception 10: "If I use a framework, I don't need to understand the underlying model"

**What people believe:** LangChain / LlamaIndex handles everything, I just need to know the API.

**The reality:** Frameworks abstract implementation. They don't abstract understanding. When something goes wrong — and it will — you need to know what's happening underneath. Debugging a broken RAG pipeline is impossible if you don't understand embeddings, retrieval, and context injection.

**This roadmap's philosophy:** Understand the fundamentals first. Add frameworks later, when they save you time rather than hide the mechanics.

---

*Back to [README](../README.md) · [Concepts](CONCEPTS.md) · [Glossary](GLOSSARY.md)*
