# 固定环境与配置

## 硬件和软件

| 项目 | 本轮记录 |
|---|---|
| 推理节点 | 两台 DGX Spark，GB10，各标称 128GB 统一内存 |
| 节点互联 | ConnectX-7，RoCE；测试应用的网卡 MTU 9000，RDMA active_mtu 4096 |
| 控制端 | Windows，OpenCode 桌面版 2.2.5 自带后端；控制端 GPU 不承担本轮推理 |
| Spark 驱动 | 580.159.03 |
| Spark 内核 | 6.17.0-1022-nvidia，aarch64 |
| Docker | 29.2.1 |
| 模型 | DeepSeek-V4.1-Flash-1017 EXL3 2.9bpw |
| 配方记录的提交 | 6fae0846fcdd9b9fc5c054fd91e17bc86b659764 |
| 配方声明的引擎源 | Elevatormusic/TensorFold，cb4ceaff2b8c |

提取的引擎源码目录没有 Git 元数据，因此没有独立从该目录验证提交。配方声明的短提交、镜像 ID 与实际文件 SHA256 分别记录，不能互相替代。

两节点磁盘均保留模型和 Engram 文件视图；这是磁盘存储，不等于全部常驻统一内存。先前下载核验记录约 413.9GB、72 文件；本轮没有换权重。量化仓库不附带两张 Engram 表，须按模型卡使用 **1017 基座对应**的表，不能混用旧版。

## 运行参数

| 参数 | 值 |
|---|---:|
| Tensor parallel | 2 |
| 并发 | 1 |
| 视觉 | 关闭 |
| thinking / reasoning_effort | 开启 / low |
| temperature / top_p | 1 / 1 |
| max_tokens | 32768 |
| parallel_tool_calls | false |
| OpenCode context / output | 131072 / 32768 |
| 引擎 context_length | 1048576 |
| 仓库单次工具/模型预算 | 最多 80 次模型调用或 1200 秒，先到为止 |

声明窗口包含输入和输出等预算约束；131072−32768=98304 只是名义输入余量，还要考虑工具定义、系统提示及平台预留。不要把输出预算压低来获得表面提速。

## 宿主机临时配置

已记录的组合包括：swappiness=10、compaction_proactiveness=0、min_free_kbytes=1048576、THP=never、推理 slice 禁止 swap、earlyoom 活跃、网卡 MTU=9000。这里没有证明每一项分别带来提速，也没有主张这些数值适合所有机器。

本地使用可恢复的 profile 工具，应用前保存原值，停止后恢复；没有改另一个模型的启动配置。社区迁移时应自行保存每台机器原值，并核验接口名、RDMA 路径及内存余量。此草稿不提供可直接修改任意主机的通用 sudo 脚本。

## OpenCode 接入示例

见 [opencode.example.json](../configs/opencode.example.json)。它展示本轮观测到的 **2.2.5 配置结构**，不是所有 OpenCode 版本通用的格式。`local` 是本地无鉴权服务的示例占位值，不是真实密钥。

客户端通过 SSH 本地转发访问 Spark 的回环 API：

```sh
ssh -N -L 18892:127.0.0.1:8892 SPARK_USER@SPARK_HOST
```

主机名和用户名由读者自行替换。示例 baseURL 对应本机 18892。此转发只提供连接方式，不自动配置项目测试命令、完成门槛或模型服务。模型下载应在 Spark 上执行；本次控制端仅承担局域网调用和记录。

## 日常采用范围

保留 low 和单槽缓存。分阶段思考仅有小样本候选证据，未全局启用。每个真实项目仍须指定原始回归测试、构建命令及完成条件；公开测试变绿或 Agent 生成完成回执，不能代替独立验收。
