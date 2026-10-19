# KarmenLoop Bug Reproduction

Bug Reproduction helps you turn a bug report into steps someone else can try. It compares recorded attempts, calculates how often the failure occurred, and points out missing information.

By [KarmenLoop](https://github.com/KarmenLoop).

[![Release](https://img.shields.io/github/v/release/KarmenLoop/skill-bug-repro)](https://github.com/KarmenLoop/skill-bug-repro/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](docs/INPUT.md)
[![Platform](https://img.shields.io/badge/Platform-macOS%20%7C%20Linux%20%7C%20Windows-lightgrey.svg)](docs/COMPATIBILITY.md)

[Download](https://github.com/KarmenLoop/skill-bug-repro/releases) · [Quick start](#quick-start) · [Documentation](#documentation) · [Contribute](CONTRIBUTING.md) · [Contact](https://github.com/KarmenLoop/skill-bug-repro/issues)

The code is [MIT licensed](LICENSE). The local helper needs Python 3.9 or later, with no subscription or provider API key.

## Introduction

Start with what happened, what you expected, the environment, and the shortest steps you know. Add the results of each attempt. The helper keeps those results together and flags disagreements, so a well-written report is not mistaken for a bug that has actually been reproduced.

The package includes an agent skill, a local Python helper, example data, and tests. The skill guides the conversation; the helper processes the supplied data.

## Capabilities

- Calculate observed reproduction rate.
- Detect conflicting outcomes across attempts.
- Expose missing environment and evidence fields.

## Quick start

Requirements: Python 3.9+. Git is needed only for cloning; downloading the release archive also works. On Windows, replace python3 with py -3 if that is your installed launcher.

```sh
git clone https://github.com/KarmenLoop/skill-bug-repro.git
cd skill-bug-repro
python3 scripts/run.py --input examples/input.json
python3 -m unittest discover -s tests -v
```

Compare the result with [examples/expected.json](examples/expected.json). For your own data, follow the [input format](docs/INPUT.md). Relative file paths are resolved from the directory where you run the command.

To save a result without overwriting an existing file:

```sh
python3 scripts/run.py --input examples/input.json --output result.json
```

### Install the agent skill

Install it for the agent host you use:

```sh
python3 install.py --host codex
# Alternatives: --host deepseek, --host grok, or --host agents
```

The installer copies the skill into your host's skill directory. It stops if that directory already exists. To choose another location, pass `--destination` with a new directory. Host settings, credentials, permissions, and other skills are left alone.

In Codex, invoke $karmen-bug-repro. In Grok Build, invoke /karmen-bug-repro. In another compatible host, select the installed skill by name. Example request:

> Help me narrow this bug down to steps someone else can reproduce.

Refresh your host's skill discovery if needed. See [compatibility and its verification limits](docs/COMPATIBILITY.md).

## How it works

Attempt-level evidence is preserved while repeatability is calculated. The result names missing environment fields and does not equate a formatted report with a reproduced bug.

The result is JSON, so you can save it or pass it to another tool. Exit code `0` means the helper finished, even when its findings need attention. Exit code `2` means the input or a file operation failed. The helper does not run shell commands from the input or overwrite an existing output file.

## Documentation

- [Agent instructions](SKILL.md): selection, workflow, and completion criteria.
- [Input and output](docs/INPUT.md): fields and complete example.
- [Compatibility](docs/COMPATIBILITY.md): installation targets and host limits.
- [Validation](docs/VALIDATION.md): observed local results and acceptance scenarios.
- [Sources](docs/SOURCES.md): public research references and design decisions.
- [Changelog](CHANGELOG.md): release history.

## Limitations

The helper assembles evidence; it does not run commands or establish root cause. A zero failure count means the recorded attempts did not reproduce the issue.

Examples are synthetic. Local tests establish the covered helper behavior; they do not establish an authenticated provider integration or the quality of every future model response. Tools and account access remain those of the host.

## Contributing

Bug reports, focused improvements, documentation fixes, and pull requests are welcome. Read [CONTRIBUTING.md](CONTRIBUTING.md), include a sanitized reproduction, and run the tests. Development needs no third-party runtime dependency.

## Support

Use [GitHub Issues](https://github.com/KarmenLoop/skill-bug-repro/issues) for bugs and feature requests. [SUPPORT.md](SUPPORT.md) explains what to include. Never attach keys, customer records, or private conversations.

## License

Copyright © 2026 KarmenLoop. [MIT](LICENSE) permits commercial use and secondary development under its terms. Third-party services retain their own terms; see [NOTICE.md](NOTICE.md).

## Acknowledgements

This is an independent KarmenLoop implementation. [Research notes](docs/SOURCES.md) identify public design references from the Meta, DeepSeek, and xAI ecosystems as applicable. No upstream code or brand assets are bundled, and no affiliation or endorsement is claimed.

## Contact

[KarmenLoop](https://github.com/KarmenLoop) · [Issues](https://github.com/KarmenLoop/skill-bug-repro/issues) · [Security reporting](SECURITY.md)
