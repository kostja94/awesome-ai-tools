<a href="README.md" target="_blank">English</a> | 中文

# Awesome AI Tools

> 由 AI Product Registry 客观事实驱动的精选 AI 工具目录。

## 目录

- [模型](#group-models)
  - [语言与搜索模型](#section-language-models)
  - [图像模型](#section-image-models)
  - [视频模型](#section-video-models)
  - [语音模型](#section-speech-models)
  - [音乐模型](#section-music-models)
  - [三维与空间模型](#section-spatial-models)
- [Agent 开发基础设施](#group-agents)
  - [Agent 框架与基础设施](#section-agent-platforms)
  - [Agent 支付与身份](#section-agent-payments-identity)
  - [Agent 与模型评测](#section-agent-evaluation)
  - [Agent 开发平台](#section-agent-builders)
  - [LLM 与 Agent 框架](#section-llm-frameworks)
- [编程与应用开发](#group-coding)
  - [编程工具](#section-coding-tools)
  - [应用构建工具](#section-app-builders)
  - [开发者平台](#section-developer-platforms)
- [图像与设计](#group-image-design)
  - [图像生成与编辑](#section-image-creation-editing)
  - [设计与用户研究](#section-design-tools)
  - [多模态创作](#section-creative-workflows)
- [视频与影视](#group-video-film)
  - [视频生成与编辑](#section-video-generation-editing)
  - [影视制作与本地化](#section-filmmaking-localization)
- [语音与音频](#group-voice-audio)
  - [语音与转写应用](#section-speech-applications)
  - [音乐、音频与播客](#section-music-podcasts)
- [搜索与网页数据](#group-search-web-data)
  - [搜索与检索](#section-search-retrieval)
  - [网页数据与浏览器](#section-web-data-browsers)
  - [AI 搜索应用](#section-search-applications)
  - [搜索 API](#section-search-api-services)
- [数据与云基础设施](#group-data-cloud)
  - [云与模型基础设施](#section-cloud-infrastructure)
  - [数据平台与分析](#section-data-platforms)
  - [模型访问与路由](#section-model-access)
  - [模型平台与社区](#section-model-hubs)
  - [模型运行工具](#section-model-runtime-tools)
- [效率与知识管理](#group-productivity-knowledge)
  - [文档与知识](#section-documents-knowledge)
  - [效率与自动化](#section-productivity-automation)
  - [企业助手](#section-enterprise-assistants)
  - [会议记录与摘要](#section-meeting-notes)
- [营销与客户服务](#group-marketing-service)
  - [营销与内容](#section-marketing-content)
  - [客户服务与销售智能](#section-customer-service)
- [电商与购物](#group-commerce)
  - [电商与购物](#section-commerce-shopping)
- [金融与财务](#group-finance)
  - [金融与会计](#section-finance-accounting)
- [教育与研究](#group-education-research)
  - [学习与教学](#section-learning-tools)
  - [研究与学术写作](#section-research-writing)
- [招聘与职业](#group-hr-recruiting)
  - [招聘与职业](#section-recruiting-careers)
- [医疗健康](#group-healthcare)
  - [医疗健康](#section-healthcare)
- [法律](#group-legal)
  - [法律](#section-legal)
- [三维与空间](#group-spatial)
  - [三维与空间工具](#section-spatial-3d)
- [游戏与互动媒体](#group-games)
  - [游戏与互动媒体](#section-games-interactive)
- [写作与出版](#group-writing)
  - [写作与出版](#section-writing-publishing)
- [对话与社交](#group-social)
  - [对话与社交](#section-chat-social)
- [行业运营](#group-industry-solutions)
  - [行业运营](#section-industry-operations)
- [AI 工具发现](#group-discovery)
  - [AI 工具目录](#section-tool-discovery)

<a id="group-models"></a>

## 模型

<a id="section-language-models"></a>

### 语言与搜索模型

选择模型时，可以先了解[通用大语言模型的能力与评测维度](https://alignify.co/zh/tools/llm)。

- <a href="https://openai.com/" target="_blank">GPT</a> - OpenAI 的旗舰语言模型家族，涵盖 GPT-4、GPT-4.5、GPT-5、GPT-6 等系列及多个变体
- <a href="https://gemini.google.com/" target="_blank">Gemini</a> - Google DeepMind 推出的多模态大模型，支持文本、图像、音频和视频输入，版本覆盖 2.5 至 4 系列
- <a href="https://claude.com/" target="_blank">Claude</a> - Anthropic 开发的语言模型家族，通过 API 提供，并内置于 Claude 助手产品
- <a href="https://x.ai/" target="_blank">Grok</a> - xAI 推出的语言模型家族，覆盖 Grok 3、Grok 4 与 Grok 4.1，驱动 X 和 grok.com 上的 Grok 助手，并通过 xAI API 提供
- <a href="https://dev.meta.ai/" target="_blank">Llama</a> - Meta 的开放权重语言模型系列，从 Llama 3 迭代至 Llama 4
- <a href="https://www.deepseek.com/" target="_blank">DeepSeek</a> - DeepSeek 的开放权重语言模型家族，包含 V2、V3、V3.1、V4 Pro 与 R1 等版本
- <a href="https://chat.qwen.ai/" target="_blank">Qwen</a> - Alibaba 的开放权重语言模型家族，从 Qwen2.5 迭代到 Qwen3.7
- <a href="https://mistral.ai/" target="_blank">Mistral</a> - Mistral AI 的通用语言模型家族，按 Small、Medium、Large 分档（如 Mistral Large 2、Mistral Medium 3），通过 la Plateforme API 提供并支持企业部署
- <a href="https://deepmind.google/models/gemma/" target="_blank">Gemma</a> - Google 开放权重模型家族，基于 Gemini 技术构建，版本跨度至 Gemma 4
- <a href="https://www.kimi.com/" target="_blank">Kimi</a> - Moonshot AI 推出的语言模型家族，覆盖文本、代码与推理任务，包含具备视觉能力和开放权重的版本，从 K1.5 迭代到 K3
- <a href="https://docs.z.ai/" target="_blank">GLM</a> - Zhipu AI（Z.ai）推出的语言模型家族，覆盖 GLM-4、GLM-4.5 与 GLM-5，通过 Z.ai API 提供，2025 年起以 MIT 许可开放权重
- <a href="https://hunyuan.tencent.com/" target="_blank">Hunyuan</a> - Tencent 的 Hunyuan 模型家族，覆盖语言、图像、视频与三维内容生成
- <a href="https://www.minimax.io/" target="_blank">MiniMax</a> - MiniMax 的语言模型家族，权重开放，覆盖文本生成、编码与工具辅助工作流，当前版本 M2.7
- <a href="https://github.com/QwenLM/Qwen3-Coder" target="_blank">Qwen3 Coder</a> - Alibaba 旗下编码模型家族，Apache 2.0 许可，已迭代至 Qwen3-Coder
- <a href="https://aleph-alpha.com" target="_blank">Luminous</a> - Aleph Alpha 推出的语言模型家族，支持多语言文本与图像分析

<a id="section-image-models"></a>

### 图像模型

- <a href="https://www.midjourney.com/" target="_blank">Midjourney</a> - 独立实验室 Midjourney 的文生图与视频模型，以艺术质感著称，图像模型已至 V8
- <a href="https://developers.openai.com/api/docs/models/gpt-image-2" target="_blank">gpt-image-2.5</a> - OpenAI 图像生成与编辑模型家族，现行版本为 gpt-image-2.5
- <a href="https://aistudio.google.com/models/nano-banana" target="_blank">Nano Banana 2.1</a> - Google 图像生成与编辑模型家族，现行版本为 Nano Banana 2.1
- <a href="https://www.adobe.com/products/firefly.html" target="_blank">Adobe Firefly</a> - Adobe 的文生图模型，与 Creative Cloud 集成
- <a href="https://stability.ai/" target="_blank">Stable Diffusion</a> - 开源文生图模型系列，提供 API 访问
- <a href="https://bfl.ai/" target="_blank">FLUX</a> - Black Forest Labs 推出的文生图模型
- <a href="https://seed.bytedance.com/en/tech/seedream3_0" target="_blank">Seedream</a> - 字节跳动 Seed 图像模型家族，Seedream 4.0 统一生成与编辑，支持文本与多图参考输入、最高 4K 输出
- <a href="https://ideogram.ai/" target="_blank">Ideogram</a> - 以图像内文字渲染见长的文生图模型
- <a href="https://leonardo.ai/" target="_blank">Leonardo AI</a> - 面向创作者的图像与视频生成平台，内置 80 多个模型，含 Lucid 等自研系列
- <a href="https://chat.qwen.ai" target="_blank">Qwen-Image-3.0</a> - Alibaba Qwen 图像生成家族，现行 Qwen-Image-3.0，基础权重开源
- <a href="https://hunyuan.tencent.com/image/en" target="_blank">Tencent Hunyuan Image</a> - Tencent Hunyuan 图像家族，3.0 版开源，3.5 预览版支持多轮对话编辑
- <a href="https://www.recraft.ai/" target="_blank">Recraft</a> - 支持矢量图与 mockup 输出的文生图模型
- <a href="https://www.microsoft.com/en-us/ai/mai-image" target="_blank">MAI Image</a> - Microsoft AI 的文生图模型
- <a href="https://lumalabs.ai/photon" target="_blank">Luma Photon</a> - Luma Labs 的文生图模型系列，photon-1 支持多图参考与角色一致性
- <a href="https://hidreamai.com/" target="_blank">HiDream</a> - HiDream 的全模态基础模型覆盖图像、视频与 3D，并开源 E1.1 图像编辑模型
- <a href="https://www.stepfun.com/" target="_blank">StepFun</a> - 阶跃星辰的图像生成编辑模型系列，Step Image Edit 2 单模型兼顾文生图与图像编辑
- <a href="https://reve.com/" target="_blank">Reve</a> - Reve 的文生图模型，配套统一网页应用，支持创建、编辑与重混图像，将自然语言指令与拖拽式编辑器相结合

<a id="section-video-models"></a>

### 视频模型

- <a href="https://deepmind.google/technologies/veo/" target="_blank">Google Veo 3.1</a> - Google 的文生视频模型，原生输出配套音频，支持 4K 分辨率并嵌入 SynthID 水印，通过 Gemini 应用与 API 提供
- <a href="https://kling.ai/" target="_blank">Kling</a> - 快手旗下的 AI 视频与图像平台，视频模型已迭代至可灵 4.0，图像支持原生 4K 直出
- <a href="https://runway.com/" target="_blank">Runway Gen</a> - Runway 的视频生成模型家族，以 Gen-4.5 为主打，强调运动质量与提示遵循，另有 GWM-1 世界模型，经其应用与 API 提供
- <a href="https://seed.bytedance.com/en/seedance" target="_blank">Seedance</a> - ByteDance Seed 团队的视频生成模型家族，版本自 1.0 迭代至 2.5，音视频一体生成，支持参考控制与编辑，另经 Dreamina 平台提供
- <a href="https://hailuoai.video/" target="_blank">Hailuo</a> - MiniMax 旗下 AI 视频生成平台，支持文生视频与图生视频，最新模型为 H3
- <a href="https://lumalabs.ai/ray" target="_blank">Luma Ray</a> - Luma 的 Ray 模型家族，支持以文本、图像或视频为条件的视频生成与编辑，可通过 Luma Dream Machine 和 Luma API 使用
- <a href="https://pika.art/" target="_blank">Pika</a> - Pika Labs 推出的文生视频模型家族，Pika 2.2 可生成 1080p、最长 10 秒的视频，并提供 Pikaframes 关键帧控制与 Pikaffects 物理特效
- <a href="https://tongyi.aliyun.com/wanxiang/" target="_blank">WAN</a> - Alibaba 的 Wan 模型家族，支持从文本或图像生成视频
- <a href="https://aivideo.hunyuan.tencent.com/" target="_blank">Tencent Hunyuan Video</a> - Tencent Hunyuan 视频生成模型家族，可从文本和图像输入生成视频
- <a href="https://www.vidu.com/" target="_blank">Vidu</a> - 生数科技的视频生成模型家族，支持文生视频与多参考生成，含实时交互的 Vidu S
- <a href="https://pixverse.ai/" target="_blank">PixVerse</a> - AI 视频生成平台，V6 模型可输出带原生音频的 1080p 视频，另有 R2 实时世界模型，经网页、移动端与 API 提供
- <a href="https://www.genmo.ai/" target="_blank">Mochi</a> - Genmo 的开源文生视频模型，Mochi 1 权重在 Hugging Face，支持本地运行
- <a href="https://www.animon.ai/" target="_blank">Animon</a> - 东京 Animon 推出的动漫专用 AI 视频生成平台，订阅制不限量生成

<a id="section-speech-models"></a>

### 语音模型

- <a href="https://github.com/openai/whisper" target="_blank">OpenAI Whisper</a> - OpenAI 的开源语音识别模型，覆盖 99 种语言，支持本地部署，社区衍生出 WhisperX 和 faster-whisper 等版本
- <a href="https://elevenlabs.io/speech-to-text" target="_blank">ElevenLabs Scribe v2</a> - ElevenLabs 语音转文字模型家族，含批量、实时与医疗版本，支持 90 多种语言
- <a href="https://docs.cloud.google.com/speech-to-text/docs/models/chirp-3" target="_blank">Google Chirp 3</a> - Chirp 3 是 Google Cloud Speech-to-Text 中的语音转文字模型，基于 Conformer 架构，支持 100 多种语言
- <a href="https://deepgram.com/" target="_blank">Deepgram Nova</a> - Deepgram Nova 语音识别模型，每秒可转录 142 秒音频
- <a href="https://www.assemblyai.com/" target="_blank">AssemblyAI</a> - AssemblyAI 的语音转文字 API，支持长音频文件、关键词检测和情感分析
- <a href="https://www.speechmatics.com/" target="_blank">Speechmatics</a> - Speechmatics 的语音识别服务覆盖全球语言，支持多种口音和方言
- <a href="https://www.sesame.com/" target="_blank">Sesame CSM-1B</a> - Sesame 的对话语音模型，1B 参数版本以 Apache 2.0 开源；公司语音演示中展示的更大模型与之相配套
- <a href="https://www.cartesia.ai/sonic" target="_blank">Sonic</a> - Cartesia 的流式文本转语音模型系列，面向需要实时语音输出的应用
- <a href="https://dev.hume.ai/voice/docs/text-to-speech-tts/overview" target="_blank">Octave</a> - Hume 推出的语音语言模型系列，用于生成富有表现力的语音
- <a href="https://fish.audio" target="_blank">Fish Audio S2.1 Pro</a> - Fish Audio 生产级文本转语音模型，升级至 S2.1 Pro，覆盖 83 种语言
- <a href="https://inworld.ai/" target="_blank">Inworld TTS</a> - Inworld 的实时文本转语音模型，支持多种语言
- <a href="https://www.zyphra.com/models/zonos2" target="_blank">ZONOS</a> - ZONOS 是 Zyphra 的语音生成模型系列，包含声音克隆与实时文本转语音版本
- <a href="https://groq.com/" target="_blank">Groq Distil Whisper</a> - GroqCloud 上托管的 Distil-Whisper 转录服务，按用量计费，每 1000 分钟音频 0.333 美元
- <a href="https://deepinfra.com/" target="_blank">DeepInfra Whisper</a> - DeepInfra 提供的 Whisper 托管转录服务，吞吐达每秒 149 秒音频
- <a href="https://fal.ai/" target="_blank">Fal.ai Wizper</a> - Fal.ai Wizper 转录服务，每秒能转录 218 秒音频
- <a href="https://fireworks.ai/" target="_blank">Fireworks Whisper</a> - 基于 Whisper 的 Fireworks 转录服务，每秒可处理 353 秒音频

<a id="section-music-models"></a>

### 音乐模型

- <a href="https://suno.com" target="_blank">Suno</a> - Suno 是 AI 音乐生成器，可根据文本提示生成多种流派、带人声的歌曲
- <a href="https://www.udio.com/" target="_blank">Udio</a> - Udio 是 AI 音乐生成器，支持延长音轨、制作重混版和提取分轨
- <a href="https://ai.google.dev/gemini/docs/audio" target="_blank">Lyria</a> - Google 推出的音乐生成模型，已与 YouTube 集成
- <a href="https://github.com/facebookresearch/audiocraft" target="_blank">MusicGen</a> - Meta 开源的音乐生成模型，属于 AudioCraft 仓库的一部分

<a id="section-spatial-models"></a>

### 三维与空间模型

- <a href="https://www.meshy.ai/" target="_blank">Meshy</a> - Meshy 支持 text-to-3D、image-to-3D 和自动 PBR 纹理生成
- <a href="https://www.tripo3d.ai/" target="_blank">Tripo</a> - Tripo 从文本和图像生成 3D 模型，适合快速原型和概念设计
- <a href="https://3d.hunyuan.tencent.com/" target="_blank">Hunyuan3D</a> - Hunyuan3D 从文本和图像生成几何结构干净、外观逼真的 3D 模型，尤其擅长角色生成
- <a href="https://spline.design/" target="_blank">Spline AI</a> - Spline AI 从文本提示生成 3D 对象，专注网页和应用设计中的交互式 3D 场景
- <a href="https://hyper3d.ai/" target="_blank">Rodin</a> - Rodin 支持从文本提示和图像生成 3D 模型，并能导出多种格式
- <a href="https://csm.ai/" target="_blank">CSM AI</a> - 文本生成 3D 模型工具；Common Sense Machines 已被 Google 收购
- <a href="https://deepimagination.cc/Magic3D/" target="_blank">Magic3D</a> - Magic3D 是高分辨率的文本到 3D 内容生成模型，面向图形与视觉技术研究
- <a href="https://www.alpha3d.io/" target="_blank">Alpha3D</a> - Alpha3D 将文本或 2D 图像转换成游戏可用的 3D 资产，并提供 Unity 开发支持

<a id="group-agents"></a>

## Agent 开发基础设施

<a id="section-agent-platforms"></a>

### Agent 框架与基础设施

- <a href="https://www.langchain.com/langgraph" target="_blank">LangGraph</a> - LangChain 团队开源的框架，把有状态、多角色的 agent 应用建模为图，支持检查点、循环和 human-in-the-loop 控制
- <a href="https://crewai.com" target="_blank">CrewAI</a> - 开源框架，用 Python 编排基于角色的多 agent 工作流，同时提供托管平台
- <a href="https://www.langchain.com/langsmith-platform" target="_blank">LangSmith</a> - LangChain 推出的 LLM agent 追踪、调试、评估与监控平台，提供成本与延迟统计、数据集管理和回归检测
- <a href="https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool" target="_blank">Anthropic Computer Use</a> - Anthropic Computer Use 是 Claude 的工具与参考实现，让 AI agent 通过 API 识别屏幕截图并控制电脑的鼠标和键盘
- <a href="https://labs.google.com/mariner/landing" target="_blank">Google Project Mariner</a> - Google DeepMind 的研究型 agent，操控 Chrome 浏览器完成多步网页任务，以早期实验形式提供
- <a href="https://www.openinterpreter.com" target="_blank">Open Interpreter</a> - Open Interpreter 是开源编码 agent，让语言模型在用户电脑上运行代码；项目由 OpenAI Codex fork 而来，专注低成本的开源权重模型
- <a href="https://langfuse.com" target="_blank">Langfuse</a> - 开源 LLM 工程平台，提供追踪、prompt 管理、评估与分析，可自托管或使用云服务；已被 ClickHouse 收购
- <a href="https://huggingface.co/docs/smolagents" target="_blank">Smolagents</a> - Hugging Face 出品的极简开源 agent 库，CodeAgent 把动作写成 Python 代码执行，可对接任意语言模型
- <a href="https://ag2.ai" target="_blank">AG2</a> - AutoGen 团队开源的多 agent 框架，用于构建和编排多个 AI agent 协同工作的系统
- <a href="https://www.camel-ai.org" target="_blank">CAMEL-AI</a> - 开源多 agent 框架，用来构建和研究 LLM 驱动的 agent 应用，涵盖角色扮演型 agent 社会和工具使用
- <a href="https://mem0.ai/" target="_blank">Mem0</a> - Mem0 是面向 AI agent 的记忆层，在向量与知识图谱混合架构上自动完成记忆的抽取、清洗和存储，提供托管平台和开源自托管两种形式
- <a href="https://www.letta.com" target="_blank">Letta</a> - Letta 是构建有状态 AI agent 的开源平台，前身叫 MemGPT，让上下文、身份和习得行为跨会话保留
- <a href="https://livekit.com/" target="_blank">LiveKit</a> - 用于构建语音、视频应用的实时通信基础设施
- <a href="https://openfga.dev" target="_blank">OpenFGA</a> - OpenFGA 是开源的细粒度授权引擎，参照 Google Zanzibar 设计，为应用和 AI agent 系统提供基于关系的访问控制
- <a href="https://composio.dev" target="_blank">Composio</a> - Composio 为 AI agent 提供集成服务，覆盖大量第三方应用的托管认证、工具执行和触发器，附带沙箱执行和框架无关的 SDK
- <a href="https://www.getzep.com/" target="_blank">Zep</a> - Zep 为 AI agent 与助手提供托管的记忆和上下文服务，时序知识图谱层由配套开源项目 Graphiti 支撑
- <a href="https://agentops.ai" target="_blank">AgentOps</a> - 专注 AI agent 可观测性的开发者平台，用 SDK 实现跨框架的会话追踪、调试、回放与成本监控
- <a href="https://www.comet.com/site/products/opik" target="_blank">Opik</a> - Comet 开源的 LLM 与 AI agent 应用追踪、评估及监控平台（Apache-2.0 许可证），覆盖开发与生产环境
- <a href="https://trigger.dev" target="_blank">Trigger.dev</a> - 开源的 TypeScript 框架和云平台，用于构建持久化后台工作流与编排 AI agent，内置重试、状态管理和可观测性
- <a href="https://hatchet.run" target="_blank">Hatchet</a> - 面向 AI agent 与后台任务的工作流编排及任务队列平台，支持持久化执行、重试、调度和并发控制；MIT 许可证，可自托管，另有托管云服务
- <a href="https://riza.io" target="_blank">Riza</a> - Riza 是沙箱运行时，通过 API 在隔离的 WebAssembly 环境中执行 AI 应用生成的不可信代码
- <a href="https://notte.cc" target="_blank">Notte</a> - Notte 是面向 AI agent 的浏览器平台，提供具有持久身份的托管云浏览器会话、登录凭证库和为语言模型优化的页面提取
- <a href="https://lavague.ai" target="_blank">LaVague</a> - LaVague 是开源的 Large Action Model 框架，用于构建 web agent，把自然语言转成基于 Selenium 或 Playwright 的浏览器自动化代码
- <a href="https://www.useparagon.com" target="_blank">Paragon</a> - Paragon 是面向 AI agent 和软件产品的集成平台，统一管理第三方应用连接，让 agent 直接调用外部工具
- <a href="https://toolhouse.ai" target="_blank">Toolhouse</a> - Toolhouse 用于构建和运行 AI agent 与常驻 AI worker，可连接数千个外部服务，并把异常升级给人工审查
- <a href="https://supermemory.ai" target="_blank">Supermemory</a> - Supermemory 是面向 AI 应用的记忆基础设施，提供基于知识图谱的持久记忆层和 API；项目以 MIT 许可开源，另有托管 API、MCP 服务器和面向最终用户的记忆应用
- <a href="https://www.cognee.ai/" target="_blank">Cognee</a> - Cognee 是开源 AI 记忆引擎，把原始数据转化为 agent 可用的持久动态记忆，结合向量搜索与知识图谱，采用 ECL（Extract, Cognify, Link）框架
- <a href="https://github.com/MemTensor/MemOS" target="_blank">MemOS</a> - 开源的 LLM agent 记忆操作系统，以 MemCube 抽象统一明文、激活值/KV-cache 与参数化三类记忆，支持记忆生命周期调度、治理与多 agent 共享
- <a href="https://langchain-ai.github.io/langmem/" target="_blank">LangMem</a> - LangMem 是 LangChain 团队为 LangGraph 打造的开源记忆工具库，提供事实抽取、整合、更新与删除，附带热路径工具和后台记忆管理器
- <a href="https://www.memobase.io/" target="_blank">Memobase</a> - Memobase 围绕用户画像构建长期记忆，管理画像、记忆事件和不断演化的上下文，适合聊天机器人、陪伴类等以用户为中心的 AI 应用
- <a href="https://github.com/NevaMind-AI/memU" target="_blank">memU</a> - 开源的 agent 记忆 sidecar，把桌面与编程 agent 的历史记录转化为可复用的 wiki 页面、记忆和技能，并提供多主机适配器
- <a href="https://github.com/EverMind-AI/EverOS" target="_blank">EverOS</a> - 可移植的本地优先记忆层，为 AI agent 提供 Markdown 原生、用户自有的存储，支持自托管
- <a href="https://mirix.io/" target="_blank">Mirix</a> - Mirix 是屏幕级多模态记忆系统，实时监控屏幕，把画面、行为和事件沉淀为个性化记忆库并降低存储需求
- <a href="https://memories.ai" target="_blank">Memories.ai</a> - Memories.ai 提供视频智能 API，把视觉数据索引成可供 AI agent 检索的记忆，底层是大型视觉记忆模型
- <a href="https://verodat.com" target="_blank">Verodat</a> - Verodat 是数据治理平台，为 AI agent、数据分析和自动化提供经过验证、带血缘追踪并补充了上下文的数据
- <a href="https://turbomcp.ai/" target="_blank">Turbo MCP</a> - Dylibso 推出的自托管 MCP 网关与管理平台，由 MCP.run 沙箱运行时演进而来
- <a href="https://promptql.io" target="_blank">PromptQL</a> - PromptQL 是 Hasura 团队开发的代理式数据访问层，让 AI agent 对已连接的数据库和 API 生成并执行查询计划
- <a href="https://anon.com" target="_blank">Anon</a> - Anon 是开发者工具包，让 AI agent 在没有官方 API 的网站上代表用户完成认证并执行操作
- <a href="https://gensx.com" target="_blank">GenSX</a> - 开源的 TypeScript 框架，将 AI agent 与多步工作流写成可组合的组件
- <a href="https://praison.ai" target="_blank">Praison AI</a> - 开源低代码框架，负责多 agent LLM 应用的构建、管理和部署
- <a href="https://agentstack.sh" target="_blank">AgentStack</a> - 开源框架和 CLI，用于快速搭建多 agent LLM 应用并集成各类工具
- <a href="https://www.swarms.ai" target="_blank">Swarms.ai</a> - 多 agent 框架兼托管平台，支持用 Python 和 Rust 构建、部署与扩展 AI agent，附带 agent 市场
- <a href="https://raygun.com" target="_blank">Raygun</a> - 面向开发团队的错误追踪、崩溃报告与应用性能监控软件
- <a href="https://metoro.io" target="_blank">Metoro</a> - 面向 Kubernetes 的 AI SRE 与可观测性平台，基于 eBPF 遥测发现生产问题并排查告警
- <a href="https://gradial.com" target="_blank">Gradial</a> - Gradial 是面向企业的平台，用 AI agent 自动完成营销活动组装、内容撰写、QA 和品牌检查
- <a href="https://www.dropzone.ai" target="_blank">Dropzone AI</a> - Dropzone AI 是面向安全运营的 agent 平台，能在 SOC 工作流中自主调查告警、开展威胁狩猎
- <a href="https://www.tinyfish.ai/" target="_blank">Tiny Fish</a> - 面向 AI agent 的网络基础设施平台，整合联网搜索、网页抽取、云端浏览器与自然语言自动化
- <a href="https://osatlas.github.io" target="_blank">OS-Atlas</a> - OS-Atlas 是开源的 GUI grounding 基础动作模型，在大规模跨平台界面元素数据集上训练，面向通用 GUI agent
- <a href="https://fireproof.storage" target="_blank">Fireproof</a> - 开源的嵌入式 JavaScript 数据库，采用可验证的账本结构，支持浏览器端存储和加密同步，常用于 agent 与本地优先应用
- <a href="https://www.bytebot.ai" target="_blank">Bytebot</a> - Bytebot 是开源的浏览器自动化 agent 框架，采用 Apache-2.0 许可，代码仓库已归档

<a id="section-agent-payments-identity"></a>

### Agent 支付与身份

- <a href="https://docs.stripe.com/agents" target="_blank">Stripe Agent SDK</a> - Stripe 工具包，让 AI agent 发起支付、管理购物车与结账流程并使用 Link 凭证，可接入 LangChain、Vercel AI SDK 等 agent 框架
- <a href="https://auth0.com" target="_blank">Auth0</a> - Web 与移动应用的认证授权平台，同时为 AI agent 提供身份与访问控制
- <a href="https://clerk.com" target="_blank">Clerk</a> - 面向开发者的认证与用户管理平台，提供可嵌入的 UI 组件和 API，支持组织（B2B）管理、会话管理与计费集成
- <a href="https://skyfire.xyz/" target="_blank">Skyfire</a> - 服务 AI 经济的金融基础设施，支持 AI agent 自主支付与身份验证
- <a href="https://paymanai.com/" target="_blank">Payman</a> - 面向银行与信用社的 AI agent 支付设施，以语音或文字执行付款、转账与账户分析，通过 SOC 2 Type II 认证
- <a href="https://nekuda.ai/" target="_blank">Nekuda</a> - 为 AI agent 打造安全合规的支付网关，支持代用户自动付款和凭证管理
- <a href="https://www.authing.com/" target="_blank">Authing</a> - 企业身份云（IDaaS），通过 SDK/API 实现统一登录、授权与多租户管理
- <a href="https://protegee.ai" target="_blank">Protegee AI</a> - 正在为 AI agent 建设支付基础设施的初创公司，公开网站目前只有登录页

<a id="section-agent-evaluation"></a>

### Agent 与模型评测

[模型与应用评测流程](https://alignify.co/zh/tools/evaluation)提供了选择基准和测试工具的背景。

- <a href="https://lmarena.ai/" target="_blank">LMArena</a> - 让用户盲测并排比较 LLM 回答并投票的平台，汇总大众投票生成模型排行榜
- <a href="https://www.braintrust.dev" target="_blank">Braintrust</a> - 对 AI agent 和 LLM 应用做评估与观测的平台，功能涵盖追踪、评估和实验
- <a href="https://galileo.ai/" target="_blank">Galileo</a> - 评估并监控 LLM 与 AI agent 应用的平台，覆盖幻觉、事实一致性（groundedness）和 agent 轨迹等指标
- <a href="https://arize.com/phoenix" target="_blank">Phoenix</a> - Arize 推出的 LLM 可观测与 agent 评估平台，包含追踪、评估数据集和实验跟踪；源码可获取，采用 Elastic License 2.0
- <a href="https://www.patronus.ai" target="_blank">Patronus AI</a> - LLM 与 AI agent 的评估测试平台，提供自动化评分基准和 agent 模拟
- <a href="https://outlier.ai/" target="_blank">Outlier.ai</a> - 供专业人士训练和评估 AI 模型的平台，在提升模型准确性的同时获得奖励
- <a href="https://www.coval.ai/" target="_blank">Coval</a> - 评估和测试语音、对话式 AI agent 的平台，提供场景模拟与端点测试
- <a href="https://www.cekura.ai/" target="_blank">Cekura</a> - 针对生产环境语音与聊天 AI agent 的测试、监控和评估平台
- <a href="https://hamming.ai/" target="_blank">Hamming</a> - 面向语音 AI agent 的测试与监控平台
- <a href="https://canonical.ai/" target="_blank">Canonical AI</a> - 面向语音 agent 的分析与评估平台

<a id="section-agent-builders"></a>

### Agent 开发平台

- <a href="https://cloud.google.com/products/gemini-enterprise-agent-platform" target="_blank">Gemini Enterprise Agent Platform</a> - Google Cloud 上构建、扩展和治理企业 AI agent 的平台，通过 Agent Registry 与 Agent Gateway 实现治理
- <a href="https://rasa.com/" target="_blank">RASA</a> - 开源的对话式 AI 平台，用于构建语音和文本助手
- <a href="https://kore.ai/" target="_blank">Kore.ai</a> - 企业级对话式 AI 平台，可端到端处理客服与员工请求，入选 Gartner 魔力象限领导者
- <a href="https://www.ada.support/" target="_blank">Ada</a> - 面向客服的对话式 AI 平台，以低代码/无代码工具搭建
- <a href="https://vapi.ai" target="_blank">Vapi</a> - 在电话系统上构建、测试和部署对话式语音 agent 的 API 平台，支持多语言和自带模型
- <a href="https://www.retellai.com" target="_blank">Retell AI</a> - 构建、部署和管理语音 AI agent 的平台，可承担客服与呼叫中心的电话对话
- <a href="https://synthflow.ai/" target="_blank">Synthflow</a> - 无代码语音 AI 平台，用于搭建和运营 AI 电话 agent，配备流程设计器、API、电话集成、模拟与通话监控
- <a href="https://boost.ai/" target="_blank">boost.ai</a> - 低代码/无代码的对话式 AI 平台，面向客服场景
- <a href="https://www.bland.ai/" target="_blank">Bland AI</a> - 用 Conversational Pathways 分支流程加护栏构建企业电话 agent 的平台，支持自带运营商、SIP 与专属基础设施；已通过 FedRAMP 认证，并完成 SOC 2 等独立合规评估
- <a href="https://www.gumloop.com" target="_blank">Gumloop</a> - 无代码搭建 AI 自动化工作流的平台，提供拖拽节点、agent 步骤和数据集成
- <a href="https://www.wordware.ai/" target="_blank">Wordware</a> - 基于浏览器的 AI 工具开发 IDE，支持自然语言编程、LLM 编排与多模态 agent 构建
- <a href="https://happyrobot.ai/" target="_blank">HappyRobot</a> - 面向物流的语音 AI agent 平台，自动处理承运商销售与在途追踪，DHL 等企业在用
- <a href="https://thoughtly.com/" target="_blank">Thoughtly</a> - 语音 agent 开发平台，主打销售触达场景
- <a href="https://syllable.ai/" target="_blank">Syllable</a> - 构建、部署和监控对话式 AI 系统的平台，覆盖语音、消息和 Web 渠道
- <a href="https://trillet.ai/" target="_blank">Trillet</a> - 用于客户互动和业务流程的 AI 语音呼叫软件

<a id="section-llm-frameworks"></a>

### LLM 与 Agent 框架

- <a href="https://www.langchain.com/" target="_blank">LangChain</a> - 用于构建 LLM 应用与 Agent 的框架，提供链式抽象和各类集成；RAG 是主要用例，Agent 编排（LangGraph）和可观测性（LangSmith）是独立产品
- <a href="https://www.llamaindex.ai" target="_blank">LlamaIndex</a> - 面向 LLM 应用的数据框架，包含 LlamaParse 文档解析器、RAG 组件与 Agent 工作流
- <a href="https://dify.ai" target="_blank">Dify</a> - 开源 LLM 应用构建平台，提供可视化工作流、RAG 管线、Agent 工具和模型集成
- <a href="https://microsoft.github.io/autogen/" target="_blank">AutoGen</a> - 微软开源的编程框架，用于构建多 Agent 对话式 AI 应用
- <a href="https://flowiseai.com/" target="_blank">Flowise</a> - 低代码 AI 工作流构建工具，用来创建 LLM 应用和自动化流程
- <a href="https://www.griptape.ai" target="_blank">Griptape</a> - 开源 Python 框架，配套云平台，用于构建、运行和治理企业 AI Agent 与工作流
- <a href="https://deepset.ai/" target="_blank">Deepset</a> - 开发 Haystack 框架的公司，Haystack 用管线组合文档存储、检索器、排序器、生成器和 Agent，支撑语义搜索、问答与 RAG 应用

<a id="group-coding"></a>

## 编程与应用开发

<a id="section-coding-tools"></a>

### 编程工具

[AI 编程工具的工作流与适用场景](https://alignify.co/zh/tools/coding)涵盖补全、编辑及更广泛的开发辅助。

- <a href="https://github.com/features/copilot" target="_blank">GitHub Copilot</a> - GitHub 的 AI 结对编程助手，跨 GitHub.com、VS Code、JetBrains 等 IDE、GitHub CLI 与 GitHub Mobile 提供代码补全和 PR 代码审查
- <a href="https://cursor.com" target="_blank">Cursor</a> - AI 代码编辑器，自动补全理解整个代码库，另带 Chat 与 Agent 模式处理软件开发任务
- <a href="https://openai.com/codex/" target="_blank">OpenAI Codex</a> - OpenAI 的编码 Agent，在云端、IDE 和终端端到端完成软件工程任务，支持多 Agent 工作流、自定义技能和代码审查自动化
- <a href="https://devin.ai" target="_blank">Devin</a> - 自主执行编码任务的 AI 软件工程师 Agent，负责规划并完成缺陷修复、重构和代码迁移等工作
- <a href="https://replit.com/" target="_blank">Replit</a> - 云端 IDE 与开发平台，支持编程、实时协作和部署，内置可按自然语言构建应用的 AI Agent
- <a href="https://devin.ai/desktop" target="_blank">Windsurf</a> - AI 代码编辑器；已并入 Cognition，产品更名 Devin Desktop
- <a href="https://antigravity.google" target="_blank">Google Antigravity</a> - Google 的 Agent 优先开发平台，把 IDE、终端和浏览器控制与基于 Gemini 的编码 Agent 组合在一起
- <a href="https://www.warp.dev" target="_blank">Warp</a> - 终端与开发环境，内置 AI 编码 Agent，支持上下文感知的提示构建与 Agent 输出审查
- <a href="https://www.trae.ai" target="_blank">TRAE</a> - 字节跳动推出的 AI 原生 IDE，把编程任务拆解成步骤逐一实现，并提供端到端完成任务的自主模式
- <a href="https://kiro.dev/" target="_blank">Kiro</a> - AWS 的代理式 IDE，主打规范驱动开发，将需求与设计转化为结构化任务，交给 AI 编码 Agent 实现
- <a href="https://www.blackbox.ai" target="_blank">Blackbox AI</a> - AI 编程助手，跨多种编程语言与 IDE 提供代码补全、对话和代码搜索
- <a href="https://www.augmentcode.com/" target="_blank">Augment Code</a> - 面向 IDE 的 AI 编码 Agent 平台，结合本地与云端智能
- <a href="https://moderne.ai/" target="_blank">Moderne</a> - 基于 OpenRewrite 的代码修复平台，以配方批量修补漏洞、升级框架，覆盖整个代码库
- <a href="https://cleric.ai/" target="_blank">Cleric</a> - Agentik 的 AI SRE Agent，自主承担值班工作：过滤误报告警、调查事故、准备修复 PR，并验证上线后的修复是否解决问题

<a id="section-app-builders"></a>

### 应用构建工具

[应用构建方式与选型](https://alignify.co/zh/tools/app-builder)有助于区分可视化应用搭建与其他开发工具。

- <a href="https://lovable.dev/" target="_blank">Lovable</a> - AI 应用构建工具，根据聊天输入生成全栈 Web 应用和原型
- <a href="https://v0.app/" target="_blank">v0</a> - Vercel 的生成式 UI 工具，按文字提示产出 React 界面与网页，支持迭代编辑和代码导出
- <a href="https://bolt.new" target="_blank">Bolt</a> - 运行在浏览器里的 AI Agent，按自然语言提示生成、编辑并部署全栈 Web 应用
- <a href="https://retool.com" target="_blank">Retool</a> - 低代码平台，用于搭建内部业务应用和工作流，可直接连接公司数据与系统
- <a href="https://stitch.withgoogle.com/" target="_blank">Google Stitch</a> - Google 的免费实验项目，按文字与图片提示生成 UI 设计和前端代码，可导出到 Figma 和 React
- <a href="https://durable.com/" target="_blank">Durable</a> - AI 建站工具，同时是面向小企业的软件平台
- <a href="https://readdy.ai/" target="_blank">Readdy</a> - AI 设计平台，产出生产级 UI 并输出代码
- <a href="https://www.trickle.so/" target="_blank">Trickle</a> - AI 应用构建平台，其 Magic Canvas 工作区负责构建与部署全栈应用和 AI Agent，并自带内置数据库
- <a href="https://www.fine.dev/" target="_blank">Fine</a> - AI 全栈开发平台，负责 SaaS 应用的生成、部署与管理

<a id="section-developer-platforms"></a>

### 开发者平台

- <a href="https://rapidapi.com/" target="_blank">Rapid API</a> - API 市场，把 API 的查找、测试、变现与管理整合在一起
- <a href="https://apilayer.com/" target="_blank">APILayer</a> - 微 API 市场，汇集面向各类开发需求的小型 API
- <a href="https://apidog.com/" target="_blank">Apidog</a> - 端到端的 API 设计与开发平台，可作为 Postman 替代，带 AI 辅助功能
- <a href="https://www.daily.co/" target="_blank">Daily</a> - 面向开发者的视频与语音基础设施平台

<a id="group-image-design"></a>

## 图像与设计

<a id="section-image-creation-editing"></a>

### 图像生成与编辑

[图像生成、编辑与增强的工作流](https://alignify.co/zh/tools/image)对应视觉创作中的不同环节。

- <a href="https://www.midjourney.com/" target="_blank">Midjourney</a> - AI 图像生成服务，按文字提示创作图像，可通过官网和 Discord 使用
- <a href="https://picsart.com" target="_blank">Picsart</a> - Picsart 是照片与视频创意编辑平台，内置 AI 图像生成和编辑工具，提供网页版和移动端应用
- <a href="https://www.facetuneapp.com/" target="_blank">Facetune</a> - 移动修图应用，主打 AI 修饰、滤镜与美颜增强
- <a href="https://remini.ai" target="_blank">Remini</a> - 照片与视频增强应用，修复老旧或低画质图像，并把素材放大到更高清晰度
- <a href="https://www.faceapp.com/" target="_blank">FaceApp</a> - 移动端人像 AI 编辑器，可改变年龄、发型与妆容
- <a href="https://www.remove.bg/" target="_blank">remove.bg</a> - 一键自动去除背景，5 秒内生成透明或纯色背景图片
- <a href="https://prisma-ai.com/" target="_blank">Prisma Labs</a> - Prisma Labs 是一家专注深度学习产品的移动技术公司
- <a href="https://www.fotor.com" target="_blank">Fotor</a> - 在线修图工具，提供 AI 增强、背景去除、批量编辑、拼贴与文生图
- <a href="https://pixlr.com/" target="_blank">Pixlr</a> - 跨平台在线 AI 图像编辑器，支持图像生成、背景去除、增强与批量编辑
- <a href="https://www.photoroom.com" target="_blank">Photoroom</a> - 面向产品摄影的 AI 修图应用，提供背景去除、AI 背景和批量编辑，用于电商商品图制作
- <a href="https://www.craiyon.com/" target="_blank">Craiyon</a> - 免费的网页版文生图工具，前身为 DALL-E mini，按提示词秒级生成照片、插画、动漫与标志
- <a href="https://clipdrop.co" target="_blank">Clipdrop</a> - AI 图像编辑工具集，涵盖背景、物体与文字去除、图像放大、重打光、文生图和外扩补图（Uncrop），通过网页端和 API 提供
- <a href="https://creator.nightcafe.studio/" target="_blank">Nightcafe Studio</a> - Nightcafe Studio 支持用多个模型生成 AI 艺术作品，并围绕公开画廊、聊天室和每日挑战形成创作者社区
- <a href="https://openart.ai/" target="_blank">OpenArt</a> - AI 艺术创作与作品发现平台，汇集社区模型与公开画廊，支持免提示词绘画和迭代
- <a href="https://www.cutout.pro/" target="_blank">Cutout.Pro</a> - AI 图像处理平台，主打背景去除、图像修复和自动设计
- <a href="https://pixa.com" target="_blank">Pixelcut</a> - AI 图像编辑应用，提供背景去除、修饰、画面扩展和超分辨率，已从 Pixelcut 更名为 Pixa，转型自然语言创意工作台
- <a href="https://prequel.app/" target="_blank">Prequel</a> - AI 美颜特效编辑器，内置数百种照片与视频滤镜及 3D 特效
- <a href="https://www.beautyplus.com/" target="_blank">BeautyPlus</a> - 自拍与视频处理工具，内置 50 多种 AI 滤镜和一键美颜
- <a href="https://airbrush.com/" target="_blank">Airbrush</a> - 移动与网页端 AI 美颜图像编辑工具，提供背景去除、美颜和滤镜
- <a href="https://www.headshotpro.com" target="_blank">HeadshotPro</a> - AI 头像生成器，把自拍变成专业商务肖像，可选多种风格与背景
- <a href="https://www.aragon.ai" target="_blank">Aragon</a> - AI 头像生成器，用自拍生成专业肖像照，无需进棚拍摄
- <a href="https://gencraft.com/" target="_blank">Gencraft</a> - AI 艺术生成器，支持多种模型，按文字提示生成图像和视频
- <a href="https://vizcom.com/" target="_blank">Vizcom</a> - 面向工业与产品设计师的 AI 渲染工具，可将草图转为照片级渲染图与 3D 模型并支持实时渲染
- <a href="https://spellbrush.com/" target="_blank">Spellbrush</a> - 专注动漫生图的 AI 工作室，代表作有 niji・journey 与 Waifu Labs
- <a href="https://www.basedlabs.ai" target="_blank">BasedLabs</a> - BasedLabs 汇集一批 AI 模型，用来生成和编辑图像、视频与音频
- <a href="https://vivago.ai/" target="_blank">Vivago AI</a> - Vivago AI 是免费 AI 创作平台，支持文生视频、图生视频和图像编辑
- <a href="https://kive.ai/" target="_blank">Kive</a> - Kive 用 AI 帮用户整理和检索视觉素材
- <a href="https://www.creati.studio/" target="_blank">Creati Studio</a> - 生成产品视频广告与 UGC 风格短片的 AI 创意平台，前身为 ZMO.ai
- <a href="https://nyx.gallery/" target="_blank">NyxAI</a> - NyxAI 出品的全合成 AI 摄影图库，覆盖食物、动物与风景，由扩散模型与 GAN 生成，可免费商用
- <a href="https://www.photalabs.com/" target="_blank">Phota Labs</a> - 人像一致性平台，约 5 张照片数分钟训练出可复用的个人形象模型，跨场景与底模保持同一身份
- <a href="https://www.gendo.ai/" target="_blank">Gendo</a> - Gendo 是面向建筑师和设计师的浏览器端 AI 渲染平台，用来生成 CGI 图像
- <a href="https://momoai.co/" target="_blank">Momo</a> - 大众 AI 写真应用，上传 8 至 12 张自拍训练专属模型，即可生成职业头像与风格写真

<a id="section-design-tools"></a>

### 设计与用户研究

[AI 辅助设计的工作流与应用场景](https://alignify.co/zh/tools/design)为本节设计工具的选择提供背景。

- <a href="https://www.canva.com/" target="_blank">Canva</a> - Canva 是在线设计平台，用来制作图形、演示文稿、视频和文档，内置 AI 生成与编辑工具
- <a href="https://www.freepik.com" target="_blank">Freepik</a> - Freepik 是素材市场兼创意套件，2024 年收购 Magnific AI，并于 2026 年更名为 Magnific
- <a href="https://www.lovart.ai/" target="_blank">Lovart AI</a> - Lovart AI 是设计 agent，在画布工作区里把从概念到图像、视频和 3D 素材的设计工作自动化
- <a href="https://uizard.io" target="_blank">Uizard</a> - Uizard 从文本、草图或截图为应用和网站生成可编辑的线框图、样机和原型
- <a href="https://www.relume.ai/" target="_blank">Relume</a> - Relume 用 AI 生成站点地图、线框图和样式指南
- <a href="https://www.visily.ai/" target="_blank">Visily</a> - Visily 面向非设计师，从截图、草图或文本提示生成可编辑的线框图和样机
- <a href="https://designs.ai" target="_blank">Designs.ai</a> - Designs.ai 是在线创意套件，从文本输入生成 logo、图像、视频、横幅和营销文案
- <a href="https://codedesign.ai/" target="_blank">CodeDesign</a> - CodeDesign 从文本提示生成完整的响应式网站，并负责托管
- <a href="https://wegic.ai/" target="_blank">Wegic</a> - Wegic 通过对话完成网站的设计与开发
- <a href="https://uxpilot.ai/" target="_blank">UX Pilot</a> - UX Pilot 用 AI 自动生成屏幕流程图和高保真 UX/UI 原型
- <a href="https://www.mymap.ai/cheat-sheet-maker" target="_blank">My Map AI</a> - My Map AI 在聊天界面中生成条理清晰的 AI 学习速查表和快速参考指南
- <a href="https://molypix.ai/" target="_blank">MolyPix</a> - MolyPix 是 AI 平面设计工具，从文本提示生成可编辑的分层图像
- <a href="https://www.voicepanel.com/" target="_blank">Voicepanel</a> - Voicepanel 用 AI 自动开展文字、语音和视频用户访谈，并分析反馈
- <a href="https://labs.google.com/pomelli/about/" target="_blank">Pomelli</a> - Pomelli 是 AI 设计工具，分析企业网站 URL 后生成与品牌相符的营销物料

<a id="section-creative-workflows"></a>

### 多模态创作

- <a href="https://simplified.com/" target="_blank">Simplified</a> - Simplified 是 AI 内容创作平台，集设计、文案、视频生成和社媒管理工具于一体
- <a href="https://textcortex.com/" target="_blank">Text Cortex AI</a> - 可嵌入任意文本框的 AI 写作助手，提供改写与摘要等工具，已转向企业级 AI 智能体平台
- <a href="https://glif.app/" target="_blank">Glif</a> - Glif 是 AI 创作平台，通过可自定义的工作流生成图像、视频、音频和文本
- <a href="https://hypotenuse.ai/" target="_blank">Hypotenuse</a> - 面向电商的 AI 写作平台，以品牌语感生成商品文案，并针对搜索引擎与电商平台优化
- <a href="https://www.contents.com/" target="_blank">Contents</a> - 企业级内容平台，整合 AI 写作、图像生成与翻译，可编排多家大模型并统一品牌口径
- <a href="https://reccloud.com/" target="_blank">RecCloud</a> - RecCloud 是 AI 音视频工具集，支持转写、配音、字幕和短视频生成

<a id="group-video-film"></a>

## 视频与影视

<a id="section-video-generation-editing"></a>

### 视频生成与编辑

[视频生成与编辑的工作流](https://alignify.co/zh/tools/video)帮助区分生成素材与处理已有素材。

- <a href="https://www.synthesia.io/" target="_blank">Synthesia</a> - Synthesia 是 AI 视频生成平台，用 AI 数字人制作支持多语言的专业视频
- <a href="https://www.heygen.com" target="_blank">HeyGen</a> - HeyGen 用照片级数字人把文本生成为视频，支持多语言翻译、配音和对口型
- <a href="https://www.descript.com/" target="_blank">Descript</a> - Descript 是 AI 视频与播客剪辑平台，提供自动转写、文本式剪辑、屏幕录制和 AI 语音克隆，像改文档一样改视频
- <a href="https://www.loom.com/" target="_blank">Loom</a> - Loom 支持一键录屏和分享，附带 AI 视频增强、文本剪辑与跨平台协作功能
- <a href="https://www.opus.pro/" target="_blank">OpusClip</a> - OpusClip 用 AI 把长录像剪成短片，自动加字幕、调整画幅、去除静音，还支持基于文本的剪辑
- <a href="https://www.veed.io" target="_blank">VEED</a> - VEED 是浏览器端视频编辑器，支持多语言自动字幕、AI 剪辑工具和团队协作
- <a href="https://invideo.io" target="_blank">invideo</a> - invideo 是在线 AI 视频创作平台，按提示词或脚本生成视频，自带素材、字幕和配音
- <a href="https://reface.ai/" target="_blank">Reface</a> - Reface 在手机和网页端提供换脸与 AI 头像生成，可替换照片和视频中的人脸并制作动画
- <a href="https://www.d-id.com/" target="_blank">D-ID</a> - D-ID 用 AI 生成数字人视频，服务营销、培训和多语言客户服务场景
- <a href="https://www.videoleapapp.com/" target="_blank">Videoleap</a> - Videoleap 是 AI 视频编辑器，带特效、无限变焦和面向社交媒体内容的模板
- <a href="https://captions.ai" target="_blank">Mirage</a> - Mirage（原 Captions）是移动端 AI 视频剪辑应用，自动完成字幕、配音、B-roll 插入和纠错，也能用 AI 数字人生成内容
- <a href="https://fliki.ai" target="_blank">Fliki</a> - Fliki 把脚本转成视频，配上 AI 配音、素材库画面和虚拟数字人
- <a href="https://www.submagic.co" target="_blank">Submagic</a> - Submagic 用来剪辑竖屏短视频，可用 AI 生成字幕和 B-roll，并发布到多个社交平台
- <a href="https://pictory.ai" target="_blank">Pictory</a> - Pictory 自动把脚本、博客文章、URL 和演示文稿剪成视频，配上 AI 配音、字幕和素材画面
- <a href="https://www.flexclip.com/" target="_blank">Flexclip</a> - Flexclip 是在线 AI 视频制作与剪辑平台，为营销、教育类视频提供拖放式模板
- <a href="https://aistudios.com/" target="_blank">DeepBrain AI</a> - DeepBrain AI 是 AI 数字人视频平台，按脚本生成由数字人主播播报的演示视频
- <a href="https://www.hedra.com/" target="_blank">Hedra</a> - Hedra 是专注角色表演的 AI 视频平台，用 Character 模型和实时数字人把图像与文本变成会说话的角色视频
- <a href="https://artlist.io" target="_blank">Artlist</a> - Artlist 以订阅方式提供正版音乐和视频素材，并附带 AI 视频、图像与配音生成工具
- <a href="https://higgsfield.ai" target="_blank">Higgsfield (platform)</a> - Higgsfield 平台生成 AI 视频和图像，围绕镜头运动提供视频生成与剪辑工具
- <a href="https://akool.com" target="_blank">Akool</a> - Akool 是 AI 视频工具套件，涵盖数字人生成、换脸、多语言视频翻译和面向营销内容的图像生成
- <a href="https://elai.io/" target="_blank">Elai</a> - Elai 是 AI 视频生成工具，把文字脚本转成多语言虚拟主持人视频
- <a href="https://www.tavus.io" target="_blank">Tavus</a> - Tavus 是面向开发者的对话式视频平台，提供 AI 视频分身，可对接人物渲染和实时感知模型
- <a href="https://creatify.ai" target="_blank">Creatify</a> - Creatify 从产品页 URL 生成广告视频，搭配 AI 数字人、脚本和批量制作工具
- <a href="https://www.arcads.ai" target="_blank">Arcads</a> - Arcads 从文字脚本生成由 AI 演员和定制数字人出演的视频广告
- <a href="https://screen.studio/" target="_blank">Screen Studio</a> - Screen Studio 是 Mac 专用录屏软件，自动平滑光标轨迹、放大重点区域并优化动态效果
- <a href="https://www.arcade.software/" target="_blank">Arcade</a> - Arcade 是无代码平台，用来搭建可交互的产品演示页面
- <a href="https://www.goenhance.ai/" target="_blank">GoEnhance</a> - GoEnhance 是 AI 视频与图像生成及风格化平台，支持角色动画和镜头构图，能把实拍视频转成动漫、3D 或像素风
- <a href="https://www.topview.ai/" target="_blank">TopView AI</a> - TopView AI 是 AI 视频编辑器，把产品链接和上传的素材做成多语言商业与社交短视频
- <a href="https://www.jogg.ai" target="_blank">JoggAI</a> - JoggAI 是 AI 视频平台，用会说话的数字人制作短视频，还能把播客音频转成视频、翻译视频并做对口型
- <a href="https://www.argil.ai/" target="_blank">Argil</a> - Argil 把文章或单个句子变成以人物或品牌为主角的 AI 视频
- <a href="https://www.vidau.ai/" target="_blank">VidAU</a> - VidAU 把产品 URL 转成短视频广告，附带 AI 数字人、去字幕和多语言配音功能
- <a href="https://www.vmeg.ai/" target="_blank">VMEG</a> - VMEG 是 AI 视频本地化平台，支持 170 多种语言的配音、翻译和对口型，也能生成短视频
- <a href="https://www.momentslab.com/" target="_blank">Moments Lab</a> - Moments Lab 是 AI 视频索引平台，自动切分素材片段，并生成剪辑成片与社交短视频
- <a href="https://www.gling.ai" target="_blank">Gling</a> - Gling 自动剪掉废镜头、静音和口头禅，还会加字幕并生成 YouTube 标题与章节
- <a href="https://capsule.video/" target="_blank">Capsule</a> - Capsule 是 AI 视频编辑器，支持套用模板、保持品牌一致，并可一键生成 B-roll
- <a href="https://www.rephraseai.com/" target="_blank">Rephrase.ai</a> - 以真人数字分身生成个性化营销视频的平台，2023 年 11 月被 Adobe 收购，团队并入其生成式视频业务
- <a href="https://www.revid.ai" target="_blank">revid.ai</a> - revid.ai 是 AI 视频生成工具，从提示词或脚本生成面向 TikTok、Instagram 和 YouTube 的短视频
- <a href="https://rotorvideos.com/" target="_blank">Rotor Videos</a> - Rotor Videos 是面向音乐人的 AI 剪辑平台，专注生成音乐视频
- <a href="https://autoshorts.ai/" target="_blank">AutoShorts AI</a> - AutoShorts AI 一键生成无人出镜短视频并自动发布，专为 TikTok 和 YouTube Shorts 设计
- <a href="https://async.com" target="_blank">Async</a> - Async 通过对话完成视频剪辑，能切素材、清理音频、添加字幕，还可按提示生成语音和音乐
- <a href="https://cursorful.com/" target="_blank">Cursorful</a> - Cursorful 是浏览器录制插件，录演示视频时自动放大光标焦点区域

<a id="section-filmmaking-localization"></a>

### 影视制作与本地化

本节的影视制作部分可结合[AI 辅助影视创作与后期工作流](https://alignify.co/zh/tools/filmmaking)理解。

- <a href="https://www.dramaboxdb.com/" target="_blank">DramaBox</a> - DramaBox 是短剧应用，原创剧集达数千小时，支持免费观看、按集付费和广告解锁
- <a href="https://ltx.io/studio" target="_blank">LTX Studio</a> - LTX Studio 是 Lightricks 的 AI 电影制作平台，在单一项目工作区内完成剧本开发、分镜、镜头规划、生成与剪辑
- <a href="https://www.rask.ai" target="_blank">Rask</a> - Rask 做 AI 视频和音频本地化，支持 130 多种语言的自动翻译和字幕
- <a href="https://www.autodesk.com/products/flow-studio/overview" target="_blank">Autodesk Flow Studio</a> - Autodesk Flow Studio（原 Wonder Dynamics 的 Wonder Studio）把 CG 角色动画化并合成到实拍画面，还能生成 3D 资产，现已归属 Autodesk
- <a href="https://www.rws.com/localization/services/translation-services/video-and-audio-translation/ai-dubbing-and-vo/" target="_blank">Papercup</a> - 端到端 AI 配音与视频本地化平台，配人工质检，2025 年被 RWS 收购
- <a href="https://videotranslator.blipcut.com/" target="_blank">Blipcut</a> - Blipcut 是免费批量 AI 视频翻译工具，集成配音、字幕和口型同步
- <a href="https://www.skyreels.ai" target="_blank">SkyReels</a> - SkyReels 从文本、图像和角色参考生成电影感视频，用于短剧和叙事内容
- <a href="https://www.neuralframes.com/" target="_blank">NeuralFrames</a> - NeuralFrames 是 AI 视频生成平台，供音乐人创作音乐视频，官方称已生成超过 200 万条视频
- <a href="https://www.goodshort.com/" target="_blank">GoodShort</a> - GoodShort 做出海短剧，结合英美剧本剧、翻译剧集与高频短视频内容
- <a href="https://mydramawave.com/" target="_blank">DramaWave</a> - DramaWave 聚合竖屏短剧，支持高清播放，覆盖多种题材和语言
- <a href="https://netshort.com/" target="_blank">NetShort</a> - NetShort 专做 1 分钟竖屏短剧，提供高清流媒体播放
- <a href="https://www.melolo.org" target="_blank">Melolo</a> - Melolo 面向东南亚市场，免费提供本地化高清短剧并自动配上字幕
- <a href="https://wavel.ai/" target="_blank">Wavel</a> - Wavel 是 AI 语音平台，提供自然语音克隆、多语言配音和视频剪辑
- <a href="https://www.sereal.com/" target="_blank">Sereal+</a> - Sereal+ 是免费短剧平台，收录多国迷你剧，用 AI 做个性化推荐
- <a href="https://www.unireel.tv/" target="_blank">UniReel</a> - UniReel 是短剧平台，独家剧集覆盖多种类型，全球均可观看
- <a href="https://storeel.com/" target="_blank">StoReel</a> - StoReel 是专注 1-2 分钟短剧的手机应用，片库收韩剧和华语剧，支持按集付费或看广告解锁
- <a href="https://free-reels.com/" target="_blank">FreeReels</a> - FreeReels 是完全免费的短剧平台，更新频繁并内置智能推荐
- <a href="https://flickreels.net/" target="_blank">FlickReels</a> - FlickReels 汇集悬疑、奇幻等微短剧，全天候都能观看
- <a href="https://hei.io/" target="_blank">HeiTech (Hei.io)</a> - HeiTech（Hei.io）是 AI 配音公司，为视频和音频提供字幕、翻译、人声与音效服务
- <a href="https://www.solotwinstudios.com/" target="_blank">SOLO</a> - SOLO 是 AI 影视制作公司，用 AI 制作短片和广告
- <a href="https://www.utopaistudios.com/" target="_blank">Utopia Studios</a> - 人类执导、AI 加持的影视工作室，自研 PAI 制作引擎辅助创意团队开发多部影视剧集
- <a href="https://escape.ai/" target="_blank">Escape</a> - Escape 是 AI 艺术聚合平台，展示并推广新形态的数字娱乐
- <a href="https://fsh.org/" target="_blank">FSH Technologies</a> - 面向城市与公共机构的政务技术公司，由 Contenda AI 内容平台转型而来

<a id="group-voice-audio"></a>

## 语音与音频

<a id="section-speech-applications"></a>

### 语音与转写应用

语音应用包括[语音识别与转写](https://alignify.co/zh/tools/speech-to-text)，也包括[文本转语音合成](https://alignify.co/zh/tools/text-to-speech)。

- <a href="https://elevenlabs.io" target="_blank">ElevenLabs</a> - ElevenLabs 是语音 AI 平台，提供文字转语音、声音克隆、配音和音频生成，并附带 API 与多语言大型语音库
- <a href="https://aws.amazon.com/polly/" target="_blank">Amazon Polly</a> - AWS 托管文字转语音 API，上百种语音覆盖四十多种语言，支持 SSML 定制与生成式语音
- <a href="https://openai.com/index/advancing-voice-intelligence-with-new-models-in-the-api/" target="_blank">OpenAI TTS</a> - OpenAI TTS 是 OpenAI 的文字转语音 API 模型，用于在应用和语音管线中合成语音
- <a href="https://cloud.google.com/text-to-speech" target="_blank">Google Cloud TTS</a> - Google Cloud TTS 是 Google Cloud 上的云端文字转语音 API 服务
- <a href="https://azure.microsoft.com/en-us/products/ai-services/ai-speech" target="_blank">Azure Speech</a> - Azure Speech 是微软 Azure 的云端语音服务，同时覆盖语音合成（TTS）与语音识别（ASR）
- <a href="https://speechify.com" target="_blank">Speechify</a> - 把文档与网页转成语音朗读的应用，支持 60 多种语言与拍照 OCR，覆盖桌面、移动与浏览器
- <a href="https://krisp.ai/" target="_blank">Krisp</a> - Krisp 提供 AI 降噪与口音转换技术，以 macOS 和 Windows 桌面应用的形式作为虚拟麦克风和扬声器，接入现有会议与呼叫中心工具
- <a href="https://www.voicemod.net/" target="_blank">Voicemod</a> - Voicemod 是实时 AI 变声与音效板应用，用于游戏、直播和聊天软件
- <a href="https://murf.ai" target="_blank">Murf.ai</a> - Murf.ai 是 AI 文字转语音平台，提供配音生成、译制配音和 TTS API，语音库覆盖 35 种以上语言、200 多个声音
- <a href="https://www.resemble.ai/" target="_blank">Resemble AI</a> - Resemble AI 是企业级语音 AI 平台，提供声音克隆与 TTS API，支持本地部署、不可感知音频水印和深度伪造检测
- <a href="https://www.wellsaid.io/" target="_blank">Wellsaid</a> - Wellsaid 面向企业，通过 API 提供 120 多个拟人配音声音，支持团队协作
- <a href="https://www.rev.ai/" target="_blank">Rev AI</a> - Rev AI 是语音转文字转录服务，为音频和视频内容提供实时和批量 ASR API
- <a href="https://www.dialpad.com/" target="_blank">Dialpad</a> - Dialpad 是 AI 驱动的云通信平台，整合通话、消息、会议、实时摘要与洞察
- <a href="https://wisprflow.ai/" target="_blank">Wispr Flow</a> - Wispr Flow 是 AI 语音听写工具，在任何桌面应用中把语音转成排好版的文字
- <a href="https://www.plaud.ai/" target="_blank">PLAUD</a> - PLAUD 是 AI 录音与总结工具，自动转录多语言对话并生成要点与行动项
- <a href="https://superwhisper.com/" target="_blank">Superwhisper</a> - Superwhisper 是语音听写应用，把说话转成带格式的文字，桌面和移动应用都能用
- <a href="https://turboscribe.ai/" target="_blank">TurboScribe</a> - TurboScribe 提供不限量的 AI 音频转录服务，支持 98 种语言，可批量处理长录音
- <a href="https://poly.ai/en" target="_blank">PolyAI</a> - PolyAI 专注为企业客户提供语音助手解决方案
- <a href="https://www.delphi.co/" target="_blank">Delphi</a> - Delphi 是为专家和创作者创建数字分身（「Digital Minds」）的平台
- <a href="https://voice.ai/" target="_blank">Voice.ai</a> - 兼具实时变声、多语言语音合成与短样本克隆的语音 AI 平台，以 API 提供
- <a href="https://dubbingai.io" target="_blank">Dubbing AI</a> - Dubbing AI 是实时 AI 变声工具，自带 AI 声音库和玩梗音效板，覆盖游戏、直播和会议场景
- <a href="https://elevenreader.io/" target="_blank">ElevenReader by ElevenLabs</a> - ElevenReader 由 ElevenLabs 出品，用 AI 语音朗读文章、PDF 和电子书
- <a href="https://www.openai.fm/" target="_blank">OpenAI.fm</a> - OpenAI.fm 是交互式演示平台，用来体验 OpenAI 的文本转语音 API
- <a href="https://research.google/blog/real-time-speech-to-speech-translation/" target="_blank">Google Real-time S2ST</a> - Google Real-time S2ST 是端到端语音到语音翻译模型，用原说话人的声音实时翻译，延迟仅 2 秒，可在 Google Meet 和 Pixel 10 设备上使用
- <a href="https://goodcall.ai/" target="_blank">Goodcall</a> - Goodcall 为企业提供 AI 电话接听，包含来电处理与预约安排
- <a href="https://wave.co/" target="_blank">Wave AI</a> - Wave AI 是会议录音助手，自动完成多语言转录并生成摘要
- <a href="https://www.clipto.com/" target="_blank">Clipto.AI</a> - Clipto.AI 是本地运行的 AI 媒体助手，自动转录音视频，并提供字幕、编辑和下载工具
- <a href="https://willowvoice.com/" target="_blank">Willow Voice</a> - 按住快捷键即可向任意应用听写的语音输入工具，支持离线与上百种语言，覆盖三大桌面移动端
- <a href="https://autio.com/" target="_blank">Autio</a> - 自驾游 GPS 语音导览应用，自动播放两万五千多条位置故事，Kevin Costner 联合创立

<a id="section-music-podcasts"></a>

### 音乐、音频与播客

本节的音乐创作部分可结合[AI 音乐生成的方式与工作流](https://alignify.co/zh/tools/music-generator)理解。

- <a href="https://www.flowmusic.app/" target="_blank">Google Flow Music</a> - Google Flow Music 是 Google 推出的对话式 AI 音乐创作工具，基于 Lyria 系列模型生成带人声的完整歌曲。它接替了被收购的 Producer.ai 工作室
- <a href="https://music.ai/" target="_blank">Music</a> - 音频智能平台，旗下 Moises 面向音乐人创作，企业 API 日处理音频超两百万分钟
- <a href="https://libsyn.com/" target="_blank">Libsyn</a> - Libsyn 是最早的播客托管服务之一，支持音频/视频上传、定时发布、统计、分发和变现工具
- <a href="https://www.podbean.com/" target="_blank">Podbean</a> - Podbean 集播客录制、发布、分发与变现于一体，并提供音频/视频托管与直播能力
- <a href="https://acestudio.ai" target="_blank">ACE Studio</a> - ACE Studio 是桌面端 AI 音乐制作工作站，提供 AI 人声与乐器生成、声音克隆、生成式套件和分轨分离
- <a href="https://soundraw.io" target="_blank">Soundraw</a> - Soundraw 为创作者生成可定制的免版税曲目，并附带商业授权
- <a href="https://www.aiva.ai" target="_blank">AIVA</a> - AIVA 是 AI 作曲助手，可创作 250 多种风格的歌曲，生成的音乐可编辑、可授权
- <a href="https://boomy.com/" target="_blank">Boomy</a> - Boomy 是 AI 音乐创作平台，用来生成原创歌曲
- <a href="https://mubert.com" target="_blank">Mubert</a> - Mubert 通过网页生成器、开发者 API 和艺术家工作室，为视频、播客和应用生成免版税配乐
- <a href="https://endel.io/" target="_blank">Endel</a> - Endel 根据用户的活动与所处情境生成个性化声音环境
- <a href="https://soundful.com" target="_blank">Soundful</a> - Soundful 生成覆盖多种曲风的免版税原创曲目，可用于视频、播客和品牌用途
- <a href="https://www.beatoven.ai" target="_blank">Beatoven.ai</a> - Beatoven.ai 生成面向视频、播客和游戏的免版税音乐与音效，曲目支持再编辑
- <a href="https://musicfy.lol" target="_blank">Musicfy</a> - Musicfy 用 AI 人声生成翻唱与原创歌曲，支持声音克隆、文生音乐和恶搞音色
- <a href="https://www.loudly.com" target="_blank">Loudly</a> - Loudly 从文字提示生成免版税曲目，支持分轨定制并可分发到流媒体服务
- <a href="https://www.simplecast.com/" target="_blank">Simplecast</a> - Simplecast 是企业级播客托管与分发平台，提供深度统计、自定义网站和广告插播控制
- <a href="https://rss.com/" target="_blank">RSS.com</a> - RSS.com 是播客托管服务，提供无限存储、跨平台统计与动态广告
- <a href="https://fireside.fm/" target="_blank">Fireside</a> - Fireside 是播客托管平台，提供响应式网站、定时发布、可嵌入播放器和数据统计，支持自定义域名并可以从其他平台一键导入
- <a href="https://www.snipd.com" target="_blank">Snipd</a> - Snipd 是 AI 播客播放器，自动转录单集，听众可保存高光片段、与单集对话并导出笔记
- <a href="https://w.ai/" target="_blank">W.AI</a> - 汇聚全球闲置 GPU 的去中心化 AI 算力网络，由 WOMBO 转型而来
- <a href="https://altered.ai/" target="_blank">Altered</a> - Altered（Altered Studio）提供专业级 AI 变声软件与服务，面向媒体和后期制作中的声音表演
- <a href="https://musi-co.com/" target="_blank">Musico</a> - Musico 是生成式音乐引擎，产出可自适应的免版税配乐
- <a href="https://aimi.fm/" target="_blank">AiMi</a> - 浏览器端 AI 音乐工作室，把提示词变成可编辑的多轨工程，免费使用，AI 操作按积分计费
- <a href="https://podwise.ai" target="_blank">Podwise</a> - Podwise 是播客学习应用，转录单集并生成结构化摘要、思维导图和笔记
- <a href="https://www.wondera.ai/" target="_blank">Wondera</a> - iOS 与 Android 上的 AI 音乐共创应用，可从灵感做成成品歌曲，输出内容完整授权
- <a href="https://mozartai.app/" target="_blank">Mozartai</a> - AI 写歌应用，把照片、灵感或歌词在一分钟内变成带人声的完整歌曲，支持声音克隆
- <a href="https://tunee.ai" target="_blank">Tunee</a> - Tunee 是 AI 音乐创作平台，可从文字、图片、音频或视频生成歌曲，内置母带处理、Remix、分轨分离与音乐视频工具
- <a href="https://agent.mix.audio/" target="_blank">Mix Audio Agent</a> - Mix Audio Agent 是一套 AI 音乐工具集，覆盖配乐、Remix、分轨分离和音乐分析
- <a href="https://www.midiagent.com/" target="_blank">MIDI Agent</a> - MIDI Agent 是 VST 与 AU 插件，借助自然语言与主流 AI 模型（ChatGPT、Claude、Gemini、Grok）生成和转录 MIDI
- <a href="https://www.rct.ai/" target="_blank">RCT Studio</a> - 创意 AI 工作室，其 Morpheus 引擎将剧本拆成分支叙事并以 3D 与 VR 呈现，团队出自百度渡鸦，入选 YC W19
- <a href="https://www.you-ai.nl/" target="_blank">YouAI</a> - 阿姆斯特丹工作室，用 GAN 让历史画像与老照片开口说话，为博物馆与品牌定制会说话的肖像

<a id="group-search-web-data"></a>

## 搜索与网页数据

<a id="section-search-retrieval"></a>

### 搜索与检索

- <a href="https://www.algolia.com/" target="_blank">Algolia</a> - Algolia 为企业和开发者提供即时站内搜索与内容发现 API 服务
- <a href="https://www.glean.com/" target="_blank">Glean</a> - Glean 是企业 AI 助手与工作搜索平台，接入公司各类工具后即可回答问题并运行 agent
- <a href="https://jina.ai/" target="_blank">Jina AI</a> - Jina AI 已于 2025 年 10 月被 Elastic 收购，现提供面向多模态与多语言 Embedding、重排序、检索和 RAG 的 AI 搜索模型与 API 产品线
- <a href="https://www.meilisearch.com" target="_blank">Meilisearch</a> - Meilisearch 是通过 REST API 使用的搜索引擎，速度快、能容忍拼写错误，既可开源自部署，也提供托管云服务
- <a href="https://www.commonroom.io/" target="_blank">Common Room</a> - Common Room 是 GTM 情报平台，将产品使用、社区、CRM 与营销信号统一成以人为粒度的买家视图，并提供联系人补全与 AI 潜客挖掘、评分
- <a href="https://juicebox.ai" target="_blank">Juicebox</a> - Juicebox 是 AI 招聘平台，内置的 PeopleGPT 搜索用自然语言检索庞大的全球档案库，另配招聘 CRM 和负责寻访与外联的 AI agent
- <a href="https://harmonic.ai" target="_blank">Harmonic</a> - Harmonic 是面向投资人的初创公司情报数据库，结合自有数据采集与 AI，梳理非上市公司、融资与人物信息
- <a href="http://www.zeta-alpha.com/" target="_blank">Zeta Alpha</a> - Zeta Alpha 是面向企业的神经搜索平台，用于知识的发现与共享
- <a href="https://amber.de/" target="_blank">Amber</a> - 整合企业搜索、对话与智能体的商业 AI 平台，前身为 AmberSearch
- <a href="https://www.openvc.app" target="_blank">OpenVC</a> - OpenVC 是免费平台，帮初创公司创始人对接庞大的投资人数据库，并提供路演 Deck 分享、CRM 和自动跟进功能
- <a href="https://lessie.ai/" target="_blank">Lessie AI</a> - Lessie AI 是 agentic 人物搜索引擎，输入一段自然语言描述，就能在 LinkedIn、X、GitHub 等来源的档案里找到影响者、销售线索、投资人和人才
- <a href="https://www.clado.ai" target="_blank">Clado</a> - Clado 是面向招聘与销售团队的 AI 人物搜索和档案补全平台，由 agent 在大规模公开档案库中开展深度调研，按自然语言条件匹配人选

<a id="section-web-data-browsers"></a>

### 网页数据与浏览器

[网页抓取与数据提取](https://alignify.co/zh/tools/web-scraping)和[AI 辅助浏览](https://alignify.co/zh/tools/browser)是本节中两种不同的工作流。

- <a href="https://brightdata.com/" target="_blank">Bright Data</a> - Bright Data 是大规模代理与网页采集平台，直接提供结构化数据与 API
- <a href="https://oxylabs.io" target="_blank">Oxylabs</a> - Oxylabs 是网页数据提取平台，提供代理、抓取 API 与网页搜索 API，可用于 AI agent 和数据采集
- <a href="https://www.perplexity.ai/comet" target="_blank">Perplexity Comet</a> - Perplexity Comet 是 Perplexity 推出的 AI 浏览器，助手能替用户执行 agentic 浏览任务
- <a href="https://www.diabrowser.com" target="_blank">Dia Browser</a> - Dia 浏览器出自 The Browser Company，内置写作辅助，聊天助手会从用户的浏览行为中学习
- <a href="https://www.firecrawl.dev" target="_blank">Firecrawl</a> - Firecrawl 提供 API 与开源工具包，抓取网站并把页面转换成 Markdown、JSON 等干净格式，供 LLM 使用
- <a href="https://browser-use.com" target="_blank">Browser-Use</a> - Browser-Use 为运行 AI 浏览器 agent 提供云 API 与基础设施，配套基于 Playwright 的开源 Python 库，支持数据提取、网页任务自动化与测试
- <a href="https://apify.com" target="_blank">Apify</a> - Apify 是网页抓取与浏览器自动化平台，运行名为 Actor 的无服务器程序，内置代理与存储，并支持 AI agent 集成
- <a href="https://www.browserbase.com" target="_blank">Browserbase</a> - Browserbase 提供云端无头浏览器会话基础设施，供 AI agent 和网页自动化使用，附带 Fetch 与 Search API、无服务器 Functions 和可观测性工具
- <a href="https://www.browserless.io/" target="_blank">Browserless</a> - Browserless 把无头浏览器做成服务，支持 Docker 部署，自带反爬能力、REST API 和 BrowserQL 查询语言，用于页面自动化与抓取
- <a href="https://www.scrapingbee.com/" target="_blank">ScrapingBee</a> - ScrapingBee 提供网页抓取 REST API，绕过反爬虫限制提取网页数据
- <a href="https://www.scraperapi.com/" target="_blank">ScraperAPI</a> - ScraperAPI 是托管式抓取 API，自动处理代理、CAPTCHA 和 IP 封锁
- <a href="https://www.browse.ai/" target="_blank">Browse.ai</a> - Browse.ai 是无代码平台，通过配置机器人来抓取和监控网站数据
- <a href="https://lightpanda.io" target="_blank">Lightpanda</a> - Lightpanda 是用 Zig 写的开源无头浏览器，兼容 Puppeteer 和 Playwright，面向网页自动化、抓取与 AI agent，另提供云服务
- <a href="https://strawberrybrowser.com" target="_blank">Strawberry</a> - Strawberry 是内置 AI 助手的桌面浏览器，能跨标签页自动完成任务（包括登录后的操作），并基于网页内容生成文档

<a id="section-search-applications"></a>

### AI 搜索应用

[面向用户的 AI 搜索应用](https://alignify.co/zh/tools/search-engine)结合检索、回答与探索。

- <a href="https://www.perplexity.ai" target="_blank">Perplexity</a> - Perplexity 是 AI 答案引擎，依托自建网页索引（由 PerplexityBot 爬虫抓取）生成带来源的回答
- <a href="https://brave.com/search/" target="_blank">Brave Search</a> - Brave Search 是独立且注重隐私的搜索引擎，自建网页索引，不追踪用户
- <a href="https://www.phind.com/" target="_blank">Phind</a> - Phind 为开发者打造，用 AI 搜索返回可视化、可交互且引用清晰的代码与技术答案
- <a href="https://consensus.app" target="_blank">Consensus</a> - Consensus 是学术研究 AI 搜索引擎，从数百万篇同行评审论文中提取并归纳研究结论，回答科研问题
- <a href="https://iask.ai/" target="_blank">iAsk</a> - iAsk 是 AI 问答搜索引擎，用自然语言提问即可即时获得答案
- <a href="https://andisearch.com/" target="_blank">Andi</a> - Andi 用自然语言对话的方式搜索，用于推荐与知识发现
- <a href="https://komo.ai/" target="_blank">Komo</a> - Komo 是无广告的生成式 AI 搜索平台，支持对话式搜索与社区驱动的发现
- <a href="https://yep.com/" target="_blank">Yep</a> - Yep 是注重隐私的搜索引擎，会把大部分广告收入返还给创作者

<a id="section-search-api-services"></a>

### 搜索 API

[面向应用的网页搜索 API](https://alignify.co/zh/tools/web-search-api)提供程序化检索，而非面向用户的搜索界面。

- <a href="https://exa.ai" target="_blank">Exa</a> - Exa 是面向 AI 应用的搜索 API 服务，提供网页搜索、抓取与内容提取，为 LLM 和 agent 返回结构化结果
- <a href="https://tavily.com" target="_blank">Tavily</a> - Tavily 为 AI agent 和 RAG 流水线而建，把网页搜索、内容提取与抓取合并在一个搜索 API 里
- <a href="https://serpapi.com" target="_blank">SerpApi</a> - SerpApi 抓取 Google 等搜索引擎的结果，返回结构化数据，代理、验证码和解析都由它处理
- <a href="https://you.com" target="_blank">You.com</a> - You.com 现为 LLM 和企业应用提供网页搜索 API，此前曾做消费级 AI 搜索引擎
- <a href="https://serper.dev" target="_blank">Serper</a> - Serper 是搜索 API 服务，为应用和 AI agent 返回结构化的 Google 搜索结果
- <a href="https://bochaai.com/" target="_blank">博查 (Bocha)</a> - 博查（Bocha）是面向 AI 应用的多模态搜索引擎，以知识检索 API 形式提供给 agent 使用
- <a href="https://parallel.ai" target="_blank">Parallel AI</a> - Parallel AI 面向 AI agent 提供网页搜索 API，返回带证据的长篇内容供 LLM 使用，并支持异步深度研究任务和 MCP
- <a href="https://s1.dev/" target="_blank">Search1 API</a> - Search1 API 为 AI agent 提供网页访问基础设施，经由 REST、MCP 和 CLI 交付多引擎网页与新闻搜索、agentic 搜索、抓取及 sitemap API

<a id="group-data-cloud"></a>

## 数据与云基础设施

<a id="section-cloud-infrastructure"></a>

### 云与模型基础设施

- <a href="https://ai.azure.com/" target="_blank">Azure AI Foundry</a> - 企业 AI 平台，通过 API 调用多种 AI 模型，并配备构建和部署 agent 的工具
- <a href="https://cloud.google.com/vertex-ai" target="_blank">Vertex AI</a> - Google Cloud 的机器学习平台，提供模型训练与 MLOps 工具，并通过统一 API 托管调用 Gemini 模型
- <a href="https://build.nvidia.com/" target="_blank">NVIDIA NIM</a> - 基于微服务的 GPU 加速推理平台，支持自托管或在云端部署 AI 模型
- <a href="https://developers.cloudflare.com/workers-ai/" target="_blank">Cloudflare Workers AI</a> - 在 Cloudflare 边缘网络上运行模型的无服务器 GPU 推理服务，内置向量存储与 API 访问
- <a href="https://supabase.com/" target="_blank">Supabase</a> - 开源后端平台，提供托管 PostgreSQL、认证、即时 API、边缘函数、实时订阅、存储与向量嵌入
- <a href="https://www.coreweave.com/" target="_blank">CoreWeave</a> - CoreWeave 是面向 AI 负载的 GPU 云平台，提供 NVIDIA GPU 基础设施
- <a href="https://groq.com" target="_blank">Groq</a> - 在自研 LPU 处理器上运行开源模型的推理云，提供低延迟的语言与语音模型 API
- <a href="https://replicate.com" target="_blank">Replicate</a> - 通过 API 运行、微调开源 AI 模型的云平台，也支持部署自定义模型
- <a href="https://fal.ai/" target="_blank">fal.ai</a> - fal.ai 是开发者平台，用 API 调用生成式图像、视频与音频模型，并提供无服务器 GPU 推理与微调
- <a href="https://lambda.ai/" target="_blank">Lambda</a> - Lambda 是服务 AI 训练与推理的云 GPU 平台，提供 H100/H200/B200 多 GPU 实例
- <a href="https://www.runpod.io/" target="_blank">RunPod</a> - RunPod 是全球分布的 GPU 云，可即时部署 Llama 等模型用于训练和推理
- <a href="https://vast.ai/" target="_blank">Vast.ai</a> - Vast.ai 是 GPU 租赁平台，用来搜索、比较各家 GPU 资源
- <a href="https://temporal.io/" target="_blank">Temporal</a> - 持久化执行平台，故障时保留工作流状态、恢复崩溃进程，并为 LangGraph、OpenAI Agents SDK 等 agent 框架提供官方 SDK 集成
- <a href="https://www.netlify.com" target="_blank">Netlify</a> - Netlify 是 Web 开发平台，从 git 仓库部署网站和应用，自带全球 CDN、无服务器函数、部署预览和 AI 辅助功能
- <a href="https://render.com" target="_blank">Render</a> - 从 Git 直接部署 Web 服务、API、worker 与数据库的云平台，兼作 AI 应用的基础设施
- <a href="https://railway.com" target="_blank">Railway</a> - 按用量计费的云平台，可部署应用、服务器与数据库，也被用作 AI agent 的托管基础设施
- <a href="https://fly.io" target="_blank">Fly.io</a> - 面向全球多个区域部署容器化应用与数据库的云托管平台，也常用来托管 AI agent
- <a href="https://www.anyscale.com/" target="_blank">Anyscale</a> - 基于 Ray 构建的 AI 平台，用来开发、运行和扩展大规模 AI 工作负载，覆盖模型训练与推理
- <a href="https://e2b.dev/" target="_blank">E2B</a> - E2B 是开源沙箱，以托管 API 在隔离的云 microVM 中执行 AI 生成的代码，支持暂停、恢复和快照
- <a href="https://arize.com/" target="_blank">Arize AI</a> - Arize AI 是机器学习可观测性平台，用来监控、调试和改进 ML 模型
- <a href="https://codesandbox.io" target="_blank">CodeSandbox</a> - CodeSandbox 是云开发平台，提供秒级启动的 microVM 沙箱，用于 AI agent 代码执行、开发环境、CI 流水线和交互式 playground
- <a href="https://metronome.com/" target="_blank">Metronome</a> - Metronome 是用量计费平台，自动化计费模型，支持实时调价
- <a href="https://www.daytona.io" target="_blank">Daytona</a> - Daytona 是开源基础设施运行时，为执行 AI 生成代码和 agent 工作流快速开通沙箱环境
- <a href="https://www.inngest.com/" target="_blank">Inngest</a> - Inngest 是 durable functions 平台，用于执行 AI 工作流与后台任务，内置状态管理
- <a href="https://webcontainers.io" target="_blank">WebContainers</a> - WebContainers 是 StackBlitz 推出的浏览器运行时，可直接在浏览器中本地运行 Node.js 环境，用于浏览器 IDE 与沙箱化的 agent 执行
- <a href="https://scrapybara.com" target="_blank">Scrapybara</a> - Scrapybara 为 AI agent 即时开通云端桌面环境，让 agent 远程操作浏览器与计算机
- <a href="https://novita.ai" target="_blank">Novita AI</a> - 通过 API 调用大量 AI 模型的云平台，同时提供面向训练与推理的弹性 GPU 算力
- <a href="https://upsun.com/" target="_blank">Upsun</a> - 构建、部署与扩展多语言 Web 应用的云 PaaS 平台，由 Platform.sh 更名而来
- <a href="https://www.gmicloud.ai/" target="_blank">GMI Cloud</a> - GMI Cloud 是全球化 AI 云平台，提供 GPU 实例、集群和高吞吐推理 API
- <a href="https://www.hyperstack.cloud/" target="_blank">Hyperstack</a> - Hyperstack 是欧洲的绿色 GPU 云，为训练与推理提供 NVIDIA 基础设施
- <a href="https://www.e2enetworks.com/" target="_blank">E2E Networks</a> - E2E Networks 是印度的云 GPU 平台，按需提供 H100/H200 GPU，支撑 AI/ML 负载
- <a href="https://verda.com/" target="_blank">Verda (formerly DataCrunch)</a> - Verda 是欧洲 GPU 云，提供按需集群与无服务器推理，支持 NVIDIA B/H 系列 GPU；前身为 DataCrunch，2025 年 11 月更名
- <a href="https://jarvislabs.ai/" target="_blank">Jarvis Labs</a> - Jarvis Labs 是 GPU 云平台，一键即可创建预置深度学习框架的环境
- <a href="https://www.leadergpu.it/" target="_blank">LeaderGPU</a> - LeaderGPU 提供 GPU 服务器租用，专注深度学习负载，涵盖训练与图像处理
- <a href="https://irendering.net/" target="_blank">iRender</a> - iRender 是面向创作者的 GPU 渲染云，为 Blender、Unreal 等软件提供渲染加速

<a id="section-data-platforms"></a>

### 数据平台与分析

- <a href="https://www.mongodb.com" target="_blank">MongoDB</a> - 文档型 NoSQL 数据库，提供托管云服务 Atlas，广泛用于应用数据存储
- <a href="https://www.elastic.co/" target="_blank">Elastic</a> - 开源搜索与分析引擎，支持全文检索、日志与指标分析
- <a href="https://duckdb.org/" target="_blank">DuckDB</a> - 轻量级嵌入式列式 OLAP 数据库，用于复杂 SQL 分析
- <a href="https://scale.com/" target="_blank">Scale</a> - 为 AI 实验室、企业与政府提供数据标注、数据整理与模型评估服务的平台
- <a href="https://neo4j.com" target="_blank">Neo4j</a> - 以节点和关系存储数据的图数据库，附带 Cypher 查询语言与图数据科学工具
- <a href="https://www.pinecone.io/" target="_blank">Pinecone</a> - 全托管无服务器向量数据库服务，提供语义搜索与推荐查询 API，不支持自托管
- <a href="https://www.thoughtspot.com/" target="_blank">ThoughtSpot</a> - AI 分析工具，可用自然语言直接查询企业数据
- <a href="https://www.starrocks.io/" target="_blank">StarRocks</a> - 支持实时分析与数据湖查询的分布式 OLAP 数据仓库
- <a href="https://doris.apache.org/" target="_blank">Doris</a> - 开源实时分析数据库，为高并发与点查场景打造
- <a href="https://tdengine.com/" target="_blank">TDengine</a> - 面向物联网与时序数据的分布式数据库
- <a href="https://qdrant.tech/" target="_blank">Qdrant</a> - 用 Rust 编写的开源向量数据库与相似性搜索引擎，支持 payload 过滤、过滤感知 HNSW、稠密/稀疏与多向量及混合多阶段查询
- <a href="https://weaviate.io" target="_blank">Weaviate</a> - 开源向量数据库，用于存储和检索 embedding，可自托管或使用托管云服务
- <a href="https://www.trychroma.com/" target="_blank">Chroma</a> - Apache-2.0 开源向量数据库，支持词法、正则与元数据检索，可自托管或使用无服务器云服务 Chroma Cloud，用作 AI 应用与 agent 的数据存储
- <a href="https://neon.com" target="_blank">Neon</a> - 无服务器 PostgreSQL 平台，支持数据库分支、计算可缩容至零与托管存储，现由 Databricks 运营
- <a href="https://www.appen.com/" target="_blank">Appen</a> - 结合人工与 AI 能力的企业级数据平台，提供数据采集、清洗与标注
- <a href="https://www.surgehq.ai/" target="_blank">Surge</a> - 全球高技能众包标注平台，为生成式 AI 提供训练数据
- <a href="https://snorkel.ai" target="_blank">Snorkel AI</a> - 以数据为中心的 AI 平台，用程序化方式标注训练数据、生成合成数据，支撑机器学习模型的构建与调整
- <a href="https://www.superannotate.com/" target="_blank">SuperAnnotate</a> - AI 数据标注与管理平台，用于准备模型训练数据
- <a href="https://deepnote.com/" target="_blank">Deepnote</a> - 云端协作数据科学笔记本，在代码、查询与可视化环节提供 AI 辅助
- <a href="https://julius.ai" target="_blank">Julius AI</a> - 连接表格等多种数据源的对话式数据分析工具，用图表和统计回答自然语言问题，还能运行 Python 与 R 代码
- <a href="https://dataloop.ai/" target="_blank">Dataloop</a> - 端到端 AI 数据管理与标注平台，内置可视化与流水线自动化
- <a href="https://www.v7labs.com/" target="_blank">V7</a> - AI 图像与视频标注平台，支持自动分割与工作流协作
- <a href="https://motherduck.com" target="_blank">MotherDuck</a> - 基于 DuckDB 构建的无服务器云数据仓库，提供 SQL 分析、云存储与协作共享，无需运维基础设施
- <a href="https://www.tinybird.co" target="_blank">Tinybird</a> - 托管 ClickHouse 平台，把接入的事件数据发布为低延迟 SQL REST API，并带 MCP 服务器供 AI agent 查询
- <a href="https://www.weka.io/" target="_blank">Weka.IO</a> - 云端与本地部署的 AI 数据存储平台，支撑大规模 ML/HPC 训练与推理负载
- <a href="https://unstructured.io" target="_blank">Unstructured</a> - 文档 ETL 平台，将 PDF、表格、表单与扫描件转换成结构化数据并载入向量数据库，服务 RAG 与 LLM 应用
- <a href="https://www.nvidia.com/en-us/use-cases/synthetic-data-generation-for-agentic-ai/" target="_blank">Gretel AI</a> - 面向隐私保护的合成数据生成平台，已被 Nvidia 收购并并入 NeMo 体系
- <a href="https://flourish.studio/" target="_blank">Flourish</a> - 交互式数据可视化平台，适合嵌入新闻与报告
- <a href="https://www.napkin.ai/" target="_blank">Napkin</a> - 把文本转成可编辑视觉图形的工具，用来呈现业务故事
- <a href="https://www.ibm.com/products/informix" target="_blank">Informix</a> - 老牌关系型数据库，现由 HCL/Actian 运营，为金融应用提供向量检索能力
- <a href="https://www.tonic.ai" target="_blank">Tonic.ai</a> - 用 AI 与机器学习生成合成数据的公司
- <a href="https://mostly.ai" target="_blank">Mostly AI</a> - 合成数据生成工具与知识中心，聚焦隐私保护的数据生成
- <a href="https://www.morph-data.io/" target="_blank">Morph</a> - 集表格、数据库与 AI 分析于一体的无代码数据工作室
- <a href="https://www.kater.ai/" target="_blank">Kater</a> - 企业 AI 报表平台，用自然语言提问即可获得决策洞察与分析流程
- <a href="https://datasquirrel.ai/" target="_blank">DataSquirrel</a> - 无代码 BI 工具，自动完成数据清洗、分析与可视化
- <a href="https://datachat.ai/" target="_blank">DataChat</a> - 对话式生成分析平台，无需编码即可查询数据并获得洞察；2025 年被 Mews 收购
- <a href="https://vizly.ai/" target="_blank">Vizly</a> - AI 数据分析师，支持聊天式提问并自动生成可视化报告
- <a href="https://www.coactive.ai/" target="_blank">Coactive</a> - 多模态视觉内容平台，用 AI 自动为图像与视频打标签、检索并分析
- <a href="https://www.syntho.ai" target="_blank">Syntho</a> - 专注用 AI 生成合成数据的公司
- <a href="https://www.sas.com/en_th/news/press-releases/2024/november/hazy-syntheticdata.html" target="_blank">Hazy</a> - 专注隐私保护合成数据的公司，主要软件资产已被 SAS 收购
- <a href="https://aindo.com" target="_blank">Aindo</a> - 数据技术公司，用 AI 生成合成数据
- <a href="https://www.withdavid.ai/" target="_blank">David AI</a> - 音频数据服务，为对话 AI 构建语音训练数据集
- <a href="https://paradigmai.com" target="_blank">Paradigm</a> - 电子表格形态的智能体研究平台，单元格内可运行 AI agent，并行完成数据搜索、增强与操作

<a id="section-model-access"></a>

### 模型访问与路由

- <a href="https://aws.amazon.com/bedrock/" target="_blank">Amazon Bedrock</a> - 用单一 API 调用多个基础模型，支持文本、图像与多模态推理
- <a href="https://openrouter.ai/" target="_blank">OpenRouter</a> - 统一的 LLM API 平台，单一端点即可调用多家提供商的众多语言模型
- <a href="https://www.edenai.co/" target="_blank">Eden AI</a> - 统一 API 平台，通过一个接口调用模型市场上的各类 AI 模型
- <a href="https://www.notdiamond.ai" target="_blank">Not Diamond</a> - 模型路由器，自动决定每个请求由哪个 LLM 处理，供编程 agent 与 LLM 应用优化成本、延迟和质量
- <a href="https://withmartian.com" target="_blank">Martian</a> - 模型路由平台，为每个请求自动选择 LLM，在成本、延迟与输出质量之间取得平衡
- <a href="https://www.requesty.ai/" target="_blank">Requesty</a> - AI 模型市场与 API 聚合平台，可将请求路由到多家提供商的模型
- <a href="https://www.eachlabs.ai/" target="_blank">EachLabs</a> - AI 模型市场，内置 150+ 模型与可视化工作流，用于搭建 AI 后端

<a id="section-model-hubs"></a>

### 模型平台与社区

- <a href="https://huggingface.co" target="_blank">Hugging Face Hub</a> - 托管、分享和发现机器学习模型的平台，内容涵盖模型、数据集、Spaces 演示与应用
- <a href="https://civitai.com/" target="_blank">Civitai</a> - 生成式视觉模型社区，创作者在此发布 checkpoint、LoRA，以及附带提示词与元数据的生成图片和视频

<a id="section-model-runtime-tools"></a>

### 模型运行工具

- <a href="https://lmstudio.ai/" target="_blank">LM Studio</a> - 在本地运行开源 LLM 的桌面工具，既能对话使用，也能把模型部署成本地微服务

<a id="group-productivity-knowledge"></a>

## 效率与知识管理

<a id="section-documents-knowledge"></a>

### 文档与知识

知识管理部分可结合[知识库的组织与检索方式](https://alignify.co/zh/tools/knowledge-base)理解，不限于单个文档工具。

- <a href="https://evernote.com/" target="_blank">Evernote</a> - 笔记与任务管理工具，支持跨平台同步、AI 整理和多媒体输入
- <a href="https://obsidian.md" target="_blank">Obsidian</a> - 本地优先的 Markdown 笔记应用，具备双向链接、关系图谱、画布和可扩展的插件生态
- <a href="https://notebook.google/" target="_blank">Gemini Notebook</a> - Google 的 AI 研究笔记本，原名 NotebookLM，回答、摘要与音频概述均基于用户上传的资料生成
- <a href="https://www.gitbook.com" target="_blank">GitBook</a> - 面向技术团队的文档平台，提供可视化编辑器、Git 同步与 AI 搜索
- <a href="https://logseq.com/" target="_blank">Logseq</a> - 以隐私为先的本地知识库，构建在 Markdown 与双向链接之上
- <a href="https://www.mintlify.com" target="_blank">Mintlify</a> - 从代码库生成并托管开发者文档的平台，配有 AI 辅助写作、内容更新和用户分析
- <a href="https://scribe.com" target="_blank">Scribe</a> - 录制屏幕上的操作，自动生成带截图的分步指南，可用于培训、客服支持和流程文档
- <a href="https://updf.com/" target="_blank">UPDF</a> - 跨平台 AI PDF 编辑器，支持阅读、编辑、批注与对话
- <a href="https://get.mem.ai/" target="_blank">Mem</a> - AI 笔记工作区，自动整理笔记、会议与研究资料，内置 agent 可对话检索并主动提醒待办
- <a href="https://feather.so/" target="_blank">Feather</a> - 发布平台，把 Notion 页面变成面向 SEO 的博客
- <a href="https://stenography.dev/" target="_blank">Stenography</a> - 结合 AI 与代码解析的代码文档工具，保存即更新文档，提供 VS Code 插件与解释 API

<a id="section-productivity-automation"></a>

### 效率与自动化

本节的自动化部分可结合[工作流编排与集成方式](https://alignify.co/zh/tools/workflow)理解工具如何连接各个步骤。

- <a href="https://www.notion.com" target="_blank">Notion</a> - 协作工作区，把文档、Wiki、数据库与项目管理放到一处，并内置支持搜索和写作的 AI 功能
- <a href="https://zapier.com" target="_blank">Zapier</a> - 无代码工作流自动化平台，通过 Zap（触发即执行的工作流）连接数千款应用，还可搭建 AI agent、聊天机器人和表格
- <a href="https://trello.com/" target="_blank">Trello</a> - 看板式协作工具，用卡片和列表直观管理项目任务
- <a href="https://asana.com/" target="_blank">Asana</a> - 团队任务管理平台，支持项目规划、进度跟踪与实时报告
- <a href="https://www.uipath.com/" target="_blank">UiPath</a> - RPA 平台，将 AI 与机器人流程自动化结合，执行重复性任务
- <a href="https://miro.com" target="_blank">Miro</a> - 在线协作白板平台，用于绘图、工作坊与规划，配有 AI 辅助创作功能
- <a href="https://www.airtable.com/" target="_blank">Airtable</a> - 融合电子表格与数据库的协作平台，适合搭建自定义应用和数据驱动的工作流
- <a href="https://calendly.com" target="_blank">Calendly</a> - 会议安排平台，通过可分享的空闲时间链接自动完成预约，并处理日历同步、提醒与后续跟进
- <a href="https://clickup.com/" target="_blank">ClickUp</a> - 项目管理平台，将任务、文档、时间线与 AI 功能放进同一个工作区
- <a href="https://www.surveymonkey.com" target="_blank">SurveyMonkey</a> - 在线问卷平台，AI 辅助问卷的创建、发放与结果分析
- <a href="https://n8n.io" target="_blank">n8n</a> - 面向技术团队的工作流自动化平台，以低代码逻辑连接应用与 API，支持 AI agent 工作流，可云端部署或自托管
- <a href="https://www.make.com" target="_blank">Make</a> - 可视化工作流自动化平台，用来连接应用、搭建业务流程自动化，前身为 Integromat
- <a href="https://www.automationanywhere.com/" target="_blank">Automation Anywhere</a> - 面向端到端流程自动化的 RPA 平台
- <a href="https://www.typeform.com/" target="_blank">Typeform</a> - 交互式表单与问卷工具，以对话式的填写体验提高完成率
- <a href="https://manus.im" target="_blank">Manus</a> - 能自主执行多步任务的 AI agent，例如搭建网站、做数据分析、产出报告，并具备持久记忆
- <a href="https://www.usemotion.com/" target="_blank">Motion</a> - AI 日程应用，统一任务管理与日历自动化，会依据任务优先级自动排布任务、会议和专注时段
- <a href="https://cal.com" target="_blank">Cal.com</a> - 开源且可自托管的会议预约基础设施，服务个人、团队与开发者
- <a href="https://quip.com/" target="_blank">Quip</a> - 嵌入 Salesforce 的实时文档协作工具，整合了电子表格与聊天功能
- <a href="https://tally.so/" target="_blank">Tally</a> - 无代码表单构建工具，编辑方式类似 Notion，可免费创建各类表单
- <a href="https://pig.dev" target="_blank">Pig</a> - 用 computer-use AI 操作 Windows 桌面应用的自动化平台，提供聊天界面、agent API 和 SDK，默认自托管
- <a href="https://flowith.io" target="_blank">Flowith</a> - 带无限画布的 agentic AI 工作区，跨线程衔接知识、创作与多步任务执行
- <a href="https://www.induced.ai/" target="_blank">Induced</a> - Human-in-the-loop 的 RPA，用 AI 自动执行网页端任务
- <a href="https://www.dasis.ai/" target="_blank">Dasis</a> - 团队工作区，借助 AI 辅助的工作流协同处理运营任务
- <a href="https://www.airtime.com/" target="_blank">Airtime</a> - mmhmm 推出的视频办公工具，整合主讲人镜头特效、屏幕与幻灯片录制和互动共享屏幕
- <a href="https://withmana.com" target="_blank">Mana</a> - 自动处理日常工作的 AI agent，能解答 HR 问题、办理文件事务，也可用于学习与娱乐

<a id="section-enterprise-assistants"></a>

### 企业助手

- <a href="https://www.moveworks.com/" target="_blank">Moveworks</a> - 自动响应员工请求并执行任务的企业 AI 助手，现已被 ServiceNow 收购
- <a href="https://aisera.com/" target="_blank">Aisera</a> - 企业 AI 服务台助手，自动处理 IT/HR 请求并生成工单与解决方案
- <a href="https://contextual.ai/" target="_blank">Contextual AI</a> - 用于搭建知识驱动型企业助手的 RAG 平台
- <a href="https://ushur.ai/" target="_blank">Ushur</a> - AI 驱动的客户体验自动化平台，结合聊天与流程机器人提供端到端客户服务
- <a href="https://www.pryon.com/" target="_blank">Pryon</a> - 企业知识搜索与自动问答系统，建立在语义理解之上
- <a href="https://www.blinkops.com/" target="_blank">BlinkOps</a> - 面向网络安全运营的安全自动化平台，内置 AI agent

<a id="section-meeting-notes"></a>

### 会议记录与摘要

- <a href="https://otter.ai" target="_blank">Otter.ai</a> - 会议助手，实时转录会议并生成自动摘要和行动项，可与日历、CRM 及协作工具集成
- <a href="https://fireflies.ai/" target="_blank">Fireflies.ai</a> - 会议助手，接入各类视频会议平台，录制、转录、总结团队谈话并支持检索
- <a href="https://www.granola.ai/" target="_blank">Granola</a> - AI 会议记事本，转录音频的同时润色用户手打的笔记，整理成结构化摘要和行动项
- <a href="https://www.fathom.ai/" target="_blank">Fathom</a> - AI 会议记录员，自动录制、转录并总结通话，提炼出重点片段和行动项
- <a href="https://tldv.io" target="_blank">tl;dv</a> - 会议录制工具，支持多语言转录并生成 AI 笔记和摘要，可同步到 CRM 及其他工作应用
- <a href="https://www.read.ai/" target="_blank">Read</a> - AI 会议平台，生成会议转写和自动摘要，并对录制过的会议提供企业级搜索
- <a href="https://fellow.ai/" target="_blank">Fellow</a> - 会议管理与笔记软件，覆盖议程准备、讨论记录和行动项跟进
- <a href="https://tactiq.io/" target="_blank">Tactiq</a> - 面向 Google Meet、Zoom 和 Microsoft Teams 的会议转录与笔记应用
- <a href="https://www.sembly.ai/" target="_blank">Sembly</a> - 会议助手，录制并转录会议，整理出笔记、待办和摘要
- <a href="https://meetgeek.ai/" target="_blank">MeetGeek</a> - 会议录制与转录平台，生成会议摘要并自动执行跟进流程
- <a href="https://circleback.ai/" target="_blank">Circleback</a> - 会议笔记应用，生成笔记和行动项，并保留可检索的会议记录
- <a href="https://www.supernormal.com/" target="_blank">Supernormal</a> - 会议笔记软件，录制谈话内容，生成摘要和行动项，还能撰写跟进文档
- <a href="https://www.notta.ai" target="_blank">Notta</a> - AI 会议助手，多语言实时转录和总结会议、访谈、讲座，配有协作和导出功能
- <a href="https://www.recall.ai/" target="_blank">Recall.ai</a> - 统一 API，一个接口即可获取 Zoom/Meet 会议录制、实时转录和元数据
- <a href="https://www.claap.io/" target="_blank">Claap</a> - 销售对话平台，录制客户会议并整理通话数据，用于销售辅导和跟进
- <a href="https://grain.com/" target="_blank">Grain</a> - 会议录制与笔记平台，产出转写文本、摘要和行动项
- <a href="https://www.meetjamie.ai/" target="_blank">Jamie</a> - 会议助手，记录谈话内容，生成笔记、摘要和行动项
- <a href="https://cogram.com/" target="_blank">Cogram</a> - AI 平台，自动生成会议笔记、行动项和摘要
- <a href="https://noty.ai/" target="_blank">Noty.ai</a> - 会议助手，转录并总结谈话，把讨论内容转成待办任务
- <a href="https://www.leexi.ai/" target="_blank">Leexi</a> - 会议助手，录制并转录通话，生成摘要和后续待办
- <a href="https://paxo.ai/" target="_blank">Paxo</a> - 移动端优先的 AI 会议速记应用，在 iPhone 上录音并生成清晰可执行的笔记，主打随身速记场景
- <a href="https://www.fieldy.ai/" target="_blank">Fieldy</a> - 可穿戴设备加配套应用，捕捉线下面对面谈话并生成笔记
- <a href="https://myminutes.ai/" target="_blank">MyMinutes</a> - 音频笔记应用，转录录音并整理成结构化笔记
- <a href="https://adot.ai" target="_blank">Adot</a> - 韩国移动端 AI 助手，把语音录音转成结构化、可搜索的笔记，适用于会议、讲座和头脑风暴

<a id="group-marketing-service"></a>

## 营销与客户服务

<a id="section-marketing-content"></a>

### 营销与内容

- <a href="https://linktr.ee/" target="_blank">Linktree</a> - 个性化「Link in Bio」页面，把多个平台的链接聚合到一页，并附带数据分析
- <a href="https://gptzero.me/" target="_blank">GPTZero</a> - 免费的 AI 文本检测器，逐句分析文本是否由 AI 生成
- <a href="https://writesonic.com" target="_blank">Writesonic</a> - AI 写作与 SEO 平台，用来生成文章并追踪品牌在 AI 搜索引擎中的曝光
- <a href="https://www.weglot.com/" target="_blank">Weglot</a> - 无代码多语言网站翻译平台，附带 SEO 优化与内容编辑能力
- <a href="https://originality.ai/" target="_blank">Originality AI</a> - 内容质量工具，集 AI 检测、抄袭查重、事实核查和可读性评估于一体
- <a href="https://anyword.com/" target="_blank">Anyword</a> - AI 营销文案生成工具，支持多语言优化和跨渠道分析
- <a href="https://www.clearscope.io/" target="_blank">Clearscope</a> - 内容优先的 AI SEO 工具，通过关键词优化和竞争分析带动流量增长
- <a href="https://www.frase.io/" target="_blank">Frase</a> - SEO 内容优化与 AI 写作工具，支持自动化生成内容
- <a href="https://undetectable.ai/" target="_blank">Undetectable.ai</a> - 汇总多个 AI 检测器的判定结果，并提供改写服务帮助 AI 内容规避检测
- <a href="https://beacons.ai" target="_blank">Beacons</a> - 创作者平台，提供「Link in Bio」页面、媒体资料包、在线店面和粉丝变现工具
- <a href="https://scrunch.com/" target="_blank">Scrunch AI</a> - Agent Experience Platform（AXP），把品牌内容以压缩、结构化、机器可读的形式提供给 AI agent 和爬虫，按 LLM 解析、理解与返回内容的方式做了优化
- <a href="https://www.airops.com/" target="_blank">Airops</a> - 内容运营 AI 平台，自动生成经过 SEO 优化的内容
- <a href="https://www.pepper.inc/" target="_blank">Pepper Content</a> - 具备 AI 能力的内容营销平台，同时运营一个由专家把关的创作者人才市场
- <a href="https://byword.ai/" target="_blank">Byword</a> - AI SEO 写作助手，一键生成结构化、利于排名的文案
- <a href="https://regie.ai/" target="_blank">Regie</a> - 面向销售团队的 AI 内容平台，生成个性化销售素材和沟通文案
- <a href="https://nooks.ai/" target="_blank">Nooks</a> - 销售平台，集成了电话拨号器、对话数据以及潜客开发和辅导工具
- <a href="https://hyperbound.ai/" target="_blank">Hyperbound</a> - 销售培训平台，模拟买家对话供销售做角色扮演演练并接受辅导
- <a href="https://secondnature.ai/" target="_blank">Second Nature</a> - 销售培训平台，用 AI 角色扮演模拟让销售练习对话并获得反馈
- <a href="https://www.munchstudio.com/" target="_blank">Munch Studio</a> - AI 平台，基于企业自有素材生成社交媒体帖子和内容策略，附带审核流程、一键发布和跨平台分析
- <a href="https://www.bluefishai.com/" target="_blank">Bluefish</a> - AI 可见性分析平台，帮助品牌优化其在各 AI 搜索平台中的露出
- <a href="https://www.evertune.ai/" target="_blank">Evertune</a> - GEO 优化平台，帮助品牌在 AI 搜索结果中获得更多可见性
- <a href="https://www.withdaydream.com" target="_blank">Daydream</a> - SEO 与 AI 搜索可见性公司，整合服务、AI agent 和平台，帮助品牌增长自然流量以及在各 AI 助手中的露出
- <a href="https://www.globalseo.ai/" target="_blank">GlobalSEO</a> - 用 AI 自动把网站翻译成多种语言，带动国际自然搜索流量增长
- <a href="https://lit.link/" target="_blank">lit.link</a> - 免费的「Link in Bio」服务，聚合多个社交媒体链接，提供多种设计选项
- <a href="https://campsite.bio/" target="_blank">Campsite.bio</a> - 制作适配移动端的「Link in Bio」页面，用来整理和追踪社交媒体链接
- <a href="https://portaly.cc/" target="_blank">Portaly</a> - AI 平台，从社交媒体内容一键生成品牌展示页
- <a href="https://terrakotta.ai/" target="_blank">Terrakotta</a> - 商业地产行业的潜客开发平台，把房源数据与电话外呼流程结合起来
- <a href="https://digitalfirst.ai/" target="_blank">Digital First AI</a> - 营销平台，用 AI 制定并执行营销计划
- <a href="https://www.anoki.ai/" target="_blank">Anoki</a> - 面向 CTV 广告的多模态 AI 平台，提供场景级上下文视频智能和品牌安全保障，支持用 GenAI 创建和个性化广告
- <a href="https://icon.com" target="_blank">Icon</a> - UGC 广告平台，为品牌制作创作者出镜的视频广告，配套广告活动管理软件用于追踪效果和迭代
- <a href="https://leadbeam.ai/" target="_blank">Leadbeam</a> - 面向外勤销售团队的移动 CRM，记录客户互动并更新销售记录

<a id="section-customer-service"></a>

### 客户服务与销售智能

- <a href="https://www.zendesk.com/" target="_blank">Zendesk</a> - 全渠道客户支持系统，以 AI 增强工单管理并自动化工作流
- <a href="https://www.intercom.com" target="_blank">Intercom</a> - 客户消息平台，整合帮助台和共享收件箱，由 AI agent Fin 解决客户支持会话
- <a href="https://sierra.ai/" target="_blank">Sierra</a> - 企业级平台，用于构建和运营跨渠道解决客服问题的对话式 AI agent
- <a href="https://decagon.ai" target="_blank">Decagon</a> - 构建和运营 AI agent 的平台，在聊天、邮件和语音渠道自动化客户支持
- <a href="https://cresta.com/" target="_blank">Cresta</a> - 呼叫中心软件，自动处理客户对话、辅助坐席沟通并分析会话数据
- <a href="https://parloa.com/" target="_blank">Parloa</a> - 面向呼叫中心的企业级 AI agent 管理平台，覆盖 agent 设计、仿真、评估、部署与监控，支持 CCaaS/CRM 集成和转人工
- <a href="https://yellow.ai/" target="_blank">Yellow.ai</a> - 企业级对话式 AI 平台，提供具备 agentic AI 能力的全渠道客服聊天机器人
- <a href="https://forethought.ai/" target="_blank">Forethought</a> - 基于 SupportGPT 的平台，自动回答客户问题，用 AI 排定工单优先级并完成分派
- <a href="https://www.chatbase.co" target="_blank">Chatbase</a> - 基于企业自有数据构建客服 AI agent 的平台，提供工作流自动化、模型对比与转人工
- <a href="https://replicant.com/" target="_blank">Replicant</a> - 面向呼叫中心客服的对话自动化与分析平台
- <a href="https://www.crescendo.ai/" target="_blank">Crescendo</a> - 把对话式 AI 与人工专家结合起来的客户服务平台
- <a href="https://symbl.ai/" target="_blank">Symbl</a> - 实时对话智能平台，从语音、视频和聊天中提取洞察；2025 年 5 月被 Invoca 收购
- <a href="https://lavender.ai/" target="_blank">Lavender</a> - AI 销售邮件训练平台，为邮件打分、给出个性化建议并调研收件人
- <a href="https://outplay.ai/" target="_blank">Outplay</a> - 多渠道销售自动化平台，支持邮件、电话和 LinkedIn 沟通，并提供数据分析
- <a href="https://kaizan.ai/" target="_blank">Kaizan</a> - 对话智能平台，帮助管理客户关系，自动填充工作流并集成常用工具
- <a href="https://www.hellorep.ai" target="_blank">Rep AI</a> - 面向电商品牌（Shopify）的对话式 AI 销售平台，识别购物意向、主动触达顾客，引导其从发现商品到完成结账
- <a href="https://www.rilla.com/" target="_blank">Rilla</a> - 对话智能平台，记录线下销售对话并支持销售辅导
- <a href="https://siro.ai/" target="_blank">Siro</a> - 销售辅导平台，记录并分析外勤面谈、电话和会议
- <a href="https://winn.ai/" target="_blank">Winn AI</a> - 销售执行助手，记录通话、调出 playbook 并更新 CRM 记录
- <a href="https://voctiv.com/" target="_blank">Voctiv</a> - 用于客户沟通和通话处理的 AI 语音与消息软件
- <a href="https://marrlabs.com/" target="_blank">Marr Labs</a> - 客户语音与聊天自动化平台；2026 年 9 月被 PayNearMe 收购
- <a href="https://www.edgetier.com/" target="_blank">Edge Tier</a> - 用 NLP 优化客服对话质量的技术，支持异常检测与自动化决策辅助
- <a href="https://smartly.ai/" target="_blank">Smartly.ai</a> - 用于搭建跨设备对话式应用的平台，覆盖 Messenger、Alexa 等渠道

<a id="group-commerce"></a>

## 电商与购物

<a id="section-commerce-shopping"></a>

### 电商与购物

- <a href="https://www.amazon.com/Rufus/b?ie=UTF8&node=121214013011" target="_blank">Amazon Rufus</a> - Amazon 的 AI 购物助手，正在被并入 Alexa 体验
- <a href="https://www.accio.com" target="_blank">Accio</a> - Alibaba 推出、面向 B2B 买家的 AI 选品与采购助手，按产品创意匹配供应商并提供市场调研
- <a href="https://www.karmanow.com" target="_blank">Karma</a> - AI 购物助手，跨商店追踪价格、自动找优惠码并提醒降价，已转型智能体购物平台
- <a href="https://www.pietrastudio.com/" target="_blank">Pietra</a> - 面向品牌的电商平台，把采购、履约、营销与 AI 辅助运营放进同一套系统
- <a href="https://www.doji.com/" target="_blank">Doji</a> - 生成 AI 虚拟形象，用于时装的在线虚拟试穿
- <a href="https://yuma.ai/" target="_blank">Yuma</a> - 电商客服平台，跨渠道接待并处理买家咨询
- <a href="https://beni.ai/" target="_blank">Beni</a> - 专注二手时尚的搜索引擎，一次搜索四十多个转售平台，支持图片搜索与上架提醒
- <a href="https://www.whering.co/" target="_blank">Whering</a> - 带社交功能的数字衣橱应用，登记衣物、规划穿搭并分享造型
- <a href="https://www.acloset.app/" target="_blank">Acloset</a> - 数字衣橱应用，登记衣物并推荐穿搭
- <a href="https://cladwell.com/" target="_blank">Cladwell</a> - 衣橱规划应用，帮助用户整理衣物并规划穿搭
- <a href="https://www.myindyx.com/" target="_blank">Indyx</a> - 数字衣橱应用，支持登记衣物、规划穿搭并记录穿着情况
- <a href="https://www.altadaily.com/" target="_blank">Alta</a> - AI 穿搭助手应用，从衣物照片建立数字衣橱，依据现有衣物和天气推荐每日穿搭
- <a href="https://faircado.com/" target="_blank">Faircado</a> - AI 浏览器插件与应用，聚合数百万级二手商品平台，支持智能搜索与比价
- <a href="https://getmanifest.ai/" target="_blank">Manifest AI</a> - 电商助手，回答购物者提问、推荐商品并提供客服支持
- <a href="https://raspberry.ai/" target="_blank">Raspberry AI</a> - 时尚团队用的设计平台，可创作和编辑商品图与设计概念
- <a href="https://glam.ai/" target="_blank">Glam AI</a> - 面向时尚电商的虚拟试穿 API，用图生图技术把服装贴合到顾客照片，附滤镜与图像生成能力
- <a href="https://www.shopencore.ai/" target="_blank">Encore</a> - AI 二手购物助手，聚合多个平台，通过对话搜索商品
- <a href="https://spoken.ai/" target="_blank">Spoken</a> - 围绕价格进行商品发现与搜索的平台
- <a href="https://phia.ai/" target="_blank">Phia</a> - AI 购物助手，在任意商品页寻找更低价替代，覆盖 22 万余个含二手电商在内的网站，提供 iOS 应用与 Chrome 扩展
- <a href="https://retrofit.ai/" target="_blank">Retrofit</a> - 面向二手商品的商品发现与搜索平台
- <a href="https://www.openwardrobe.co" target="_blank">OpenWardrobe</a> - 数字衣橱应用，用来整理衣物和创建穿搭
- <a href="https://lookverse.ai/" target="_blank">Lookverse</a> - 主打时尚品类的 AI 视觉购物平台，把商品搜索与发现做成个性化、预测式体验
- <a href="https://onton.com/" target="_blank">Onton</a> - 无广告的 AI 家居购物搜索引擎，支持自然语言与以图搜图，可跨上百家零售商检索商品
- <a href="https://thehumind.com/" target="_blank">Humind</a> - 面向网店的购物助手，回答商品问题并通过同步的商品目录引导顾客
- <a href="https://alhena.ai/" target="_blank">Alhena</a> - 面向网店的客服平台，回答购物者问题并辅助商品发现
- <a href="https://cherry.ai/" target="_blank">Cherry</a> - 面向成年用户（18+）的 AI 伴侣与角色扮演聊天应用，支持图像生成
- <a href="https://printgen.ai/" target="_blank">PrintGen</a> - 按需定制印花服务，把文字描述变成 T 恤与卫衣图案，下单才生产、无起订量，美国境内免运费

<a id="group-finance"></a>

## 金融与财务

<a id="section-finance-accounting"></a>

### 金融与会计

- <a href="https://www.bill.com/" target="_blank">Bill</a> - 面向中小企业的财务运营平台，自动处理发票生成、收付款、账单、费用管理与预算控制
- <a href="https://rogo.com/" target="_blank">Rogo AI</a> - 面向金融机构的 AI 分析平台，自动调研数据、生成洞察，加快投资决策
- <a href="https://www.rillet.com/" target="_blank">Rillet</a> - AI 原生 ERP 系统，自动完成月末关账、合并报表、GAAP 报告与发票处理
- <a href="https://samaya.ai/" target="_blank">Samaya AI</a> - 为金融服务与投行领域专家打造的 AI 知识发现平台
- <a href="https://skit.ai/" target="_blank">Skit.ai</a> - 为催收和应收账款团队提供语音与消息自动化
- <a href="https://www.kastle.ai/" target="_blank">Kastle AI</a> - 金融服务语音 AI agent 平台，专注抵押贷款业务
- <a href="https://www.aviaryai.co/" target="_blank">Aviary AI</a> - 面向金融服务运营的语音 AI agent 平台
- <a href="https://www.evalyze.ai" target="_blank">Evalyze</a> - AI 融资平台，审阅路演 PPT、评估融资准备度，并帮创始人匹配投资人

<a id="group-education-research"></a>

## 教育与研究

<a id="section-learning-tools"></a>

### 学习与教学

[AI 辅助学习与教学的应用场景](https://alignify.co/zh/tools/education)为这些教育工具提供背景。

- <a href="https://www.duolingo.com" target="_blank">Duolingo</a> - 游戏化的语言学习应用，用短小课程教多门语言，分免费与订阅两档
- <a href="https://quizlet.com" target="_blank">Quizlet</a> - 提供数字闪卡、练习测验和 AI 辅助学习模式的学习平台，覆盖各学科
- <a href="https://www.khanmigo.ai" target="_blank">Khanmigo</a> - Khan Academy 推出的 AI 导师与教学助手，引导学生逐步学完平台课程，并协助教师备课与批改
- <a href="https://www.chegg.com/" target="_blank">Chegg</a> - 全天候在线作业辅导与教材租赁平台
- <a href="https://photomath.com/" target="_blank">Photomath</a> - 数学拍照解题工具，提供分步讲解与多种解法
- <a href="https://wayground.com" target="_blank">Wayground</a> - 在线互动测验平台（原 Quizizz），支持课堂与远程的游戏化学习
- <a href="https://www.coursehero.com/" target="_blank">Course Hero</a> - 在线学习平台，提供与课程配套的学习资料、作业帮助和在线辅导
- <a href="https://www.blinkist.com/" target="_blank">Blinkist</a> - 15 分钟「Blink」书籍摘要，提供音频与文本格式，并规划个性化学习路径
- <a href="https://notability.com/" target="_blank">Notability</a> - 手写笔记应用，可将笔记、录音与文档自动转为 AI 摘要、闪卡与测验，辅助学习
- <a href="https://www.gauthmath.com" target="_blank">Gauth</a> - 数学等 STEM 题目拍照即解的 AI 作业助手，提供分步解析与真人导师在线支持
- <a href="https://www.questionai.com" target="_blank">Question.AI</a> - AI 作业助手，用分步讲解回答数学、科学等学科问题
- <a href="https://www.speak.com" target="_blank">Speak</a> - 专注口语练习的 AI 语言辅导应用，即时反馈发音与对话，支持英语、西班牙语、法语、韩语、意大利语和日语
- <a href="https://www.datacamp.com/" target="_blank">DataCamp</a> - 编程与数据分析在线学习平台，提供项目式课程和技能学习路径
- <a href="https://www.mathway.com/" target="_blank">Mathway</a> - 多用途数学解题工具，题目支持拍照或手动输入
- <a href="https://www.mondly.com/" target="_blank">Mondly</a> - 多语言学习应用，提供会话练习与语音识别功能
- <a href="https://lingokids.com/" target="_blank">Lingokids</a> - 面向 2-8 岁儿童的语言学习应用，借助互动游戏与语音识别教学
- <a href="https://answerai.pro" target="_blank">Answer.AI</a> - AI 学习助手应用，提供作业答疑、备考与写作建议，覆盖 iOS、Android 与 Chrome 扩展
- <a href="https://makeheadway.com/" target="_blank">Headway</a> - 15 分钟书籍摘要，提供文本与音频版本，配可视化呈现和个性化推荐
- <a href="https://knowt.com" target="_blank">Knowt</a> - 学习工具，把笔记、视频和 PDF 变成 AI 闪卡与练习测验，支持间隔重复复习和课堂笔记记录
- <a href="https://www.shortform.com/" target="_blank">Shortform</a> - 为 1000+ 部深度非虚构书籍提供专家引导式的摘要与见解
- <a href="https://instaread.co/" target="_blank">Instaread</a> - 专业撰写的 15 分钟书籍摘要，覆盖热门畅销书
- <a href="https://solvely.ai" target="_blank">Solvely</a> - 拍照解题的 AI 学习助手，给出分步解答，并辅助生成测验、作文与笔记
- <a href="https://cameramath.com/" target="_blank">UpStudy</a> - 多学科作业拍照解题工具，逐步讲解并配有导师辅导
- <a href="https://www.mindgrasp.ai/" target="_blank">Mindgrasp</a> - AI 学习平台，上传文档即可生成笔记、闪卡与测验
- <a href="https://www.studyfetch.com/" target="_blank">Study Fetch</a> - 学习助手，把录音文件转成 AI 笔记和测验
- <a href="https://www.scholarcy.com" target="_blank">Scholarcy</a> - 网页工具，将论文、书籍等文献整理为结构化摘要、闪卡和引文摘录，辅助文献综述
- <a href="https://www.mathos.ai/" target="_blank">Mathos</a> - AI 数学解题器，键入或上传题目即可获得分步解答、交互式绘图与作业辅导
- <a href="https://math-gpt.org/" target="_blank">MathGPT</a> - 图片识题的数学计算器，用视频和动画演示解题过程
- <a href="https://qanda.ai/" target="_blank">Quanda</a> - 用 OCR 识别题目的 AI 数学学习平台，一步给出解答，注册用户超 9000 万
- <a href="https://www.trancy.org/" target="_blank">Trancy</a> - 自动为视频生成双语字幕，并配套生成学习卡片
- <a href="https://gliglish.com/" target="_blank">Gliglish</a> - 通过与 AI 角色的语音对话练习，提升口语和听力
- <a href="https://praktika.ai/" target="_blank">Praktika.ai</a> - AI 语言导师应用，以对话练习提升口语
- <a href="https://www.boldvoice.com" target="_blank">BoldVoice</a> - 美式英语发音与口音训练应用，跟着语音教练的视频课练习，即时获得 AI 反馈
- <a href="https://www.apeuni.com/" target="_blank">APEUni</a> - 免费 AI 驱动的 PTE 备考练习平台，评估口语与写作表现
- <a href="https://penseum.com/" target="_blank">Penseum</a> - 按上传资料定制笔记、闪卡与测验内容的 AI 学习平台
- <a href="https://curipod.com/" target="_blank">Curipod</a> - 面向 K-12 的 AI 互动课堂工具，可生成投票和测验
- <a href="https://classcompanion.com/" target="_blank">Class Companion</a> - 教师 AI 批改与辅导工具；2025 年 4 月被 Panorama Education 收购
- <a href="https://www.doctrina.ai/" target="_blank">Doctrina AI</a> - AI 教育平台，可生成笔记、测验、作文与对话
- <a href="https://echolabs.ai/" target="_blank">Echolabs</a> - 面向高等教育的 AI 字幕平台，最快二十四小时产出字幕与口述影像，接入 Canvas 等系统
- <a href="https://www.coconote.app/" target="_blank">Coconote</a> - AI 笔记与学习 App，把课堂录音、文档和视频转成笔记、转录、测验、闪卡与模拟试卷，并可生成播客摘要；已并入 Quizlet，仍作为独立应用运营
- <a href="https://sobrief.com/" target="_blank">Sobrief</a> - 书籍摘要库，提供 10 分钟 AI 音频与文本摘要，支持 40 种语言
- <a href="https://www.bohrium.com/en" target="_blank">Bohrium</a> - 科学计算研究平台，内置 AI 辅助的文献探索、文章检索与问答工具

<a id="section-research-writing"></a>

### 研究与学术写作

- <a href="https://paperguide.ai/" target="_blank">Paperguide</a> - AI 研究助手，自动检索文献、起草文献综述并管理引用
- <a href="https://eduwriter.ai/" target="_blank">EduWriter</a> - AI 辅助论文写作工具，实时生成可下载的论文草稿

<a id="group-hr-recruiting"></a>

## 招聘与职业

<a id="section-recruiting-careers"></a>

### 招聘与职业

本节的招聘部分可结合[AI 辅助招聘工作流](https://alignify.co/zh/tools/recruiting)理解人才寻访与筛选场景。

- <a href="https://www.mercor.com" target="_blank">Mercor</a> - AI 招聘市场，为专业岗位搜寻并面试候选人，同时处理全球合同与付款
- <a href="https://www.turing.com/" target="_blank">Turing</a> - AI 驱动的远程开发者平台，自动匹配并管理全球软件工程师
- <a href="https://www.brighthire.com/" target="_blank">BrightHire</a> - 面试智能平台，配备全天候 AI 首轮面试官，提供录制、转写与作弊信号检测
- <a href="https://www.metaview.ai/" target="_blank">Metaview</a> - agent 化的招聘平台，AI 自动寻访候选人并生成面试笔记与评分卡，对接主流 ATS
- <a href="https://www.finalroundai.com" target="_blank">Final Round AI</a> - 在线面试实时助手，转写面试问题并给出回答建议，另提供 AI 模拟面试练习和简历工具
- <a href="https://jobright.ai/" target="_blank">Jobright AI</a> - AI 求职副驾驶，匹配岗位、自动填写申请，并优化简历、生成求职信
- <a href="https://www.micro1.ai" target="_blank">micro1</a> - AI 招聘平台，内置语音面试官 Zara，并提供承接数据标注与 AI 训练数据业务的全球人才队伍
- <a href="https://www.alex.com/" target="_blank">Alex</a> - Apriora 推出的 AI 招聘官，现更名 Alex，自动进行首轮面试与简历筛选，接入 33+ 招聘系统
- <a href="https://www.ribbon.ai/" target="_blank">Ribbon</a> - 语音 AI 招聘员，全天候用 10 种语言进行自适应双向面试，按评分标准自动打分，可与 60 多个 ATS 同步
- <a href="https://www.carv.com" target="_blank">Carv</a> - AI 招聘平台，由自主 agent 承担岗位需求受理、筛选和 ATS 更新等招聘行政工作
- <a href="https://joinbrix.com" target="_blank">Brix</a> - 面向应用型 AI 人才的智能体招聘平台，生成职位描述、搜寻并筛选候选人，并在 120 多个国家办理合同、薪酬发放与合规
- <a href="https://lightscreen.ai/" target="_blank">Lightscreen</a> - 语音 AI 招聘平台，AI 面试官评估沟通与匹配度，自动完成简历筛选、背调与约面
- <a href="https://www.lockedinai.com" target="_blank">LockedIn AI</a> - 实时面试与会议助手，提供回答建议、编程副驾驶，并支持自动投递求职申请
- <a href="https://www.senseicopilot.com/" target="_blank">Sensei AI</a> - 浏览器内的面试助手，实时生成结构化回答
- <a href="https://www.vervecopilot.com/" target="_blank">Verve AI</a> - AI 面试陪练助手，实时给出建议，并优化冷邮件与简历
- <a href="https://himalayas.app/" target="_blank">Himalayas</a> - 远程与 AI 岗位平台，为用户匹配职位并生成求职信
- <a href="https://www.thecorrelate.com" target="_blank">Correlate AI</a> - 求职工具，按岗位定制简历并一键投递匹配职位
- <a href="https://nodeflair.com/" target="_blank">NODEFLAIR</a> - 东南亚技术人才求职平台，提供简历工具和公开透明的职位、薪资信息
- <a href="https://helloboss.com/" target="_blank">Hello Boss</a> - 面向日式招聘的求职应用，提供 AI 职位推荐并一键生成履历
- <a href="https://corecruit.com/" target="_blank">CoRecruit</a> - 招聘机构 AI 助手（原 Quil，更名 CoRecruit），自动写面试笔记并同步 ATS

<a id="group-healthcare"></a>

## 医疗健康

<a id="section-healthcare"></a>

### 医疗健康

[医疗 AI 的应用场景与边界](https://alignify.co/zh/tools/healthcare)为本节的行业工具提供背景。

- <a href="https://flo.health/" target="_blank">Flo</a> - 全球女性健康追踪应用，记录月经周期、排卵与怀孕状态
- <a href="https://www.calai.app" target="_blank">Cal AI</a> - 手机应用，通过餐食照片、条形码扫描或文字描述估算卡路里和营养成分
- <a href="https://www.hippocratic.ai/" target="_blank">Hippocratic AI</a> - 医疗对话软件，用于患者互动和非诊断类护理流程
- <a href="https://growtherapy.com/" target="_blank">Grow Therapy</a> - 线上线下心理治疗平台，支持保险支付并简化预约流程
- <a href="https://www.blinkhealth.com/" target="_blank">Blink Health</a> - 数字处方药平台，提供低价药品、免费配送与线下自取服务
- <a href="https://billiontoone.com/" target="_blank">BillionToOne</a> - 精准分子诊断公司，研发单碱基级别的产前与癌症筛查技术
- <a href="https://www.eliseai.com/" target="_blank">Elise AI</a> - 面向住房与医疗机构的对话自动化平台，承接租赁、住户与患者沟通
- <a href="https://www.navina.ai/" target="_blank">Navina</a> - 医疗 AI 平台，实时优化临床决策与住院资源分配
- <a href="https://infinitus.ai/" target="_blank">Infinitus</a> - 医疗对话自动化，处理保险福利核验、预授权和诊疗协调
- <a href="https://hyro.ai/" target="_blank">Hyro</a> - 医疗语音与聊天自动化工具，覆盖患者接入、预约排期与咨询支持
- <a href="https://www.mdclone.com/" target="_blank">MDClone</a> - 医疗数据分析平台，在保护隐私的同时生成合成数据
- <a href="https://www.soniahealth.com" target="_blank">Sonia</a> - Sonia Health 推出的 AI 心理健康陪伴应用
- <a href="https://www.develophealth.ai/" target="_blank">Develop Health</a> - 医疗 AI 平台，为处方医生自动化预授权全流程，支持实时保障核验与自动申诉
- <a href="https://superdial.com/" target="_blank">Super Dial</a> - 帮医疗收入循环团队对接保险公司的语音自动化工具
- <a href="https://arini.ai/" target="_blank">Arini</a> - 牙科诊所的 AI 电话前台与患者互动软件
- <a href="https://www.hellopatient.com" target="_blank">Hello Patient</a> - 医疗沟通软件，处理患者来电与消息，支持预约排期和初诊登记
- <a href="https://standardpractice.ai/" target="_blank">Standard Practice</a> - 语音自动化工具，替诊所完成面向保险公司和药房的外呼
- <a href="https://assorthealth.com/" target="_blank">Assort Health</a> - 语音形式的患者接入软件，负责预约、转诊、登记与随访
- <a href="https://www.clarionhealth.com/" target="_blank">Clarion</a> - 医疗前台自动化，处理患者来电、转诊、预约与主动外联
- <a href="https://healthharbor.co" target="_blank">Health Harbor</a> - 帮医疗机构自动拨打保险福利核验电话并接听患者来电的软件
- <a href="https://www.getmagical.com/" target="_blank">Magical</a> - 医疗运营平台，部署 AI agent 执行患者接入与收入循环流程

<a id="group-legal"></a>

## 法律

<a id="section-legal"></a>

### 法律

[AI 辅助法律工作流](https://alignify.co/zh/tools/legal)介绍本类别涉及的法律研究与文档任务。

- <a href="https://www.harvey.ai/" target="_blank">Harvey AI</a> - 供律所与公司法务团队使用的法律及专业服务 AI 平台，提供检索、文书起草与分析流程
- <a href="https://www.thomsonreuters.com/en/cocounsel" target="_blank">Casetext</a> - 法律研究与 AI 法律助手平台，已被 Thomson Reuters 收购
- <a href="https://www.evenuplaw.com/" target="_blank">EvenUp</a> - 替律所自动化处理人身伤害案件的平台，涵盖索赔材料、医疗记录时间线与文件审查
- <a href="https://legora.com/" target="_blank">Legora</a> - 律师的 AI 工作空间，加速文书起草、法律检索与团队协作
- <a href="https://www.supio.com/" target="_blank">Supio</a> - 专为原告律师打造的法律 AI 平台

<a id="group-spatial"></a>

## 三维与空间

<a id="section-spatial-3d"></a>

### 三维与空间工具

[3D 创作与建模工作流](https://alignify.co/zh/tools/3d)为这些空间工具提供背景。

- <a href="https://www.meshy.ai/" target="_blank">Meshy</a> - AI 3D 模型生成器，从文本提示或图片生成带贴图的网格模型，并提供编辑工具和面向游戏、AR 的导出格式
- <a href="https://www.tripo3d.ai" target="_blank">Tripo</a> - 网页端 3D 生成平台，从文本、图片或草图生成成品级 3D 模型，支持 AI 贴图与自动绑定
- <a href="https://www.kaedim3d.com" target="_blank">Kaedim</a> - 把 2D 图片和草图转换为生产级 3D 模型的平台，输出可用于 Unity、Unreal Engine 和 Blender
- <a href="https://deepmotion.com/" target="_blank">DeepMotion</a> - DeepMotion 是一家聚焦动作智能的公司，专攻动作捕捉技术
- <a href="https://www.hexa3d.io/" target="_blank">Hexa</a> - 3D 电商平台，提供创建、管理、分析和分发 3D 资产的技术栈，服务在线购物场景
- <a href="https://www.backflip.ai/" target="_blank">Backflip</a> - 一键将 3D 扫描转换为 CAD 模型的 AI 工具
- <a href="https://www.intangible.ai/" target="_blank">Intangible.ai</a> - 借助 AI 创建、编辑 3D 场景并支持协作的无代码平台
- <a href="https://www.eufymake.com/" target="_blank">Eufymake</a> - 无代码 AI 工具，可生成、编辑 3D 场景并支持团队协作
- <a href="https://ai-build.com/" target="_blank">AI Build</a> - 结合 3D 打印与 CNC 技术、用于自动化生产的制造平台

<a id="group-games"></a>

## 游戏与互动媒体

<a id="section-games-interactive"></a>

### 游戏与互动媒体

- <a href="https://www.aidungeon.com/" target="_blank">AI Dungeon</a> - AI Dungeon 是一款 AI 驱动的开放式文字冒险游戏，玩家自由输入，故事情节可以无限延展
- <a href="https://aimlabs.com/" target="_blank">Aimlabs</a> - 内置 AI 教练的瞄准训练器，含 Valorant 等游戏官方训练内容
- <a href="https://mobalytics.gg/" target="_blank">Mobalytics</a> - Mobalytics 是游戏数据分析工具，支持多款热门游戏
- <a href="https://volley.com/" target="_blank">Volley</a> - 开发纯语音交互游戏的娱乐科技公司，拥有 Jeopardy! 等授权节目游戏，登陆智能音箱与电视
- <a href="https://kinetix.tech/" target="_blank">Kinetix</a> - Kinetix 让用户从视频生成 3D 动画虚拟形象并转换为 NFT，支持跨虚拟世界使用
- <a href="https://www.auki.com/" target="_blank">Auki Labs</a> - Auki Labs 研发增强现实技术，构建持久且保护隐私的元宇宙，提供分布式定位和空间多人解决方案
- <a href="https://www.layer.ai/" target="_blank">Layer</a> - 面向游戏团队的 AI 资产生成平台，聚合 300 多个模型，可训练专属画风
- <a href="https://modl.ai/" target="_blank">Modl.ai</a> - Modl.ai 提供面向游戏的 AI 工具，用于自动化测试和内容生成
- <a href="https://regression.gg/" target="_blank">Regression Games</a> - Regression Games 是 AI 游戏与电竞平台，用户通过编程控制游戏角色
- <a href="https://agentic.xyz/" target="_blank">Agentic</a> - Agentic 是虚拟世界创建平台，可训练并部署 AI 玩家
- <a href="https://epochml.com/" target="_blank">Epoch</a> - Epoch 是游戏 QA 测试工具，支持机器学习任务
- <a href="https://www.ggpredict.io/" target="_blank">GG Predict</a> - GG Predict 是 CS:GO 训练平台，由 AI 定制挑战并给出反馈
- <a href="https://incymo.ai/" target="_blank">Incymo</a> - Incymo 是游戏变现平台，提供广告优化和玩家行为分析
- <a href="https://www.oneirocom.ai/" target="_blank">Oneirocom</a> - Oneirocom 是元宇宙平台，将 AI 与分布式沉浸式叙事技术结合，提供互动体验
- <a href="https://theculturedao.com/" target="_blank">The Culture DAO</a> - 用 $CULTUR 代币资助虚拟人、AI 游戏与电影创作的 Web3 组织

<a id="group-writing"></a>

## 写作与出版

<a id="section-writing-publishing"></a>

### 写作与出版

- <a href="https://www.grammarly.com/" target="_blank">Grammarly</a> - Grammarly 是跨平台 AI 写作助手，实时检查语法、风格与语气，并给出文字建议
- <a href="https://jasper.ai" target="_blank">Jasper</a> - Jasper 是面向营销和商务团队的 AI 写作助手，支持品牌语气控制、模板和 SEO 工作流
- <a href="https://gamma.app/" target="_blank">Gamma</a> - Gamma 从文字提示生成演示文稿、文档和网页，自带模板、多媒体嵌入和协作功能
- <a href="https://rytr.me/" target="_blank">Rytr</a> - Rytr 是 AI 写作助手，设有免费版和付费版
- <a href="https://slidesgo.com/" target="_blank">Slidesgo</a> - Slidesgo 提供数万套免费 Google/PowerPoint 模板下载
- <a href="https://sudowrite.com/" target="_blank">Sudowrite</a> - Sudowrite 通过自然语言描述生成并编辑小说、故事、博客等内容
- <a href="https://jenni.ai/" target="_blank">Jenni.ai</a> - Jenni.ai 是 AI 写作助手，辅助学术写作、研究整理与逻辑生成
- <a href="https://www.beautiful.ai/" target="_blank">Beautiful.ai</a> - Beautiful.ai 是智能演示设计平台，自动保持排版与品牌一致
- <a href="https://www.goodnovel.com/" target="_blank">GoodNovel</a> - 面向海外市场的网络小说平台，类型覆盖广，同时支持创作与阅读
- <a href="https://www.copysmith.ai/" target="_blank">Copysmith</a> - AI 内容平台套件：Frase 做搜索优化，Describely 做电商文案，Rytr 做写作助手
- <a href="https://hyperwriteai.com/" target="_blank">HyperWrite</a> - HyperWrite 是 OthersideAI 推出的 AI 写作助手，提供 Chrome 扩展与网页应用，内置自动补全、写作工具、聊天和网络搜索
- <a href="https://fizzo.org/" target="_blank">Fizzo</a> - 阅读娱乐平台，集小说、漫画与短剧于一体，主打本地化内容
- <a href="https://www.prezent.ai/" target="_blank">Prezent</a> - Prezent 是面向生命科学与科技企业的一体化 AI 演示平台，按行业、公司和受众定制，结合 AI agent、软件与专家服务
- <a href="https://www.squibler.io/" target="_blank">Squibler</a> - AI 故事写作平台，生成故事开头和写作提示，帮助作者开启新项目
- <a href="https://audiopen.ai/" target="_blank">AudioPen</a> - 录音转文字应用，把口述录音整理、编辑成有条理的文字
- <a href="https://www.bedtimestory.ai/" target="_blank">Bedtimestory.ai</a> - Bedtimestory.ai 根据提示词即时生成高度个性化的睡前故事
- <a href="https://www.compose.ai/" target="_blank">Compose</a> - Compose 是免费的 Chrome 扩展，用 AI 自动补全和生成文本
- <a href="https://cleftnotes.com/" target="_blank">Cleft</a> - 语音笔记应用，把口述的想法转写成结构化的文字笔记
- <a href="https://copymonkey.ai/" target="_blank">CopyMonkey.ai</a> - 面向亚马逊卖家的 AI 文案工具，生成关键词优化的商品文案，官网宣布向继任产品过渡
- <a href="https://www.rosebud.app/" target="_blank">Rosebud</a> - AI 日记应用，以追问展开对话并记住既往条目、关联行为模式，配合每周报告与习惯追踪，支持网页与移动端
- <a href="https://mindsera.com/" target="_blank">mindsera</a> - AI 心理健身日记应用，支持文字、语音与拍照记录，自动分析情绪并内置 50 多种思维模型模板
- <a href="https://bertha.ai/" target="_blank">Bertha AI</a> - 曾内嵌于 WordPress 编辑器的写作与图片生成助手，官网已宣布停止服务
- <a href="https://www.gomoonbeam.com/" target="_blank">Go Moonbeam</a> - Go Moonbeam 是文本内容生成服务，覆盖多种内容类型
- <a href="https://www.pirr.ai/" target="_blank">Pirr</a> - Pirr 是创作浪漫与情色故事的 AI 平台
- <a href="https://www.presentations.ai/" target="_blank">Presentations.AI</a> - Presentations.AI 是快速生成图表、时间线、报告与演示幻灯片的 AI 助手
- <a href="https://slidesgpt.com/" target="_blank">SlidesGPT AI</a> - SlidesGPT AI 基于文本提示生成幻灯片，输出自带备注和主题样式
- <a href="https://storybee.app/" target="_blank">StoryBee</a> - StoryBee 是专注童话题材的 AI 故事与插画生成平台
- <a href="https://www.storiesforkids.ai/" target="_blank">StoriesForKids.ai</a> - StoriesForKids.ai 是把真实情境转化为图画书故事和插画的 AI 平台
- <a href="https://www.storywizard.ai/" target="_blank">Storywizard.ai</a> - Storywizard.ai 是 AI 教育工具，为孩子生成个性化的学习故事
- <a href="https://www.storybooks.app/" target="_blank">Storybooks</a> - Storybooks 是 AI 平台，一键生成可互动的儿童故事和插画
- <a href="https://www.aistorygenerator.org/" target="_blank">AI Story Generator</a> - AI Story Generator 是免费的 AI 写作工具，可快速生成故事
- <a href="https://www.story.com/" target="_blank">Story.com</a> - Story.com 用于创作带互动选项和 AI 动画视频的 AI 故事
- <a href="https://www.storybookai.app/" target="_blank">StoryBook AI</a> - StoryBook AI 是根据提示词创作互动儿童睡前故事与插画的平台
- <a href="https://storyspark.ai/" target="_blank">Story Spark</a> - Story Spark 是不限长度的 AI 故事生成器，支持续写和记忆
- <a href="https://fabled.ai/" target="_blank">Fabled AI</a> - Fabled AI 支持上传书籍并与书中角色对话，展开互动式文学冒险
- <a href="https://www.childbook.ai/" target="_blank">Child Book</a> - Child Book 是 AI 儿童故事生成工具，可快速制作个性化儿童书
- <a href="https://www.scarlettpanda.com/" target="_blank">Scarlett Panda</a> - Scarlett Panda 能在 30 秒内生成定制插画的睡前故事，适合家庭亲子共读
- <a href="https://www.bookbildr.com/" target="_blank">BookBildr</a> - BookBildr 是在线图画书编辑平台，集成 AI 插画、排版和 PDF/打印导出
- <a href="https://www.ainia.ai/" target="_blank">Ainia</a> - Ainia 是互动式情感教育平台，孩子与角色互动，激发同理心和想象力
- <a href="https://www.lumistory.ai/" target="_blank">Story Lumi</a> - Story Lumi 由 Colin Kaepernick 创立，帮助创作者发布文字和图像内容

<a id="group-social"></a>

## 对话与社交

<a id="section-chat-social"></a>

### 对话与社交

角色互动部分可结合[角色聊天与角色扮演应用](https://alignify.co/zh/tools/character-chat)理解；它们只是对话工具的一部分。

- <a href="https://character.ai" target="_blank">Character AI</a> - AI 角色聊天平台，可与个性鲜明、带持久记忆的角色对话，也能自己创建角色
- <a href="https://replika.com" target="_blank">Replika</a> - AI 陪伴聊天机器人，人设可定制，能进行开放式对话，覆盖移动端和网页端
- <a href="https://poe.com/" target="_blank">Poe</a> - Quora 旗下平台，在一个界面中使用多个 AI 聊天机器人与语言模型，支持用户自建 bot 并提供 API
- <a href="https://www.quark.cn/" target="_blank">Quark</a> - 阿里巴巴旗下的 AI 超级助手，整合搜索、笔记、云盘、文档与深度推理能力
- <a href="https://www.chai-research.com/" target="_blank">Chai Research</a> - 对话式 AI 平台，供用户与 AI 角色聊天
- <a href="https://monica.im/" target="_blank">Monica</a> - 接入 GPT、Claude、Gemini、DeepSeek 等多家模型的 AI 助手，功能覆盖聊天、搜索、写作、图像与视频生成和编程
- <a href="https://candy.ai" target="_blank">Candy AI</a> - AI 陪伴平台，用户可创建可定制的虚拟角色并在角色扮演场景中对话，含成人内容
- <a href="https://spicychat.ai" target="_blank">Spicychat.ai</a> - 网页端角色扮演聊天平台，不设内容审查，用户创建的 AI 角色库庞大，含成人（NSFW）内容
- <a href="https://crushon.ai" target="_blank">CrushOn.AI</a> - 成人向角色聊天平台，支持自定义角色并保留长期对话记忆，仅限 18 岁以上用户使用
- <a href="https://www.polybuzz.ai" target="_blank">Polybuzz</a> - AI 角色聊天平台，支持角色扮演对话与 AI 生成条漫，并可自定义创建角色
- <a href="https://www.chub.ai/" target="_blank">Chub AI</a> - 角色扮演 AI 聊天平台，支持自定义角色体验与互动叙事
- <a href="https://www.joyland.ai" target="_blank">Joyland</a> - AI 角色创建与聊天平台，涵盖动漫风陪伴角色、互动故事和角色扮演，配有社区角色库
- <a href="https://moescape.ai/" target="_blank">Moescape</a> - 动漫角色聊天与图像生成平台，前身为 Yodayo，现已更名 Moescape
- <a href="https://chaton.ai/" target="_blank">ChatOn</a> - 移动端 AI 聊天助手，组合对话模型、图像生成、联网搜索、文档处理与写作语气工具，用于写作和办公任务
- <a href="https://novaapp.ai" target="_blank">Nova</a> - 基于 GPT-4o 和 Gemini 的跨平台聊天助手，提供问答、写作帮助和文字校对
- <a href="https://www.popai.pro/" target="_blank">PopAi</a> - AI 助手应用，支持与文档对话、制作幻灯片、解答作业和生成图像
- <a href="https://chatboxai.app/" target="_blank">ChatBox</a> - 跨平台 AI 客户端，处理对话、文档、图片和代码，辅助写作与办公
- <a href="https://chatbotai.com/" target="_blank">Genie</a> - 集成 GPT-4o、Gemini 等模型的 AI 聊天助手，可用于写作、客服等场景
- <a href="https://heeyo.ai/" target="_blank">Heeyo AI</a> - 面向 3-11 岁儿童的多语言 AI 聊伴，内置教育游戏与自适应成长功能，由 OpenAI Startup Fund 和 Amazon Alexa Fund 支持
- <a href="https://www.autoresponder.ai/" target="_blank">AutoResponder.ai</a> - AI 自动回复机器人生成器，支持 WhatsApp、Telegram 等平台
- <a href="https://crosstalk.ai/" target="_blank">CrossTalk</a> - 基于圣经的对话式 AI 助手，用于互动学习、经文索引与祷告交流

<a id="group-industry-solutions"></a>

## 行业运营

<a id="section-industry-operations"></a>

### 行业运营

- <a href="https://pos.toasttab.com/" target="_blank">Toast</a> - 餐饮云端 POS 系统，整合点单、支付、员工管理与 AI 分析
- <a href="https://www.servicetitan.com/" target="_blank">ServiceTitan</a> - 供水暖、暖通空调和电工承包商使用的管理系统，涵盖调度排班、CRM 和财务功能
- <a href="https://www.mindbodyonline.com/" target="_blank">Mindbody</a> - Mindbody 服务健身、水疗与养生行业，预约、收款和营销都在一个平台上完成
- <a href="https://www.appfolio.com/" target="_blank">AppFolio</a> - 物业管理 SaaS，自动化处理租赁、财务与物业组合运营
- <a href="https://helsing.ai/" target="_blank">Helsing</a> - 为民主国家研发 AI 驱动的自主军事系统，包括作战无人机和水下无人机
- <a href="https://shield.ai/" target="_blank">Shield AI</a> - 国防科技公司，研发自主 AI 飞行系统（Nova、V-BAT），用于战术侦察与作战
- <a href="https://www.placer.ai/" target="_blank">Placer.ai</a> - 位置分析平台，提供线下客流、商圈与竞争情报，将访客趋势可视化
- <a href="https://www.picturethisai.com" target="_blank">PictureThis</a> - 植物识别应用，通过照片辨认植物种类，并提供病害诊断与养护指导
- <a href="https://www.homelight.com/" target="_blank">HomeLight</a> - 美国房产平台，为买家和卖家匹配经纪人，提供现金购房与先买后卖服务
- <a href="https://carbyne.com/" target="_blank">Carbyne</a> - 面向应急响应中心的云原生通信平台，以实时定位和视频交互提升救援效率
- <a href="https://altana.ai/" target="_blank">Altana</a> - 全球供应链数据平台，以 AI 提供风险可视化、合规与成本优化
- <a href="https://www.aidash.com/" target="_blank">AiDash</a> - 结合卫星与 AI 的工具，监测电力、水务等基础设施并支持远程巡检
- <a href="https://www.brightmachines.com/" target="_blank">Bright Machines</a> - 用机器人与 Physical AI 制造 AI 服务器、机架与存储等数据中心基础设施
- <a href="https://www.ottotheagent.com/" target="_blank">Otto</a> - AI 商旅助手，自动学习出行习惯并完成机票和酒店预订
- <a href="https://www.moego.pet/" target="_blank">MoeGo</a> - 面向宠物寄养、美容和日托门店的运营管理软件
- <a href="https://miovision.com/" target="_blank">Miovision</a> - 智能交通系统，通过传感器加 AI 提供实时交通监控与城市交通洞察
- <a href="https://www.spothopperapp.com/" target="_blank">SpotHopper</a> - 餐饮营销平台，覆盖建站、社交媒体、邮件和订位管理
- <a href="https://monograph.com/" target="_blank">Monograph</a> - Monograph 是建筑与工程设计团队的项目管理平台，统一管理项目预算、排期与开票
- <a href="https://gloo.com/" target="_blank">Gloo</a> - 连接信仰生态的技术平台，为教会、宗教组织和非营利机构提供 AI 驱动的内容分发与管理工具，已服务超 14 万家机构
- <a href="https://zoca.com/" target="_blank">Zoca</a> - 面向本地美容美发门店的 AI 营销平台，自动化获客与客户留存
- <a href="https://liberate.ai/" target="_blank">Liberate</a> - 金融服务行业的语音 AI agent 平台
- <a href="https://toma.com/" target="_blank">Toma</a> - 面向汽车行业的语音 AI agent 平台
- <a href="https://numa.com/" target="_blank">Numa</a> - 服务汽车行业的语音 AI agent 平台
- <a href="https://kea.ai/" target="_blank">Kea</a> - 餐厅电话与短信点餐软件，与 POS 系统对接
- <a href="https://voiceplug.ai/" target="_blank">Voiceplug</a> - 餐厅语音点餐软件，覆盖电话、得来速车道和自助点餐机场景
- <a href="https://hiauto.ai/" target="_blank">Hi Auto</a> - 为餐厅得来速车道提供语音接单的软件
- <a href="https://slang.ai/" target="_blank">slang.ai</a> - slang.ai 为餐厅提供语音 AI 电话应答，接待顾客咨询、处理订位
- <a href="https://loman.ai/" target="_blank">Loman.ai</a> - 为餐厅接听电话的 AI，处理点餐、订位和顾客咨询
- <a href="https://avoca.ai/" target="_blank">Avoca</a> - Avoca 专为家庭上门服务行业打造语音 AI agent，用于客服对话场景
- <a href="https://sameday.ai/" target="_blank">Sameday AI</a> - 面向暖通、水管、屋顶、光伏等上门服务行业的语音 AI 接线平台，全天候接听并下单，发起外呼营销，对接 ServiceTitan
- <a href="https://www.fleetworks.ai/" target="_blank">Fleetworks</a> - 货运语音 AI 平台，为经纪人与车队拨打跟踪电话、议价并订舱，全天候运转
- <a href="https://myplantin.com/" target="_blank">Plantin</a> - AI 植物识别与养护助手，凭照片识别植物，给出定制养护方案和病害诊断
- <a href="https://www.celebrateally.com/" target="_blank">CelebrateAlly</a> - AI 庆典助手，可生成定制演讲稿与贺卡文案，并辅助派对策划

<a id="group-discovery"></a>

## AI 工具发现

<a id="section-tool-discovery"></a>

### AI 工具目录

- <a href="http://generativeai.net/" target="_blank">Generative AI</a> - Generative AI 是独立博客兼咨询服务，做生成式 AI 的科普教学与资源汇总

---

## 关于

本目录由 **[Kostja](https://alignify.co)** 整理维护。产品事实在 AI Product Registry 中维护；本清单的收录与栏目位置属于编辑选择。

欢迎通过 [GitHub Issues](https://github.com/kostja94/awesome-ai-tools/issues) 或 **zyjstc@gmail.com** 提交建议。

## 许可证

本项目采用 [MIT 许可证](LICENSE)。

## 致谢

感谢贡献者与 AI 社区的支持和反馈。
