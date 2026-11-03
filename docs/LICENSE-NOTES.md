# 署名、许可与上游归属

维护与实测：[@flowerpig886](https://github.com/flowerpig886)。维护者于2026-11-03确认：文档与报告使用CC BY 4.0，新写的辅助脚本使用MIT，允许在各许可条件下转载、修改和商用。完整范围见根目录[LICENSE.md](../LICENSE.md)。

文档许可正文：[CC BY 4.0](../LICENSES/CC-BY-4.0.txt)；代码许可正文：[MIT](../LICENSES/MIT.txt)。数字结果仅就原创呈现与汇编中可许可的权利适用CC BY 4.0，不主张垄断原始事实。

上游模型、引擎和评测材料分别对待：

- 模型权重不随仓库分发，向DeepSeek/量化发布方获取并查看对应版本许可。
- TensorFold上游及各fork以对应版本LICENSE/NOTICE为准；[参考fork的LICENSE](https://github.com/bertholomus/TensorFold/blob/deepseek-v41-tp2/LICENSE)为Apache-2.0。不能因为模型是MIT，就把引擎也标成MIT。
- 缓存准备脚本是本项目辅助代码，只定位并改写固定版本的一行，不附带完整上游engine.py。其MIT许可不改变上游源码或派生镜像适用的许可；再分发派生源码/镜像时须保留相应上游授权及通知。
- 配置示例中引用第三方包名称，不重新授权这些包。完整OpenCode项目验证插件与桥接没有打包进本仓库。
- 未复制pydicom完整源码、隐藏测试或SWE-bench参考补丁。题目标识和结果用于说明方法与成败，不代表获得上游背书。

转载署名示例：

> 来源：flowerpig886，双 DGX Spark × DeepSeek × OpenCode：配置与实测记录，CC BY 4.0。项目：https://github.com/flowerpig886/spark-deepseek-opencode-lab 。如有修改，请另行注明。

项目对自身新增材料的授权不替代任何第三方权利或许可。
