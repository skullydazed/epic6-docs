# Overview of commands

Commands let you interact with IRC servers, change the client interface, and program EPIC. The groups below provide a navigation guide to the current built-in command set. Follow each link for syntax, arguments, defaults, errors, and examples; commands in one group do not necessarily share those details.

At the input prompt, begin a command with `/`, for example `/join #example`. Ordinary text is normally sent to the current target. Inside a script [block](block.md), statements are interpreted as commands or expressions according to [ircII syntax](ircii_syntax.md). Command names are case-insensitive; argument text can still be case-sensitive or interpreted by the server.

An alias can replace the normal behavior of a built-in command with the same name. A double prefix such as `//echo text` bypasses the alias and selects the built-in command when present. If a name is unrecognized, configured unknown-command dispatch or an `unknown_command` hook can affect its handling; it is not necessarily a locally rejected typo.

## IRC commands

| Task | Commands | Purpose |
| --- | --- | --- |
| Channels | [invite](../command/invite.md), [join](../command/join.md), [kick](../command/kick.md), [knock](../command/knock.md), [mode](../command/mode.md), [names](../command/names.md), [part](../command/part.md), [topic](../command/topic.md), [who](../command/who.md) | Invite or join, manage channel state, request membership information, or leave. Permissions and returned data depend on the server. |
| Messages and actions | [msg](../command/msg.md), [notice](../command/notice.md), [me](../command/me.md), [describe](../command/describe.md), [say](../command/say.md), [send](../command/send.md), [wallchops](../command/wallchops.md), [wallops](../command/wallops.md) | Send messages, notices, or actions. `send` prefers the current query over channel; `say` prefers the current channel. |
| Client information requests | [ctcp](../command/ctcp.md), [ping](../command/ping.md) | Send CTCP requests; `ping` measures a client CTCP response, not an operating-system ICMP ping. |
| Network information | [admin](../command/admin.md), [info](../command/info.md), [links](../command/links.md), [list](../command/list.md), [lusers](../command/lusers.md), [map](../command/map.md), [motd](../command/motd.md), [stats](../command/stats.md), [time](../command/time.md), [trace](../command/trace.md), [version](../command/version.md) | Request server/network information. Some commands have local display behavior as well; see each command page. |
| Identity and presence | [away](../command/away.md), [nick](../command/nick.md), [ison](../command/ison.md), [userhost](../command/userhost.md), [whois](../command/whois.md), [whowas](../command/whowas.md) | Set presence or nickname and request user information. Queries can have asynchronous script callbacks. |
| Operator requests | [connect](../command/connect.md), [deop](../command/deop.md), [die](../command/die.md), [kill](../command/kill.md), [oper](../command/oper.md), [rehash](../command/rehash.md), [restart](../command/restart.md), [squit](../command/squit.md) | Request operator actions or authentication. `connect` asks a server to link servers; it does not establish your own client connection. |
| Network-specific requests | [rping](../command/rping.md), [servlist](../command/servlist.md), [silence](../command/silence.md), [squery](../command/squery.md), [uping](../command/uping.md), [userip](../command/userip.md), [usrip](../command/usrip.md), [note](../command/note.md) | Send requests whose availability, syntax, and meaning depend on the network. Recognition by EPIC is not server support. |
| Protocol text | [quote](../command/quote.md), [xquote](../command/xquote.md) | Forward protocol text, with `xquote` providing additional server/encoding controls. |

## Programming

| Task | Commands | Purpose |
| --- | --- | --- |
| Control flow | [break](../command/break.md), [continue](../command/continue.md), [do](../command/do.md), [fe](../command/fe.md), [fec](../command/fec.md), [for](../command/for.md), [foreach](../command/foreach.md), [if](../command/if.md), [repeat](../command/repeat.md), [return](../command/return.md), [switch](../command/switch.md), [unless](../command/unless.md), [until](../command/until.md), [while](../command/while.md) | Conditionals, loops, iteration, and control transfer. `return` has function-result behavior when used in a function context. |
| Definitions and events | [alias](../command/alias.md), [on](../command/on.md), [hook](../command/hook.md), [shook](../command/shook.md), [stub](../command/stub.md) | Define commands/functions and event handlers, generate script events, or arrange definitions loaded on demand. |
| Variables and storage | [assign](../command/assign.md), [local](../command/local.md), [push](../command/push.md), [pop](../command/pop.md), [shift](../command/shift.md), [unshift](../command/unshift.md), [stack](../command/stack.md) | Assign values, create locals, manipulate word lists, and save or restore supported definitions/state. |
| Evaluation and context | [eval](../command/eval.md), [xeval](../command/xeval.md), [bless](../command/bless.md), [call](../command/call.md) | Evaluate code, select window/server context, expose a locked local frame, or inspect the call stack. See individual scope rules. |
| Scheduling and waits | [defer](../command/defer.md), [queue](../command/queue.md), [timer](../command/timer.md), [wait](../command/wait.md), [pause](../command/pause.md), [sleep](../command/sleep.md), [usleep](../command/usleep.md) | Defer/queue execution, schedule callbacks, wait for events, or pause. These commands do not all have the same blocking or callback behavior. |
| Scripts and packages | [load](../command/load.md), [which](../command/which.md), [package](../command/package.md), [subpackage](../command/subpackage.md), [unload](../command/unload.md) | Load or locate scripts and associate definitions with packages for later removal. `unload` is package removal, not reversal of every effect a file caused. |
| Input and output | [echo](../command/echo.md), [xecho](../command/xecho.md), [input](../command/input.md), [input_char](../command/input_char.md), [sendline](../command/sendline.md), [parsekey](../command/parsekey.md), [type](../command/type.md), [xtype](../command/xtype.md) | Display text, request input, process an input line, invoke a key action, or edit/simulate input. `sendline` can execute commands, not merely send text. |
| Testing and diagnostics | [abort](../command/abort.md), [call](../command/call.md), [debuglog](../command/debuglog.md), [dump](../command/dump.md), [pretend](../command/pretend.md), [xdebug](../command/xdebug.md) | Diagnostics, intentional abort, definition removal, synthetic protocol input, and debugging controls. These are operational commands with effects described on their own pages. |

## Client interface and connections

| Task | Commands | Purpose |
| --- | --- | --- |
| Windows | [window](../command/window.md), [clear](../command/clear.md), [unclear](../command/unclear.md), [shh](../command/shh.md), [lastlog](../command/lastlog.md), [log](../command/log.md) | Manage windows and display views, inspect retained output, and control logging. `shh` suppresses output in the current output context; it is not server-side silence. |
| Configuration | [set](../command/set.md), [bind](../command/bind.md), [rbind](../command/rbind.md), [encoding](../command/encoding.md) | Query/change registered settings, install or inspect key bindings, and manage character encodings. |
| Server connections | [server](../command/server.md), [disconnect](../command/disconnect.md), [reconnect](../command/reconnect.md), [hostname](../command/hostname.md), [vhosts](../command/vhosts.md) | Select and manage your own server connections and local host choices. Automatic retry policy can additionally come from a script. |
| Local environment | [cd](../command/cd.md), [setenv](../command/setenv.md), [exec](../command/exec.md), [beep](../command/beep.md), [license](../command/license.md) | Change directory/environment, run local processes, signal the terminal, or display license information. |
| Exit | [quit](../command/quit.md), [exit](../command/exit.md) | Exit the client through the built-in quit handling. |

## Script-provided commands

The available command vocabulary also depends on loaded scripts. For example, the supplied [builtins](../scripts/builtins.md) environment defines compatibility aliases such as `bye` and `ircname` and loads the [notify](../scripts/notify.md) MONITOR wrapper. Optional scripts provide commands such as [save](../scripts/save.md), [scan](../scripts/scan.md), and [renumber](../scripts/renumber.md). These names are not proof that a corresponding C built-in exists.

A personal startup file can replace the default [global](../scripts/global.md) setup. Consequently, two installations or sessions with the same executable can expose different aliases, pseudo-settings, completion behavior, and hooks. Load the relevant script and its dependencies before relying on its commands.

## External language support

When compiled with Python support, [python](../command/python.md) and [pydirect](../command/pydirect.md) provide Python execution interfaces. Availability is conditional on the build and does not imply that every legacy embedded-language interface is present. Local process execution through `exec` is separate from embedded Python support.

## Server-dependent behavior

Server requests are subject to connection state, network extensions, privileges, target visibility, and server policy. A command can be recognized and transmitted while the server rejects it or returns different information. Operator commands do not grant privileges merely because they are listed here. Commands that only modify local windows or script definitions need not send any IRC request.

This overview has no single return value or default argument set. A command's displayed output, script function results, asynchronous callbacks, and effects on client/server state are separate interfaces. Consult the individual page rather than inferring behavior from a shared C handler or a familiar command name.

## Examples

```text
/window list
/set clock on
/echo Local client text
```

These inspect windows, enable a registered setting, and print locally. To request a server operation, use its documented command, for example `/motd` on a connected session. A server reply is asynchronous and is not the return value of a script function.

## Source references

- [source/commands.c](../../source/commands.c): built-in command table, alias precedence, double-prefix handling, interactive parsing, and unknown-command dispatch.
- [source/alias.c](../../source/alias.c): aliases, variables, stubs, packages, and definition removal.
- [source/if.c](../../source/if.c): conditionals and iteration.
- [source/hook.c](../../source/hook.c) and [source/keys.c](../../source/keys.c): event and key-binding interfaces.
- [source/server.c](../../source/server.c), [source/window.c](../../source/window.c), and [source/who.c](../../source/who.c): connections, local windows, and server-query callbacks.
- [source/python.c](../../source/python.c): optional Python integration.
- [script/builtins](../../script/builtins) and [script/global](../../script/global): supplied aliases and startup dependencies.
