<a href="README.md" target="_blank">English</a> | 中文

# Awesome AI Tools

> 精选的 AI/SaaS 产品列表

精选的 AI 和 SaaS 产品集合，定期更新最新的工具和模型。

## 目录

- 🤖 [大语言模型 (LLMs)](#大语言模型-llms)
  - [通用大语言模型](#通用大语言模型)
  - [Web 开发 LLM](#web-开发-llm)
- 🖼️ [AI 图像工具](#ai-图像工具)
  - [文生图大模型](#文生图大模型)
  - [图生图大模型](#图生图大模型)
- 📽️ [AI 视频工具](#ai-视频工具)
  - [文生视频大模型](#文生视频大模型)
  - [图生视频大模型](#图生视频大模型)
- 🎶 [AI 音频工具](#ai-音频工具)
  - [文字转语音 (TTS) 大模型](#文字转语音-tts-大模型)
  - [语音转文字 (ASR) 大模型](#语音转文字-asr-大模型)
  - [音乐生成大模型](#音乐生成大模型)
  - [播客托管平台](#播客托管平台)
- 💻 [AI 编程工具](#ai-编程工具)
  - [AI 编程代理与 IDE](#ai-编程代理与-ide)
  - [代码补全工具](#代码补全工具)
  - [低代码/无代码平台](#低代码无代码平台)
  - [代码质量与安全工具](#代码质量与安全工具)
- 🔍 [AI 搜索工具](#ai-搜索工具)
  - [搜索增强型 LLM](#搜索增强型-llm)
  - [AI 搜索 API 与基础设施](#ai-搜索-api-与基础设施)
  - [网页抓取工具](#网页抓取工具)
  - [AI 搜索引擎](#ai-搜索引擎)
  - [电商搜索助手](#电商搜索助手)
  - [AI 浏览器](#ai-浏览器)
- 🔗 [AI 聚合平台](#ai-聚合平台)
  - [面向开发者](#面向开发者)
  - [面向企业](#面向企业)
  - [面向普通用户](#面向普通用户)
- ⚙️ [AI 基础设施与 GPU 云](#ai-基础设施与-gpu-云)
  - [GPU 云平台](#gpu-云平台)
  - [数据基础设施与 OLAP 数据库](#数据基础设施与-olap-数据库)
  - [AI 训练与计费工具](#ai-训练与计费工具)
  - [后端即服务](#后端即服务)
  - [虚拟化与沙箱环境](#虚拟化与沙箱环境)
  - [LLM 应用框架](#llm-应用框架)
  - [AI Agent 基础设施](#ai-agent-基础设施)
    - [Agent 平台](#agent-平台)
    - [Agent 工具与服务](#agent-工具与服务)
    - [Agent 数据基础设施](#agent-数据基础设施)
    - [Agent 编排](#agent-编排)
    - [Agent 平台基础设施](#agent-平台基础设施)
- 🔐 [认证与身份服务](#认证与身份服务)
- 💳 [AI Agent 支付基础设施](#ai-agent-支付基础设施)
- 📊 [AI 演示文稿工具](#ai-演示文稿工具)
- 🎨 [AI 设计工具](#ai-设计工具)
- 📚 [AI 故事书生成](#ai-故事书生成)
- 💬 [对话智能](#对话智能)
- 📈 [销售与营销内容](#销售与营销内容)
- 🎨 [AI 3D 模型生成](#ai-3d-模型生成)
  - [文本到 3D 模型](#文本到-3d-模型)
  - [图像到 3D 模型](#图像到-3d-模型)
  - [3D 电商平台](#3d-电商平台)
  - [无代码 3D 创作工具](#无代码-3d-创作工具)
  - [3D CAD 与制造工具](#3d-cad-与制造工具)
  - [概念艺术与创意工具](#概念艺术与创意工具)
- 💬 [AI 聊天机器人](#ai-聊天机器人)
  - [角色聊天机器人](#角色聊天机器人)
  - [NSFW 聊天机器人](#nsfw-聊天机器人)
  - [专业聊天机器人](#专业聊天机器人)
- 🤖 [AI 代理](#ai-代理)
- 🏭 [应用开发工厂](#应用开发工厂)
- 💼 [AI 招聘与求职](#ai-招聘与求职)
  - [面向招聘者](#面向招聘者)
  - [面向求职者](#面向求职者)
  - [通用平台](#通用平台)
- 📊 [AI 数据工具](#ai-数据工具)
  - [数据标注](#数据标注)
  - [数据分析](#数据分析)
  - [合成数据](#合成数据)
- 📚 [AI 教育)
  - [作业与解题](#作业与解题)
  - [学习工具与闪卡](#学习工具与闪卡)
  - [语言学习](#语言学习)
  - [数学工具](#数学工具)
  - [辅导平台](#辅导平台)
  - [课堂工具](#课堂工具)
- 📝 [AI 生产力工具](#ai-生产力工具)
  - [项目管理与协作](#项目管理与协作)
  - [笔记与知识管理](#笔记与知识管理)
  - [表单与问卷](#表单与问卷)
  - [日程安排](#日程安排)
  - [PDF 与文档工具](#pdf-与文档工具)
  - [文档平台](#文档平台)
  - [工作流自动化](#工作流自动化)
  - [数据可视化](#数据可视化)
  - [内容创作](#内容创作)
  - [企业 AI 助手](#企业-ai-助手)
  - [AI 聊天助手](#ai-聊天助手)
- 💰 [AI 金融与会计工具](#ai-金融与会计工具)
  - [财务运营与会计](#财务运营与会计)
  - [金融分析与情报](#金融分析与情报)
  - [金融基础设施](#金融基础设施)
- 📈 [AI SEO 与营销工具](#ai-seo-与营销工具)
  - [GEO (Google E-E-A-T 优化) 工具](#geo-google-e-e-a-t-优化-工具)
  - [SEO 优化工具](#seo-优化工具)
  - [SEO 本地化工具](#seo-本地化工具)
- 🏢 [垂直领域解决方案](#垂直领域解决方案)
- 🎥 [屏幕录制工具](#屏幕录制工具)
- 📊 [AI 电子表格工具](#ai-电子表格工具)

## 大语言模型 (LLMs)

### 通用大语言模型

_这些是基础的大语言模型，可通过 API 调用。许多 AI 应用都是基于这些模型构建的。_

- <a href="https://gemini.google.com/" target="_blank">Gemini</a> (**Google** · 3.0 Pro / 2.5 Pro) - Google DeepMind 的多模态大模型，支持文字、图像、音频甚至视频输入
- <a href="https://x.ai/" target="_blank">Grok</a> (**xAI** · 4.1) - 埃隆·马斯克创办的 AI 公司，开发 Grok 聊天模型并探索解释型智能
- <a href="https://www.anthropic.com/" target="_blank">Claude</a> (**Anthropic** · Opus 4.5 / Sonnet 4.5 / Opus 4.1) - 主打安全与可控性的 LLM 开发商，其 Claude 系列也是代表产品
- <a href="https://openai.com/" target="_blank">GPT</a> (**OpenAI** · 5.1 / 5 / 4.5 / 4o) - AI 研究和部署先锋，致力于让通用人工智能造福全人类
- <a href="https://chat.qwen.ai/" target="_blank">Qwen</a> (**Alibaba** · 3 Max) - 大语言模型
- <a href="https://kimi.moonshot.cn/" target="_blank">Kimi</a> (**Moonshot AI** · K2) - 大语言模型，文章总结能力较强
- <a href="https://docs.z.ai/guides/llm/glm-4.6" target="_blank">GLM</a> (**Z.ai** · 4.6) - 大语言模型
- <a href="https://www.deepseek.com/" target="_blank">DeepSeek</a> (**DeepSeek** · v3.2) - 大语言模型
- <a href="https://llama.meta.com/" target="_blank">Llama</a> (**Meta** · 最新版) - Meta 推出的开源大语言模型系列，轻量高效覆盖多模态功能
- <a href="https://www.minimax.io/" target="_blank">MiniMax</a> (**MiniMax** · 最新版) - 大语言模型
- <a href="https://hunyuan.tencent.com/" target="_blank">Hunyuan</a> (**Tencent** · 最新版) - 大语言模型
- <a href="https://mistral.ai/" target="_blank">Mistral</a> (**Mistral AI** · 最新版) - 法国开源 LLM 新势力，Mistral 推理模型强化链式思维能力
- <a href="https://deepmind.google/models/gemma/" target="_blank">Gemma</a> (**Google** · 最新版) - 大语言模型
- <a href="https://aleph-alpha.com" target="_blank">Luminous</a> (**Aleph Alpha** · 最新版) - 强人工智能技术研发，支持多语言文本和图像分析

### Web 开发 LLM

_这些是针对 Web 开发任务优化的大语言模型，可通过 API 调用。许多 AI 编程应用都是基于这些模型构建的。_

- <a href="https://www.anthropic.com/news/claude-opus-4-5" target="_blank">Claude Opus 4.5</a> (**Anthropic** · 20251101) - 针对 Web 开发任务优化，具备思考能力
- <a href="https://aistudio.google.com/app/prompts/new_chat?model=gemini-3-pro-preview" target="_blank">Gemini 3 Pro</a> (**Google** · 最新版) - 针对 Web 开发优化的多模态模型
- <a href="https://platform.openai.com/docs/models/gpt-5" target="_blank">GPT-5 Medium</a> (**OpenAI** · 最新版) - 针对 Web 开发任务优化
- <a href="https://www.anthropic.com/news/claude-sonnet-4-5" target="_blank">Claude Sonnet 4.5</a> (**Anthropic** · 20250929) - 针对 Web 开发优化，具备思考能力
- <a href="https://openai.com/index/gpt-5-1/" target="_blank">GPT-5.1</a> (**OpenAI** · 最新版) - 先进的 Web 开发模型
- <a href="https://docs.z.ai/guides/llm/glm-4.6" target="_blank">GLM-4.6</a> (**Z.ai** · 最新版) - 开源 MIT 许可模型，针对编码优化
- <a href="https://huggingface.co/moonshotai/Kimi-K2-Thinking" target="_blank">Kimi K2 Thinking</a> (**MoonshotAI** · Turbo) - 针对 Web 开发任务优化
- <a href="https://platform.openai.com/docs/models/gpt-5.1-codex" target="_blank">GPT-5.1 Codex</a> (**OpenAI** · 最新版) - 专门的代码生成模型
- <a href="https://www.minimax.io/news/minimax-m2" target="_blank">MiniMax M2</a> (**MiniMax** · 最新版) - 开源 Apache 2.0 许可模型
- <a href="https://api-docs.deepseek.com/news/news250929" target="_blank">DeepSeek V3.2</a> (**DeepSeek AI** · Exp) - 开源 MIT 许可模型
- <a href="https://qwenlm.github.io/blog/qwen3-coder" target="_blank">Qwen3 Coder</a> (**Alibaba** · 480B) - 专门的编码模型，Apache 2.0 许可

## AI 图像工具

### 文生图大模型

_这些是基础的文生图大模型，可通过 API 调用。许多 AI 图像应用都是基于这些模型构建的。_

- <a href="https://ai.studio/banana" target="_blank">Gemini</a> (**Google** · 3.0 Pro / 2.5 Flash) - Google 开发的文生图大模型
- <a href="https://hunyuan.tencent.com/image/en" target="_blank">腾讯混元</a> (**Tencent** · 3.0) - 腾讯开发的文生图大模型
- <a href="https://deepmind.google/models/imagen/" target="_blank">Imagen</a> (**Google** · 4.0 Ultra / 4.0) - Google DeepMind 开发的文生图大模型
- <a href="https://seed.bytedance.com/en/tech/seedream3_0" target="_blank">Seedream</a> (**ByteDance** · 4.0) - 字节跳动开发的文生图大模型
- <a href="https://modelstudio.console.alibabacloud.com/" target="_blank">WAN</a> (**Alibaba** · 2.5) - 阿里巴巴开发的文生图大模型
- <a href="https://platform.openai.com/docs/models/gpt-image-1" target="_blank">GPT Image</a> (**OpenAI** · 1) - OpenAI 开发的文生图大模型
- <a href="https://microsoft.ai/news/introducing-mai-image-1-debuting-in-the-top-10-on-lmarena/" target="_blank">MAI Image</a> (**Microsoft AI** · 1) - Microsoft AI 开发的文生图大模型
- <a href="https://qwenlm.github.io/blog/qwen-image/" target="_blank">Qwen Image</a> (**Alibaba** · 开源) - 阿里巴巴开发的开源文生图大模型
- <a href="https://openai.com/index/dall-e-3/" target="_blank">DALL-E</a> (**OpenAI** · 3) - OpenAI 开发的文生图大模型
- <a href="https://bfl.ai/" target="_blank">Flux</a> (**Black Forest Labs** · 1.1 Pro / 1 Kontext) - Black Forest Labs 开发的文生图大模型
- <a href="https://stability.ai/" target="_blank">Stable Diffusion</a> (**Stability AI** · v3.5) - 开源文生图大模型（Stable Diffusion），提供 API 访问
- <a href="https://ideogram.ai/" target="_blank">Ideogram</a> (**Ideogram** · v3) - 文生图大模型，擅长文字渲染
- <a href="https://www.midjourney.com/" target="_blank">Midjourney</a> (**Midjourney** · 最新版) - 以艺术性著称的文生图大模型
- <a href="https://reve.art/" target="_blank">Reve</a> (**Reve** · v1) - 文生图大模型
- <a href="https://leonardo.ai/" target="_blank">Leonardo AI</a> (**Leonardo AI** · Lucid Origin) - 文生图和视频生成大模型
- <a href="https://www.recraft.ai/" target="_blank">Recraft</a> (**Recraft** · v3) - 支持矢量和 mockups 的文生图大模型
- <a href="https://www.adobe.com/products/firefly.html" target="_blank">Adobe Firefly</a> (**Adobe** · 最新版) - Adobe 开发的文生图大模型，与 Creative Cloud 集成
- <a href="https://lumalabs.ai/photon" target="_blank">Luma Photon</a> (**Luma Labs** · 最新版) - Luma Labs 开发的文生图大模型

### 图生图大模型

_这些是基础的图生图生成和编辑大模型，可通过 API 调用。许多 AI 图片编辑应用都是基于这些模型构建的。_

- <a href="https://ai.studio/banana" target="_blank">Gemini</a> (**Google** · 3.0 Pro) - Google 开发的图片编辑大模型
- <a href="https://seed.bytedance.com/en/seedream4_0" target="_blank">Seedream</a> (**ByteDance** · 4.0) - 字节跳动开发的图片编辑大模型
- <a href="https://platform.openai.com/docs/models/gpt-image-1" target="_blank">GPT Image</a> (**OpenAI** · 1) - OpenAI 开发的图片编辑大模型
- <a href="https://qwenlm.github.io/blog/qwen-image/" target="_blank">Qwen Image Edit</a> (**Alibaba** · 最新版) - 阿里巴巴开发的图片编辑大模型
- <a href="https://reve.art/" target="_blank">Reve</a> (**Reve** · v1) - 图片编辑大模型
- <a href="https://bfl.ai/announcements/flux-1-kontext" target="_blank">Flux Kontext</a> (**Black Forest Labs** · 1 Kontext) - Black Forest Labs 开发的图片编辑大模型
- <a href="https://www.adobe.com/products/firefly.html" target="_blank">Adobe Firefly</a> (**Adobe** · 5 Preview) - Adobe 开发的图片编辑大模型，与 Creative Cloud 集成
- <a href="https://www.hidream.ai/" target="_blank">HiDream</a> (**HiDream** · 最新版) - 图片编辑大模型
- <a href="https://www.stepfun.com/" target="_blank">StepFun</a> (**StepFun** · 最新版) - 图片编辑大模型

## AI 视频工具

### 文生视频大模型

_这些是基础的文生视频大模型，可通过 API 调用。许多 AI 视频应用都是基于这些模型构建的。_

- <a href="https://deepmind.google/models/veo/" target="_blank">Veo</a> (**Google** · 3.1) - Google 开发的文生视频大模型
- <a href="https://openai.com/sora/" target="_blank">Sora</a> (**OpenAI** · 2 Pro / 2) - OpenAI 开发的文生视频大模型
- <a href="https://www.klingai.com/" target="_blank">Kling</a> (**KlingAI** · 2.5 Turbo) - KlingAI 开发的文生视频大模型
- <a href="https://lumalabs.ai/ray" target="_blank">Ray</a> (**Luma AI** · 3) - Luma AI 开发的文生视频大模型
- <a href="https://hailuoai.video/" target="_blank">Hailuo</a> (**MiniMax** · 2.3) - MiniMax 开发的文生视频大模型
- <a href="https://seed.bytedance.com/en/seedance" target="_blank">Seedance</a> (**ByteDance** · 1.0 Pro) - 字节跳动开发的文生视频大模型
- <a href="https://wan.video/" target="_blank">WAN</a> (**Alibaba** · 2.5) - 阿里巴巴开发的文生视频大模型
- <a href="https://hunyuanvideoai.com/" target="_blank">Hunyuan</a> (**Tencent** · 最新版) - 腾讯开发的文生视频大模型
- <a href="https://pika.art/" target="_blank">Pika</a> (**Pika** · 2.2) - 文生视频大模型
- <a href="https://www.genmo.ai/" target="_blank">Mochi</a> (**Genmo AI** · 1) - Genmo AI 开发的文生视频大模型

### 图生视频大模型

_这些是基础的图生视频大模型，可通过 API 调用。许多 AI 视频应用都是基于这些模型构建的。_

- <a href="https://deepmind.google/models/veo/" target="_blank">Veo</a> (**Google** · 3.1) - Google 开发的图生视频大模型
- <a href="https://www.klingai.com/" target="_blank">Kling</a> (**KlingAI** · 2.5 Turbo) - KlingAI 开发的图生视频大模型
- <a href="https://pixverse.ai/" target="_blank">PixVerse</a> (**PixVerse** · V5) - 图生视频大模型
- <a href="https://cloud.baidu.com/product/wenxinworkshop" target="_blank">GenFlare</a> (**Baidu** · 最新版) - 百度开发的图生视频大模型
- <a href="https://hailuoai.video/" target="_blank">Hailuo</a> (**MiniMax** · 2.3) - MiniMax 开发的图生视频大模型
- <a href="https://seed.bytedance.com/en/seedance" target="_blank">Waver</a> (**ByteDance** · 1.0) - 字节跳动开发的图生视频大模型
- <a href="https://www.vidu.com/" target="_blank">Vidu</a> (**Vidu** · Q2 Turbo) - 图生视频大模型
- <a href="https://ltx.studio/" target="_blank">LTX Studio</a> (**Lightricks** · 2 Pro) - 图生视频大模型
- <a href="https://seed.bytedance.com/en/seedance" target="_blank">Seedance</a> (**ByteDance Seed** · 1.0) - 字节跳动 Seed 开发的图生视频大模型
- <a href="https://wan.video/" target="_blank">WAN</a> (**Alibaba** · 2.5) - 阿里巴巴开发的图生视频大模型
- <a href="https://lumalabs.ai/ray" target="_blank">Ray</a> (**Luma Labs** · 3) - Luma Labs 开发的图生视频大模型
- <a href="https://hunyuanvideoai.com/" target="_blank">Hunyuan</a> (**Tencent** · 最新版) - 腾讯开发的图生视频大模型
- <a href="https://www.animon.ai/" target="_blank">Animon</a> (**Animon** · AniCut Pro 1.6) - 图生视频大模型
- <a href="https://www.midjourney.com/" target="_blank">Midjourney</a> (**Midjourney** · V1) - 图生视频大模型
- <a href="https://www.hidream.ai/" target="_blank">Vivago</a> (**HiDream** · 2.0) - HiDream 开发的图生视频大模型
- <a href="https://runwayml.com/" target="_blank">Runway Gen</a> (**Runway** · Gen 4) - Runway 开发的图生视频大模型

## AI 音频工具

### 文字转语音 (TTS) 大模型

_这些是基础的文字转语音大模型，可通过 API 调用。许多 AI 音频应用都是基于这些模型构建的。_

- <a href="https://elevenlabs.io/" target="_blank">ElevenLabs</a> (**ElevenLabs** · 最新版) - 业界领先的 AI 语音合成平台，生成自然语音用于播客、配音等
- <a href="https://fish.audio/" target="_blank">Fish Studio</a> (**Fish Studio** · 最新版) - 文字转语音大模型
- <a href="https://www.sesame.com/" target="_blank">Sesame</a> (**Sesame** · 最新版) - 文字转语音大模型
- <a href="https://platform.openai.com/docs/guides/text-to-speech" target="_blank">OpenAI TTS</a> (**OpenAI** · 最新版) - 文字转语音大模型
- <a href="https://www.minimax.io/audio" target="_blank">MiniMax Audio</a> (**MiniMax** · 最新版) - 文字转语音大模型
- <a href="https://cartesia.ai/" target="_blank">Cartesia</a> (**Cartesia** · 最新版) - 文字转语音大模型
- <a href="https://speechify.com/" target="_blank">Speechify</a> (**Speechify** · 最新版) - 顶级文字转语音工具，支持200+自然语音，OCR读取文档，读速提升至4.5×
- <a href="https://www.resemble.ai/" target="_blank">Resemble AI</a> (**Resemble AI** · 最新版) - 专注于生成人声的人工智能公司
- <a href="https://www.hume.ai/" target="_blank">Hume</a> (**Hume** · 最新版) - 文字转语音大模型
- <a href="https://play.ht/" target="_blank">Play AI</a> (**Play AI** · 最新版) - 文字转语音大模型
- <a href="https://www.zyphra.com/" target="_blank">Zyphra</a> (**Zyphra** · 最新版) - 文字转语音大模型
- <a href="https://murf.ai/" target="_blank">Murf</a> (**Murf** · 最新版) - 文字转语音大模型
- <a href="https://azure.microsoft.com/en-us/products/ai-services/ai-speech" target="_blank">Azure Speech</a> (**Microsoft** · 最新版) - 文字转语音大模型
- <a href="https://aws.amazon.com/polly/" target="_blank">Amazon Polly</a> (**Amazon** · 最新版) - 文字转语音大模型
- <a href="https://cloud.google.com/text-to-speech" target="_blank">Google Cloud TTS</a> (**Google** · 最新版) - Google Cloud 的文字转语音服务，提供 Chirp 3: HD、WaveNet 和 Studio 等模型，支持 380+ 种语音和 75+ 种语言
- <a href="https://inworld.ai/" target="_blank">Inworld TTS</a> (**Inworld** · 最新版) - 实时多模态 AI，支持丰富的多语言功能
- <a href="https://stepfun.com/" target="_blank">StepFun TTS</a> (**StepFun** · 最新版) - 文字转语音大模型
- <a href="https://wellsaidlabs.com/" target="_blank">WellSaid Labs</a> (**WellSaid Labs** · 最新版) - AI 文本转语音技术公司，开发自然语音合成技术，提供120+真实AI语音
- <a href="https://amai.io/" target="_blank">AMAI</a> (**AMAI** · 最新版) - 语音AI解决方案，提供语音合成技术

### 语音转文字 (ASR) 大模型

_这些是基础的语音转文字（自动语音识别）大模型，可通过 API 调用。许多 AI 音频应用都是基于这些模型构建的。_

- <a href="https://aws.amazon.com/transcribe/" target="_blank">Amazon Transcribe</a> (**Amazon** · 最新版) - 自动语音识别服务，支持多种语言和音频格式，价格为每 1000 分钟 24 美元
- <a href="https://www.assemblyai.com/" target="_blank">AssemblyAI</a> (**AssemblyAI** · Universal 2) - 高精度语音转文字 API，支持长音频文件、关键词检测和情感分析
- <a href="https://azure.microsoft.com/en-us/products/ai-services/ai-speech" target="_blank">Azure Speech-to-Text</a> (**Microsoft** · 最新版) - 语音识别服务，支持自定义模型和多语言转录
- <a href="https://deepgram.com/" target="_blank">Deepgram Nova</a> (**Deepgram** · Nova-2) - 先进的语音识别模型，每秒转录 142 秒音频，提供高精度和低延迟
- <a href="https://deepinfra.com/" target="_blank">DeepInfra Whisper</a> (**DeepInfra** · Large v3) - 高性能转录服务，每秒可转录 149 秒音频
- <a href="https://elevenlabs.io/blog/meet-scribe" target="_blank">ElevenLabs Scribe</a> (**ElevenLabs** · V1) - 世界最准确的语音转文字模型，支持 99 种语言的语音转录，提供词级时间戳、说话人分离和音频事件标记
- <a href="https://fal.ai/" target="_blank">Fal.ai Wizper</a> (**Fal.ai** · Large v3) - 高性能转录服务，每秒可转录 218 秒音频
- <a href="https://fireworks.ai/" target="_blank">Fireworks Whisper</a> (**Fireworks** · Large v3 Turbo) - 超快速基于 Whisper 的转录服务，每秒可转录 353 秒音频
- <a href="https://cloud.google.com/speech-to-text" target="_blank">Google Cloud Speech-to-Text</a> (**Google** · Chirp 2) - 高精度语音识别服务，支持实时和批量处理
- <a href="https://groq.com/" target="_blank">Groq Distil Whisper</a> (**Groq** · 最新版) - 快速转录服务，每秒转录 204 秒音频，价格为每 1000 分钟 0.33 美元
- <a href="https://platform.openai.com/docs/guides/speech-to-text" target="_blank">OpenAI Whisper</a> (**OpenAI** · 最新版) - 开源语音识别模型，彻底改变了 AI 转录领域，使云推理服务商能够在速度和价格上展开竞争
- <a href="https://www.rev.ai/" target="_blank">Rev AI</a> (**Rev** · 最新版) - 高精度语音转文字服务，支持实时和批量转录
- <a href="https://www.speechmatics.com/" target="_blank">Speechmatics</a> (**Speechmatics** · Enhanced) - 全球语言覆盖的语音识别服务，支持多种口音和方言

### 音乐生成大模型

_这些是基础的音乐生成大模型，可通过 API 调用。许多 AI 音乐应用都是基于这些模型构建的。_

- <a href="https://suno.ai/" target="_blank">Suno</a> (**Suno** · V4.5) - AI 音乐生成器，从文本提示创建高质量歌曲，支持人声和多种流派
- <a href="https://elevenlabs.io/music" target="_blank">Eleven Music</a> (**ElevenLabs** · 最新版) - 录音室级 AI 音乐生成器，可即时创建任何流派或风格的音乐，支持有/无人声
- <a href="https://udio.com/" target="_blank">Udio</a> (**Udio** · v1.5 Allegro) - AI 音乐生成器，为任何时刻创建个性化音乐，支持扩展、混音和音轨提取
- <a href="https://stability.ai/stable-audio" target="_blank">Stable Audio</a> (**Stability AI** · 2.0) - 文本转音频生成模型，用于创建音乐和音效
- <a href="https://ai.google.dev/gemini/docs/audio" target="_blank">Lyria</a> (**Google** · 2) - Google 的音乐生成模型，与 YouTube 集成
- <a href="https://github.com/facebookresearch/audiocraft" target="_blank">MusicGen</a> (**Meta** · 最新版) - Meta 的开源音乐生成模型

### 播客托管平台

_这些平台为播客创作者提供完整的播客托管、分发、分析和变现服务。_

- <a href="https://fireside.fm/" target="_blank">Fireside</a> (**Fireside**) - 完整的播客托管平台，提供响应式网站、定时发布、嵌入播放器与分析；支持自定义域名和从其他平台一键导入
- <a href="https://www.podbean.com/" target="_blank">Podbean</a> (**Podbean**) - 一体化播客平台，支持录制、发布、分发与变现；包括音频/视频托管和直播功能
- <a href="https://rss.com/" target="_blank">RSS.com</a> (**RSS.com**) - 播客托管服务，提供无限存储、跨平台分析与动态广告；支持快速托管与推广
- <a href="https://www.simplecast.com/" target="_blank">Simplecast</a> (**Simplecast**) - 企业级播客托管与分发平台，具备深度统计、自定义网站和广告投放控制功能
- <a href="https://libsyn.com/" target="_blank">Libsyn</a> (**Libsyn**) - 最早期的播客托管服务之一，支持音/视频上传、定时发布、分析、分发和货币化工具

## AI 编程工具

### AI 编程代理与 IDE

_这些是基础的 AI 编程代理和 IDE，提供端到端的代码生成和开发辅助功能。_

- <a href="https://www.cursor.com/" target="_blank">Cursor</a> (**Cursor**) - AI 驱动的 IDE，支持自然语言提示进行端到端代码生成与查询
- <a href="https://devin.ai/" target="_blank">Devin</a> (**Devin**) - AI 软件工程师，负责代码自动生成、调试与部署流程
- <a href="https://replit.com/" target="_blank">Replit</a> (**Replit**) - 云端 IDE 平台，AI Agent 根据自然语言生成并部署完整应用
- <a href="https://www.trae.ai/" target="_blank">Trae</a> (**字节跳动**) - ByteDance 出品的免费 AI IDE，通过 Builder 模式智能拆解任务并补全代码
- <a href="https://stackblitz.com/" target="_blank">StackBlitz</a> (**StackBlitz**) - 基于浏览器的一体化全栈 IDE，用 WebAssembly 启动 Node.js，适合即时构建和协作开发
- <a href="https://www.reflection.ai/" target="_blank">Reflection AI</a> (**Reflection AI**) - 打造具自主决策能力的"超智能"编程 AI，可模拟人类开发过程
- <a href="https://www.wordware.ai/" target="_blank">Wordware</a> (**Wordware**) - 基于浏览器的 AI 工具开发 IDE，支持自然语言编程、LLM 编排与多模态 agent 构建

### 代码补全工具

_这些是 AI 驱动的代码补全工具，提供智能建议和自动补全功能。_

- <a href="https://github.com/features/copilot" target="_blank">GitHub Copilot</a> (**GitHub**) - AI 对话式编程副驾，即时补全代码、修复 bug 与提交 PR
- <a href="https://windsurf.com/" target="_blank">Codeium (Windsurf)</a> (**Codeium**) - AI 编程助手，提供高质量代码补全
- <a href="https://supermaven.com/" target="_blank">Supermaven</a> (**Supermaven**) - 百万 token 上下文的极速 AI 编程助手，提供高质量代码补全
- <a href="https://www.blackbox.ai/" target="_blank">BlackBox AI</a> (**BlackBox AI**) - AI 编程助手，实时提供智能补全、文档和调试建议，提高工程效率
- <a href="https://www.augmentcode.com/" target="_blank">Augment Code</a> (**Augment**) - AI 编码代理平台，在 IDE 中通过本地 + 云智能自动提升代码质量
- <a href="https://openai.com/codex/" target="_blank">OpenAI Codex</a> (**OpenAI**) - AI 系统，将自然语言转换为代码，为编程助手提供支持

### 低代码/无代码平台

_这些平台通过 AI 驱动的自然语言界面，以最少或无需编码的方式构建应用程序。_

- <a href="https://www.fine.dev/" target="_blank">Fine</a> (**Fine**) - AI 驱动的全栈开发平台，一键生成、部署并管理 SaaS 应用
- <a href="https://magic.dev/" target="_blank">Magic</a> (**Magic**) - Low‑Code 全栈生成平台，一句英文描述即可自动生成并部署 SaaS 应用
- <a href="https://bolt.new/" target="_blank">Bolt</a> (**Bolt**) - 浏览器内 AI Agent，可对话生成并部署全栈 Web 应用
- <a href="https://retool.com/" target="_blank">Retool</a> (**Retool**) - 低代码内部应用构建器，通过自然语言生成界面与业务逻辑
- <a href="https://lovable.dev/" target="_blank">Lovable</a> (**Lovable**) - 通过聊天输入，AI 自动生成全栈应用与网站原型
- <a href="https://www.trickle.so/" target="_blank">Trickle</a> (**Trickle**) - 无代码工具，构建 AI 代理、网站与表单，支持截图搜索
- <a href="https://v0.dev/" target="_blank">V0 by Vercel</a> (**Vercel**) - 对话式 IDE，一键生成 React/Svelte 等项目前端并部署
- <a href="https://readdy.ai/" target="_blank">Readdy</a> (**Readdy**) - AI 驱动设计平台，一键打造生产级 UI 并输出代码
- <a href="https://glif.app/" target="_blank">Glif</a> (**Glif**) - 轻量生成器平台，制作 AI 小应用、图像/视频生成与漫画等
- <a href="https://www.narrative.bi/" target="_blank">Narrative BI</a> (**Narrative BI**) - 无代码生成式 BI 平台，将数据自动转化为自然语言洞察与异常警示
- <a href="https://poolside.ai/" target="_blank">Poolside</a> (**Poolside**) - 专为软件工程设计的 AI 编码平台，利用自研模型自动补全与生成代码

### 代码质量与安全工具

_这些工具通过 AI 驱动的分析帮助提高代码质量、安全性和文档化。_

- <a href="https://moderne.io/" target="_blank">Moderne</a> (**Moderne**) - 专注于自动识别和修补代码中的安全漏洞
- <a href="https://stenography.dev/" target="_blank">Stenography</a> (**Stenography**) - 利用人工智能技术为代码生成自动文档
- <a href="http://codiga.io/" target="_blank">Codiga</a> (**Codiga** · 最新版) - 创新的代码分析平台

## AI 搜索工具

### 搜索增强型 LLM

_这些是集成网络搜索功能的大语言模型，提供实时信息检索、外部知识和引用来源。_

- <a href="https://x.ai/news/grok-4-fast" target="_blank">Grok-4-Fast-Search</a> (**xAI** · 最新版) - 搜索增强型 LLM，提供快速准确的搜索结果
- <a href="https://docs.perplexity.ai/getting-started/overview" target="_blank">Perplexity Sonar Pro High</a> (**Perplexity** · 最新版) - 搜索增强型 LLM，结合搜索引擎与 LLM 实现实时网络检索
- <a href="https://ai.google.dev/gemini-api/docs/google-search" target="_blank">Gemini 2.5 Pro Grounding</a> (**Google** · 最新版) - 搜索增强型 LLM，提供带引用来源的实时信息
- <a href="https://platform.openai.com/docs/guides/tools-web-search?api-mode=responses" target="_blank">O3-Search</a> (**OpenAI** · 最新版) - 搜索增强型 LLM，提供实时信息检索和外部知识
- <a href="https://docs.x.ai/docs/guides/live-search" target="_blank">Grok-4-Search</a> (**xAI** · 最新版) - 搜索增强型 LLM，提供快速搜索功能
- <a href="https://platform.openai.com/docs/guides/tools-web-search?api-mode=responses" target="_blank">GPT-5-Search</a> (**OpenAI** · 最新版) - 搜索增强型 LLM，提供实时信息检索
- <a href="https://www.anthropic.com/news/claude-opus-4-1" target="_blank">Claude Opus 4.1 Search</a> (**Anthropic** · 最新版) - 搜索增强型 LLM，提供带外部知识的实时信息
- <a href="https://www.anthropic.com/news/claude-opus-4-1" target="_blank">Claude Opus 4 Search</a> (**Anthropic** · 最新版) - 搜索增强型 LLM，提供高质量搜索结果
- <a href="https://docs.perplexity.ai/getting-started/overview" target="_blank">Perplexity Sonar Reasoning Pro High</a> (**Perplexity** · 最新版) - 搜索增强型 LLM，结合推理与搜索功能
- <a href="https://github.com/diffbot/diffbot-llm-inference" target="_blank">Diffbot Small XL</a> (**Diffbot** · 最新版) - 搜索增强型 LLM，开源 Apache 2.0 许可模型
- <a href="https://platform.openai.com/docs/models/gpt-4o-search-preview" target="_blank">GPT-4o-Search</a> (**OpenAI** · 最新版) - 搜索增强型 LLM，通过 API 提供搜索功能

### AI 搜索 API 与基础设施

_这些是基础的 AI 搜索 API 和基础设施，可通过 API 调用。许多 AI 搜索应用都是基于这些模型构建的。_

- <a href="https://exa.ai/" target="_blank">Exa.ai</a> (**Exa** · 最新版) - 实时 AI 搜索引擎，提供网页爬虫 API、SERP API 和深度研究工具，搜索并提取网站和实时数据的结构化内容
- <a href="https://you.com/" target="_blank">You.com</a> (**You.com** · 最新版) - 面向 LLM 和企业 AI 解决方案的网络搜索 API（之前做 toC AI 搜索，已经转型）
- <a href="https://tavily.com/" target="_blank">Tavily</a> (**Tavily** · 最新版) - 面向 AI 代理和 RAG 工作流的实时搜索引擎，提供快速安全的网络搜索和内容提取 API
- <a href="https://serpapi.com/" target="_blank">SerpApi</a> (**SerpApi** · 最新版) - 实时抓取 Google/Bing 等搜索引擎结果并结构化返回 API 响应
- <a href="https://bochaai.com/" target="_blank">博查</a> (**博查** · 最新版) - 面向 AI 应用的多模态搜索引擎，为智能体提供高质量知识检索 API
- <a href="https://jina.ai/" target="_blank">Jina AI</a> (**Jina AI** · 最新版) - 构建多模态/文本企业级神经检索与 RAG 系统的 API 平台
- <a href="https://www.algolia.com/" target="_blank">Algolia</a> (**Algolia** · 最新版) - 为企业和开发者提供即时、可定制和高性能的站内搜索与内容发现 API 服务
- <a href="https://deepset.ai/" target="_blank">Deepset</a> (**Deepset** · 最新版) - 自然语言处理框架 Haystack，支持语义搜索、问答与 RAG 应用
- <a href="http://www.zeta-alpha.com/" target="_blank">Zeta Alpha</a> (**Zeta Alpha** · 最新版) - 神经搜索平台，优化知识发现与共享
- <a href="https://www.ai21.com/" target="_blank">AI21 Labs</a> (**AI21 Labs** · 最新版) - 以强大 RAG 能力著称的智能 NLP 平台，推动生成式 AI 商业化

### 网页抓取工具

_这些是网页抓取 API 和工具，用于从网站提取数据，为 AI 应用和代理提供干净、结构化的内容。_

- <a href="https://www.browse.ai/" target="_blank">Browse.ai</a> (**Browse.ai** · 最新版) - 无代码 AI 网页抓取与监控平台，点击即可设置机器人采集网页数据
- <a href="https://www.firecrawl.dev/" target="_blank">Firecrawl</a> (**Firecrawl** · 最新版) - 网页抓取 API，将网站转换为 LLM 就绪数据（Markdown、JSON、截图），开源并针对 AI 代理优化
- <a href="https://www.scrapingbee.com/" target="_blank">ScrapingBee</a> (**ScrapingBee** · 最新版) - 简便的网页内容抓取 REST API，绕过反爬虫限制快速获取网页数据
- <a href="https://www.scraperapi.com/" target="_blank">ScraperAPI</a> (**ScraperAPI** · 最新版) - 托管的爬虫 API，自动处理代理、CAPTCHA 与 IP 封锁问题

### AI 搜索引擎

_这些是 AI 驱动的搜索引擎，提供对话式搜索体验，支持实时网络检索和引用来源的答案。_

- <a href="https://ambersearch.de/" target="_blank">AmberSearch</a> (**AmberSearch** · 最新版) - 企业智能搜索引擎，支持多媒体内容搜索
- <a href="https://andisearch.com/" target="_blank">Andi</a> (**Andi** · 最新版) - 自然语言交互搜索引擎，提供推荐和知识发现
- <a href="https://www.perplexity.ai/" target="_blank">Perplexity</a> (**Perplexity** · 最新版) - 一个结合搜索引擎与 LLM 的 AI 回答平台，能实时检索网络并给出引用来源的详实答案
- <a href="https://yep.com/" target="_blank">Yep</a> (**Yep** · 最新版) - 私隐搜索引擎，广告收入 90％返还创作者
- <a href="https://www.phind.com/" target="_blank">Phind</a> (**Phind** · 最新版) - 为开发者打造的 AI 搜索引擎，提供可视化、交互式且引用清晰的代码与技术答案
- <a href="https://iask.ai/" target="_blank">iAsk</a> (**iAsk** · 最新版) - 免费 AI 问答搜索，支持自然语言即时回答
- <a href="https://consensus.app/" target="_blank">Consensus</a> (**Consensus** · 最新版) - 一个专注于学术研究的 AI 搜索引擎，从数百万篇论文中提炼并汇总科学结论
- <a href="https://komo.ai/" target="_blank">Komo</a> (**Komo** · 最新版) - 一个免广告的生成式 AI 搜索平台，支持深度对话式探讨和社区驱动探索功能
- <a href="https://brave.com/search/" target="_blank">Brave Search</a> (**Brave** · 最新版) - 一个独立、注重隐私的搜索引擎，拥有自己的网页索引，不追踪用户行为
- <a href="https://adot.ai/" target="_blank">Adot</a> (**Adot** · 最新版) - Web3 智能搜索 Chrome 扩展，提供多模型 AI 摘要

### 电商搜索助手

_这些是专门为电商和购物体验设计的 AI 搜索助手。_

- <a href="https://www.amazon.com/Rufus/b?ie=UTF8&node=121214013011" target="_blank">Amazon Rufus</a> (**Amazon** · 最新版) - 亚马逊内置的 AI 购物助手，通过对话推荐产品、比较选项，驱动流量提升零售销售
- <a href="https://www.accio.com/" target="_blank">Accio</a> (**Alibaba** · 最新版) - Alibaba 驱动的 B2B AI 采购引擎，智能匹配供应商与市场洞察
- <a href="https://www.shopencore.ai/" target="_blank">Encore</a> (**Encore** · 最新版) - AI 二手商品搜索助手，聚合多平台提供对话式精准淘货体验
- <a href="https://faircado.com/" target="_blank">Faircado</a> (**Faircado** · 最新版) - AI 驱动的浏览器插件/应用，汇聚百万级二手商品平台，帮你智能搜索比价，省钱又环保
- <a href="https://onton.com/" target="_blank">Onton</a> (**Onton** · 最新版) - 无广告、无垃圾信息的 AI 购物搜索引擎

### AI 浏览器

_这些是集成 AI 助手的浏览器，通过智能功能增强浏览体验。_

- <a href="https://arc.net/" target="_blank">Arc</a> (**Arc** · 最新版) - 重新构想浏览器界面，以侧边栏与可定制空间提升效率
- <a href="https://www.diabrowser.com/" target="_blank">Dia</a> (**Dia** · 最新版) - AI 浏览器，可与标签对话、实时生成助手
- <a href="https://strawberrybrowser.com/" target="_blank">Strawberry</a> (**Strawberry** · 最新版) - 内置 AI 助手，自动化研究、撰写与日常任务
- <a href="https://www.perplexity.ai/comet" target="_blank">Comet by Perplexity</a> (**Perplexity** · 最新版) - 集成 Perplexity 搜索侧边栏并能自动组织标签、屏蔽广告等

## AI 聚合平台

### 面向开发者

_这些平台提供统一的 API 访问多个 AI 模型，方便开发者集成各种 AI 功能。_

- <a href="https://openrouter.ai/" target="_blank">OpenRouter</a> (**OpenRouter** · 最新版) - 统一 LLM 接入平台，一键调用多个开源或商业大模型 API，目前业内排行第一
- <a href="https://fal.ai/" target="_blank">Fal</a> (**Fal** · 最新版) - 统一 API 接入平台，一键调用多个开源或商业生图大模型 API，极速扩散模型推理与训练 API，提升生成效率最高达 4×
- <a href="https://replicate.com/" target="_blank">Replicate</a> (**Replicate** · 最新版) - 一行代码运行或微调开源模型，托管自定义 AI 推理服务
- <a href="https://huggingface.co/" target="_blank">Hugging Face</a> (**Hugging Face** · 最新版) - 一站式 AI 模型平台与 API，提供 Transformers 库、Hub 与推理服务
- <a href="https://www.eachlabs.ai/" target="_blank">EachLabs</a> (**EachLabs** · 最新版) - 提供 150+ AI 模型与可视化工作流，一键构建安全、可扩展的 AI 后端
- <a href="https://requesty.ai/" target="_blank">Requesty</a> (**Requesty** · 最新版) - AI 模型市场与 API 聚合平台
- <a href="https://www.edenai.co/" target="_blank">Eden AI</a> (**Eden AI** · 最新版) - AI 模型市场与统一 API 平台
- <a href="https://fireworks.ai/" target="_blank">Fireworks</a> (**Fireworks** · 最新版) - 高性能生成式 AI 推理引擎 API，支持函数调用与多模式集成
- <a href="https://groq.com/" target="_blank">Groq API</a> (**Groq** · 最新版) - 专为 AI 推理打造的高性能 LPU 芯片与云端/本地计算平台，实现极速、低成本的 AI 模型部署
- <a href="https://www.together.ai/" target="_blank">Together AI</a> (**Together AI** · 最新版) - AI 加速云平台，一键部署/微调上百种开源模型
- <a href="https://novita.ai/" target="_blank">Novita AI</a> (**Novita AI** · 最新版) - 一站式 AI 云，简单 API 访问 200+ 模型并弹性 GPU 扩展
- <a href="https://lmstudio.ai/" target="_blank">LM Studio</a> (**LM Studio** · 最新版) - 本地运行开源 LLM 的桌面工具，支持聊天与本地微服务部署
- <a href="https://deepinfra.com/" target="_blank">Deep Infra</a> (**Deep Infra** · 最新版) - 多模型推理 API，涵盖文本、图像、语音、分类等丰富功能
- <a href="https://apilayer.com/" target="_blank">APILayer</a> (**APILayer** · 最新版) - 高质量微型 API 市场，低延迟集成各种开发者需求
- <a href="https://rapidapi.com/" target="_blank">Rapid API</a> (**Rapid API** · 最新版) - 全球最大 API 市场，集 API 查找、集 API 查找、测试、盈利与管理于一体
- <a href="https://apidog.com/" target="_blank">Apidog</a> (**Apidog** · 最新版) - 端到端 API 设计开发平台，支持设计、调试与文档同步
- <a href="https://octo.ai/" target="_blank">OctoAI</a> (**OctoAI** · 最新版) - 开发者用的一站式生成式 AI 基础设施，支持模型部署、微调与无缝扩展
- <a href="https://www.anyscale.com/" target="_blank">Anyscale</a> (**Anyscale** · 最新版) - AI 应用平台，基于 Ray，可即时构建、运行并扩展大规模 AI 工作负载
- <a href="https://mainfunc.ai/" target="_blank">MainFunc</a> (**MainFunc** · 最新版) - AI 驱动产品创新平台，由 Tech 大厂出身团队打造，用生成式 AI 构建应用

### 面向企业

_这些平台提供企业级 AI 基础设施和多模型 API 访问，适用于大规模部署。_

- <a href="https://aws.amazon.com/bedrock/" target="_blank">Amazon Bedrock</a> (**Amazon** · 最新版) - 单一 API 调用多家基础模型，实现文本、图像等多模态推理
- <a href="https://ai.azure.com/" target="_blank">Azure AI Foundry</a> (**Microsoft** · 最新版) - 企业 AI 平台，提供统一访问多个 AI 模型和服务
- <a href="https://cloud.google.com/vertex-ai" target="_blank">Google Vertex AI</a> (**Google** · 最新版) - Google Cloud 上的企业 AI 平台，提供访问多个 AI 模型和服务
- <a href="https://build.nvidia.com/" target="_blank">NVIDIA NIM</a> (**NVIDIA** · 最新版) - 微服务化 GPU 加速推理平台，自托管或云端部署最新 AI 模型
- <a href="https://developers.cloudflare.com/workers-ai/" target="_blank">Cloudflare Workers AI</a> (**Cloudflare** · 最新版) - Cloudflare 无服务器边缘 GPU 推理，集成向量存储与 API 调用

### 面向普通用户

_这些平台通过用户友好的界面提供对多个 AI 模型的便捷访问。_

- <a href="https://poe.com/" target="_blank">Poe</a> (**Poe** · 最新版) - 通过统一界面访问多个 AI 模型的平台
- <a href="https://monica.im/" target="_blank">Monica</a> (**Monica** · 最新版) - 集成多种 AI 模型的全能助手，支持 GPT-5.1、Claude 4.5、Gemini 3 Pro 等，提供聊天、搜索、写作、图像生成、视频生成和编码功能

## AI Agent 基础设施

_这些平台和服务、框架和基础设施专门用于构建、部署和管理 AI 代理。_

### Agent 数据基础设施

_这些平台为 AI 代理提供数据存储、记忆和 ETL 服务。_

#### Memory

_这些平台为 AI 代理提供长期记忆和认知架构，使其能够记住过去的交互、保持一致性，并随着时间的推移建立用户理解。_

- <a href="https://mem0.ai/" target="_blank">Mem0</a> (**Mem0**) - AI 代理的通用记忆层，支持自动抽取、清洗和存储；混合向量+知识图谱架构；自改进记忆压缩引擎；LoCoMo 得分约 60-70%
- <a href="https://www.getzep.com/" target="_blank">Zep</a> (**Zep**) - 企业级 Memory Server，使用时序知识图谱架构，支持 Docker 部署，企业级稳定性；系统化地从聊天历史和业务数据中构建相关上下文；LoCoMo 得分约 85%
- <a href="https://github.com/MemTensor/MemOS" target="_blank">MemOS</a> (**MemOS**) - 记忆操作系统，采用神经张量记忆架构（MemCube）；三层系统架构（接口层、操作层、基础设施层）；代表神经记忆研究的前沿探索
- <a href="https://github.com/NevaMind-AI/memU" target="_blank">MemU</a> (**MemU**) - 结构化记忆系统，采用层级化记忆树架构（根、枝、叶节点）；自动分类和动态扩展；在用户画像、档案管理和结构化任务方面表现优异
- <a href="https://github.com/EverMind-AI/EverMemOS" target="_blank">EverMemOS</a> (**EverMind**) - 第二代 Memory OS，采用仿生四层记忆架构（分类提取、MemCell 原子化存储、事件边界、多跳召回）；LoCoMo SOTA 92.3%，首个超越 Full-context 基准的记忆系统
- <a href="https://mirix.io/" target="_blank">Mirix</a> (**Mirix**) - 屏幕级多模态记忆系统，捕获屏幕 → 行为 → 事件；实时监控屏幕，构建个性化记忆库，LoCoMO 准确率 85.38%，存储减少 99.9%
- <a href="https://www.memobase.io/" target="_blank">Memobase</a> (**Memobase**) - 基于 Profile 的长期记忆系统，适用于 AI 应用；处理用户画像、记忆事件和不断演化的上下文；非常适合聊天机器人、伴侣和以用户为中心的 AI 应用
- <a href="https://github.com/letta-ai/letta" target="_blank">Letta</a> (**Letta**) - 文件系统式记忆架构，用于构建有状态的代理；为 LLM 添加状态以实现高级推理能力和透明的长期记忆；Agent File (.af) 格式用于序列化有状态的 AI 代理
- <a href="https://memories.ai/" target="_blank">Memories.ai</a> (**Memories.ai**) - 视频级记忆 / LVMM（大型视觉记忆模型），用于长视频理解；构建可搜索、连接和推理的持久视觉记忆
- <a href="https://supermemory.ai/" target="_blank">Supermemory</a> (**Supermemory**) - 基于知识图谱的超记忆系统，具备高级图谱推理能力；构建适应每个用户知识的持久学习图谱；在 LongMemEval 上达到最先进的性能
- <a href="https://github.com/langchain-ai/langmem" target="_blank">LangMem</a> (**LangChain**) - LangChain 官方 Memory SDK，用于构建具备记忆能力的 LLM 应用；轻量级 Python 库，帮助代理通过长期记忆学习和改进
- <a href="https://www.cognee.ai/" target="_blank">Cognee</a> (**Cognee**) - 开源 AI 记忆引擎，将原始数据转换为代理的持久和动态 AI 记忆；结合向量搜索和知识图谱；ECL（提取、认知化、链接）框架
- **Zap** - 代理记忆平台

## 认证与身份服务

_这些平台为 AI 应用提供认证、授权和用户管理服务。_

- <a href="https://clerk.com/" target="_blank">Clerk</a> (**Clerk**) - 提供可嵌入的用户认证界面、API 和管理后台，简化身份验证与账户管理
- <a href="https://www.authing.com/" target="_blank">Authing</a> (**Authing**) - 企业级身份云（IDaaS），通过 SDK/API 实现统一登录、授权及多租户管理

## AI Agent 支付基础设施

_这些平台为 AI 代理和自主交易提供支付基础设施和服务。_

- <a href="https://www.paid.ai/" target="_blank">Paid</a> (**Paid**) - AI 驱动的多网关支付编排平台，智能路由提升支付成功率
- <a href="https://paymanai.com/" target="_blank">Payman AI</a> (**Payman AI**) - 为 AI 代理提供安全支付基础设施，让 AI 可托管交易但需人工审核
- <a href="https://skyfire.xyz/" target="_blank">Skyfire</a> (**Skyfire**) - AI 经济的财务基础设施，支持 AI 代理自主付款及身份验证
- <a href="https://nekuda.ai/" target="_blank">Nekuda</a> (**Nekuda**) - 为 AI 代理构建安全合规支付网关，实现自动代付与凭证管理

## AI 演示文稿工具

_这些平台使用 AI 自动从文本提示或大纲生成专业演示文稿和幻灯片。_

- <a href="https://gamma.app/" target="_blank">Gamma</a> (**Gamma**) - AI 驱动的演示文稿生成器，一键输入主题即刻生成精美演示文稿
- <a href="https://tome.app/" target="_blank">Tome</a> (**Tome**) - AI 驱动叙事演示工具，支持视频、互动与网页内容
- <a href="https://www.beautiful.ai/" target="_blank">Beautiful.ai</a> (**Beautiful.ai**) - 智能设计演示平台，自动保持排版与品牌一致
- <a href="https://slidesgo.com/" target="_blank">Slidesgo</a> (**Slidesgo**) - 提供数万套免费 Google/PowerPoint 模板供下载使用
- <a href="https://www.presentations.ai/" target="_blank">Presentations.AI</a> (**Presentations.AI**) - AI 助手快速生成图表、时间线、报告与演示幻灯片
- <a href="https://slidesgpt.com/" target="_blank">SlidesGPT AI</a> (**SlidesGPT AI**) - 基于文本提示的 AI 幻灯片生成器，输出带备注与主题风格
- <a href="https://www.prezent.ai/" target="_blank">Prezent</a> (**Prezent**) - 面向生命科学和技术企业的全功能 AI 演示文稿平台，针对行业、公司和受众定制，提供 AI 代理、软件和专家服务

## AI 3D 模型生成

### 文本到 3D 模型

_这些是基础的 AI 3D 模型生成工具，可以从文本提示生成 3D 模型。许多 3D 应用都是基于这些模型构建的。_

- <a href="https://lumalabs.ai/genie" target="_blank">Luma Genie</a> (**Luma Labs** · 最新版) - 从文本提示创建详细的 3D 网格，适用于快速概念设计，提供基本的 PBR 纹理和可导出格式
- <a href="https://csm.ai/" target="_blank">CSM AI</a> (**CSM** · 最新版) - AI 驱动的 3D 模型生成工具，能够根据文本描述自动生成高质量的 3D 模型
- <a href="https://spline.design/" target="_blank">Spline AI</a> (**Spline** · 最新版) - 从文本提示生成 3D 对象，专注于交互式 3D 场景创建，适用于网页和应用设计
- <a href="https://www.meshy.ai/" target="_blank">Meshy</a> (**Meshy** · 最新版) - AI 驱动的 3D 模型生成，支持文本到 3D、图像到 3D 以及自动 PBR 纹理生成
- <a href="https://www.tripo3d.ai/" target="_blank">Tripo</a> (**Tripo** · 最新版) - 从文本提示和图像生成多样化的 3D 模型，适合快速原型设计和概念开发
- <a href="https://hyper3d.ai/" target="_blank">Rodin</a> (**Hyper3D** · 最新版) - 从文本提示和图像生成高质量 3D 模型，支持多种导出格式
- <a href="https://hunyuan.tencent.com/3d" target="_blank">混元 3D</a> (**腾讯** · 最新版) - 从文本和图像生成具有干净几何结构的逼真 3D 模型，特别擅长生成人物角色和光滑表面的物体
- <a href="https://www.alpha3d.io/" target="_blank">Alpha3D</a> (**Alpha3D** · 最新版) - 将文本或 2D 图像一键转成游戏级 3D 资产，含 Unity 开发支持
- <a href="https://deepimagination.cc/Magic3D/" target="_blank">Magic3D</a> (**NVIDIA Research** · 最新版) - 高分辨率文本到 3D 内容生成模型，用于图形和视觉技术研究

### 图像到 3D 模型

_这些是基础的 AI 3D 模型生成工具，可以从 2D 图像生成 3D 模型。许多 3D 应用都是基于这些模型构建的。_

- <a href="https://www.kaedim3d.com/" target="_blank">Kaedim</a> (**Kaedim** · 最新版) - 在几分钟内将 2D 图像或草图转换为 3D 模型，支持多种输出风格，与 Unity、Unreal Engine 和 Blender 无缝集成
- <a href="https://www.meshy.ai/" target="_blank">Meshy</a> (**Meshy** · 最新版) - AI 驱动的 3D 模型生成，支持文本到 3D、图像到 3D 以及自动 PBR 纹理生成
- <a href="https://www.tripo3d.ai/" target="_blank">Tripo</a> (**Tripo** · 最新版) - 从文本提示和图像生成多样化的 3D 模型，适合快速原型设计和概念开发
- <a href="https://hyper3d.ai/" target="_blank">Rodin</a> (**Hyper3D** · 最新版) - 从文本提示和图像生成高质量 3D 模型，支持多种导出格式
- <a href="https://hunyuan.tencent.com/3d" target="_blank">混元 3D</a> (**腾讯** · 最新版) - 从文本和图像生成具有干净几何结构的逼真 3D 模型，特别擅长生成人物角色和光滑表面的物体

### 3D 电商平台

_这些平台专注于为电商应用创建和管理 3D 内容，帮助企业以 3D 形式展示产品。_

- <a href="https://www.hexa3d.io/" target="_blank">Hexa</a> (**Hexa** · 最新版) - 3D 电商平台，提供完整的 3D 技术栈，用于创建、管理、分析和分发 3D 资产，提升在线购物体验

### 无代码 3D 创作工具

_这些是无代码平台，使用户能够创建、编辑和协作 3D 内容，无需编程知识。_

- <a href="https://www.eufymake.com/" target="_blank">Eufymake</a> (**Eufymake** · 最新版) - 无代码 AI 3D 创作工具，快速生成、编辑并协作高质量场景
- <a href="https://www.intangible.ai/" target="_blank">Intangible.ai</a> (**Intangible.ai** · 最新版) - 无代码 AI 3D 创作平台，快速生成、编辑并协作高质量场景

### 3D CAD 与制造工具

_这些工具专注于将 3D 扫描转换为 CAD 模型，并集成 3D 打印和制造工作流程。_

- <a href="https://www.backflip.ai/" target="_blank">Backflip</a> (**Backflip** · 最新版) - AI 一键将 3D 扫描转为 CAD 模型
- <a href="https://ai-build.com/" target="_blank">AI Build</a> (**AI Build** · 最新版) - 融合 3D 打印与 CNC 的制造平台

### 概念艺术与创意工具

_这些工具专为概念艺术家和从事 3D 内容创作的创意专业人士设计。_

- <a href="https://mirageml.com/" target="_blank">Mirage</a> (**Mirage** · 最新版) - 为概念艺术家提供创作工具，支持 3D 内容生成

## AI 聊天机器人

### 角色聊天机器人

_这些是允许用户创建和与自定义 AI 角色进行对话、角色扮演和陪伴的 AI 聊天机器人平台。_

- <a href="https://character.ai/" target="_blank">Character.ai</a> (**Character.ai** · 最新版) - 可自定义角色聊天平台，提供深度、持续记忆的对话体验
- <a href="https://www.joyland.ai/" target="_blank">Joyland.AI</a> (**Joyland.AI** · 最新版) - 生成动漫风格 AI 角色，打造沉浸式角色陪伴与演绎体验
- <a href="https://yodayo.com/" target="_blank">Yodayo</a> (**Yodayo** · 最新版) - 面向动漫爱好者的 AI 聊天与图生图平台，支持角色创造体验
- <a href="https://www.polybuzz.ai/" target="_blank">PolyBuzz</a> (**PolyBuzz** · 最新版) - 拥有数百万虚拟角色的 AI 聊天与角色扮演平台，支持文本与语音互动
- <a href="https://www.chub.ai/" target="_blank">Chub AI</a> (**Chub AI** · 最新版) - 交互式角色扮演 AI 聊天平台，可创建自定义角色体验故事
- <a href="https://replika.ai/" target="_blank">Replika</a> (**Replika** · 最新版) - AI 伴侣聊天机器人，支持用户定制性格、声音和对话模式

### NSFW 聊天机器人

_这些是支持 NSFW 内容和成人内容的虚拟陪伴 AI 聊天机器人平台。_

- <a href="https://crushon.ai/" target="_blank">CrushOn.AI</a> (**CrushOn.AI** · 最新版) - NSFW 虚拟 AI 伴侣聊天，支持可定制角色与深层记忆
- <a href="https://candy.ai/" target="_blank">Candy AI</a> (**Candy AI** · 最新版) - 高质量 AI 虚拟伴侣聊天，模拟真实情感场景
- <a href="https://spicychat.ai/" target="_blank">Spicychat</a> (**Spicychat** · 最新版) - NSFW 角色扮演 AI 聊天平台，拥有丰富用户创作角色库

### 专业聊天机器人

_这些是为特定用途或受众设计的 AI 聊天机器人。_

- <a href="https://www.autoresponder.ai/" target="_blank">AutoResponder.ai</a> (**AutoResponder.ai** · 最新版) - 支持 WhatsApp、Telegram 等平台的 AI 自动回复机器人生成器
- <a href="https://www.heeyo.ai/" target="_blank">Heeyo AI</a> (**Heeyo AI** · 最新版) - 为 3-11 岁儿童打造的多语言 AI 聊伴，具教育游戏与成长适应能力

## AI 代理

### 视频剪辑代理

_这些是自动化视频剪辑工作流的 AI 代理，从概念到最终制作。_

- <a href="https://mosaic.so/" target="_blank">Mosaic</a> (**Mosaic** · 最新版) - 自动化整个视频制作工作流的智能 AI 视频剪辑平台
- <a href="https://www.opus.pro/agent" target="_blank">Opus Pro Agent</a> (**Opus Pro** · 最新版) - 面向社交媒体的 AI 视频生成器，可将新闻文章、脚本、音频、博客和 X 帖子转换为视频

### 设计代理

_这些是自动化设计工作流的 AI 代理，从概念到最终交付物。_

- <a href="https://www.lovart.ai/" target="_blank">Lovart</a> (**Lovart** · 最新版) - 世界首个设计代理，自动化整个设计流程，从概念到图像、视频、3D 等

### 音乐代理

_这些是通过自然对话和智能自动化辅助音乐创作、制作和编辑的 AI 代理。_

- <a href="https://agent.mix.audio/" target="_blank">Mix Audio Agent</a> (**MixAudio** · 最新版) - 一体化 AI 音乐代理，用于创建配乐、混音、音轨分离和音乐分析
- <a href="https://www.midiagent.com/" target="_blank">MIDI Agent</a> (**MIDI Agent** · 最新版) - AI VST & AU 插件，使用自然语言和主流 AI 模型（ChatGPT、Claude、Gemini、Grok）生成和转录 MIDI
- <a href="https://www.producer.ai/" target="_blank">Producer.ai</a> (**Producer.ai** · 最新版) - 从想象中创作音乐的 AI 音乐代理
- <a href="https://www.wondera.ai/" target="_blank">Wondera</a> (**Wondera** · 最新版) - 帮助实现音乐创意的 AI 音乐共创工具
- <a href="https://tunee.ai/" target="_blank">Tunee</a> (**Tunee** · 最新版) - 下一代 AI 音乐代理，通过自然对话创建定制音乐，理解风格偏好和创作模式

## 应用开发工厂

_这些是作为"应用工厂"或"产品工作室"运营的公司，构建和运营多个消费者应用程序，通常利用 AI 技术和系统化的产品开发方法。_

- <a href="https://www.lightricks.com/" target="_blank">Lightricks</a> (**Lightricks** · 最新版) - 以 Facetune、Videoleap 等热门应用构建的视觉内容"一体化创作工厂"，融合 AI 图像、视频生成与编辑引擎
- <a href="https://bendingspoons.com/" target="_blank">Bending Spoons</a> (**Bending Spoons** · 最新版) - 意大利技术集团，通过收购+优化模式，构建 Evernote、Meetup、Remini 等多款高活跃数字产品
- <a href="https://www.freepikcompany.com/" target="_blank">Freepik</a> (**Freepik** · 最新版) - 西班牙 AI 视觉平台，提供亿级素材库与图片/视频/音频生成及企业级创意工具
- <a href="https://www.kaleido.ai/" target="_blank">Kaleido</a> (**Canva** · 最新版) - 专注视觉 AI 编辑与自动化处理的工具平台，现为 Canva 旗下产品
- <a href="https://www.codeway.co/" target="_blank">Codeway</a> (**Codeway** · 最新版) - AI 驱动的移动应用开发工厂，从创意出发快速构建并运营高下载量 App
- <a href="https://www.pixerylabs.com/" target="_blank">Pixerylabs</a> (**Pixerylabs** · 最新版) - 面向内容创作者的手机视频编辑工具开发者，支持动画、特效与 AI 生成
- <a href="https://www.codeorgana.com/" target="_blank">Code (Organa)</a> (**Code Organa** · 最新版) - 开发支持艺术创作的手机 App 与视觉特效工具，包括 Brushstroke、Animatix 等
- <a href="https://vyro.ai/" target="_blank">Vyro</a> (**Vyro** · 最新版) - 多语言 AI 设计平台，将文本快速转化为高质量品牌视觉内容与图形设计
- <a href="https://www.learneo.com/" target="_blank">Learneo</a> (**Learneo** · 最新版) - 在线教育与创作平台，汇聚 Course Hero、Symbolab 等品牌，助力分享与访问学习资源
- <a href="https://www.intuit.com/" target="_blank">Intuit</a> (**Intuit** · 最新版) - 综合金融科技公司，提供 TurboTax 纳税、QuickBooks 账务、Credit Karma 信用监控与 Mailchimp 营销工具
- <a href="https://superapplabs.co/" target="_blank">Superapp Labs</a> (**Superapp Labs** · 最新版) - AI 移动应用孵化者，打造数款面向全球千万级用户的视觉与生产力 App
- <a href="https://aiby.com/" target="_blank">AIBY</a> (**AIBY** · 最新版) - 美国 AI 联合创公司，构建并运营多款下载过亿的消费者应用和游戏
- <a href="https://hubx.com/" target="_blank">HUBX</a> (**HUBX** · 最新版) - 全球化科技孵化器，构建 AI 驱动移动 App 并支持团队协作与资源共享
- <a href="https://www.mobiversite.com/" target="_blank">Mobiversite</a> (**Mobiversite** · 最新版) - 专注于移动应用开发和发行的公司，致力于为全球用户提供高质量的应用产品

## AI 招聘与求职

### 面向招聘者

_这些是专为招聘者和招聘经理设计的 AI 工具，帮助简化招聘流程，从职位发布到候选人筛选和管理。_

- <a href="https://www.moonhub.ai/" target="_blank">Moonhub</a> (**Moonhub** · 最新版) - AI 招聘助手，自动筛选面试并促进公平匹配
- <a href="https://mercor.com/" target="_blank">Mercor</a> (**Mercor** · 最新版) - AI 驱动招聘平台，生成匹配、面试及支付流程
- <a href="https://joinbrix.com/" target="_blank">Brix</a> (**Brix** · 最新版) - AI 自动生成 JD、筛选候选人及预审
- <a href="https://www.carv.com/" target="_blank">Carv</a> (**Carv** · 最新版) - 为招聘者自动处理流程并更新 ATS 系统
- <a href="https://www.turing.com/" target="_blank">Turing</a> (**Turing** · 最新版) - AI 驱动远程开发者平台，自动匹配和管理全球软件工程师
- <a href="https://micro1.io/" target="_blank">Micro1</a> (**Micro1** · 最新版) - AI 语音驱动的招聘平台
- <a href="https://apriora.ai/" target="_blank">Apriora</a> (**Apriora** · 最新版) - AI 语音驱动的招聘平台
- <a href="https://lightscreen.ai/" target="_blank">Lightscreen</a> (**Lightscreen** · 最新版) - AI 语音驱动的招聘平台

### 面向求职者

_这些是专为求职者设计的 AI 工具，帮助寻找机会、优化申请并准备面试。_

- <a href="https://www.thecorrelate.com" target="_blank">Correlate AI</a> (**Correlate AI** · 最新版) - 一键自动投简历，定制并投递匹配岗位
- <a href="https://helloboss.com/" target="_blank">Hello Boss</a> (**Hello Boss** · 最新版) - AI 职位推荐和一键生成履历日式招聘应用
- <a href="https://jobright.ai/" target="_blank">Jobright</a> (**Jobright** · 最新版) - AI 求职副驾驶，智能匹配并一键申请
- <a href="https://himalayas.app/" target="_blank">Himalayas</a> (**Himalayas** · 最新版) - 远程/AI 职位平台，匹配职位并生成简历封信
- <a href="https://nodeflair.com/" target="_blank">NODEFLAIR</a> (**NODEFLAIR** · 最新版) - 东南亚技术职业平台，简历工具+职位/工资透明
- <a href="https://www.senseicopilot.com/" target="_blank">Sensei AI</a> (**Sensei AI** · 最新版) - 浏览器面试伴侣，实时生成结构化答案
- <a href="https://www.finalroundai.com/" target="_blank">Final Round AI</a> (**Final Round AI** · 最新版) - AI 面试助手，自动生成简历，进行模拟面试
- <a href="https://www.lockedinai.com/" target="_blank">Lockedin AI</a> (**Lockedin AI** · 最新版) - 实时面试/会议助手，提供语音反馈和答案建议
- <a href="https://www.vervecopilot.com/" target="_blank">Verve AI</a> (**Verve AI** · 最新版) - AI 面试陪练助手，实时建议+冷邮和简历优化

### 通用平台

_这些平台同时为招聘者和求职者提供全面的招聘和求职解决方案。_

- <a href="https://clado.ai/" target="_blank">Clado AI</a> (**Clado AI** · 最新版) - AI 驱动的招聘和求职平台

## AI 数据工具

### 数据标注

_这些是用于数据标注、标记和管理的 AI 平台和服务，以支持机器学习模型训练。_

- <a href="https://scale.com/" target="_blank">Scale AI</a> (**Scale AI** · 最新版) - AI 驱动的数据标注平台，为机器学习模型提供高质量的训练数据
- <a href="https://snorkel.ai/" target="_blank">Snorkel</a> (**Snorkel** · 最新版) - 数据中心 AI 平台，将专业知识快速转成训练数据
- <a href="https://www.superannotate.com/" target="_blank">SuperAnnotate</a> (**SuperAnnotate** · 最新版) - 高效 AI 数据标注与管理平台，适用于模型训练
- <a href="https://www.coactive.ai/" target="_blank">Coactive</a> (**Coactive** · 最新版) - 多模态视觉内容平台，AI 自动标签、检索与分析图像/视频
- <a href="https://www.appen.com/" target="_blank">Appen</a> (**Appen** · 最新版) - 人机结合的企业级 AI 数据采集、清洗与标注平台
- <a href="https://www.surgehq.ai/" target="_blank">Surge</a> (**Surge** · 最新版) - 全球高技能众包标注平台，为生成式 AI 提供训练数据
- <a href="https://dataloop.ai/" target="_blank">Dataloop</a> (**Dataloop** · 最新版) - 端到端 AI 数据管理与标注平台，支持可视化和流水线自动化
- <a href="https://www.v7labs.com/" target="_blank">V7</a> (**V7** · 最新版) - AI 驱动的图像/视频数据标注平台，支持自动分割与流程协作

### 数据分析

_这些是通过对话界面和自动化洞察进行数据分析、商业智能和预测建模的 AI 工具。_

- <a href="https://julius.ai/" target="_blank">Julius</a> (**Julius** · 最新版) - 对数据进行对话式分析与预测建模的 AI 数据分析师
- <a href="https://datasquirrel.ai/" target="_blank">DataSquirrel</a> (**DataSquirrel** · 最新版) - 无代码 BI 工具，自动清洗、分析并可视化数据
- <a href="https://datachat.ai/" target="_blank">DataChat</a> (**DataChat** · 最新版) - 无需编码即能通过聊天查询并洞察数据的生成式分析平台
- <a href="https://vizly.fyi/" target="_blank">Vizly</a> (**Vizly** · 最新版) - AI 数据分析师，支持聊天查询并自动生成可视化报告
- <a href="https://www.morphdb.io/" target="_blank">Morph</a> (**Morph** · 最新版) - 一体化 No‑Code 数据工作室，结合表格、数据库与 AI 分析
- <a href="https://datagpt.com/" target="_blank">DataGPT</a> (**DataGPT** · 最新版) - 对话式 AI 数据分析师，实时提供业务数据洞察
- <a href="https://www.kater.ai/" target="_blank">Kater</a> (**Kater** · 最新版) - 企业 AI 报告平台，一问直达决策洞察与分析流程
- <a href="https://deepnote.com/" target="_blank">Deepnote</a> (**Deepnote** · 最新版) - 云端协作数据科学笔记本，AI 驱动代码、查询与可视化
- <a href="https://www.thoughtspot.com/" target="_blank">ThoughtSpot</a> (**ThoughtSpot** · 最新版) - AI 驱动分析工具，通过自然语言查询企业数据

### 合成数据

_这些平台生成合成数据用于训练 AI 模型，同时保护隐私并解决数据稀缺挑战。_

- <a href="https://aindo.com" target="_blank">Aindo</a> (**Aindo** · 最新版) - 数据科技公司，利用人工智能技术生成合成数据
- <a href="https://gretel.ai" target="_blank">Gretel AI</a> (**Gretel AI** · 最新版) - 提供合成数据平台的企业，专注于隐私保护的数据生成解决方案
- <a href="https://www.syntho.ai" target="_blank">Syntho</a> (**Syntho** · 最新版) - 数据技术公司，专注于利用人工智能生成合成数据
- <a href="https://mostly.ai" target="_blank">Mostly AI</a> (**Mostly AI** · 最新版) - 合成数据生成器和知识中心，专注于隐私保护的数据生成
- <a href="https://www.tonic.ai" target="_blank">Tonic.ai</a> (**Tonic.ai** · 最新版) - 数据技术公司，专注于利用人工智能和机器学习生成合成数据
- <a href="https://hazy.com" target="_blank">Hazy</a> (**Hazy** · 最新版) - 专注于合成数据领域的公司，提供隐私保护的数据生成解决方案

## AI 教育

### 作业与解题

_这些是专为学生设计的 AI 工具，帮助解决作业问题并提供即时答案和分步解释。_

- <a href="https://solvely.ai/" target="_blank">Solvely</a> (**Solvely** · 最新版) - 拍照解题的 AI 家庭作业助手，提供分步解法
- <a href="https://www.questionai.com/" target="_blank">Question AI</a> (**Question AI** · 最新版) - AI 即问即答作业助手，解题＋总结一步到位
- <a href="https://answerai.pro/" target="_blank">Answer AI</a> (**Answer AI** · 最新版) - 24/7 AI 学伴，答疑解题并提供写作/应用建议
- <a href="https://www.gauthmath.com/" target="_blank">Gauth</a> (**Gauth** · 最新版) - 多学科 AI 作业助手，拍照解题并提供详细解析
- <a href="https://cameramath.com/" target="_blank">Upstudy</a> (**Upstudy** · 最新版) - 拍照即解，涵盖所有学科的 AI 辅导助手

### 学习工具与闪卡

_这些工具帮助学生创建学习材料、生成闪卡并组织学习。_

- <a href="https://quizlet.com/" target="_blank">Quizlet</a> (**Quizlet** · 最新版) - AI 闪卡与学习工具，支持自建与分享学习集
- <a href="https://knowt.com/" target="_blank">Knowt</a> (**Knowt** · 最新版) - AI 笔记与闪卡生成器，一键转录高效学习
- <a href="https://www.studyfetch.com/" target="_blank">Study Fetch</a> (**Study Fetch** · 最新版) - 录音转 AI 笔记与测验的个性学习助手
- <a href="https://www.mindgrasp.ai/" target="_blank">Mindgrasp</a> (**Mindgrasp** · 最新版) - 上传文稿生成笔记、闪卡与测验的 AI 学习平台
- <a href="https://www.scholarcy.com/" target="_blank">Scholarcy</a> (**Scholarcy** · 最新版) - AI 自动摘要研究文献，生成互动式闪卡
- <a href="https://penseum.com/" target="_blank">Penseum</a> (**Penseum** · 最新版) - AI 学习平台，上传资料生成定制笔记、闪卡与测验

### 语言学习

_这些平台使用 AI 帮助用户通过对话、发音训练和互动练习学习语言。_

- <a href="https://www.boldvoice.com/" target="_blank">BoldVoice</a> (**BoldVoice** · 最新版) - AI+好莱坞口音教练辅助发音训练 App
- <a href="https://www.duolingo.com/" target="_blank">Duolingo</a> (**Duolingo** · 最新版) - 游戏化语言学习应用，提供多语种课程与每日练习
- <a href="https://www.apeuni.com/" target="_blank">APEUni</a> (**APEUni** · 最新版) - 免费 AI 驱动的 PTE 考试练习平台，评估口语与写作
- <a href="https://praktika.ai/" target="_blank">Praktika.ai</a> (**Praktika.ai** · 最新版) - AI 语言导师 App，通过对话练习提升口语
- <a href="https://www.speak.com/" target="_blank">Speak</a> (**Speak** · 最新版) - AI 对话教学 App，通过实时口语练习反馈提升流利度
- <a href="https://www.trancy.org/" target="_blank">Trancy</a> (**Trancy** · 最新版) - 为视频自动生成双语字幕并建立学习卡片
- <a href="https://gliglish.com/" target="_blank">Gliglish</a> (**Gliglish** · 最新版) - 通过语音与 AI 角色演练，提升口语与听力
- <a href="https://lingokids.com/" target="_blank">Lingokids</a> (**Lingokids** · 最新版) - 儿童语言学习 App，通过游戏互动和语音识别让 2-8 岁孩子快乐学习
- <a href="https://www.mondly.com/" target="_blank">Mondly</a> (**Mondly** · 最新版) - 多人语言学习 App，提供会话式练习和语音识别功能

### 数学工具

_这些是专注于解决数学问题和提供数学辅导的专业 AI 工具。_

- <a href="https://www.mathgptpro.com/" target="_blank">Mathos</a> (**Mathos** · 最新版) - AI 数学解题器与个性化辅导工具
- <a href="https://math-gpt.org/" target="_blank">MathGPT</a> (**MathGPT** · 最新版) - 图像数学计算器，提供视频+动画解题教程
- <a href="https://photomath.com/" target="_blank">Photomath</a> (**Photomath** · 最新版) - 拍照识别数学题，分步教学多种解法
- <a href="https://www.mathway.com/" target="_blank">Mathway</a> (**Mathway** · 最新版) - 支持拍照与输入的多用途数学问题解决器
- <a href="https://qanda.ai/" target="_blank">Quanda</a> (**Quanda** · 最新版) - OCR 识题+一步解答的 AI 数学学习平台，用户超 9000 万

### 辅导平台

_这些平台提供全面的辅导服务、学习材料和学术支持。_

- <a href="https://www.chegg.com/" target="_blank">Chegg</a> (**Chegg** · 最新版) - 24/7 在线作业辅导与教材租赁平台
- <a href="https://www.coursehero.com/" target="_blank">Course Hero</a> (**Course Hero** · 最新版) - 百万课程资料+在线辅导一站式学习平台
- <a href="https://www.khanmigo.ai/" target="_blank">Khanmigo</a> (**Khan Academy** · 最新版) - Khan Academy 的智能辅导员，提供引导式学习支持
- <a href="https://www.datacamp.com/" target="_blank">DataCamp</a> (**DataCamp** · 最新版) - 编程与数据分析在线学习平台，提供项目和技能课程

### 课堂工具

_这些工具专为教师设计，用于创建互动课程、测验和管理课堂活动。_

- <a href="https://quizizz.com/" target="_blank">Quizizz</a> (**Quizizz** · 最新版) - 在线互动测验平台，支持课堂与远程游戏式学习
- <a href="https://curipod.com/" target="_blank">Curipod</a> (**Curipod** · 最新版) - 为 K-12 设计的 AI 互动课堂，生成投票与测验
- <a href="https://classcompanion.com/" target="_blank">Class Companion</a> (**Class Companion** · 最新版) - 教师工具，AI 即时批改反馈并辅导学生
- <a href="https://www.doctrina.ai/" target="_blank">Doctrina AI</a> (**Doctrina AI** · 最新版) - 多功能 AI 教育平台，生成笔记、测验、论文与对话
- <a href="https://www.bohrium.com/" target="_blank">Bohrium</a> (**Bohrium** · 最新版) - 学术类教育平台

## AI 生产力工具

### 项目管理与协作

_这些平台帮助团队管理项目、协作并高效组织工作。_

- <a href="https://www.notion.so/" target="_blank">Notion</a> (**Notion** · 最新版) - 可定制的一体化协作空间，集笔记、数据库、任务与 AI 助手于一体
- <a href="https://miro.com/" target="_blank">Miro</a> (**Miro** · 最新版) - 在线视觉白板，支持分布式团队的创新协作与头脑风暴
- <a href="https://clickup.com/" target="_blank">ClickUp</a> (**ClickUp** · 最新版) - 全能型项目管理平台，集任务、文档、时间线、AI 功能于一处
- <a href="https://trello.com/" target="_blank">Trello</a> (**Trello** · 最新版) - 看板式协作工具，用卡片与列表直观管理项目任务
- <a href="https://asana.com/" target="_blank">Asana</a> (**Asana** · 最新版) - 团队任务管理平台，支持项目规划、进度跟踪与实时报告
- <a href="https://www.airtable.com/" target="_blank">Airtable</a> (**Airtable** · 最新版) - 表格+数据库协作平台，适用自定义应用与数据驱动流程
- <a href="https://quip.com/" target="_blank">Quip</a> (**Quip** · 最新版) - Salesforce 内嵌实时文档协作，融合表格与聊天功能

### 笔记与知识管理

_这些工具帮助用户捕获、组织和管理知识与信息。_

- <a href="https://evernote.com/" target="_blank">Evernote</a> (**Evernote** · 最新版) - 笔记与任务管理工具，全平台同步、AI 整理与支持多媒体输入
- <a href="https://obsidian.md/" target="_blank">Obsidian</a> (**Obsidian** · 最新版) - Markdown 本地笔记工具，支持插件与强大双向链接
- <a href="https://logseq.com/" target="_blank">Logseq</a> (**Logseq** · 最新版) - 隐私优先的本地知识库，基于 Markdown 与双向链接构建
- <a href="https://feather.so/" target="_blank">Feather</a> (**Feather** · 最新版) - 轻量级协作笔记/文档应用，强调极简与多平台同步
- <a href="https://flowith.io/" target="_blank">Flowith</a> (**Flowith** · 最新版) - 面向创作者的 AI 工作空间，多线程画布助力知识管理与创作

### 表单与问卷

_这些工具能够高效创建表单、问卷并收集数据。_

- <a href="https://tally.so/" target="_blank">Tally</a> (**Tally** · 最新版) - 无代码表单工具，类似 Notion 式编辑，免费创建多样表单
- <a href="https://www.typeform.com/" target="_blank">Typeform</a> (**Typeform** · 最新版) - 交互式表单/问卷生成器，打造对话式用户体验，提升完成率
- <a href="https://www.surveymonkey.com/" target="_blank">Survey Monkey</a> (**Survey Monkey** · 最新版) - 专业在线问卷平台，支持多种题型及 AI 辅助问卷生成

### 日程安排

_这些工具帮助管理日程、预约和日历事件。_

- <a href="https://cal.com/" target="_blank">Cal.com</a> (**Cal.com** · 最新版) - 可自托管的开源日程安排基础设施，支持高度定制化排期
- <a href="https://calendly.com/" target="_blank">Calendly</a> (**Calendly** · 最新版) - 自动化日程管理工具，一键安排并去除多余沟通成本
- <a href="https://www.usemotion.com/" target="_blank">Motion</a> (**Motion** · 最新版) - AI 项目/时间管理助手，自动生成任务与日程安排

### PDF 与文档工具

_这些工具帮助编辑、注释和管理 PDF 和文档文件。_

- <a href="https://updf.com/" target="_blank">UPDF</a> (**UPDF** · 最新版) - 跨平台 AI PDF 编辑器，具备阅读、编辑、注释与聊天功能

### 文档平台

_这些平台帮助创建、管理和分享文档。_

- <a href="https://www.gitbook.com/" target="_blank">Gitbook</a> (**Gitbook** · 最新版) - 面向技术团队的文档平台，AI 搜索+可视化协作编辑文档
- <a href="https://scribehow.com/" target="_blank">Scribe</a> (**Scribe** · 最新版) - 自动捕捉操作并生成带截图的步骤指南，用 AI 快速输出流程文档
- <a href="https://mintlify.com/" target="_blank">Mintlify</a> (**Mintlify** · 最新版) - AI 驱动文档平台，一键从代码生成可交互、高度可定制的开发者文档

### 工作流自动化

_这些工具自动化工作流、流程和重复性任务。_

- <a href="https://n8n.io/" target="_blank">n8n</a> (**n8n** · 最新版) - 可自托管的低代码 AI 自动化平台，连接多种服务并构建流程
- <a href="https://www.getmagical.com/" target="_blank">Magical</a> (**Magical** · 最新版) - Chrome 自动填充 AI 助手，支持表单、消息与表格一键执行
- <a href="https://brightdata.com/" target="_blank">Bright Data</a> (**Bright Data** · 最新版) - 大规模代理与网页采集平台，提供结构化数据与 API
- <a href="https://www.automationanywhere.com/" target="_blank">Automation Anywhere</a> (**Automation Anywhere** · 最新版) - 面向企业的全流程智能 RPA 自动化平台
- <a href="https://www.gumloop.com/" target="_blank">Gumloop</a> (**Gumloop** · 最新版) - 无代码 AI 自动化平台，通过拖拽组件构建复杂工作流
- <a href="https://composio.dev/" target="_blank">Composio.dev</a> (**Composio** · 最新版) - 连接 LLM 与 250+ 工具的集成平台，轻松构建具代理能力的 AI 应用
- <a href="https://www.uipath.com/" target="_blank">UiPath</a> (**UiPath** · 最新版) - 企业级 RPA 平台，结合 AI 与机器人流程自动化，智能执行重复任务
- <a href="https://www.induced.ai/" target="_blank">Induced</a> (**Induced** · 最新版) - Human-in-the-loop RPA 3.0，AI 驱动网页任务自动化，实现实时智能判断
- <a href="https://www.stagehand.dev/" target="_blank">Stagehand</a> (**Stagehand** · 最新版) - AI 浏览器自动化框架，支持代码与自然语言混合控制浏览器操作
- <a href="https://www.browserless.io/" target="_blank">Browserless</a> (**Browserless** · 最新版) - 无头浏览器即服务，支持 Docker 部署，自动避开反爬虫并实现页面自动化

### 企业 AI 助手

_这些是企业级 AI 助手，自动化业务流程并处理复杂任务。_

- <a href="https://www.moveworks.com/" target="_blank">Moveworks</a> (**Moveworks** · 最新版) - 企业级智能 AI 助手，自动响应员工请求并执行任务
- <a href="https://aisera.com/" target="_blank">Aisera</a> (**Aisera** · 最新版) - 企业 AI 服务台助手，自动处理 IT/HR 请求并生成工单和解决方案
- <a href="https://kore.ai/" target="_blank">Kore.ai</a> (**Kore.ai** · 最新版) - 企业级对话式 AI 平台，构建智能客服机器人
- <a href="https://www.sierra.com/" target="_blank">Sierra</a> (**Sierra** · 最新版) - 企业级会话 AI 代理平台，定制化品牌虚拟助手用于客户服务与任务处理
- <a href="https://www.pryon.com/" target="_blank">Pryon</a> (**Pryon** · 最新版) - 企业知识搜索与自动化问答系统，通过语义理解提升信息生产效率
- <a href="https://momoai.co/" target="_blank">Momo</a> (**Momo** · 最新版) - AI 对话助手，可接入业务系统实现自动客户问答与智能流程处理
- <a href="https://ushur.ai/" target="_blank">Ushur</a> (**Ushur** · 最新版) - AI 驱动的客户体验自动化平台，通过聊天与流程机器人实现端到端服务变革
- <a href="https://contextual.ai/" target="_blank">Contextual AI</a> (**Contextual AI** · 最新版) - 企业级 RAG 平台，构建具高度真实度的知识驱动智能助手

### AI 聊天助手

_这些是 AI 驱动的聊天助手，用于各种生产力与沟通任务。_

- <a href="https://www.popai.pro/" target="_blank">PopAi</a> (**PopAi** · 最新版) - 多功能 AI 助手 App，支持对话查询文档、制作幻灯片、作业解答与图像生成
- <a href="https://usegenie.ai/" target="_blank">Genie</a> (**Genie** · 最新版) - 集成 GPT‑4o、Gemini 等多模型的 AI 聊天助手，用于写作、客服等多场景
- <a href="https://chatboxai.app/" target="_blank">ChatBox</a> (**ChatBox** · 最新版) - 跨平台 AI 客户端，可处理对话、文档、图片和代码，助力写作与生产力
- <a href="https://chaton.ai/" target="_blank">ChatOn</a> (**ChatOn** · 最新版) - 结合 GPT‑4/GPT‑4o 的写作与生产力 AI 聊天助手，涵盖内容创作和搜索工具
- <a href="https://ai.quark.cn/" target="_blank">Quark</a> (**Alibaba** · 最新版) - 阿里巴巴旗下 AI 超级助手，集成搜索、笔记、云盘、文档与深度推理功能
- <a href="https://novaapp.ai/" target="_blank">Nova A.I.</a> (**Nova A.I.** · 最新版) - 基于 GPT‑4o 和 Gemini 的全平台聊天助手，支持写作、问答、推荐等多功能
- <a href="https://manus.im/" target="_blank">manus</a> (**manus** · 最新版) - 中国首款通用自主 AI 代理，可自主执行复杂在线任务并生成输出结果
- <a href="https://inflection.ai/" target="_blank">Inflection AI</a> (**Inflection AI** · 最新版) - 个人AI助手Pi，提供富有同理心的对话体验，用于规划、日程安排和信息收集

## AI 金融与会计工具

### 财务运营与会计

_这些平台自动化财务运营、会计流程和企业的财务管理。_

- <a href="https://www.bill.com/" target="_blank">Bill</a> (**Bill.com** · 最新版) - 中小企业财务运营平台，自动处理发票生成支付、开票、费用管理与预算控制
- <a href="https://www.rillet.com/" target="_blank">Rillet</a> (**Rillet** · 最新版) - AI 原生 ERP 系统，自动完成月末关账、合并、GAAP 报表与发票处理

### 金融分析与情报

_这些工具提供 AI 驱动的金融分析、市场情报和投资决策支持。_

- <a href="https://rogo.ai/" target="_blank">Rogo AI</a> (**Rogo AI** · 最新版) - 面向金融机构的专属 AI 分析平台，自动研究数据、生成洞察并加速投资决策
- <a href="https://www.alpha-sense.com/" target="_blank">AlphaSense</a> (**AlphaSense** · 最新版) - AI 企业搜索引擎，实时分析市场与财务情报

### 金融基础设施

_这些是专为金融应用和高性能金融数据处理设计的基础设施工具和数据库。_

- <a href="https://www.ibm.com/products/informix" target="_blank">Informix</a> (**IBM** · 最新版) - IBM 的多模态关系数据库，适合混合事务与分析场景

## AI SEO 与营销工具

### GEO (Google E-E-A-T 优化) 工具

_这些工具帮助品牌优化在 AI 搜索平台和 LLM 生成内容中的可见性和存在感。_

- <a href="https://www.bluefishai.com/" target="_blank">Bluefish</a> (**Bluefish** · 最新版) - AI 可见性分析平台，帮助品牌优化在 AI 搜索平台中的存在感
- <a href="https://scrunchai.com/" target="_blank">Scrunch AI</a> (**Scrunch AI** · 最新版) - 构建了面向 AI 爬虫的基础设施层 - Agent Experience Platform（AXP），帮助品牌提供为 AI agent 和爬虫压缩、结构化的内容，创建品牌的机器可读版本，针对大语言模型解析、解释和返回内容的方式进行了优化
- <a href="https://www.tryprofound.com/" target="_blank">Profound</a> (**Profound** · 最新版) - 面向企业的 AI 可见性分析工具，实时监控并优化品牌 AI 搜索平台上的曝光与引用
- <a href="https://www.evertune.ai/" target="_blank">Evertune</a> (**Evertune** · 最新版) - GEO 优化平台，帮助品牌提升在 AI 搜索结果中的可见性

### SEO 优化工具

_这些工具帮助优化网站内容、关键词和 SEO 性能。_

- <a href="https://www.withdaydream.com/" target="_blank">Daydream</a> (**Daydream** · 最新版) - SEO 优化工具，用于提升搜索引擎排名
- <a href="https://www.airops.com/" target="_blank">Airops</a> (**Airops** · 最新版) - 内容运营 AI 平台，结合专家策略与 SEO 自动生成优化内容
- <a href="https://www.clearscope.io/" target="_blank">Clearscope</a> (**Clearscope** · 最新版) - 内容优先的 AI SEO 工具，关键词优化与竞争分析助流量增长
- <a href="https://byword.ai/" target="_blank">Byword</a> (**Byword** · 最新版) - AI SEO 写作助手，一键生成高质量、结构化并优化排名文案
- <a href="https://frase.io/" target="_blank">Frase</a> (**Frase** · 最新版) - SEO 内容优化与 AI 写作工具，结合专家策略与自动化内容生成

### SEO 本地化工具

_这些工具帮助创建针对国际 SEO 优化的多语言网站。_

- <a href="https://www.globalseo.ai/" target="_blank">GlobalSEO</a> (**GlobalSEO** · 最新版) - AI 驱动网站多语言自动翻译，提升国际有机搜索流量

_这些工具帮助创建针对国际 SEO 优化的多语言网站。_

- <a href="https://www.globalseo.ai/" target="_blank">GlobalSEO</a> (**GlobalSEO** · 最新版) - AI 驱动网站多语言自动翻译，提升国际有机搜索流量
- <a href="https://www.weglot.com/" target="_blank">Weglot</a> (**Weglot** · 最新版) - 无代码多语言网站翻译平台，支持 SEO 优化与内容编辑

## 屏幕录制工具

_这些工具帮助捕获屏幕录制、创建演示并分享视觉内容。_

- <a href="https://www.loom.com/" target="_blank">Loom</a> (**Loom** · 最新版) - 一键录屏分享，辅以 AI 视频增强、文本剪辑与跨平台协作功能
- <a href="https://screen.studio/" target="_blank">Screen Studio</a> (**Screen Studio** · 最新版) - Mac 专用屏幕录像软件，自动平滑光标、放大重点并优化动态
- <a href="https://www.arcade.software/" target="_blank">Arcade</a> (**Arcade** · 最新版) - 无代码互动演示平台，快速制作引人入胜的产品 demo 页面
- <a href="https://cursorful.com/" target="_blank">Cursorful</a> (**Cursorful** · 最新版) - 浏览器录制插件，自动缩放光标焦点，实现专业级演示视频

## 垂直领域解决方案

_这些平台为特定行业和垂直市场提供专业的 AI 驱动解决方案。_

### 宗教与非营利组织
- <a href="https://gloo.us/" target="_blank">Gloo</a> (**Gloo** · 最新版) - 连接信仰生态系统的技术平台，为教会、宗教组织和非营利机构提供 AI 驱动的内容分发与管理工具，已服务超过 14 万个机构

## AI 电子表格工具

_这些是 AI 驱动的电子表格工具，提供智能数据分析和自动化。_

- <a href="https://endex.ai/" target="_blank">Endex.ai</a> (**Endex.ai** · 最新版) - AI 电子表格工具，提供智能数据分析和可视化功能
- <a href="https://www.paradigmai.com/" target="_blank">Paradigm</a> (**Paradigm** · 最新版) - AI 电子表格平台，支持自动化数据处理和高级分析

---

## 关于

由 **<a href="https://alignify.co" target="_blank">Kostja</a>** 精心整理和维护。欢迎通过 <a href="https://github.com/kostja94/awesome-ai-tools/issues" target="_blank">GitHub Issues</a> 或邮件 **zyjstc@gmail.com** 贡献

### 数据来源

本仓库的信息来源于多个渠道，包括 LMArena（模型排名和性能基准测试）、Artificial Analysis（全面的 AI 模型评估和比较）、大模型回复、网络资源（官方文档、网站和公开资源）以及个人从业经验。

## 许可证

本项目采用 MIT 许可证 - 详见 <a href="LICENSE" target="_blank">LICENSE</a> 文件。

## 致谢

感谢所有贡献者和 AI 社区的支持与反馈。
- 感谢所有构建出色产品的 AI/SaaS 创作者

---

**维护者：<a href="https://alignify.co" target="_blank">Kostja</a>** | 最后更新：2025

