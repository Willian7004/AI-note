import streamlit as st

st.title("对AI模型发展路线的推测")
st.write("这部分内容参考了目前的AI模型的情况以及网友的观点，讨论了我和一些网友比较关注的问题。仅代表个人看法，不保证准确。")
st.sidebar.title("对AI模型发展路线的推测")
st.sidebar.write("1.思维链模型和合成数据")
st.sidebar.write("2.小参数量模型")
st.sidebar.write("3.多模态模型和世界模型")
st.sidebar.write("4.绘画模型/视频模型的参数量和成本")
st.sidebar.write("5.提高免费的在线模型的水平")
st.subheader("1.思维链模型和合成数据", divider=True)
st.write("思维链模型使用思维链和多次采样等方法提高性能，大部分方法会只能带来一次提升并且增加推理成本。目前高质量公开数据基本耗尽，但其中的推理数据偏少。使用思维链模型合成数据后，可以训练推理能力更强的基础模型，使用这样的基础模型能训练出性能更高的思维链模型。这种方式带来的提升可能有上限但在几代以内应该是有效的，但是在提高思维链最大长度上可能还需要一些人工创建的数据。")
st.write("思维链模型的发展方向是进一步提高性能从而更好地为技术工作者提供帮助，也有望突破以应试为主的教育理念，使教育更注重科研能力。")
st.subheader("2.小参数量模型", divider=True)
st.write("小参数量模型的需求至少在硬件性价比没有大幅提升前是一直存在的。对大参数量模型进行知识蒸馏以及把数据处理为问答对来获取出现次数较少的信息等方法可以提高小参数量模型的效果。")
st.write("phi4的经验表明，14b参数量可以达到接近旗舰模型的水平，但由于新一代模型出现以及缺少实测数据，还不能完全确定这一结论。以后能否用更小参数量实现这一水平也要等有相应的模型出现才能确定。")
st.write("根据在测试集的表现，至少短期内3b和7b参数量都是不少常规任务的门槛，不过由于支持3b模型的手机和支持7b模型的电脑普及率足够高，这一问题影响不大。")
st.subheader("3.多模态模型和世界模型", divider=True)
st.write("使用实拍或其它满足要求的形式创建的数据训练的模型一般可以称为世界模型，包括视频生成模型、3D生成模型、交互式视频模型和端到端无人驾驶模型等。由于这类数据比较丰富，短期内不会耗尽，模型性能可以持续提升。")
st.write("对多模态模型来说，使用更多实拍数据训练也有助于提高空间理解等能力，扩展任务范围，用于视频聊天和解决实际问题。视频模型能力提升有望降低视频制作成本；交互式视频模型能力提升有望突破实时渲染效果瓶颈。")
st.subheader("4.绘画模型/视频模型的参数量和成本", divider=True)
st.write("第一个能接近相应分辨率的细节上限的绘画模型FLux.1 dev是12b参数量，而后来的Stable Diffusion3.5 large是8.3b参数量，实测生成细节不及FLux.1 dev；Hunyuan Video作为第一个达到同期优秀闭源视频模型水平的开源视频模型，参数量为13b，因此这个参数量有可能是绘画/视频模型性价比最高的参数量。")
st.write("在进行显存优化后，以上两个模型都可以在主流配置运行，但Flux.1 dev的显存门槛约为3.1g，Hunyuan Video在8g显存只能生成较短的720p视频，说明视频模型的成本还是相对较高。不过Hunyuan Video的图生视频版本发布后可以用上一个视频最后一帧和相同随机种继续生成后续内容，应该能解决低显存生成的视频长度受限问题。")
st.write("一些有批量生成需求的用户认为Flux.1 dev生成较慢，不过如果是轻度使用，在主流配置时的生成速度足够。Hunyuan Video在主流配置的生成速度比较慢，但使用第三方api平台，例如在Siliconflow的价格是每个视频0.7元（完整长度），大部分用户应该可以接受。视频模型中成本问题明显的主要是一些参数量较大或架构优化不足的商业模型，考虑市场因素，成本不高于Hunyuan Video的视频模型会成为主流。")
st.subheader("5.提高免费的在线模型的水平", divider=True)
st.write("通用AI模型的大部分用户实际上是对AI了解不多的用户，其中大部分会选择免费的在线模型。Huggingface和魔塔社区等模型平台都分配了一定的资源用于提供模型的demo，但用户较多时需要排队，并且一般只作为测试用途，对AI了解较少的人一般也不了解这类途径，因此后面主要讨论面向一般用户的应用的情况。")
st.write("LLM方面，从成本角度讲，云端部署使用并发有成本优势，而一般用户使用量不大，激活参数量14b的模型一般可以免费提供，14b的phi4已经达到接近旗舰模型的性能。实际上各厂商一般只提供自家产品，大多没有接近phi4的模型，就没有免费提供这个规格的模型。deepseek可能偏向企业用户，并且模型成本控制优秀，就免费提供了旗舰模型。对于大部分厂商，免费提供的LLM的水平的提升主要看自家小参数量模型的发展进度。")
st.write("AI绘画和AI视频模型的算力成本相对较高。AI绘画模型中蒸馏模型的成本不高，例如Siliconflow免费提供了Flux.1 schnell的模型的有限频率使用。但Siliconflow同样不面向一般用户，大部分平台仍然只提供基于Stable Diffusion1.5的模型。具体原因可能是要满足响应较多时的成本控制需求或者避免对新模型二次开发。考虑二次开发进度，长期来看还是有望免费提供Stable Diffusion 3.5 medium tubro或更大的模型。AI视频模型算力成本更高，只有Siliconflow提供了成本最低的LTX Video的有限频率使用，大部分厂商开发的模型成本更高，即使能免费提供也要长时间排队。虽然前面提到12b可能是比较合适的参数量，但为了向更多用户提供，各厂商还是有可能开发小参数量且生成快的视频模型。")
