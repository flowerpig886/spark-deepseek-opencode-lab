# 双 DGX Spark × DeepSeek × OpenCode：配置与实测记录

维护与实测：[@flowerpig886](https://github.com/flowerpig886)

用两台 128GB DGX Spark 运行 DeepSeek-V4.1-Flash-1017 EXL3 2.9bpw，再接入 Windows OpenCode，实际修仓库、运行工具和测试恢复能力。

这份报告希望回答：**这套设备能不能稳定工作，以及工作结果能不能放心交给它。**

记录日期：2026-11-03。状态：v0.1.0 预览版。数据来自我们自己的固定样本，不是官方 SWE-bench 分数。

## 先看结果

| 项目 | 实测结果 | 能说明什么 |
|---|---|---|
| OpenCode 接入 | 真实小修复通过，14 请求，38.46 秒 | 接入、工具链和参数可用 |
| 新仓库修复 | 3 道 pydicom 题 × 2 种子，补丁及完整任务均 4/6 | 有失败，不能据此保证无人值守可靠 |
| 连续负载 | 65.01 分钟，19 个串行任务，706 请求、687 次工具调用 | 服务耐久；重复任务不算新质量样本 |
| 基础恢复 | 两种流程均能恢复会话，恢复后修复正确仅 1/2 | 恢复流程与修复质量分开判断 |
| 实际修改后的恢复补测 | 5 分钟内未观察到生产代码改动，按预登记上限停止 | 未进入该检查点的重启环节，这项仍未验证 |

**我们的结论：适合带独立验证和人工复核的本地编程自动化，尚不足以认定为无人值守长任务主力。**

## 本轮配置

- 2 × NVIDIA DGX Spark，每台标称 128GB 统一内存，ConnectX-7 直连。
- DeepSeek-V4.1-Flash-1017，EXL3 2.9bpw，TensorFold TP2。
- 单并发，关闭视觉，启用已验收的本地单槽缓存改动。
- low 思考，temperature=1，top_p=1，每请求输出上限 **32768**。
- Windows OpenCode 2.2.5 桌面版自带后端；通过其 API 自动执行，未模拟 GUI 点击。
- OpenCode 声明窗口 131072；引擎配置 1048576。两者不是同一个验收结论。

连续阶段最大记录的 `tokens.input + tokens.cache.read` 为 **95499**。这是观测范围，不是极限测试；也没有在该输入规模实测生成完整 32768 tokens。

## 从哪里开始

1. [环境与版本](docs/CONFIGURATION.md)：硬件、固定参数、内存与网络设置。
2. [缓存改动与回退](docs/CACHE-CHANGE.md)：为什么单并发也需要缓存，以及怎样准备派生镜像。
3. [测试方法](docs/METHODOLOGY.md)：题目、种子、工具和成功判定。
4. [完整结果与失败](docs/RESULTS.md)：保留成功、失败和未验证项。
5. [复现范围](docs/REPRODUCTION.md)：哪些材料已提供，哪些还不是开箱即用。
6. [第一次发布 GitHub](docs/FIRST-PUBLISH.md)：给首次发布者的简短步骤。

## 这个仓库提供什么

配置参考、带版本保护的缓存修改脚本、脱敏后的数字结果和报告。它没有附带模型权重、私有镜像、原始会话数据库或完整评测题库。

本地缓存派生镜像不是公开下载地址。OpenCode 示例也不包含本轮项目专用验证插件；只套用示例配置，不等于复现了本轮完整 Agent 流程。详见[复现范围](docs/REPRODUCTION.md)。

## 上游与致谢

- [DeepSeek 原始 1017 模型](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017)
- [LibertAI EXL3 2.9bpw 权重](https://huggingface.co/LibertAIDAI/DeepSeek-V4.1-Flash-1017-EXL3-2.9bpw)
- [测试配方记录中的 TensorFold 源地址](https://github.com/Elevatormusic/TensorFold)，以及 [bertholomus/TensorFold](https://github.com/bertholomus/TensorFold)
- [相关双 Spark 部署配方](https://github.com/MiaAI-Lab/DeepSeek-v4.1-Flash-1017-2x-DGX-Sparks)
- [OpenCode](https://opencode.ai/)、[SWE-bench](https://github.com/SWE-bench/SWE-bench)、[pydicom](https://github.com/pydicom/pydicom)

模型和推理引擎来自上游；本项目贡献是本地配置改动、测试与整理。相关配方链接用于参考，不代表上游背书或逐版本等同。授权范围见 [LICENSE-NOTES](docs/LICENSE-NOTES.md)。

## 许可

文档与报告：**CC BY 4.0**；新写的辅助脚本和配置：**MIT**。署名：flowerpig886。上游材料保留原有许可。完整范围与正文见 [LICENSE.md](LICENSE.md)。
