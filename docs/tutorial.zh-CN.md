# Bug Repro：从下载到稳定使用

[English](tutorial.en.md) | 简体中文 · [项目首页](../README.zh-CN.md)

本教程对应 v0.2.1。把“偶尔会坏”变成别人能照着查的记录。复现步骤、运行环境、每次实际结果和证据放在一起，避免只剩一句“我这里不行”。

## 1. 下载与核对

打开 [v0.2.1 发行页](https://github.com/KarmenLoop/skill-bug-repro/releases/tag/v0.2.1)，同时下载 `karmen-bug-repro-v0.2.1.zip` 与 `karmen-bug-repro-v0.2.1.zip.sha256`。ZIP 包含源文件与可安装的智能体技能，不是桌面应用安装器。需要 Python 3.9 或更新版本，无需第三方 Python 依赖。

macOS 使用 `shasum -a 256 karmen-bug-repro-v0.2.1.zip`，Linux 使用 `sha256sum karmen-bug-repro-v0.2.1.zip`，Windows PowerShell 使用 `Get-FileHash .\karmen-bug-repro-v0.2.1.zip -Algorithm SHA256`。将完整哈希与校验文件核对后再解压；预期哈希本身也应来自可信来源。

在解压后的顶层目录打开终端。Windows 可把下文的 `python3` 换成 `py -3` 或自己配置的 Python 命令。

## 2. 跑通第一个结果

```sh
python3 scripts/run.py --version
python3 scripts/run.py --input examples/input.json
```

预期版本为 `karmen-bug-repro 0.2.1`。两次尝试只有一次复现，因此 classification 为 intermittent，reproduction_rate 为 0.5。 可与[完整样例结果](../examples/expected.json)对照。退出码 0 表示输入处理完成，不代表所检查的任务或发现均已通过。

## 3. 安装到 AI 宿主

不使用宿主也能运行本地工具。需要把技能说明与参考文件加入共享技能目录时：

```sh
python3 install.py --host agents
```

也可明确选择 `--host codex`、`--host deepseek` 或 `--host grok`。这些选项只是目录约定，不代表已经验证所有宿主版本。如需指定位置，运行 `python3 install.py --destination /path/to/a/new/karmen-bug-repro`，替换为自己的新目录，且不能位于源包内。

安装后刷新宿主的技能发现或新建会话，确认能读取 `karmen-bug-repro/SKILL.md` 及其参考文件。安装只复制文件，不授予工具、凭据或账号权限。

## 4. 配置真实输入

把 `examples/input.json` 复制为 `my-input.json`，保留 JSON 键名，替换样例内容。每次尝试使用唯一 ID；填写系统、运行时和应用版本，每条观察附上真实证据路径或引用。 [输入参考（英文）](INPUT.md)列出完整字段和结果键。

使用 UTF-8 JSON，顶层为对象，最大 10 MiB。不接受重复键、无效 JSON 或非有限数字。涉及时间戳时明确 UTC 偏移，保留原始观察与来源，方便其他人核对。

```sh
python3 scripts/run.py --input my-input.json --output my-result.json
```

输出路径必须是新文件。交给其他工具之前先读结果。每次尝试的结果由你或实际工具提供；本工具不会打开应用，也不会替你复现问题。

## 5. 进阶练习

修复后添加第三次尝试，保留之前的失败记录，让接手的人能区分偶发现象与已验证修复。

把输入、结果、安装版本和支持证据保存在一起。一次改变一个相关输入，比较输出。如果由 AI 准备 JSON，仍需对照原始资料检查记录，不能用文字流畅代替事实或权限依据。

使用 `--input -` 可读取标准输入。PowerShell 示例：`Get-Content -Raw .\my-input.json | py -3 scripts/run.py --input -`。自动化时既要检查退出码，也要检查业务结果后再采取动作。

## 6. 排查问题

- **找不到 Python：** 安装 Python 3.9+，用 `python3 --version` 或 `py -3 --version` 确认。
- **输入被拒绝或退出码为 2：** 读终端错误信息，核对 JSON 与[字段约定](INPUT.md)。
- **输出文件已存在：** 先检查或重命名旧结果，再选择新文件名。写入失败可能留下不完整的新文件，应检查后再重试。
- **宿主看不到技能：** 检查其配置的技能目录并刷新发现；直接运行本地工具，区分宿主设置与输入问题。
- **结果不符合预期：** 保留原始输入和输出，通过 [Issues](https://github.com/KarmenLoop/skill-bug-repro/issues) 提供版本及最小合成样例，先移除私人记录。

## 7. 升级、回退与卸载

把自己的输入与结果放在技能目录之外。核对新发行包后安装到新目录，安装器会主动拒绝覆盖。移动技能目录前关闭相关宿主会话，保留旧版本备份，再按宿主说明选择所需目录。回退时恢复旧目录并刷新发现。

卸载前核对路径，只删除为 `karmen-bug-repro` 创建的技能目录。本包不会安装账号、系统服务或后台调度器。

## 8. 检查与打包修改

```sh
python3 -B -m unittest discover -s tests -v
python3 -B scripts/check_docs.py
```

审阅并提交源码改动后，可用 `python3 scripts/package_release.py --output /path/to/new/release-dir`，将包输出到仓库外的新目录。构建器保留中英文、样例、测试和法律声明，生成校验值及提交记录。更新文档或结果图片时，应与生成的发行包版本一致。

[MIT 许可证](../LICENSE) · [项目首页](../README.zh-CN.md)
