# 署名与授权说明（发布前确认）

此草稿没有放置最终LICENSE文件，没有替作者作最终许可选择。没有LICENSE时，不应把整个草稿描述为已完成开源授权。

文档、数字导出和新写的辅助脚本，与上游模型、引擎、评测数据分别对待：

- 模型权重不随仓库分发，向DeepSeek/量化发布方获取并查看对应许可。
- TensorFold上游及各fork以对应版本LICENSE/NOTICE为准；[参考fork的LICENSE](https://github.com/bertholomus/TensorFold/blob/deepseek-v41-tp2/LICENSE)为Apache-2.0。不能因为模型是MIT，就把引擎也标成MIT。
- 缓存脚本仅定位并改写固定版本的一行，不附带完整上游engine.py；实际派生源码/镜像再分发前，应随对应上游授权和通知要求整理。
- 当前未复制完整OpenCode验证插件、pydicom源码、隐藏测试或SWE-bench参考补丁。数字结果仍应注明来源与方法；这不替代第三方数据许可核查。

上游项目链接在README中。没有任何上游背书、联合发布或官方评分主张。
