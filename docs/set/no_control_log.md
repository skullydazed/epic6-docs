# set no_control_log

## Synopsis

```text
/set no_control_log [on|off|toggle]
```

Default: `off`. With no argument, [set](../command/set.md) displays the current value.

## Description

Enables additional unprintable-character stripping during logfile processing, subject to the log's mangling selection. Turning it off removes this additional rule; other selected mangling rules still apply.

When a destination supplies a nonempty log-specific mangling mask, this setting adds the `unprintable` rule to that mask for each write. This includes per-window [log_mangle](../window/log_mangle.md) rules and selective [log](../command/log.md) objects with their own `mangle` rules. If the log-specific mask is empty, a nonempty global [mangle_logfiles](mangle_logfiles.md) selection takes precedence; when that global selection is also empty, `no_control_log` selects `unprintable` by itself.

The global session [log](log.md) uses the fallback path when its log-specific mask is empty. Turning this setting on strips controls from that log only when the global selection is empty; if `mangle_logfiles` has rules, those rules are used without adding `unprintable`.

## What is stripped

The added rule removes ordinary nonprinting controls, IRC attribute-toggle controls, reset controls, and bells. Tabs are expanded rather than simply removed. For color sequences, stripping can remove only the introducing control character and leave following color-number text. Escape handling also depends on the other enabled rules; normalization may interpret an escape sequence and generate IRC attribute controls. This setting is not a guarantee that every output byte is printable.

Use explicit [mangle types](../special/mangle_types.md) when you need a particular formatting policy. For example, `all` combines normalization with formatting stripping, whereas `unprintable` alone does not reliably remove complete color or escape sequences.

Mangling runs before [log_rewrite](log_rewrite.md) or a log-specific rewrite, so a rewrite can introduce new controls afterward. Log start/end markers bypass this processing. Changes affect subsequent writes, do not edit existing files or enable logging, and do not change display or lastlog records.

## Examples

Enable the additional rule for the current window's nonempty logging override:

```text
/window log_mangle bold
/set no_control_log on
```

Logging must already be enabled for that window, or enabled separately. Here `bold` supplies the nonempty override; `no_control_log` adds `unprintable` during writes. Turning it off leaves the `bold` rule active.

To request normalized formatting stripping through the global logfile policy instead:

```text
/set mangle_logfiles none,all
```

This policy applies to logs using the global fallback regardless of `no_control_log`.

## Source references

- `source/vars.c` and `include/config.h`: boolean registration and off default.
- `source/log.c`: `add_to_log` selects the caller mask, global fallback, or `no_control_log` fallback before rewriting.
- `source/output.c`, `source/screen.c`, and `source/logfiles.c`: global, window, and selective-log callers supply their masks.
- `source/screen.c`: `new_normalize_string` implements control-character, color, escape, and tab handling.
