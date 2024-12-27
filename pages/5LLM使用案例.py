import streamlit as st

st.title("LLM使用案例")
st.sidebar.title("LLM使用案例")
st.sidebar.write("1.思维链模型解题")
st.sidebar.write("2.编程")
st.sidebar.write("3.短文写作")
st.sidebar.write("4.长文写作")
st.subheader("1.思维链模型解题", divider=True)
st.write("这里使用的模型是Deepseek-R1-Lite-Preview，所有题目回答正确。")
with open("files/题目1.txt", "r", encoding='utf-8') as f:
            t1= f.read()
with st.container(height=240):
    st.write(t1)
with open("files/题目2.txt", "r", encoding='utf-8') as f:
            t2= f.read()
with st.container(height=240):
    st.write(t2)
with open("files/题目3.txt", "r", encoding='utf-8') as f:
            t3= f.read()
with st.container(height=240):
    st.write(t3)
st.subheader("2.编程", divider=True)
st.write("在开源思维链模型出现后，我暂时没有使用AI模型编程。如果有详细的提示词，非思维链模型可以编写大部分程序，使用思维链模型可以适度精简提示词，但也可能导致程序部分细节不符合预期。以下仓库是我之前使用AI开发的程序，大多使用Deepseek Coder v2，仓库中包含编写对应程序的提示词。")
st.write("https://github.com/Willian7004/LLM-Code-Tools")
st.write("https://github.com/Willian7004/LLM-Document-Tools")
st.write("https://github.com/Willian7004/LLM-novel-writer/tree/v0.9")
st.subheader("3.短文写作", divider=True)
st.write("我部署LLM后经常使用介绍一个地点的指令进行测试，这部分的文章也来源于这项流程。个人感觉Qwen2 72b在写作上比较优秀，后面的模型引入了不少指令数据后反而导致在写作上缺少亮点。")
with open("files/qwen2底特律.txt", "r", encoding='utf-8') as f:
            t4= f.read()
with st.container(height=240):
    st.write(t4)
with open("files/qwen2威尼斯.txt", "r", encoding='utf-8') as f:
            t5= f.read()
with st.container(height=240):
    st.write(t5)
with open("files/qwen2乌鲁木齐.txt", "r", encoding='utf-8') as f:
            t6= f.read()
with st.container(height=240):
    st.write(t6)
st.subheader("4.长文写作", divider=True)   
st.write("使用longwriter模型可以直接生成长文，个人感觉longwriter GLM4 9b效果相对较好，但由于参数量较小，实际效果不太好。")
with open("files/longwriter glm4 9b法国介绍.txt", "r", encoding='utf-8') as f:
            t7= f.read()
with st.container(height=240):
    st.write(t7)
with open("files/longwriter glm4 9b曲速航天 .txt", "r", encoding='utf-8') as f:
            t8= f.read()
with st.container(height=240):
    st.write(t8)    
st.write("对于各部分关联较小的游记等文章，可以生成摘要并分别生成各部分，以下文章使用deepseek v2生成。")
with open("files/deepseek-v2美国游记.txt", "r", encoding='utf-8') as f:
            t9= f.read()
with st.container(height=240):
    st.write(t9)
with open("files/deepseek-v2法国游记.txt", "r", encoding='utf-8') as f:
            t10= f.read()
with st.container(height=240):
    st.write(t10)
st.write("对于小说等各部分关联较大的文章，需要向模型输入上下文和各部分摘要，以下文章使用上述的小说agent项目调用deepseek v2.5生成，目前该项目仍不完善，生成时部分章节内容重复。")
with open("files/极速梦想.txt", "r", encoding='utf-8') as f:
            t11= f.read()
with st.container(height=240):
    st.write(t11)
