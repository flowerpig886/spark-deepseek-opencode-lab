# 第一次发布到 GitHub

可以先把它看成“带文件夹结构的项目主页”。README是首页，docs是详细说明，results是可查的数据，后续每次更新都能留下版本记录。

## 建议的第一版

- 仓库名：`spark-deepseek-opencode-lab`，只是建议，可以更改。
- 简介：`双 DGX Spark 上 DeepSeek + OpenCode 的配置、缓存优化与实测记录，包含失败与适用边界。`
- 第一版定位：实验报告预览；不要写“最强”“零损失”“无人值守已验证”。
- 作者署名使用你希望公开的GitHub昵称，不必公开真实姓名。

## 用网页发布

1. 登录GitHub，点右上角“+”，选择New repository，填写名称和简介。
2. 可先设为Private，核对文件和署名后再改Public；是否公开由你决定。
3. 创建空仓库即可。若GitHub提供README/许可自动初始化选项，本文件夹已有README，避免生成第二份冲突内容；许可先按下面的说明决定。
4. 选择上传已有文件，将这个项目文件夹**里面的内容**上传到仓库根目录。不要上传整个咨询工作区，也不要上传私有原始归档。
5. 提交说明可以写：`docs: add initial dual-Spark OpenCode experiment report`。
6. 打开README检查相对链接、表格和CSV。许可确认、发布检查完成后，再决定是否公开和创建预览Release。

网页上传会绕过本地.gitignore的自动过滤，所以只能上传这个独立草稿文件夹。不要把它与原始记录目录混选。

先不用开Actions、Pages或购买服务。这份报告是普通仓库文件，不需要部署服务器。我们可以在你准备好后一起完成建仓库、上传和页面检查；这份草稿尚未做任何远端操作。

官方说明：[创建仓库入门](https://docs.github.com/en/repositories/creating-and-managing-repositories/quickstart-for-repositories)。按钮措辞可能随界面变化，以页面为准。

## 许可先做一个明确选择

草稿没有替你选择最终LICENSE。可考虑为自己新写的文档选一个允许引用/分享的许可，为新脚本选MIT或Apache-2.0；上游引擎、模型和数据仍遵守各自许可。首次公开时再确定署名及许可范围，见[许可说明](LICENSE-NOTES.md)。
