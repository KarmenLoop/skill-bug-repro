# Bug Repro

English | [简体中文](README.zh-CN.md)

Turn a vague “it sometimes breaks” report into a record someone else can follow. Keep the steps, environment, actual results, and evidence for each attempt together.

[Download v0.2.1](https://github.com/KarmenLoop/skill-bug-repro/releases/tag/v0.2.1) · [Tutorial](docs/tutorial.en.md) · [Input reference](docs/INPUT.md) · [Report an issue](https://github.com/KarmenLoop/skill-bug-repro/issues)

## What it does

Two attempts produce one reproduction: classification is intermittent and reproduction_rate is 0.5.

Attempt results are supplied by you or your tools. This helper does not open the application or reproduce the bug itself.

![Bug Repro sample JSON output from version 0.2.1](docs/images/example-output-v0.2.1.svg)

*Actual local output from v0.2.1, rendered as an image. [Complete result](examples/expected.json) · [Image provenance](docs/images/provenance.json).*

## Start here

Download `karmen-bug-repro-v0.2.1.zip` and its `.sha256` file from the release, verify the hash, then extract the ZIP. In the extracted directory, use Python 3.9 or later:

```sh
python3 scripts/run.py --version
python3 scripts/run.py --input examples/input.json
```

Expected version: `karmen-bug-repro 0.2.1`. Two attempts produce one reproduction: classification is intermittent and reproduction_rate is 0.5.

To install the complete skill into a host that reads `~/.agents/skills`:

```sh
python3 install.py --host agents
```

The installer refuses an existing destination. Host discovery and invocation vary; see the [full setup and practice guide](docs/tutorial.en.md). You can run the helper directly without an AI host.

## Use it with your own work

Use one stable ID per attempt. Fill in OS, runtime, and application version, then attach a real evidence path or reference to each observation.

Add a third attempt after a fix. Keep the earlier failures so the next reader can distinguish an intermittent bug from a verified repair.

Read the [field contract](docs/INPUT.md) before preparing a new input. The helper runs locally with the Python standard library; it needs no model account, API key, or network connection. An AI host has its own data and permission settings.

## Questions

**Does a successful helper run mean the bug is fixed?** No. Exit 0 means the report was processed. Check actual application behavior and retain the evidence for the fixed version.

**Where does the result go?** JSON is printed to stdout unless you request a new file with `--output`. Existing output files are preserved. The helper reads only the submitted records and any local paths documented in its input contract.

## Documentation and support

- [Download, install, configure, practice, upgrade, and remove](docs/tutorial.en.md)
- [Input/output contract](docs/INPUT.md) and [compatibility](docs/COMPATIBILITY.md)
- [Changelog](CHANGELOG.md), [contributing](CONTRIBUTING.md), [support](SUPPORT.md), and [security reports](SECURITY.md)

## License

[MIT](LICENSE). Keep the license and [notice](NOTICE.md) with redistributed copies. Maintained by [KarmenLoop](https://karmenloop.com).
