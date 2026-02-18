---
theme: default
title: What are you Inferring?
author: Jonathan Bowman
info: |
  An overview of small, local, and open-source Large Language Models (LLMs), how to run them, and where to find them.

  llms.bowmanjd.com
highlighter: shiki
presenter: dev
download: false
drawings:
  presenterOnly: true
  persist: false
selectable: true
mdc: true
transition: slide-left
class: text-center
hideInToc: true
layout: intro
---

# What are you Inferring?

LLMs that are Small, Local, and Different

[llms.bowmanjd.com](https://llms.bowmanjd.com)

<!--
It is a pleasure to be with you all this evening.
-->

---

# How many large language models can you name?

<v-clicks>

- **GPT-5.2** (OpenAI)
- **Claude Sonnet/Opus/Haiku 4.5** (Anthropic)
- **Gemini 3 Flash/Pro** (Google)
- **Grok 4.1** (xAI)

</v-clicks>

<!--
On a piece of paper or in your head, take 20 seconds and name as many models that you can think of. Just tally them up on your fingers, quietly. Models or labs that you know the models come from... Need a hint? Time... I have a hunch that for most of us, we pretty easily named 1 or two of these proprietary models from big US-based labs.
-->

---
layout: two-cols
---

<v-clicks>

- Deepseek V3.2
- GLM 5 (Z.ai)
- Gemma 3 4/12/27B (Google)
- Granite 4.0 Micro/Tiny/Small (IBM)
- Kimi K2.5 (Moonshot AI)
- LFM 2.5-1.2B (Liquid AI)
- Llama 4 Maverick (Meta)

</v-clicks>

::right::

<v-clicks>

- MiniMax M2.5
- Mistral Large 3 2512
- Nanbeige 4.1 3B
- Nemotron 3 Nano 30B A3B (Nvidia)
- Phi 4 (Microsoft)
- Qwen 3 235B A22B 2507 (Alibaba)
- gpt-oss (OpenAI)

</v-clicks>

<!--

I wonder if any of you had any open models in your list? Care to share what you thought of?

Here are a few open ones. Open, as in, free to download the model weights and run inference yourself.

For about a year, I have been strangely obsessed with alternate language models other than just the big name flagship models that make most news. I don't have one clear reason for this attraction, but I think this diversity and the portability make this territory really fun to explore. It is simply fun to try the different models, and see what purposes they serve best.

-->

---
layout: image
image: /model_comparison.png
backgroundSize: contain
---

<!--

I'd like to begin by remembering GPT-4. Luke Demi took the stage at CPOSC in 2023 and wowed us with a presentation that GPT-4 produced. And it was good! Do you remember that tipping point, when AI became good? That was GPT-4. And look at how it compares to even small models. I included large and proprietary models for reference. The open weights models are in blue. None of these have reasoning on except for MiniMax, gpt-oss, and Nemotron.

Of the open models, some of these, towards the right, are self-hostable for any of us. Some, towards the left, are self-hostable if you want to buy a few Nvidia B200 GPUs. Each B200 costs a minimum of $30,000, so do the math. That sounds crazy, but there could be companies who want that level of control and privacy, and this would be an acceptable cost.

There is a mid-range -- with a few thousand or even just a few hundred, you can run a smaller model that certainly isn't as capable as the large ones, but isn't puny either.

-->

---

Related but not Equal:

- Open models
- Small models
- Self-hostable models

<!--

Today we are talking about these potentially overlapping qualities. If you want to self-host, then you need an open model, and probably a pretty small model. But just because a model is open doesn't mean you can self-host it realistically, and just because a model is small doesn't mean it is small enough to run in any usable way on your hardware. But there are small open models that any of you can self-host, and there are probably applications and activities in which even those very small models are desirable.

-->

---
layout: image-right
image: /open-door.svg
backgroundSize: contain
---

# Open is better

<v-clicks>

- **"Own"-able**
- **Studyable**
- **Sustainable**
- **Shareable**
- **Customizable**

</v-clicks>

<!--
**"Own"-able**: You control the model,  **Studyable**: inspect, understand, trust, consistent Sustainable**: usable apart from a lab, **Shareable**: use and build upon, recommend to others without strings attached. **Customizable**: You can fine-tune it with your own data for specific tasks. I do not do this, and I am skeptical that fine-tuning is as easy and useful as what some think. More importantly, if you have a candy store of small models to choose from (which you do on huggingface), you can easily swap them in and out
-->

---
layout: image-left
image: /feather.svg
backgroundSize: contain
---

# The Benefits of being Small

<v-clicks>

- **Low latency**: Faster response time
- **Can be purpose-built**: May be fine-tuned for specific tasks
- **Low cost**: Cheaper to run and better for the environment.

</v-clicks>

<!--

On the same hardware, a 32 billion parameter model will scream in comparison to a 1 trillion parameter model.

A smaller model can be trained to be better at a task than a larger behemoth. Re-ranking for instance. Huge models are great at taking a list, and a text, and ranking which items from the list are most relevant to the text. But the best re-rankers are a small fraction of the size of the behemoths.

Finally, they are much cheaper and more energy-efficient to run, whether you're paying a cloud inference provider or your own electricity bill.
-->

---
layout: image-right
image: /local.svg
backgroundSize: contain
---

# Local

<v-clicks>

- **Privacy and Security**
- **Learning and fun**
- **Portable, edge deployment**
- **Offline**

</v-clicks>

::right::

`::1`{.biggie}

<!--
So what happens when you combine small and open? You get the ability to run models locally, on your own hardware.

The most obvious benefit is privacy. If you're working with sensitive information, running a model locally means your data never gets sent to a third-party server.

But it is just fun and satisfying. And you don't even need the internet.

-->

---
layout: section
---

# How Do I Run Models Locally?

<!--
A few popular tools for running models locally, along with my recommendation.
-->

---
layout: image-right
image: /ollama.svg
backgroundSize: contain
---

## Ollama

Ollama is great for experimentation, as it has a lot of sane defaults and makes it easy to swap out models.

See models at [ollama.com/search](https://ollama.com/search) but warning: it is confusing

---
layout: image-left
image: /jan.png
backgroundSize: contain
---

# Desktop apps

- [LM Studio](https://lmstudio.ai/)
- [Jan](https://www.jan.ai/)
- [GPT4All](https://www.nomic.ai/gpt4all)
- [AnythingLLM](https://anythingllm.com/)

---
layout: two-cols
---

## vLLM, SGLang

For production deployments in which VRAM is abundant, you may want to seriously consider vLLM or SGLang.

::right::

![vLLM](/vllm.svg){style="height:200px"}

![SGLang](/sglang.svg){style="height:100px"}

<!--
When you move from experimenting on your laptop to a serious production environment with powerful GPUs, you'll want more performance.

Tools like vLLM and SGLang are optimized for high-throughput serving. They use clever techniques like paged attention to serve many users at once from a single GPU, maximizing your hardware's potential. These are the tools you'd use to build your own AI-powered application at scale.
-->

---

```sh
# https://github.com/ml-explore/mlx-lm
mlx.generate --prompt "Summarize the stochastic parrot paper"
--model mlx-community/Qwen3-4B-Instruct-2507-mxfp8
```

![mlx](/mlx-horizontal.svg)

---
layout: image-left
image: /llama-cpp.svg
backgroundSize: contain
---

## llama.cpp

I recomend `llama.cpp`. It works well with GPUs, and is also the best tool to use if you only have CPU. It uses a quantization format called GGUF.

---

### Using llama.cpp

1.  Install it from [github.com/ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp)
2.  Run the command-line interface, pulling a model directly from Hugging Face:
    ```bash
    llama-cli -hf unsloth/Qwen3-4B-Instruct-2507-GGUF:Q4_K_M \
		      -p "Is there a seahorse emoji?"
    ```
3. Web interface: once you have a model, just run `llama-server` then browse to localhost:8080
4.  Chat away!

<!--
Now let's look at the engine that powers many of these tools: llama.cpp. This is a C++ library that is incredibly efficient.

While Ollama is easier for beginners, llama.cpp gives you more direct control. It's particularly amazing because it's highly optimized for running on CPUs. So even if you don't have a fancy GPU, you can still run some very capable models.

Here, we're using its command-line tool to download a specific model file from Hugging Face and run it directly.
-->

---

> Is there a seahorse emoji?

Yes, there is a seahorse emoji. It is represented by 🐙, which is the seahorse emoji...

> Really!? 🐙 is the *seahorse* emoji?

You're absolutely right! 🐙 is indeed the seahorse emoji... The emoji was introduced in Unicode and is widely used...

So yes—🦞 is the seahorse emoji! 🐙✨ 😄

<!--
To start out, I recommend giving Qwen 3 4B Instruct a try. It is small enough to run on your laptop, even if you don't have a GPU. Might even run on your phone. This was not its best moment...
-->

---
layout: two-cols
---

## Web Clients

- llama.cpp's `llama-server`
- Open-WebUI
- LibreChat

::right::

## CLI Clients

- OpenCode
- Pi
- Codex
- Claude Code (with some help)
- Aider

![Aider Logo](/opencode.svg){style="height: 100px; margin-top: 2rem"}

<!--

Once you have a server running, you can connect with any client.
And because these servers use a standard, OpenAI-compatible API, you have a massive ecosystem of clients to choose from.

-->

---
layout: image
image: /open-webui.png
backgroundSize: contain
---

<!--
This is Open-WebUI, running in our basement
-->

---
layout: image
image: /llama-server.png
backgroundSize: contain
---

<!--
This is llama.cpp's llama-server, running locally on my laptop
-->

---
layout: section
---

# Model selection

<!--
You may have noticed that weird `Q4_K_M` in the model name earlier. That brings us to a key concept that makes all of this possible on consumer hardware: Quantization.
-->

---
layout: image-right
image: /compress.svg
backgroundSize: contain
---

## Quantization is Lossy Compression

Model weights that have had precision reduced from 32-bit or 16-bit floats to, say, 8-bit, 4-bit, or even smaller integers.

````md magic-move
```text
FP16 Weight: 0.82470703125
```

```text
INT8 Weight: 0.828125
(Stored as 106)
```

```text
INT4 Weight: 0.8125
(Stored as 13)
```
````

With integers, they are dequantized back to floats when running the model, *with some loss of precision* (rounding).

<!--
Think of quantization as lossy compression for AI models, like converting a massive WAV audio file to a much smaller MP3.

The original model weights are stored as high-precision numbers, like 16-bit floating points. Quantization converts them to lower-precision numbers, like 4-bit integers.

This makes the model file dramatically smaller and faster to run, but there's a trade-off. As you can see here, when you convert back and forth, you lose a tiny bit of the original information due to rounding. The magic is that for most language models, you can do this quite aggressively without a noticeable drop in quality.
-->

---
layout: section
---

# Finding and Choosing Models

<!--
Okay, so you have the tools, you understand the basics of quantization. Now for the fun part: where do you find all these models?
-->

---
layout: image
image: /screenshots/huggingface-hub.png
backgroundSize: cover
---

<div class="absolute bottom-10 left-10 p-4 bg-black bg-opacity-50 rounded">

## The Hugging Face "Candy Store"

The Hugging Face Hub hosts millions of open source, downloadable models.

[huggingface.co/models](https://huggingface.co/models)

</div>

<!--
The main place everyone goes is the Hugging Face Hub. It's like a giant GitHub for AI.

You can find models, datasets, and even demo applications. There are leaderboards to compare model performance, and each model has a "model card" that explains what it is, how it was trained, and how to use it. It is an indispensable resource for the entire open-source AI community.
-->

---
layout: two-cols
---

## Cloud Inference Providers

If you don't want to run models locally, these services provide APIs for hundreds of different open and proprietary models.

![OpenRouter Logo](/openrouter.svg){class="m-auto"}

[openrouter.ai/models](https://openrouter.ai/models)

::right::

<br/>
<br/>

![Vercel AI Gateway](/vercel.svg){class="m-auto"}

[vercel.com/ai-gateway/models](https://vercel.com/ai-gateway/models)


<!--
Finally, what if you want the variety of open models without the hassle of running them yourself?

There's a growing category of services that I call "meta-APIs". Companies like OpenRouter and Vercel host dozens of open and closed models, all accessible through a single, unified API. You can switch from a Mistral model to a Llama model to a Qwen model just by changing one parameter in your API call. It's the best of both worlds: access and convenience.
-->

---
layout: default
---

# Thank You

**Questions?**

<!--
That's a whirlwind tour of the world beyond the big, proprietary LLMs. We've seen why small, open, and local models are so powerful, and we've looked at the tools you need to get started.

I hope this has inspired you to download a model and give it a try. Thank you. I'd be happy to take any questions.
-->
```
