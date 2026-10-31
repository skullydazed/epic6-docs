# Getting started with EPIC

[Welcome](welcome.md) to EPIC, a programmable IRC client with a traditional ircII interface and scripting language.

EPIC may suit you if you want to customize how an IRC client behaves:

- Its own scripting language provides commands, functions, aliases, and event handlers. Optional Python integration is available when enabled in the build.
- Scripts can change output, react to events, and define workflows rather than relying only on fixed interface choices.
- It runs in a terminal. Resource use depends on configuration, retained history, scripts, and workload.

Start with the [IRC introduction](introduction.md) and [new-user guide](new_user.md). For customization, see [the scripting introduction](epic_scripting.md), then the [command overview](commands_overview.md) and [function overview](functions_overview.md).

The project’s historical community contact is `#epic` on EFNet. Documentation is available at [epicsol.org](https://epicsol.org/).

## Source references

- `source/commands.c`: current scripting and Python command registration, without Perl, Ruby, or Tcl commands.
- `configure.ac` and `source/python.c`: optional Python integration.
- [UPDATES](../UPDATES.md): EPIC6's feature-retirement list includes Perl and Ruby.
