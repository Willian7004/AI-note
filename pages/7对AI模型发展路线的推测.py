import streamlit as st

st.title("对AI模型发展路线的推测")
st.write("这部分内容参考了目前的AI模型的情况以及网友的观点，讨论了我和一些网友比较关注的问题。仅代表个人看法，不保证准确。")
st.sidebar.title("对AI模型发展路线的推测")
st.sidebar.write("1.思维链模型和合成数据")
st.sidebar.write("2.小参数量模型")
st.sidebar.write("3.多模态模型和世界模型")
st.sidebar.write("4.绘画模型/视频模型的参数量、效果和成本")
st.subheader("1.思维链模型和合成数据", divider=True)
st.write("思维链模型使用思维链和多次采样等方法提高性能，大部分方法会只能带来一次提升并且增加推理成本。目前高质量公开数据基本耗尽，但其中的推理数据偏少。使用思维链模型合成数据后，可以训练推理能力更强的基础模型，使用这样的基础模型能训练出性能更高的思维链模型。这样可以在编程和推理等思维链有优势的领域带来提升，但在其它领域提升不明显。")
st.write("思维链模型的换代在编程和数学竞赛等测试集中有提升，并且在不少测试集达到或超过人类水平，但在Frontier Math等研究性测试集中表现较差。随着模型换代，思维链模型应该能逐步用于辅助技术、教育和医疗等工作，但短期内还不能完全代替人工。")
st.subheader("2.小参数量模型", divider=True)
st.write("小参数量模型的需求至少在硬件性价比没有大幅提升前是一直存在的。进行数据处理、对大参数量模型进行知识蒸馏和合成思维链数据等方法可以提高小参数量模型的效果。")
st.write("phi4的经验表明，14b参数量可以达到接近旗舰模型的水平。Deepseek R1的蒸馏模型也说明目前小型化进度在14b参数量，但在best of 64测试中7b以上模型都能达到教师模型的表现，说明能提高可靠性的话以后7b参数量模型有望接近旗舰模型水平。")
st.write("根据在测试集的表现，至少短期内3b和7b参数量都是不少常规任务的门槛，不过由于支持3b模型的手机和支持7b模型的电脑普及率足够高，这一问题影响不大。")
st.subheader("3.多模态模型和世界模型", divider=True)
st.write("使用实拍或其它满足要求的形式创建的数据训练的模型一般可以称为世界模型，包括视频生成模型、3D生成模型、交互式视频模型和端到端无人驾驶模型等。由于这类数据比较丰富，短期内不会耗尽，模型性能可以持续提升。")
st.write("对多模态模型来说，使用更多实拍数据训练也有助于提高空间理解等能力，扩展任务范围，用于视频聊天和解决实际问题。交互式视频模型能力提升有望突破实时渲染效果瓶颈，改变游戏等应用的形式。")
st.subheader("4.绘画模型/视频模型的参数量、效果和成本", divider=True)
st.write("第一个能接近相应分辨率的细节上限的绘画模型FLux.1 dev是12b参数量，而后来的Stable Diffusion3.5 large是8.3b参数量，实测生成细节不及FLux.1 dev；Hunyuan Video作为第一个达到同期优秀闭源视频模型水平的开源视频模型，参数量为13b，因此这个参数量有可能是绘画/视频模型性价比最高的参数量。")
st.write("生成效果上Flux.1主要改进了细节和人物生成，Hunyuan Video在光照上有一定提升。但即使是Veo2等最新模型，在严格标准下光照和物理表现都不算好，短期内应该也达不到接近离线渲染的效果，但在要求不高的场景可以逐步应用。")
st.write("在进行显存优化后，以上两个模型都可以在主流配置运行，但Flux.1 dev的显存门槛约为3.1g，Hunyuan Video在8g显存只能在最大分辨率生成较短的视频，说明视频模型的成本还是相对较高。不过Hunyuan Video的图生视频版本发布后可以用上一个视频最后一帧和相同随机种继续生成后续内容，应该能解决低显存生成的视频长度受限问题。")
st.write("一些有批量生成需求的用户认为Flux.1 dev生成较慢，不过如果是轻度使用，在主流配置时的生成速度足够。Hunyuan Video在主流配置的生成速度比较慢，但使用第三方api平台，例如在Siliconflow的价格是每个视频0.7元（完整长度），大部分用户应该可以接受。视频模型中成本问题明显的主要是一些参数量较大或架构优化不足的商业模型，但目前也有Vidu2.0等主打快速生成、低成本的模型。由于模型结构和小型化还有改进空间，以后应该会有成本更低的视频模型。")
