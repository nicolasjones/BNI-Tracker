# SDD launcher

Use this repo-local launcher instead of the global `codex` binary when you want to run SDD commands.

## Why

- Global `~/.codex` is not writable in this machine for automated runs.
- A repo-local `CODEX_HOME` avoids the readonly SQLite/config issue.
- The launcher forces `multi_agent = true`.
- The launcher sets a CA bundle so Codex can connect successfully.

## Command

```bash
./.atl/bin/codex-sdd
```

Then, inside Codex, run:

```text
sdd init
```

And later any SDD command you need, for example:

```text
/sdd-new <change>
/sdd-continue
/sdd-verify
```
