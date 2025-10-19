# Going Small, Local, Different with LLMs

## Title Slide

## Pop Quiz

Off the top of your head, how many language models can you name other than
OpenAI's, Anthropic's, X's, or Google's _flagship_ models? (In other words, other than GPT-*, Claude,
Grok, or Gemini)

- gpt-oss (OpenAI open source)
- Qwen (Alibaba)
- Llama (Meta)
- Deepseek
- Kimi K2 (Moonshot)
- GLM (Z.ai)
- Nemotron (Nvidia)
- Mistral

## Why Small?

- Lower latency
- May excel at a specific purpose
- Low cost, energy efficient

## Why Open?

- "Own"-able
- Studyable
- Sustainable
- Shareable
- Customizable

## Why Local?

- Privacy and Security
- Personalization
- Learning and fun
- Portable, edge deployment
- Offline

## How Do I Run Models Locally?

### Ollama

Ollama is great for experimentation, as it has a lot of sane defaults, and makes it easy to swap out models.

- Install it
- `ollama serve`
- `ollama run qwen3:4b-instruct`
- Chat away

### vLLM, SGLang

For production deployments, you may want to seriously consider vLLM or SGLang.

### llama.cpp

(svg picture)

llama.cpp is what ollama and many other tools use under the hood. It works well with GPUs, and is also the best tool to use if you only have CPU.

- Install it
- `llama-cli -hf unsloth/Qwen3-4B-Instruct-2507-GGUF:Q4_K_M`
- Chat away

### Serving

- llama.cpp works best as a server, then you can connect to its OpenAI-like API with a client of your choice
- `llama-server -hf unsloth/Qwen3-4B-Instruct-2507-GGUF:Q4_K_M`

### Clients

- Web: Open-WebUI, LibreChat
- CLI: OpenCode, Aider, Codex, Crush, Nanocoder, Goose, llm, mods
- Desktop: Jan, GPT4All, LM Studio

## Quantization



## Finding and Choosing Models

### The Hugging Face "Candy Store"

The Hugging Face Hub hosts millions of open source, downloadable models.

huggingface.co


## Other Candy Stores

- openrouter.ai/models (open and proprietary)
- vercel.com/ai-gateway/models (open and proprietary)

