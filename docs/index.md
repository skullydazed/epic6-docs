# Welcome to EPIC6

EPIC is a terminal IRC client forked from ircII over 30 years ago. It focuses on old school irc users and scripters and those who just enjoy irc the way it used to be. It is mature, stable, and behaves just like ircII out of the box, but can be so much more with some configuration! Start with [about EPIC](special/about_epic.md) for background or the [introduction](special/introduction.md) for basic use.

EPIC6 was forked from EPIC5 on 08/26/2024, and has been in active development since. It is a deliberate modernization of a mature, highly programmable IRC client, emphasizing architectural simplicity, scriptability, security, and long-term maintainability over historical compatibility and feature accumulation.

## Getting EPIC6

EPIC6 is distributed as source code. From an EPIC6 source checkout, the usual build and installation sequence is:

```sh
./configure
make
make install
```

Configuration checks the local compiler and libraries. The intended environment is a modern POSIX system with a C99-or-newer compiler and terminfo support, plus the required libraries identified by configuration. Installation writes to the configured prefix; choose one appropriate for your system. See [compile options](special/compile_opts.md) and the repository's `configure.ac` for build requirements and options. Optional integrations depend on how the client was built.

EPIC6 is an evolving development line. Features, defaults, and script interfaces can differ from EPIC4 or EPIC5; an older package or script pack is not automatically an EPIC6-compatible installation. The repository's [UPDATES](UPDATES.md) and [KNOWNBUGS](KNOWNBUGS.md) describe changes and ongoing work. Distribution package names and availability depend on the operating system and its maintainers.

## Script packs and configuration

The initial interface is intentionally small. Supplied scripts and personal configuration can add completion, history, automatic reconnection, and other behavior. A script pack may provide a substantially different interface, so check its supported client version and dependencies. The presence of an old script in the source tree does not guarantee all its original dependencies remain available.

Read [global startup](scripts/global.md), [loading scripts](command/load.md), and the documentation for the scripts you use. For script-specific behavior, consult that script's author or documentation.

## Using EPIC

Provide a nickname and a server description when starting the client:

```sh
epic6 mynick irc.example.net
```

Replace the example hostname with your network's server. This requests a connection using `mynick`; the server decides whether the nickname and registration are accepted. Network addresses, TLS requirements, authentication, channel rules, and available extensions vary. See [server descriptions](special/server_description.md) for specifying the connection.

To display command-line options:

```sh
epic6 -h
```

See [command-line options](special/command_line.md) for details. If typing or display is incorrect, consult [output help](special/output-help.md), [input handling](special/input_handling.md), and [graphics characters](special/graphics_chars.md). Terminal configuration, fonts, and encoding all affect the result.

## What is IRC?

IRC connects people through servers and networks. Users join channels and exchange messages with other people on the same network. EPIC can manage connections to multiple servers, but channel names and nicknames belong to their network context. IRC has multiple server implementations and protocol extensions; support for a particular operation depends on the server and client implementation. See [new users](special/new_user.md) and [IRC etiquette](special/etiquette.md).

## Help and programming

These pages document client features and supplied scripts. Useful reference starting points are [commands](special/commands_overview.md), [functions](special/functions_overview.md), [key bindings](special/key_bindings.md), and [special variables](special/special_vars.md).

To customize or automate the client, begin with [programming](special/programming.md), [ircII syntax](special/ircii_syntax.md), and [expando substitution](special/expando_substitution.md). Scripts execute local client operations as well as server requests, so read their requirements and effects before loading them.

## Repository references

- `source/irc.c`: program identity, startup arguments, and help output.
- `configure.ac` and `Makefile.in`: build checks and installation targets.
- `script/global` and `script/builtins`: supplied startup environment.
- `KNOWNBUGS` and `UPDATES`: development direction and change history.
