# Input and output

Supply a UTF-8 JSON object (maximum 10 MiB). Use `--input PATH` for a file or `--input -` for standard input. Run `--version` to inspect the installed helper version. Duplicate JSON keys and non-finite JSON constants are rejected. Arrays are required unless documented as optional. IDs must be stable and unique. Dates use ISO 8601; timestamps require an explicit UTC offset.

| Field | Contract |
| --- | --- |
| summary/expected | Nonempty strings. |
| steps | Nonempty array of step strings. |
| environment | Object with OS/runtime/version details; missing values are reported. |
| attempts | Objects: unique id, reproduced boolean, actual string, evidence string. |

## Example

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

## Result

summary, steps, environment, missing_environment, attempts, reproduced_count, reproduction_rate, and classification.

See [the complete sample result](../examples/expected.json). Exit 0 means processing completed, not that all reported findings passed.

## Errors and side effects

The helper makes no network requests and executes no submitted commands. It reads the input and explicitly documented local paths. It writes only a requested new output file; stdout is the default. Invalid input exits 2. Existing output is preserved. An output write failure can leave a partial new file; remove that file before retrying. Installation is a separate explicit action.
