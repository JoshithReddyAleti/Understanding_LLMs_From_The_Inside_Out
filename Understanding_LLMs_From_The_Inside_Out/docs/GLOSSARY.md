# 📖 Glossary — AI Engineering Terms, Defined Clearly

> Every term you'll encounter in AI engineering — explained without jargon.
> Bookmark this. You'll come back to it.

---

## A

**Agent**
An AI system that can take actions, not just generate text. It decides what to do, does it, observes the result, and decides what to do next. Covered in Episode 7.

**Attention**
The mechanism inside transformers that lets the model decide which previous tokens are most relevant when predicting the next one. The "A" in the famous paper "Attention Is All You Need."

**API (Application Programming Interface)**
A way for your code to talk to another service. When you call `openai.chat.completions.create(...)`, you're using OpenAI's API. Covered heavily in Episode 2 and 3.

---

## B

**Base Model**
A model that has been pre-trained on text data but not yet fine-tuned to be an assistant. Base models just continue text — they don't follow instructions or have a persona.

**Benchmark**
A standardised test used to measure model performance. Examples: MMLU (general knowledge), HumanEval (coding), HellaSwag (commonsense reasoning). Useful for comparing models but not always representative of real-world performance.

---

## C

**Chain-of-Thought (CoT)**
A prompting technique where you ask the model to "think step by step" before giving an answer. Dramatically improves performance on reasoning tasks. Example: "Explain your reasoning, then give your final answer."

**Context Window**
The maximum amount of text (measured in tokens) that a model can process in a single call. Everything the model "sees" — system prompt, conversation history, documents, your message — must fit within this limit.

**Completion**
The text a model generates in response to a prompt. Also the name for the older API endpoint style (as opposed to the newer chat-based format).

---

## E

**Embedding**
A numerical representation of text as a list of floating-point numbers (a vector). Texts with similar meanings have similar embeddings. Used for semantic search, RAG, and classification.

**Encoder / Decoder**
Two types of transformer architecture. Encoders (like BERT) are good at understanding text. Decoders (like GPT) are good at generating text. Most modern LLMs are decoder-only.

---

## F

**Fine-tuning**
Training a pre-trained model further on a smaller, task-specific dataset. Used to specialise a general model for a particular domain or behaviour. More expensive than prompting but can produce better results for narrow tasks.

**Foundation Model**
A large model trained on broad data that can be adapted to many tasks. GPT-4, Claude, Llama are all foundation models.

---

## G

**Generation**
The process of producing text token by token. The model generates one token at a time, adds it to the context, then generates the next token — until it hits a stop condition.

**GPU (Graphics Processing Unit)**
The hardware that makes training and running LLMs practical. Originally designed for gaming, GPUs can process thousands of mathematical operations simultaneously — exactly what neural networks need.

---

## H

**Hallucination**
When a model generates text that sounds confident and plausible but is factually incorrect. Not a bug — it's a side effect of how LLMs work. The fix is validation, RAG, and structured outputs.

**HuggingFace**
A company and platform that hosts thousands of open-source models and datasets. Think "GitHub for AI models."

---

## I

**Inference**
Using a trained model to generate responses. As opposed to training, which is when the model's weights are being updated. When you call the OpenAI API, you're doing inference.

**In-Context Learning**
The ability to teach an LLM new behaviour by including examples in the prompt — without changing the model's weights. Few-shot prompting is a form of in-context learning.

---

## L

**LLM (Large Language Model)**
A neural network with billions of parameters, trained on vast amounts of text, that can generate coherent, contextually appropriate text. GPT-4, Claude, Gemini, Llama are all LLMs.

**Loss**
A number that measures how wrong the model's predictions are during training. The training process tries to minimise loss. Lower loss = better predictions.

---

## M

**Model**
In this context, the trained neural network — the weights file that encodes everything the model has "learned." Not to be confused with the product built around it.

**Multimodal**
A model that can process more than one type of data — text, images, audio, video. GPT-4o and Claude are multimodal.

---

## P

**Parameters**
The numbers inside a neural network that are adjusted during training. "GPT-4 has 1 trillion parameters" means there are 1 trillion numbers that collectively encode what the model knows. More parameters generally means more capable — but also more expensive.

**Prompt**
The text you send to an LLM. The quality of your prompt directly affects the quality of the response. Prompt engineering is the skill of writing prompts that reliably get good outputs.

**Prompt Engineering**
The practice of writing, testing, and refining prompts to get better outputs from LLMs. A real skill — not just "asking questions better."

---

## R

**RAG (Retrieval-Augmented Generation)**
A technique that retrieves relevant documents from a database and adds them to the LLM's context before generating a response. Gives the model access to up-to-date or private information. Covered in Episode 5.

**RLHF (Reinforcement Learning from Human Feedback)**
The training technique used to turn a base model into a helpful assistant. Humans rate model outputs, a reward model learns those preferences, and the LLM is trained to maximise the reward.

---

## S

**Sampling**
How the model picks the next token. It calculates a probability distribution, then picks one token based on those probabilities (at temperature > 0) or always picks the most likely token (at temperature = 0).

**Semantic Search**
Search that finds results by meaning, not exact keyword match. "Show me articles about fixing my car" finds relevant content even if the word "car" doesn't appear — because embeddings capture meaning.

**System Prompt**
An instruction given to the model before the conversation starts. Invisible to the end user but shapes all model behaviour. As an AI engineer, this is one of your most important tools.

---

## T

**Temperature**
A number (usually 0–2) that controls how random the model's outputs are. 0 = always picks most likely token. Higher values = more variety, more creativity, more randomness.

**Token**
The basic unit of text that LLMs process. Not quite words — tokens can be whole words, word fragments, punctuation, or spaces. "unhappiness" is 2 tokens. "ChatGPT" is 3 tokens.

**Tokenisation**
The process of splitting text into tokens before feeding it to the model. Different models use different tokenisers.

**Transformer**
The neural network architecture that powers all modern LLMs. Introduced in 2017. Uses attention mechanisms to process all input tokens simultaneously rather than sequentially.

---

## V

**Vector**
A list of numbers. Embeddings are vectors. The "distance" between two vectors in high-dimensional space represents how similar or different two pieces of text are.

**Vector Database**
A database designed to store and search vectors (embeddings) efficiently. Examples: Pinecone, Weaviate, ChromaDB, pgvector. Used in RAG systems to find relevant documents.

---

## W

**Weights**
Same as parameters — the numbers inside a model that are set during training and fixed during inference. "Loading a model" means loading its weights into memory.

---

*Back to [README](../README.md) · [Concepts](CONCEPTS.md) · [Misconceptions](MISCONCEPTIONS.md)*
