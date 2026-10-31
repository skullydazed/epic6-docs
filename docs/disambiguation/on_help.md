# on help (removed event)

EPIC6 does not register the former `HELP` hook type. There is no current built-in event argument layout or default HELP-hook action to document. Old `on help` handlers do not provide a working callback for the retired help browser.

The built-in help browser and pre-wiki help-file support were retired. The retained [`help` script](scripts_help.md) is a separate interface, and its `connect()` dependency returns empty in the current C implementation. Merely loading that script does not restore the former HELP event or its browser integration.

Use the documentation pages directly and [`on`](../command/on.md) for currently registered event types. A separately supplied script can define its own help workflow, but its callbacks and arguments belong to that implementation.

## Source references

- `source/hook.c`: `hook_function_templates` has no HELP entry.
- `source/commands.c`: current command registration omits the old built-in help browser.
- [KNOWNBUGS](../KNOWNBUGS.md) and [UPDATES](../UPDATES.md): retirement of HELP and pre-wiki help-file support.
- [`script/help.irc`](scripts_help.md) and `source/functions.c`: retained script and disabled connection dependency.
