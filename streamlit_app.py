import streamlit as st

st.title("概述")
st.sidebar.title("概述")
st.sidebar.write("1.技术路线选择")
st.sidebar.write("2.项目内容")
st.subheader("1.技术路线选择", divider=True)
st.write("本人对Python了解相对较多。此前为了接触UI和前端了解了HTML、CSS、JavaScript以及Ionic框架等，但感觉开发较为繁琐并且难以结合Python生态。因此了解了Python中的NiceGUI和Streamlit两个GUI库。考虑到方便编写和部署，本项目使用Streamlit库。")
st.subheader("2.项目内容", divider=True)
st.write("2.1记录当前各类AI模型中有优势的模型，以及我部署开源模型的情况。")
st.write("2.2运行AI模型的硬件方案，其中会更多地介绍适合个人用户的方案。")
st.write("2.3文中提到的一些AI模型的使用案例。")
st.write("在边栏中选择其它页面，页面宽度较小时需要通过右上角的Menu按钮展开边栏。")
