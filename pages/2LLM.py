import streamlit as st

st.title("LLM")
st.sidebar.title("LLM")
st.sidebar.write("1.旗舰模型")
st.sidebar.write("2.多模态模型")
st.sidebar.write("3.思维链模型")
st.sidebar.write("4.小型化旗舰模型")
st.sidebar.write("5.端侧模型")
st.sidebar.write("6.无审查模型")
st.sidebar.write("7.长序列模型")
st.sidebar.write("8.模型部署")
st.subheader("1.旗舰模型", divider=True)
st.write("旗舰模型参数量较大，运行成本较高但可完成的任务也较多。Deepseek v3算是的一个下一代模型，而其它厂商的下一代模型，包括Grok3和GPT5均未发布，因此Deepseek v3具有性能优势，也是第一个发布时性能超越所有闭源模型的开源模型，并且通过混合专家架构避免成本过高。以下是几个模型的对比")
import pandas as pd
df = pd.DataFrame({
    "模型": ["Deepseek v3", "Qwen2.5 72B", "Llama3.1 405B", "Claude3.2 Sonnet", "GPT-4o"],
  "架构": ["MoE", "Dense", "Dense", "#", "#"],
    "激活参数": ["37B", "72B", "405B", "#", "#"],
    "总参数": ["671B", "72B", "405B", "#", "#"],
    "MMLU": [88.5, 85.3, 88.6, 88.3, 87.2],
    "MMLU-Redux": [89.1, 85.6, 86.2, 88.9, 88],
    "MMLU-Pro": [75.9, 71.6, 73.3, 78, 72.6],
    "DROP": [91.6, 76.7, 88.7, 88.3, 83.7],
    "IF-Eval": [86.1, 84.1, 86, 86.5, 84.3],
    "GPQA-Diamond": [59.1, 49, 51.1, 65, 49.9],
    "SimpleQA": [24.9, 9.1, 17.1, 28.4, 38.2],
    "FRAMES": [73.3, 69.8, 70, 72.5, 80.5],
    "LongBenchv2": [48.7, 39.4, 36.1, 41, 48.1],
    "HumanEval-Mul": [82.6, 77.3, 77.2, 81.7, 80.5],
    "LiveCodeBench(cot)": [40.5, 31.1, 28.4, 36.3, 33.4],
    "LiveCodeBench(Pass@1)": [37.6, 28.7, 30.1, 32.8, 34.2],
    "Codeforces": [51.6, 24.8, 25.3, 20.3, 23.6],
    "SWEVerified": [42, 23.8, 24.5, 50.8, 38.8],
    "Aider-Edit": [79.7, 65.4, 63.9, 84.2, 72.9],
    "Aider-Polyglot": [49.6, 7.6, 5.8, 45.3, 16],
    "AIME2024": [39.2, 23.3, 23.3, 16, 9.3],
    "MATH-500": [90.2, 80, 73.8, 78.3, 74.6],
    "CNMO2024": [43.2, 15.9, 6.8, 13.1, 10.8],
    "CLUEWSC": [90.9, 91.4, 84.7, 85.4, 87.9],
    "C-Eval": [86.5, 86.1, 61.5, 76.7, 76],
    "C-SimpleQA": [64.1, 48.4, 50.4, 51.3, 59.3]
})

df

st.subheader("2.多模态模型", divider=True)
st.write("多模态模型开源处理图片。对于非思维链模型，闭源模型中Claude3.5 Sonnet表现最好，开源模型中Qwen2VL 72B表现最好。对于思维链模型，闭源模型中o1表现最好，开源模型中QvQ 72B Preview表现最好。以下是几个模型的对比")
df2= pd.DataFrame({
    'Model': ['QvQ-72B-preview', 'OpenAI o1', 'GPT-4o', 'Cloude3.5 Sonnet', 'Qwen2-VL 72B'],
    'MMMU': [70.3, 77.3, 69.1, 70.4, 64.5],
    'MathVista': [71.4, 71.0, 63.8, 65.3, 70.5],
    'MathVision': [35.9, None, 30.4, 35.6, 25.9],
    'OlympiadBench': [20.4, None, 25.9, None, 11.2]
})

df2

st.subheader("3.思维链模型", divider=True)
st.write("思维链模型可以通过增加推理步骤来提高性能。目前最优秀的闭源思维链模型是OpenAI o1，最优秀的开源思维链模型是Qwq 32b preview，以下是几个模型的对比（由于不少模型不是同时测试，表中只保留了有较多模型进行的测试，另外使用非思维链模型中表现最好的Deepseek v3作为对照）")
df3= pd.DataFrame({
     "Model": ["DeepSeek-R1-Lite-Preview","QwQ-32B-Preview","OpenAI o1","o1 mini","o3","o3 mini(high)","Deepseek v3"],
    "AIME": [52.5,50.0,83.3,63.6,96.7,83.6,39.2],
    "GPQA Diamond": [58.5,65.2,78.0,60.0,87.7,70.0,59.1],
    "Codeforces": [1450,None,1891,None,2727,None,None],
    "LiveCodeBench": [51.6,50.0,None,None,None,None,40.5]
})

df3
st.write("表中的OpenAI o3系列只开放了安全测试，还没有正式发布。o3 mini相比o1系列有性价比优势，o3在ARC AGI测试能达到人类水平，但成本高于人工，在EpochAI Frontier Math达到25.2%准确度。")

st.subheader("4.小型化旗舰模型", divider=True)
st.write("有几个系列的模型在有模型达到GPT4水平后开始小型化并保持性能，其中闭源模型主要有Gemini2.0 Flash和Yi Lighting，开源模型主要有phi4，14b参数量适合在PC部署。")
st.subheader("5.端侧模型", divider=True)
st.write("端侧模型用于手机或在PC后台运行，主要考虑7b和3b参数量，并且只能使用开源模型。考虑多语言后有优势的多模态模型有Qwen2 VL 7B和Megrez 3B Omni，单模态模型有Qwen2.5 7B和Qwen2.5 3B。")
st.subheader("6.无审查模型", divider=True)
st.write("比较新的模型大部分进行了对齐，可以避免生成不道德的内容，但在角色扮演等用途仍需要未对齐的模型，在写作中未对齐的模型也有更好的表现。")
st.write("目前效果最好的无审查模型是旧版CommandR和CommandR+，官方版本是未对齐的。另外大部分常见模型有第三方的去对齐版本。")
st.subheader("7.长序列模型", divider=True)
st.write("处理或生成较长的文章需要支持较大输入或输出上下文长度的模型，考虑对api成本的影响，这类只讨论开源模型。目前比较好的开源长上下文模型是InternLM2.5 7b 1M和GLM4 9b 1M。长输出模型只有使用longwriter数据集微调的模型，目前只有GLM4 9b、Qwen2.5 7B和Llama3.1 8b。")
st.subheader("8.模型部署", divider=True)
st.write("有多个运行框架可以部署LLM，我目前用的是Ollama。Ollama的优势是安装比较方便，还可以直接在命令行下载量化后的模型。")
st.write("Ollama没有GUI但可以通过http请求或使用Python和Javascript等语言的库文件整或到应用中。我目前通过Chatbox使用Ollama的单模态模型和调用线上模型的api。调用Ollama的多模态模型开始时用了Openwebui，但由于需要在安装时部署嵌入模型，比较麻烦，就改用了使用Streamlit开发的Local Multimodal AI Chat。Local Multimodal AI Chat可以调用Ollama的多模态模型和嵌入模型，虽然有不支持流式响应和运行慢的问题，但由于部署方便还是考虑替换Openwebui。")
st.write("我目前部署的模型有phi4、MiniCPM v2.6（用于多模态，效果更好的Qwen2 VL 7b目前还不能在Ollama运行）、InternLM2.5 7b（用于长序列）。嵌入模型用了Bge-m3，支持多语言，在嵌入模型中参数量较大，性能也较高。")
