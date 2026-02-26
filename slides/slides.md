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
- **Claude Sonnet/Opus/Haiku 4.5/4.6** (Anthropic)
- **Gemini 3 Flash, 3.1 Pro** (Google)
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
- Qwen3.5 397B A17B (Alibaba)
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

- "Own"-able
- Studyable
- Sustainable
- Shareable
- Verifiable
- Customizable

</v-clicks>

<!--
"Own"-able: You control the model,  Studyable: inspect, understand, trust, consistent Sustainable: usable apart from a lab, Shareable: use and build upon, recommend to others without strings attached. Verifiable: you know what model you have and whether it is changing or not, and don't have to 2nd-guess if the provider has nerfed it or swapped it out on you. Customizable: You can fine-tune it with your own data for specific tasks. I do not do this, and I am skeptical that fine-tuning is as easy and useful as what some think. But you can at least choose a model that fits your particular need, if you have a candy store of small models to choose from (which you do on huggingface), you can easily swap them in and out
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
layout: center
---

Right-sizing models{.biggie}

<!--
Last week I decided it was high time I finish a long-standing task of migrating blog platforms -- but the URLs didn't match. And it wasn't just something I could write a script to do, because while the URLs matched titles semantically, and strict string equality or even regular expressions weren't going to cut it. So, I thought, an LLM could do this easily! I used an agentic tool with Claude Opus 4.6, gave it a 3 sentence prompt, and done without a flaw. But then I wondered if I could use smaller models... Tried with Qwen Coder 30b and it took longer, and few more turns, but got the job done (python scripts everywhere). Then went to local models, another Qwen Coder 30b, and even got Qwen3-4B to do it! It was a bit of a lesson -- do I always need the largest, best model?
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

<!--
I don't generally feel the need to add another desktop app to my system, but people do love their LM Studio -- a very intuitive and fast way to work with local models. If you like open source, the other three are good options.
-->

---
layout: image-right
image: /apollo.png
backgroundSize: contain
---

# Mobile

- [Google Edge AI Gallery](https://github.com/google-ai-edge/gallery)
- [PocketPal](https://github.com/a-ghorbani/pocketpal-ai)
- [MNN Chat](https://github.com/alibaba/MNN) by Alibaba
- [Lemonade](https://github.com/lemonade-sdk/lemonade/)
- [Apollo](https://www.liquid.ai/apollo) by Liquid AI

<!--
Running models locally on your phone is tricky. I have been impressed with Google Edge AI Gallery. It uses hardware acceleration. At least on my phone, though, the models have to be exceedingly small.
-->

---
layout: two-cols
---

## vLLM, SGLang

For production deployments in which VRAM is abundant and you have many users, you may want to seriously consider the well-trusted vLLM or SGLang.

::right::

![vLLM](/vllm.svg){style="height:200px"}

![SGLang](/sglang.svg){style="height:100px"}

<!--
-->

---
layout: image
image: /mlx.svg
backgroundSize: contain
---

<!--
MLX for Apple Silicon -- I am about to recommend llama.cpp for everything, but I will say, in my testing, if you want raw tokens per second, MLX is faster than llama.cpp, even though llama.cpp does have Metal support.
-->

---

```sh
# https://github.com/ml-explore/mlx-lm
mlx.generate \
--prompt \
"Summarize the stochastic parrot paper" \
--model \
mlx-community/Qwen3-4B-Instruct-2507-mxfp8
```

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
llama-cli -hf \
unsloth/Qwen3-4B-Instruct-2507-GGUF:Q4_K_M \
-p "Is there a seahorse emoji?"
```

3. Web interface: once you have a model, just run `llama-server` then browse to localhost:8080
4.  Chat away!

<!--
I like llama.cpp because it is fast, optimized for CPU only, gives you direct control. It is the engine that is hiding behind tools like Ollama or LM Studio.
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

- `llama-server` (llama.cpp)
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

And because these servers use a standard, OpenAI-compatible API, you have a massive ecosystem of clients to choose from. These are just a few.

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

---
layout: image-right
image: /hf-models.png
backgroundSize: contain
---

## Hugging Face

The Open Model Store

[hf.co](https://hf.co)

<!--
In my hometown there was this variety store called Glen's Fair Priced Store. It had a hard to define range of goods. Pro photographers went there to get their equipment, as did kids to find Halloween costumes. There were layers upon layers of things for sale on the shelves, some quality things and some that were more suspicious. You had to move things around to even figure out what was there, and then you still might not be sure what you were looking at. You have probably walked into wonderful stores like this. Now imagine such a store, except almost everything is free. That is Hugging Face. Scholarly papers, models, information about models, even inference (costs associated). For today's discussion, let's just focus on downloadable model weights
-->

---

## So much in a name...

<v-clicks>

- `google/gemma-3n-E2B-it-litert-lm`
- `Qwen/Qwen3-VL-8B-Instruct-GGUF`
- `unsloth/GLM-4.7-Flash-REAP-23B-A3B-GGUF`
- `mradermacher/Qwen3-Coder-30B-A3B-Instruct-i1-GGUF`

</v-clicks>

<!--
I admit the naming can be intimidating. Especially when you realize that most every segment in the name matters. Let me try to read these in English... Gemma 3n from Google, 2 billion active parameters at a time, instruction tuned, built with LiteRT so that devices like newer Android phones can enjoy accelerated inference. An 8 billion Qwen 3 model, provided by the lab itself, instruct tuned, packaged in GGUF file format, and multi-modal -- this is a vision model able to take a picture as input and tell you that it is a picture of a shiny red apple. GLM 4.7 Flash (not to be confused with the much larger GLM 4.7), pruned by Cerebras to have 23 billion parameters total, with only 3 billion active at a time, presented by the very popular unsloth folks. And Qwen 3 Coder, 30 billion parameters total, only 3 billion of which are active, instruction trained, dynamically quantized, in GGUF file format, packaged by the prolific mradermacher.
-->

---
layout: image-right
image: /hf-community.png
backgroundSize: contain
---

## HF Communities

- unsloth
- mlx-community
- litert-community
- mradermacher
- bartowski
- Mungert

<!--
The first part of the model name is the community on Hugging Face. This is similar to an organization on Github. Just because you see a model that looks like what you want -- don't necessarily trust it. You will find that certain people release more reliable packages and quants than others. Here are some I am familiar with.
-->

---
layout: image-left
image: /hf-libraries.png
backgroundSize: contain
---

# Filter by Library

- GGUF for llama.cpp
- MLX for mlx-lm (Apple Silicon)
- LiteRT (Android/Google acceleration)

<!--
There are many ways of packaging models. A "library" on HF refers to the ML framework or tooling integration that a model's files are designed to work with.
-->

---

## 🎵 Tunes

Models often are denoted with "instruct" or "it" to indicate they are instruction-tuned -- this is usually the behavior you want; avoid "base" models.

Sometimes there are "thinking" variants.

You can also find models tuned for reranking, embedding, tool-calling, and other specific tasks.

---

## Parameters

The learned weights and biases that define how the model processes language, the number of "dials and switches" tuned during training to determine the weight of influence between input and output token. How likely is "hello" to be followed by "world"?

---

```python
# Our vocabulary: a=0, b=1, c=2
VOCAB = "abc"

def tokenize(text):
	"""Convert 'ab' -> [1,0,0, 0,1,0]"""
	indices = [VOCAB.index(c) for c in text]
	vector = torch.zeros(6)
	vector[indices[0]] = 1.0  # encode first char
	vector[3 + indices[1]] = 1.0  # encode second char (offset by 3)
	return vector

def decode(predicted_index):
	"""Convert a single index like 2 back to the character 'c'."""
	return VOCAB[predicted_index.item()]
```

<!--
Let's build a tiny model now to demonstrate the concept of parameters and weights. Here is the tokenizer. Our model understands 3 tokens: abc
-->

---

```python
import torch
weights = torch.tensor(
	[
		# 'a' 'b' 'c'  | 'a' 'b' 'c'  (for 1st and 2nd letter)
		[5.0, 0.0, 4.0, 5.0, 0.0, 4.0],  # predict 'a'
		[0.0, 0.0, 5.0, 5.0, 0.0, 0.0],  # predict 'b'
		[5.0, 5.0, 0.0, 4.0, 5.0, 5.0],  # predict 'c'
	]
)
def infer(input_vector):
	"""Predict the index of the next token from an input vector."""
	# multiply input by weights to get scores (logits)
	logits = torch.matmul(weights, input_vector)
	return torch.argmax(logits)
```

<!--
Here are the weights, and the inference function. Each of these weights is a parameter that can be tuned to indicate what token should follow what token.
-->

---

```python
if __name__ == "__main__":
	while True:
		text = input("Enter the first two letters: ")
		vector = tokenize(text)
		prediction = infer(vector)
		print(decode(prediction))
```

<!-- And here is our user interface, that chatbot loop -->

---
layout: image
image: /machine_learning.png
backgroundSize: contain
---

<!-- Let's tune our model to behave in useful ways. Just a reminder here of how machine learning works. (If asked: The pile gets soaked with data and starts to get mushy over time, so it's technically recurrent.) -->

---

````md magic-move
```python
# With the weights all equal, prediction would be random
[
	# a    b    c ,  a    b    c
	[0.0, 0.0, 0.0, 0.0, 0.0, 0.0],  # predict 'a'
	[0.0, 0.0, 0.0, 0.0, 0.0, 0.0],  # predict 'b'
	[0.0, 0.0, 0.0, 0.0, 0.0, 0.0],  # predict 'c'
]
```

```python {2,6}
[
# ab ⇒ c
	# a    b    c ,  a    b    c
	[0.0, 0.0, 0.0, 0.0, 0.0, 0.0],  # predict 'a'
	[0.0, 0.0, 0.0, 0.0, 0.0, 0.0],  # predict 'b'
	[5.0, 0.0, 0.0, 0.0, 5.0, 0.0],  # predict 'c'
]
```

```python {2,4}
[
# aa ⇒ a
	# a    b    c ,  a    b    c
	[5.0, 0.0, 0.0, 5.0, 0.0, 0.0],  # predict 'a'
	[0.0, 0.0, 0.0, 0.0, 0.0, 0.0],  # predict 'b'
	[5.0, 0.0, 0.0, 0.0, 5.0, 0.0],  # predict 'c'
]
```

```python {2,5}
[
# ca ⇒ b
	# a    b    c ,  a    b    c
	[5.0, 0.0, 0.0, 5.0, 0.0, 0.0],  # predict 'a'
	[0.0, 0.0, 5.0, 5.0, 0.0, 0.0],  # predict 'b'
	[5.0, 0.0, 0.0, 0.0, 5.0, 0.0],  # predict 'c'
]
```

```python {2,6}
[
# bb ⇒ c
	# a    b    c ,  a    b    c
	[5.0, 0.0, 0.0, 5.0, 0.0, 0.0],  # predict 'a'
	[0.0, 0.0, 5.0, 5.0, 0.0, 0.0],  # predict 'b'
	[5.0, 5.0, 0.0, 0.0, 5.0, 0.0],  # predict 'c'
]
```

```python {2,4}
[
# cc ⇒ a
	# a    b    c ,  a    b    c
	[5.0, 0.0, 4.0, 5.0, 0.0, 4.0],  # predict 'a'
	[0.0, 0.0, 5.0, 5.0, 0.0, 0.0],  # predict 'b'
	[5.0, 5.0, 0.0, 0.0, 5.0, 5.0],  # predict 'c'
]
```

```python {2,6}
[
# bc ⇒ c
	# a    b    c ,  a    b    c
	[5.0, 0.0, 0.0, 5.0, 0.0, 0.0],  # predict 'a'
	[0.0, 0.0, 5.0, 5.0, 0.0, 0.0],  # predict 'b'
	[5.0, 5.0, 0.0, 0.0, 5.0, 5.0],  # predict 'c'
]
```
````

<!--
In our case, the weights are a matrix showing each token's relationship to every other token. (click through each to show desired next token prediction.) For a given token, I am putting weight on the two tokens that I want to predict that letter.
-->

---
layout: center
---

<SlidevVideo v-click autoplay autoreset='click'>
  <source src="/llm.webm" type="video/webm" />
</SlidevVideo>

<!--
Even short words and abbreviations are a struggle sometimes, so I made this small language model to help me remember the third letter of so many things. First, just the general alphabet... Then I wanted to send a note and blind copy someone -- how do you spell that... my car was broken down and I need to call that roadside assistance organization... I wanted to ask them if my car battery had sufficient cold cranking... Maybe I should just call a taxi, but how do you spell it... I want to listen to british radio, and what's that network called...

And there you have it: artificial general intelligence! We have arrived.
-->

---

## Parameters, Weights

```python
		[5.0, 0.0, 4.0, 5.0, 0.0, 4.0],
		[0.0, 0.0, 5.0, 5.0, 0.0, 0.0],
		[5.0, 5.0, 0.0, 4.0, 5.0, 5.0],
```

- Above is an 18 parameter model (18 adjustable values)
- These are "the model weights"
- Smallest model I have used: 270M parameters
- Largest I have run on my hardware: 30B parameters
- Good size for a laptop with 16GB RAM: 4B parameters
- Flagship proprietary models are likely in trillions

---

## More parameters

- bigger
- smarter
- slower
- more consumptive

---

## Less parameters

- smaller
- more simplistic, hallucinating
- less world knowledge
- faster
- leaner, energy efficient

---
layout: image-right
image: /compress.svg
backgroundSize: contain
---

## Quantization is Lossy Compression


````md magic-move
```text
FP16 Weight: 0.82470703125
```

```text
FP16 Weight: 0.82470703125
INT8 Weight: 0.828125
(Stored as 106)
```

```text
FP16 Weight: 0.82470703125
INT8 Weight: 0.828125
INT4 Weight: 0.8125
(Stored as 13)
```
````

Integers are dequantized back to floats with some loss of precision (rounding).

<!--
Model weights that have had precision reduced from 16-bit floats to, say, 8-bit, 4-bit, or even smaller integers.

Think of quantization as lossy compression for AI models, like converting a massive WAV audio file to a much smaller MP3, or a raw bitmap photo to JPEG or PNG.

This makes the model file dramatically smaller and faster to run, but there's a trade-off. As you can see here, when you convert back and forth, you lose a tiny bit of the original information due to rounding. The magic is that for most language models, you can do this quite aggressively without a noticeable drop in quality.
-->

---

- K-Quants: Modern standard
- I-Quants: extreme low-bit compression for GPU
- Suffixes (S/M/L): Mixed precision for accuracy
- Q8_0: near-lossless
- Q6_K: Uncompromising model quality.
- Q4_K_M: Good balance
- IQ3 / IQ2: Use only when VRAM is tight
- CPU Users: Stick to K-quants

<!--
Experiment! Models quantize differently. Test - make a "sniff" test and a suite
-->

---

## unsloth/Qwen3.5-35B-A3B-GGUF

<v-clicks>

- Community: Unsloth
- Model: Qwen 3.5
- Parameters: 35 billion
- Activated Parameters: 3 Billion
- File format for llama.cpp
- Which quant? Q4_K_M is a good start

</v-clicks>

---
layout: image
image: /cloud-gpu.svg
backgroundSize: contain
---

<!--
Self hosting models could happen on rented hardware... here are some options. A little frightening.
-->

---

![OpenRouter Logo](/openrouter.svg){style="height:80px"}

[openrouter.ai/models](https://openrouter.ai/models)

![Vercel AI Gateway](/vercel.svg){style="height:60px"}

[vercel.com/ai-gateway/models](https://vercel.com/ai-gateway/models)

![Nvidia NIM](/nvidia.svg){style="height:60px"}

[build.nvidia.com/models](https://build.nvidia.com/models)


<!--
Finally, what if you want the variety of open models without the hassle of running them yourself?

There's a growing category of services that I call "meta-APIs". Companies like OpenRouter and Vercel host dozens of open and closed models, and Nvidia hosts quite a few open models, with a generous free request limit of 40 requests per minute.

I highly recommend OpenRouter. It has a number of free models with daily limits. It can also serve as a catalog of inference providers. If you find a particular inference provider you like, such as Fireworks, or SambaNova, or Baseten, or Cloudflare -- you can compare, decide, and then go directly to that provider and purchase inference.
-->

---
layout: center
---

<SlidevVideo v-click autoplay autoreset='click'>
  <source src="/local.webm" type="video/webm" />
</SlidevVideo>

<!-- local cpu on my laptop -->

---
layout: center
---

<SlidevVideo v-click autoplay autoreset='click'>
  <source src="/gpu.webm" type="video/webm" />
</SlidevVideo>

<!-- gpu in our basement, RTC 3080 Ti -->

---
layout: center
---

<SlidevVideo v-click autoplay autoreset='click'>
  <source src="/cloud.webm" type="video/webm" />
</SlidevVideo>

<!-- gpu in our basement, RTC 3080 Ti -->


---
layout: center
---

<SlidevVideo v-click autoplay autoreset='click'>
  <source src="/conclusion.webm" type="video/webm" />
</SlidevVideo>
