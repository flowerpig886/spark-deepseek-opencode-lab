# 单并发缓存改动与回退

原固定版本以 `int(parallel) > 1` 决定是否走 MultiDecoder 调度。我们让 `parallel=1` 且显式开关打开时，也走单槽 MultiDecoder / Scheduler，以复用前缀缓存。没有修改权重、量化或输出预算。

| 标识 | 固定值 |
|---|---|
| 本地基础镜像标签 | tensorfold-dsv41:cb4ceaff2b8c |
| 本地基础镜像 ID | sha256:669a0e890ab2686c5fbff981ade4c9d5519454468e38d19d3a1c6179a04a7ad8 |
| 本地派生镜像标签 | tensorfold-dsv41:localbench-single-lane-cache-v1 |
| 已运行派生镜像 ID | sha256:516c3ca473fb413a0973d32d7c90c87a1d25472bdb7a79e850008e8a7cb03702 |
| 开关 | TF_DS_SINGLE_LANE_CACHE=1 |

这些是测试环境的本地镜像标识，并未推送为公共镜像；重新构建的 ID 也可能因构建元数据不同而变化。

## 准备方法

先按上游固定配方构建基础镜像并提取其 `tensorfold/families/deepseek_v41/cuda/engine.py`，放到独立工作目录，不覆盖基础镜像的源文件。脚本严格核对原文件和目标文件 SHA256，不接受仅仅“长得像”的新版源码。

```sh
python scripts/prepare_cache_patch.py /path/to/original/engine.py /path/to/build/engine.py
docker build --network=none --pull=false -f configs/cache.Dockerfile -t tensorfold-dsv41:local-cache-build /path/to/build
```

Dockerfile 参数指向本地基础镜像。两台节点需使用同一构建结果；可通过局域网传递镜像，再在两边核对镜像 ID。应用前保留原配方和基础镜像，确认实际并发仍为 1。此处只给出缓存层的构建材料，不自动修改上游启动脚本或宿主机参数。

## 已得到的证据

2026-11-02 的配对验收：66 次功能/代码请求两边都通过 65 次，66 次输出逐字相同；6 次仓库尝试两边都完成 3 次。固定样本未观察到新增回退，不代表普遍质量等价。

6 次仓库尝试合计耗时从 479.76 秒降到 292.27 秒（约 39.1%）。包含失败尝试，同一题的不同种子可能复用前缀；不能宣传成“所有编码任务快39%”，也不能把它当作今天 OpenCode 的成对加速结果。

## 回退

用部署配方的协调停止入口停掉两边 rank，并先停止自动恢复；切回已保留的基础镜像，关闭该开关，恢复保存的配方参数，再做健康、文本、JSON、工具调用检查。启动失败时恢复保存的宿主机配置。具体入口名称取决于读者部署的配方，本草稿没有发放通用启停脚本。
