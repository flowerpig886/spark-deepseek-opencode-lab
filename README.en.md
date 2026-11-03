# Dual DGX Spark + DeepSeek + OpenCode: configuration and measured results

[中文主页](README.md)

This draft records our configuration and bounded experiments with DeepSeek-V4.1-Flash-1017 EXL3 2.9bpw on two 128GB DGX Sparks, using TensorFold TP2 and the backend bundled with Windows OpenCode 2.2.5.

The fixed configuration uses one inference stream, vision disabled, a locally validated single-slot prefix-cache change, low reasoning effort, temperature/top_p=1, and a 32,768-token output ceiling. The OpenCode context declaration is 131,072; the engine's 1M configuration does not constitute a native OpenCode 1M acceptance test.

| Experiment | Observation |
|---|---|
| Native integration | Small repair passed: 14 requests, 38.46 seconds |
| Fresh repository tasks | Three pydicom issues, two seeds each: 4/6 correct patches and completed tasks |
| Serial service endurance | 65.01 minutes, 19 repeated tasks, 706 requests, 687 tool calls; no abnormal endings or sampled thermal throttling |
| Basic recovery | Both session-resume mechanisms worked, but only 1/2 resumed repairs was correct |
| Recovery after a production edit | Not validated: no production mutation observed within the predefined five-minute checkpoint window |

Two failed repairs obtained project validation receipts but failed the same independent hidden edge-case test. We support independently checked, human-reviewed automation; these results do not qualify unattended long-task reliability.

Experiments used private-profile backend APIs, not GUI clicks. Endurance tasks repeated known issues in fresh sessions and are not additional independent quality samples. The largest recorded uncached-input-plus-cache-read count during endurance was 95,499 tokens. That is an observation, not a context limit or a test of full 32K generation at that input size.

This draft provides configuration references, numeric exports, and a fixed-version cache preparation script. It does not ship model weights, private images, raw sessions, hidden tests, or the complete project-specific validation plugin/bridge. The basic OpenCode example is not an exact reproduction of the benchmark Agent stack.

See the [Chinese configuration guide](docs/CONFIGURATION.md), [methodology](docs/METHODOLOGY.md), [results and failures](docs/RESULTS.md), and [reproduction scope](docs/REPRODUCTION.md). Upstream credits and links are in the Chinese README. Final licensing and author attribution remain to be chosen before public release; no remote repository has been created by this draft.
