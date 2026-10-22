# 输入与输出

[English](INPUT.md) | 简体中文 · [教程](tutorial.zh-CN.md)

对应 **v0.2.1**。输入为 UTF-8 JSON 对象，最大 10 MiB。支持 --input 文件路径与 --input -；拒绝重复 JSON 键和非有限常量。

| 字段 | 约定 |
| --- | --- |
| summary / expected | 非空字符串，描述问题及预期行为。 |
| steps | 非空字符串数组，按顺序列出操作。 |
| environment | 对象，填写 OS、runtime、version 等环境信息，缺项会在结果中报告。 |
| attempts | 数组，每项含唯一 id、布尔 reproduced、实际观察 actual 和证据引用 evidence。 |

## 样例

```json
{
  "summary": "Save button times out",
  "expected": "Saved record appears once",
  "steps": [
    "Open the edit form",
    "Change the title",
    "Click Save once"
  ],
  "environment": {
    "os": "macOS",
    "runtime": "Node 22",
    "version": "demo"
  },
  "attempts": [
    {
      "id": "1",
      "reproduced": true,
      "actual": "Timeout after 10 seconds",
      "evidence": "logs/attempt-1.txt"
    },
    {
      "id": "2",
      "reproduced": false,
      "actual": "Saved after 2 seconds",
      "evidence": "logs/attempt-2.txt"
    }
  ]
}
```

[完整预期结果](../examples/expected.json)。JSON 键名保留英文以匹配程序接口；字符串内容使用你的实际记录。退出码 0 代表处理完成，不代表所报告问题已经通过。

## 错误与副作用

工具不联网，不执行提交的命令。只读取输入及约定中明确指出的本地路径；默认向终端输出，只在明确 --output 时写入新文件。无效输入退出码为 2，已有结果文件不覆盖。写入失败可能留下不完整新文件，应先检查。安装是独立的明确操作。
