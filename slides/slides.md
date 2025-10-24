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
layout: two-cols-header
---

# How many large language models can you name?

::left::

<v-clicks>

- **Deepseek** (Deepseek AI)
- **GLM** (Z.ai)
- **Gemma** (Google)
- **Granite** (IBM)
- **Kimi K2** (Moonshot)
- **LFM** (Liquid AI)

</v-clicks>

::right::

<v-clicks>

- **Llama** (Meta)
- **Mistral** (Mistral AI)
- **Nemotron** (Nvidia)
- **Phi** (Microsoft)
- **Qwen** (Alibaba)
- **gpt-oss** (OpenAI)

</v-clicks>

<!--
On a piece of paper or in your head, take 20 seconds and name as many models that you can think of. Just tally them up on your fingers, quietly, and then we will see how we did.

Who had at least two? three?

Here are a few open ones. Open, as in, free to download the model weights and run inference yourself.

For about a year, I have been strangely obsessed with alternate language models other than just the big name flagship models that make most news. I don't have one clear reason for this attraction, but I think this diversity and the portability both make this territory really fun to explore. It is simply fun to try the different models, and see what purposes they serve best.
-->

---
layout: image
image: /emperor.png
backgroundSize: contain
---

<!--
The emperor has no clothes! This is that old Hans Christian Andersen story in which the vain emperor is conned into parading about in nothing, believing that he is wearing clothers, until a kid in the crowd says, "the emperor has no clothes!" which then causes the crowd to come to its senses as well.

I think that in the midst of all the AI hype and huckstering there is plenty of opportunity to point out that there are a lot of elaborate clothes everyone is marveling about and they just aren't real. The shallow religion of AGI hope, the ever-evolving landscape of buzzwords that themselves are so semantically diffused there good for not much other than exciting and belittling others. Even the term "Artifical Intelligence" seems like a misnomer and a load of human hubris. But after 75 years, I guess the name has stuck, so we'll use it.
-->

---
layout: image
image: /useful-engines.png
backgroundSize: contain
---

<!--
At the same time, there is something really useful here. Why spend so much energy imagining outlandish constructs of the future when what we have, even if AI development would stop and plateau today, is so rich with usability? We have tools that can parse and produce human language with imperfect yet impressive coherence. You might be surprised how much can be accomplished by even some of the smallest such engines. And you don't have to take someone else's word for it, you can download and try it yourself.
-->


---
layout: image
image: /model_comparison.png
backgroundSize: contain
---

<!--

I'd like to begin by remembering GPT-4. Luke Demi took the stage at CPOSC in 2023 and wowed us with a presentation that GPT-4 produced. And it was good! Do you remember that tipping point, when AI became good? That was GPT-4. And look at how it compares to even small models. I included large and proprietary models for reference. The open weights models are in blue. None of these except for gpt-oss have reasoning on.

Most of the models shown here are small, open, and can be hosted locally. Why might that be appealing?
-->

---
layout: image-right
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
If you run a 1 trillion parameter model and a 600 million parameter model on the same hardware, the 600 million one is going to feel realtime by comparison.

A smaller model can be trained to be better at a task than a larger behemoth. Re-ranking for instance. Huge models are great at taking a list, and a text, and ranking which items from the list are most relevant to the text. But the best re-rankers are a small fraction of the size of the behemoths.

Finally, they are much cheaper and more energy-efficient to run, whether you're paying a cloud inference provider or your own electricity bill.
-->

---
layout: image-left
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
**"Own"-able**: You control the model,  **Studyable**: inspect, understand, trust,  Sustainable**: usable apart from a lab, **Shareable**: use and build upon, recommend to others without strings attached. **Customizable**: You can fine-tune it with your own data for specific tasks. I do not do this, and I am skeptical that fine-tuning is as easy and useful as what some think. More importantly, if you have a candy store of small models to choose from, you can easily swap them in and out
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

This also unlocks deep personalization. You can train a model on your personal emails or notes to create a truly personal assistant.

It's also just a fantastic way to learn and have fun.

And practically, it enables portability and edge computing. Imagine a powerful language model running on a device in a remote location with no internet. It's possible today.
-->

---
layout: section
---

# How Do I Run Models Locally?

<!--
Okay, I've hopefully convinced you that this is a cool and useful thing to do. So, how do you actually do it? Let's look at a few popular tools.
-->

---
layout: image-right
image: /ollama.svg
backgroundSize: contain
---

## Ollama

Ollama is great for experimentation, as it has a lot of sane defaults and makes it easy to swap out models.

See models at [ollama.com/search](https://ollama.com/search) (stick with 4b or smaller for now; try qwen3, gemma3n, gemma3, granite4, phi4-mini...)

---

## Using ollama

1.  Install it from `ollama.com`
2.  Start the server (usually runs automatically)
    ```bash
    ollama serve
    ```
3.  Run a model from the command line
    ```bash
	ollama run qwen3:4b-instruct
    ```
4.  Chat away!

<!--
The easiest entry point for most people is a tool called Ollama. It bundles everything you need into one simple package.

You just install it, and it runs a server in the background. Then, from your terminal, you can type 'ollama run' followed by the name of a model. It will download the model if you don't have it and drop you right into a chat interface. It's the 'it just works' solution for local LLMs.
-->

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
layout: image-left
image: mlx.png
backgroundSize: contain
---

## On Apple Silicon

```sh
mlx_vlm.generate \
--model mlx-community/Qwen3-VL-4B-Instruct-6bit \
--prompt "Describe this image." \
--image picture_of_an_apple.png
```

<!--
-->

---
layout: image-right
image: /llama-cpp.svg
backgroundSize: contain
---

## llama.cpp

`llama.cpp` is what Ollama and many other tools use under the hood. It works well with GPUs, and is also the best tool to use if you only have CPU. It uses a quantization format called GGUF

---

### Using llama.cpp

1.  Install it from [github.com/ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp)
2.  Run the command-line interface, pulling a model directly from Hugging Face:
    ```bash
    llama-cli -hf unsloth/Qwen3-4B-Instruct-2507-GGUF:Q4_K_M
    ```
3.  Chat away!

<!--
Now let's look at the engine that powers many of these tools: llama.cpp. This is a C++ library that is incredibly efficient.

While Ollama is easier for beginners, llama.cpp gives you more direct control. It's particularly amazing because it's highly optimized for running on CPUs. So even if you don't have a fancy GPU, you can still run some very capable models.

Here, we're using its command-line tool to download a specific model file from Hugging Face and run it directly.
-->

---
layout: image-left
image: /llama-cpp-logo.svg
backgroundSize: contain
---

### Serving with `llama.cpp`

`llama.cpp` works best as a server. You can then connect to its OpenAI-like API with a client of your choice.

```sh
llama-server \
-hf unsloth/Qwen3-4B-Instruct-2507-GGUF:Q4_K_M
```
<!--
<SlidevVideo v-click autoplay autoreset='click'>
  <source src="/videos/llama-server-demo.webm" type="video/webm" />
</SlidevVideo>
-->

<!--
The real power of llama.cpp, much like Ollama, is running it as a server. You start the server process, pointing it at your model file.

It then exposes an API that is compatible with OpenAI's API. This is a game-changer. It means that any of the hundreds of tools and libraries designed to talk to GPT can be pointed at your local model with just a one-line change.

Here's a quick demo of what that looks like. You see the server starting up, and now it's ready to accept requests.
-->

---
layout: two-cols
---

### Clients

Once you have a server running, you can connect with any client.

<div class="pt-4">

#### Web
- Open-WebUI
- LibreChat

#### Desktop
- Jan
- GPT4All
- LM Studio

</div>

::right::

### CLI Clients

- OpenCode
- Aider
- Codex
- Crush
- Nanocoder
- Goose
- `llm`
- `mods`

![Aider Logo](/opencode.svg){style="height: 100px; margin-top: 2rem"}

<!--
And because these servers use a standard, OpenAI-compatible API, you have a massive ecosystem of clients to choose from.

If you want a web interface similar to ChatGPT, you can use Open-WebUI.
If you prefer a polished desktop app, Jan or LM Studio are great choices.
And if you're a command-line person like me, there are amazing tools like Aider for pair-programming with your local AI. The choice is yours.
-->

---
layout: section
---

# Quantization

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
