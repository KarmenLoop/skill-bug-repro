# Bug Repro · 问题复现记录

[English](README.md) | 简体中文

把“偶尔会坏”变成别人能照着查的记录。复现步骤、运行环境、每次实际结果和证据放在一起，避免只剩一句“我这里不行”。

[下载 v0.2.1](https://github.com/KarmenLoop/skill-bug-repro/releases/tag/v0.2.1) · [完整教程](docs/tutorial.zh-CN.md) · [输入参考（英文）](docs/INPUT.md) · [反馈问题](https://github.com/KarmenLoop/skill-bug-repro/issues)

## 能做什么

两次尝试只有一次复现，因此 classification 为 intermittent，reproduction_rate 为 0.5。

每次尝试的结果由你或实际工具提供；本工具不会打开应用，也不会替你复现问题。

![问题复现记录 0.2.1 版本样例的真实 JSON 输出](docs/images/example-output-v0.2.1.svg)

*图片来自 v0.2.1 的真实本地输出，采用英文键名；[完整结果](examples/expected.json) · [图片来源记录](docs/images/provenance.json)。*

## 开始使用

在发行页下载 `karmen-bug-repro-v0.2.1.zip` 与对应 `.sha256` 文件，核对哈希后解压。在解压目录中使用 Python 3.9 或更新版本：

```sh
python3 scripts/run.py --version
python3 scripts/run.py --input examples/input.json
```

预期版本：`karmen-bug-repro 0.2.1`。两次尝试只有一次复现，因此 classification 为 intermittent，reproduction_rate 为 0.5。

如果宿主读取 `~/.agents/skills`，可安装完整技能：

```sh
python3 install.py --host agents
```

目标目录已存在时安装器会拒绝覆盖。宿主发现和调用方式可能不同，见[安装与实践教程](docs/tutorial.zh-CN.md)。不使用 AI 宿主也能直接运行本地工具。

## 用于自己的任务

每次尝试使用唯一 ID；填写系统、运行时和应用版本，每条观察附上真实证据路径或引用。

修复后添加第三次尝试，保留之前的失败记录，让接手的人能区分偶发现象与已验证修复。

准备新输入前可查看[字段约定（英文）](docs/INPUT.md)。工具只依赖 Python 标准库，本身不需要模型账号、API 密钥或网络。使用 AI 宿主时，宿主有自己的数据与权限设置。

## 常见问题

**工具执行成功就代表问题修好了吗？** 不是。退出码 0 只表示报告处理完成。修复结论仍需对应版本的实际行为和证据。

**结果保存在哪里？** 默认向终端输出 JSON；使用 `--output` 时只创建新文件，已有输出文件会保留。工具只读取提交的记录和输入约定中明确列出的本地路径。

## 文档与支持

- [下载、安装、配置、练习、升级与卸载](docs/tutorial.zh-CN.md)
- [输入输出约定](docs/INPUT.md)与[兼容性说明](docs/COMPATIBILITY.md)（英文参考）
- [更新记录](CHANGELOG.md)、[参与贡献](CONTRIBUTING.md)、[支持](SUPPORT.md)和[安全反馈](SECURITY.md)

## 许可证

[MIT](LICENSE)。再分发时保留许可证和[声明](NOTICE.md)。由 [KarmenLoop](https://karmenloop.com) 维护。
