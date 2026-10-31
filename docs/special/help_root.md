# EPIC help collection: comprehensive index

[Welcome](welcome.md) to the help collection. For a short current introduction, start with [getting started](getting_started.md), [commands](commands_overview.md), [functions](functions_overview.md), and [scripting](epic_scripting.md).

This index covers commands, functions, settings, hooks, key bindings, window operations, and scripts. Follow each reference for syntax, prerequisites, limitations, and examples.

Scripts must be loaded before their definitions are available.

Historical entries are collected in [removed in EPIC6](removed_in_epic6.md) and the older [EPIC4-to-EPIC5 compatibility lists](removed_in_epic5.md).

## Using the index

- CTCP handlers other than ACTION in this index are supplied by `script/ctcp`. The retained outgoing reply-throttle branch does not establish a working limit or a supported `no_ctcp_flood` setting.
- `notify`, `ignore`, mail checking, and many compatibility commands/settings are supplied through scripts rather than their former built-in interfaces. Script availability must be checked alongside dependencies.
- `set client_information` supplies the VERSION responder's configurable text, while `set user_information` supplies USERINFO; neither is the CLIENTINFO command-description source.
- `switch` selects wildcard patterns, not regular expressions. `bless` exposes the oldest enclosing locked waiting frame under its documented scope rules; it does not automatically expose the immediate caller when no frame is locked.
- IRC network operations remain subject to server support and permissions. KICK, INVITE, MODE, WHO, WHOIS, and similar requests do not guarantee their requested result. TRACE asks for IRC routing diagnostics, not an IP traceroute. KNOCK requests network-specific channel entry assistance rather than guaranteeing an invitation.
- Hook names describe callback opportunities, not guarantees that every operation succeeds or that all state is already complete. In particular, CHANNEL_SYNC has the cache-completeness limitations in its reference, and suppression normally controls the caller's default handling rather than undoing the network event.


## The most common commands

| Reference | Description |
| --- | --- |
| [away](../command/away.md) | Tell the server you are not paying attention |
| [channel](../command/channel.md) | Join or associate a channel with a window. |
| [clear](../command/clear.md) | Do a [window clear](../window/clear.md); Display nothing in the window. |
| [ctcp](../command/ctcp.md) | **C**lient **T**o **C**lient **P**rotocol: ask other clients for information. |
| [disconnect](../command/disconnect.md) | Close the connection to a server |
| [exit](../command/exit.md) | Tell the client to shut down. |
| [invite](../command/invite.md) | Ask someone to join a channel. |
| [join](../command/join.md) | Join or associate a channel with a window. |
| [kick](../command/kick.md) | Remove someone from a channel. |
| [knock](../command/knock.md) | Ask to be [invite](../command/invite.md)d to a channel. |
| [lastlog](../command/lastlog.md) | Redisplay stuff that has previously shown up in a window. |
| [log](../command/log.md) | General purpose logfiles. |
| [me](../command/me.md) | Tell the channel what you are doing with a [ctcp action](../ctcp/action.md). |
| [mode](../command/mode.md) | Change the mode of a channel. |
| [msg](../command/msg.md) | Send a message to someone. |
| [nick](../command/nick.md) | Change your nickname. |
| [notify](../disambiguation/notify.md) | Script-provided nickname monitoring through the server’s MONITOR facility. |
| [part](../command/part.md) | Leave a channel. |
| [query](../command/query.md) | Change the current target of a window to a nickname. |
| [quit](../command/quit.md) | Same as [exit](../command/exit.md). |
| [reconnect](../command/reconnect.md) | Reconnect to a server. |
| [server](../command/server.md) | Connect to an irc server. |
| [topic](../command/topic.md) | Change the topic of the channel. |
| [who](../command/who.md) | Ask the server for a list of who is on the channel. |
| [whois](../command/whois.md) | Ask the server for detailed information about one person. |
| [whowas](../command/whowas.md) | Ask the server for info about someone who is not on irc any more. |


## Less common IRC commands

| Reference | Description |
| --- | --- |
| [admin](../command/admin.md) | Ask the server how to contact the server admin. |
| [connect](../command/connect.md) | Ask a server on the network to link to another server not on the network (oper only). |
| [ctcp action](../ctcp/action.md) | Action protocol used by ME/DESCRIBE; direct CTCP sending bypasses SEND_ACTION. |
| [ctcp clientinfo](../ctcp/clientinfo.md) | Ask another client what ctcp commands they support. |
| [ctcp echo](../ctcp/echo.md) | Ask another client to send you a string back. |
| [ctcp finger](../ctcp/finger.md) | Ask another client about the man behind the mask. |
| [ctcp ping](../ctcp/ping.md) | Ask another client to respond, to measure lag time. |
| [ctcp time](../ctcp/time.md) | Ask another client what time they think it is. |
| [ctcp userinfo](../ctcp/userinfo.md) | Ask another client for its user-customizable string. |
| [ctcp utc](../ctcp/utc.md) | Render a supplied seconds-since-epoch timestamp in the receiver's local timezone. |
| [ctcp version](../ctcp/version.md) | Ask for client identification; replies may be customized or falsified. |
| [deop](../command/deop.md) | Revoke your own irc operatorship privileges (oper only) |
| [describe](../command/describe.md) | Tell another nick what you are doing with a [ctcp action](../ctcp/action.md). |
| [die](../command/die.md) | Tell your server to shut down (oper only) |
| [hostname](../command/hostname.md) | Change your virtual hostname. |
| [info](../command/info.md) | Ask the client and server about the software you're using. |
| [ison](../command/ison.md) | Ask the server if nicknames in a list are on the network. |
| [kill](../command/kill.md) | Remove someone from the irc network. (oper only) |
| [links](../command/links.md) | Ask the server what servers are on the network. |
| [list](../command/list.md) | Ask the server to tell you about the network's public channels. |
| [load](../command/load.md) | Import and run commands from a file. |
| [lusers](../command/lusers.md) | Ask the server how many users and servers are on the network. |
| [map](../command/map.md) | Ask the server to show you the topology of the network. |
| [motd](../command/motd.md) | Ask the server for the Message Of The Day. |
| [names](../command/names.md) | Ask the server about who is on what channels. |
| [note](../command/note.md) | Leave a message for someone when they are away (rare) |
| [notice](../command/notice.md) | Send a response to someone's message. |
| [oper](../command/oper.md) | Assume operatorship privileges (oper only). |
| [ping](../command/ping.md) | Figure out how lagged you are. |
| [rehash](../command/rehash.md) | Ask the server to re-read its config files (oper-only) |
| [restart](../command/restart.md) | Ask the server to shut down and restart (oper-only) |
| [rping](../command/rping.md) | Send an RPING to the server. |
| [servlist](../command/servlist.md) | Send a SERVLIST to the server. |
| [squery](../command/squery.md) | Send an SQUERY to someone. |
| [squit](../command/squit.md) | Remove a server from the network. (oper only) |
| [stats](../command/stats.md) | Ask the server for statistics (oper only) |
| [time](../command/time.md) | Ask the server what time it thinks it is. |
| [trace](../command/trace.md) | Request IRC network routing diagnostics from the server. |
| [uping](../command/uping.md) | Ping the server. |
| [userhost](../command/userhost.md) | Ask the server for a nick's userhost. |
| [userip](../command/userip.md) | Ask the server for a nick's ip address. |
| [usrip](../command/usrip.md) | Ask the server for a nick's ip address. |
| [version](../command/version.md) | Ask the server what software it is using. |
| [wallchops](../command/wallchops.md) | Send a message to channel operators. |
| [wallops](../command/wallops.md) | Send a message to all irc operators (oper only). |


## Commands

| Reference | Description |
| --- | --- |
| [abort](../command/abort.md) | Kill the client with SIGABRT (trap to gdb) |
| [alias](../command/alias.md) | Create your own commands |
| [assign](../command/assign.md) | Create your own variables |
| [beep](../command/beep.md) | Make your terminal beep |
| [bind](../command/bind.md) | Tell the client what to do when you press a key |
| [bind_altcharset](../bind/altcharset.md) | Insert the char that switches your font between character sets. |
| [bind_backspace](../bind/backspace.md) | Delete the character before the cursor |
| [bind_backward_character](../bind/backward_character.md) | Move the cursor left one position |
| [bind_backward_word](../bind/backward_word.md) | Move the cursor to the start of the previous word |
| [bind_beginning_of_line](../bind/beginning_of_line.md) | Move the cursor to the start of input line |
| [bind_blink](../bind/blink.md) | Insert the char that toggles blinking |
| [bind_bold](../bind/bold.md) | Insert the char that toggles bold video |
| [bind_clear_screen](../bind/clear_screen.md) | Do a [window clear](../window/clear.md) |
| [bind_delete_character](../bind/delete_character.md) | Delete the character under the cursor |
| [bind_delete_next_word](../bind/delete_next_word.md) | Delete from the cursor to the end of the next word |
| [bind_delete_previous_word](../bind/delete_previous_word.md) | Delete from the cursor to the start of the previous word. |
| [bind_delete_to_previous_space](../bind/delete_to_previous_space.md) | Delete from the cursor to the first space before the cursor. |
| [bind_end_of_line](../bind/end_of_line.md) | Move the cursor to the end of the input line. |
| [bind_erase_line](../bind/erase_line.md) | Delete the entire input line. |
| [bind_erase_to_beg_of_line](../bind/erase_to_beg_of_line.md) | Delete from the cursor to the start of input. |
| [bind_erase_to_end_of_line](../bind/erase_to_end_of_line.md) | Delete from the cursor to the end of input. |
| [bind_forward_character](../bind/forward_character.md) | Move the cursor right one position. |
| [bind_forward_word](../bind/forward_word.md) | Move the cursor to the next word. |
| [bind_highlight_off](../bind/highlight_off.md) | Insert the character that turns all highlights off. |
| [bind_next_window](../bind/next_window.md) | Move down one visible ("split") window. |
| [bind_nothing](../bind/nothing.md) | Perform no action (unbinds a sequence) |
| [bind_parse_command](../bind/parse_command.md) | Execute a block of code (provided as argument) |
| [bind_previous_window](../bind/previous_window.md) | Move up one visible ("split") window. |
| [bind_quote_character](../bind/quote_character.md) | Tell the client the next keypress should ignore its keybinding. |
| [bind_refresh_inputline](../bind/refresh_inputline.md) | Tell the client to redraw the input line. |
| [bind_refresh_screen](../bind/refresh_screen.md) | Tell the client to redraw the entire screen. |
| [bind_refresh_status](../bind/refresh_status.md) | Tell the client to redraw the status bars. |
| [bind_reset_line](../bind/reset_line.md) | Delete the entire input line but don't save it in the cutbuffer. |
| [bind_reverse](../bind/reverse.md) | Insert the character that toggles reverse video. |
| [bind_scroll_backward](../bind/scroll_backward.md) | Move backwards (older) in the scrollback buffer. |
| [bind_scroll_end](../bind/scroll_end.md) | End scrolling back |
| [bind_scroll_forward](../bind/scroll_forward.md) | Move forwards (newer) in the scrollback buffer. |
| [bind_scroll_start](../bind/scroll_start.md) | Move to the start (oldest) of the scrollback buffer. |
| [bind_self_insert](../bind/self_insert.md) | Insert the character itself into the input buffer. |
| [bind_send_line](../bind/send_line.md) | Process the contents of the input buffer and reset the input buffer. |
| [bind_swap_last_window](../bind/swap_last_window.md) | Do a [window last](../window/last.md). |
| [bind_swap_next_window](../bind/swap_next_window.md) | Do a [window next](../window/next.md). |
| [bind_swap_previous_window](../bind/swap_previous_window.md) | Do a [window previous](../window/previous.md). |
| [bind_switch_channels](../bind/switch_channels.md) | Cycle through the channels in a window. |
| [bind_switch_query](../bind/switch_query.md) | Cycle through the queries in a window. |
| [bind_toggle_insert_mode](../bind/toggle_insert_mode.md) | Toggle between inserting before the cursor and overwriting what is under the cursor. |
| [bind_toggle_stop_screen](../bind/toggle_stop_screen.md) | Do a [window hold_mode](../window/hold_mode.md) TOGGLE. |
| [bind_type_text](../bind/type_text.md) | Insert some text (provided as argument) into the input buffer. |
| [bind_unclear_screen](../bind/unclear_screen.md) | Do a [window unclear](../window/unclear.md). |
| [bind_underline](../bind/underline.md) | Insert the character that toggles underline video. |
| [bind_unstop_all_windows](../bind/unstop_all_windows.md) | Do a [window hold_mode](../window/hold_mode.md) OFF in all windows. |
| [bind_yank_from_cutbuffer](../bind/yank_from_cutbuffer.md) | Insert into the input line whatever we last deleted into the cutbuffer. |
| [bless](../command/bless.md) | Expose the oldest enclosing locked waiting frame; no enclosing scope is attached when none is locked. |
| [break](../command/break.md) | Early termination of the loop; advance to the next command in the block. |
| [call](../command/call.md) | Dump the current script call stack to the window. |
| [cd](../command/cd.md) | Change the client's current working directory |
| [comment](../command/comment.md) | The no-op command. |
| [continue](../command/continue.md) | Early termination of the current iteration of a loop; go back to the top and start the next iteration. |
| [defer](../command/defer.md) | Run a command only when the client is not doing something. |
| [do](../command/do.md) | Post-test looping command |
| [dump](../command/dump.md) | Bulk-removal of aliases, assigns, ons, etc |
| [echo](../command/echo.md) | Display something to a window. |
| [eval](../command/eval.md) | Expand variables in a statement again and execute it. |
| [exec](../command/exec.md) | Run unix commands in a subshell. |
| [fe](../command/fe.md) | Iterate over a word list |
| [fec](../command/fec.md) | Iterate over the characters in a string |
| [for](../command/for.md) | Multi-purpose looping command. |
| [foreach](../command/foreach.md) | Iterate over aliases or assign names in a structure. |
| [hook](../command/hook.md) | Throw an [on hook](../on/hook.md) event. |
| [if](../command/if.md) | Conditional command. |
| [input](../command/input.md) | Get the user to answer a question with a modal prompt. |
| [input_char](../command/input_char.md) | Get the user to type a key with a modal prompt. |
| [license](../command/license.md) | Display the copyright and legal disclaimers. |
| [local](../command/local.md) | Create an assign that goes away when the alias is over. |
| [on](../command/on.md) | Register event handlers for certain types of hooks |
| [on_action](../on/action.md) | Hooked when people do [me](../command/me.md) or [describe](../command/describe.md). |
| [on_channel_lost](../on/channel_lost.md) | Hooked when you stop being on a channel. |
| [on_channel_nick](../on/channel_nick.md) | Hooked when people change their nickname. |
| [on_channel_signoff](../on/channel_signoff.md) | Hooked when people leave a channel. |
| [on_channel_sync](../on/channel_sync.md) | Channel synchronization notification; not a guarantee that every possible fact is known. |
| [on_connect](../on/connect.md) | Hooked when a server accepts you. |
| [on_ctcp](../on/ctcp.md) | Hooked when a [ctcp](../command/ctcp.md) message needs to be displayed. |
| [on_ctcp_reply](../on/ctcp_reply.md) | Hooked when someone response to your [ctcp](../command/ctcp.md). |
| [on_ctcp_request](../on/ctcp_request.md) | Hooked when someone sends you a [ctcp](../command/ctcp.md). |
| [on_disconnect](../on/disconnect.md) | Hooked when you're not connected to a server. |
| [on_error](../on/error.md) | Hooked when the server sends you an ERROR. |
| [on_exec](../on/exec.md) | Hooked when an [exec](../command/exec.md) process writes to stdout. |
| [on_exec_errors](../on/exec_errors.md) | Hooked when an [exec](../command/exec.md) process writes to stderr. |
| [on_exec_exit](../on/exec_exit.md) | Hooked whan [exec](../command/exec.md) process terminates. |
| [on_exec_prompt](../on/exec_prompt.md) | Hooked when [exec](../command/exec.md) process writes a partial line. |
| [on_exit](../on/exit.md) | Hooked when the client is shutting down |
| [on_general_notice](../on/general_notice.md) | Hooked when you receive any kind of [notice](../command/notice.md). |
| [on_general_privmsg](../on/general_privmsg.md) | Hooked when you receive any kind of msg. |
| [on_hook](../on/hook.md) | Hooked when you use the [hook](../command/hook.md) command. |
| [on_idle](../on/idle.md) | Hooked once a minute when you're not pressing keys. |
| [on_input](../on/input.md) | Hooked when you use [bind send_line](../bind/send_line.md). |
| [on_invite](../on/invite.md) | Hooked when someone invites you to a channel. |
| [on_join](../on/join.md) | Hooked when you join a channel. |
| [on_keybinding](../on/keybinding.md) | Hooked each time a keybinding is executed. |
| [on_kick](../on/kick.md) | Hooked when someone is kicked from a channel. |
| [on_kill](../on/kill.md) | Hooked when someone is kicked off of irc. |
| [on_list](../on/list.md) | Hooked for each line when you do [list](../command/list.md). |
| [on_mode](../on/mode.md) | Hooked when someone changes the mode on a channel. |
| [on_mode_stripped](../on/mode_stripped.md) | Hooked once for each mode change on a channel. |
| [on_msg](../on/msg.md) | Hooked when someone sends you a private message. |
| [on_msg_group](../on/msg_group.md) | Hooked when someone sends a message to everyone. |
| [on_names](../on/names.md) | Hooked for each line when you do [names](../command/names.md). |
| [on_new_nickname](../on/new_nickname.md) | Hooked when the client needs a new nickname from you. |
| [on_nickname](../on/nickname.md) | Hooked when someone changes nickname |
| [on_notice](../on/notice.md) | Hooked when someone has sent you a [notice](../command/notice.md). |
| [on_numeric](../on/numeric.md) | Hooked when you receive a numeric reply from server. |
| [on_odd_server_stuff](../on/odd_server_stuff.md) | Hooked when the server sends something that can't be parsed. |
| [on_oper_notice](../on/oper_notice.md) | Hooked when the server sends a message to opers. |
| [on_operwall](../on/operwall.md) | Hooked when someone sends a message to all opers. |
| [on_part](../on/part.md) | Hooked when someone leave the channel. |
| [on_pong](../on/pong.md) | Hooked when the server responds to your ping request. |
| [on_public](../on/public.md) | Hooked when someone talks on a current channel. |
| [on_public_msg](../on/public_msg.md) | Hooked when someone outside the channel talks. |
| [on_public_notice](../on/public_notice.md) | Hooked when someone sends a [notice](../command/notice.md) to the channel. |
| [on_public_other](../on/public_other.md) | Hooked when someoen talks to a non-current channel. |
| [on_raw_irc](../on/raw_irc.md) | Hooked for every line we get from the server. |
| [on_send_action](../on/send_action.md) | Hooked for every [me](../command/me.md) or [describe](../command/describe.md) you do. |
| [on_send_ctcp](../on/send_ctcp.md) | Hooked for every [ctcp](../command/ctcp.md) you send out. |
| [on_send_msg](../on/send_msg.md) | Hooked for every msg you send to someone else. |
| [on_send_notice](../on/send_notice.md) | Hooked for every notice you send out. |
| [on_send_public](../on/send_public.md) | Hooked for every msg you send to a channel. |
| [on_send_to_server](../on/send_to_server.md) | Hooked for every line you send to the server. |
| [on_server_established](../on/server_established.md) | Hooked when we connect to a server, before we register. |
| [on_server_lost](../on/server_lost.md) | Hooked when we lose a server connection for any reason. |
| [on_server_notice](../on/server_notice.md) | Hooked when the server sends you a notice. |
| [on_server_status](../on/server_status.md) | Hooked when the status of a server changes. |
| [on_set](../on/set.md) | Hooked when you use the [set](../command/set.md) command. |
| [on_signal](../on/signal.md) | Hooked when an OS signal is caught by the client. |
| [on_signoff](../on/signoff.md) | Hooked when someone leaves irc. |
| [on_silence](../on/silence.md) | Hooked when someone has silenced you. |
| [on_ssl_server_cert](../on/ssl_server_cert.md) | Hooked when an ssl server sends us its certificate. |
| [on_status_update](../on/status_update.md) | Hooked every time a status bar changes. |
| [on_switch_channels](../on/switch_channels.md) | Hooked every time you change the current channel. |
| [on_switch_windows](../on/switch_windows.md) | Hooked every time you change the current window. |
| [on_timer](../on/timer.md) | Hooked at the top of every minute. |
| [on_topic](../on/topic.md) | Hooked when someone changes the topic of a channel. |
| [on_unknown_command](../on/unknown_command.md) | Hooked when you run a command that isn't builtin or an alias. |
| [on_unload](../on/unload.md) | Hooked when the user does an [unload](../command/unload.md). |
| [on_wallop](../on/wallop.md) | Hooked when someone does a wallop. |
| [on_who](../on/who.md) | Hooked for each line of a [who](../command/who.md) reply. |
| [on_window](../on/window.md) | Hooked for each line of output to a window. |
| [on_window_beforekill](../on/window_beforekill.md) | Hooked just before a window is killed. |
| [on_window_command](../on/window_command.md) | Hooked for each operation of a [window](../command/window.md) command. |
| [on_window_create](../on/window_create.md) | Hooked when you create a new window. |
| [on_window_kill](../on/window_kill.md) | Hooked after a window has been destroyed. |
| [on_window_notified](../on/window_notified.md) | Hooked when a hidden window that is notifying has output. |
| [on_window_server](../on/window_server.md) | Hooked when a window changes its server association. |
| [on_yell](../on/yell.md) | Hooked when the client outputs a diagnostic message. |
| [package](../command/package.md) | Tag aliases, assigns, ons, etc, as belonging to a package group that can be [unload](../command/unload.md)ed later. |
| [parsekey](../command/parsekey.md) | Execute a keybinding by name. |
| [pause](../command/pause.md) | Nonblocking sleep for a time, or until the user presses a key. |
| [pop](../command/pop.md) | Remove the last word from a variable. |
| [pretend](../command/pretend.md) | Pretend the server just sent the client a string. |
| [push](../command/push.md) | Add a word to the end of a variable. |
| [queue](../command/queue.md) | Add a command to a named queue for executing later. |
| [quote](../command/quote.md) | Send a string directly to the server. |
| [rbind](../command/rbind.md) | Display all of the sequences bound to a keybinding. |
| [repeat](../command/repeat.md) | Execute some commands multiple times. |
| [return](../command/return.md) | Early termination of the current atomic scope. |
| [say](../command/say.md) | Say something to the current channel. |
| [send](../command/send.md) | Say something to the current target. |
| [sendline](../command/sendline.md) | Pretend the user just typed this string at the input prompt. |
| [set](../command/set.md) | Change a configuration variable. |
| [set_always_split_biggest](../set/always_split_biggest.md) | Whether to split current window or biggest window for [window new](../window/new.md). |
| [set_banner](../set/banner.md) | The thing to display before system messages (ie, `***`) |
| [set_banner_expand](../set/banner_expand.md) | Whether to run [set banner](../set/banner.md) through the $-expander. |
| [set_beep](../set/beep.md) | Whether to allow beeps or eat them. |
| [set_channel_name_width](../set/channel_name_width.md) | How wide channel name should be on status bar. |
| [set_client_information](../set/client_information.md) | Configurable text returned by the supplied CTCP VERSION responder. |
| [set_clock](../set/clock.md) | Whether to run the system clock (turning off breaks stuff!) |
| [set_clock_24hour](../set/clock_24hour.md) | Whether the system clock should be 12 hour or 24 hour. |
| [set_clock_format](../set/clock_format.md) | What strftime() format to use to make the system clock. |
| [set_clock_interval](../set/clock_interval.md) | How often to update the system clock. |
| [set_cmdchars](../set/cmdchars.md) | What characters are used before a command (ie, `/`) |
| [set_comment_hack](../set/comment_hack.md) | Whether to allow comments in the standard loader in the middle of lines. |
| [set_continued_line](../set/continued_line.md) | What to prefix before broken-up physical lines. |
| [set_current_window_level](../set/current_window_level.md) | Assume the current window always owns these levels, overruling the window levels. |
| [set_debug](../set/debug.md) | Get help debugging your script. |
| [set_default_realname](../set/default_realname.md) | The value we send to the server for your IRCNAME |
| [set_default_username](../set/default_username.md) | The value we sent to the server for your username |
| [set_dispatch_unknown_commands](../set/dispatch_unknown_commands.md) | Whether to bother the server with your typos. |
| [set_display](../set/display.md) | Whether to suppress output to windows. |
| [set_floating_point_math](../set/floating_point_math.md) | Whether to do math in floating point. |
| [set_floating_point_precision](../set/floating_point_precision.md) | How many decimal places to return for floating point numbers. |
| [set_hide_private_channels](../set/hide_private_channels.md) | Whether to hide the channel name on the status bar. |
| [set_hold_interval](../set/hold_interval.md) | Script-provided setting. The default [window hold_interval](../window/hold_interval.md) value. |
| [set_hold_mode](../set/hold_mode.md) | Script-provided setting. The default [window hold_mode](../window/hold_mode.md) value. |
| [set_hold_slider](../set/hold_slider.md) | The default [window hold_slider](../window/hold_slider.md) value. |
| [set_indent](../set/indent.md) | Whether to indent broken lines. |
| [set_input_prompt](../set/input_prompt.md) | What prompt to use in the input line. |
| [set_insert_mode](../set/insert_mode.md) | Whether to insert before or overwrite the char under the cursor. |
| [set_key_interval](../set/key_interval.md) | How many milliseconds until ambiguous keybindings time out. |
| [set_lastlog](../set/lastlog.md) | What the default [window lastlog](../window/lastlog.md) size should be. |
| [set_lastlog_level](../set/lastlog_level.md) | What the default [window lastlog_level](../window/lastlog_level.md) should be. |
| [set_lastlog_rewrite](../set/lastlog_rewrite.md) | Set a default value for [LASTLOG](../command/lastlog.md) -REWRITE |
| [set_load_path](../set/load_path.md) | Where to look for [load](../command/load.md) files. |
| [set_log](../set/log.md) | Whether to write everything displayed to the global logfile. |
| [set_log_rewrite](../set/log_rewrite.md) | Rewrite stuff before it is written to the global logfile. |
| [set_logfile](../set/logfile.md) | The default global logfile name. |
| [set_mail](../set/mail.md) | Script-provided control of local mailbox checking. |
| [set_mail_interval](../set/mail_interval.md) | Script-provided interval for local mailbox checking. |
| [set_mangle_display](../set/mangle_display.md) | How to mangle stuff before we write it to the screen. |
| [set_mangle_inbound](../set/mangle_inbound.md) | How to mangle stuff we receive from the server. |
| [set_mangle_logfiles](../set/mangle_logfiles.md) | How to mangle stuff we are writing to a logfile. |
| [set_mangle_outbound](../set/mangle_outbound.md) | How to mangle stuff we are sending to the server. |
| [set_metric_time](../set/metric_time.md) | Whether to use regular (minute) or metric (milliday) units for the clock. |
| [set_mode_stripper](../set/mode_stripper.md) | Whether to turn on [on mode_stripped](../on/mode_stripped.md). |
| [set_new_server_lastlog_level](../set/new_server_lastlog_level.md) | What level to give a window when you do [window server](../window/server.md) to a new server. |
| [set_no_control_log](../set/no_control_log.md) | Whether control character should be stripped from stuff being written to logfiles. |
| [set_no_fail_disconnect](../set/no_fail_disconnect.md) | Whether the client should disconnect from server when writes fail. |
| [set_notify_level](../set/notify_level.md) | What the default [window notify_level](../window/notify_level.md) should be. |
| [set_notify_on_termination](../set/notify_on_termination.md) | Whether to tell you that an [exec](../command/exec.md) process has finished. |
| [set_num_of_whowas](../set/num_of_whowas.md) | Script-provided setting. How many whowas entries to ask the server for. |
| [set_old_server_lastlog_level](../set/old_server_lastlog_level.md) | Resolve level conflicts when merging a window onto an already connected server. |
| [set_output_rewrite](../set/output_rewrite.md) | How output should be rewritten before it's displayed. |
| [set_pad_char](../set/pad_char.md) | What char we should use for $[num]var expandos. |
| [set_quit_message](../set/quit_message.md) | What the default quit message should be. |
| [set_screen_options](../set/screen_options.md) | What flags should be passed to gnu screen. |
| [set_scroll_lines](../set/scroll_lines.md) | How many lines the display should scroll when new output occurs in a full window. |
| [set_scrollback](../set/scrollback.md) | How big the default window scrollback size is. |
| [set_scrollback_ratio](../set/scrollback_ratio.md) | How much (percentage) each scroll back or scroll forward moves the display |
| [set_shell](../set/shell.md) | Which shell should be used for [exec](../command/exec.md) |
| [set_shell_flags](../set/shell_flags.md) | Which flags should be passed to your shell. |
| [set_shell_limit](../set/shell_limit.md) | How many lines of output from an [exec](../command/exec.md) process before we shut it down. |
| [set_show_channel_names](../set/show_channel_names.md) | Whether to show the channel roster when joining a channel. |
| [set_show_end_of_msgs](../set/show_end_of_msgs.md) | Script-provided setting. Whether to hook end-of-message events. |
| [set_show_numerics](../set/show_numerics.md) | Whether to show the numeric or [set banner](../set/banner.md) in numeric replies. |
| [set_show_status_all](../set/show_status_all.md) | Whether some status expandos show only in current window status or all window status. |
| [set_show_who_hopcount](../set/show_who_hopcount.md) | Script-provided setting. Whether to show the server hopcount in who replies. |
| [set_status_away](../set/status_away.md) | How %A looks when you are away. |
| [set_status_channel](../set/status_channel.md) | How %C looks when you are on a channel. |
| [set_status_chanop](../set/status_chanop.md) | How %@ looks when you are a chanop. |
| [set_status_clock](../set/status_clock.md) | How %T looks when the clock is on. |
| [set_status_does_expandos](../set/status_does_expandos.md) | Whether to $-expand the status format. |
| [set_status_format](../set/status_format.md) | What the status bar should look like. |
| [set_status_format1](../set/status_format1.md) | What the top line of double status bar should be. |
| [set_status_format2](../set/status_format2.md) | What the bottom line of double status bar should be. |
| [set_status_halfop](../set/status_halfop.md) | What %@ looks like when you are a half-op |
| [set_status_hold](../set/status_hold.md) | What %H looks like when youre in hold mode. |
| [set_status_hold_lines](../set/status_hold_lines.md) | How many lines you're holding in hold mode. |
| [set_status_insert](../set/status_insert.md) | What %I looks like when youre in insert mode. |
| [set_status_mail](../set/status_mail.md) | What %M looks like when you have mail. |
| [set_status_mode](../set/status_mode.md) | What %+ looks like for your channel mode. |
| [set_status_nickname](../set/status_nickname.md) | What %N looks like for your nickname. |
| [set_status_no_repeat](../set/status_no_repeat.md) | Don't repeat the last character of status format. |
| [set_status_noswap](../set/status_noswap.md) | What appears when [window swap](../window/swap.md) is turned off. |
| [set_status_notify](../set/status_notify.md) | The list of hidden windows that have output. |
| [set_status_oper](../set/status_oper.md) | What %* looks like if you are an irc oper. |
| [set_status_overwrite](../set/status_overwrite.md) | What %I looks like when you're in overwite mode. |
| [set_status_query](../set/status_query.md) | What appears when you have a query. |
| [set_status_scrollback](../set/status_scrollback.md) | What appears when you are in scrollback. |
| [set_status_server](../set/status_server.md) | What the server name looks like. |
| [set_status_ssl_off](../set/status_ssl_off.md) | What appears when server does not do ssl. |
| [set_status_ssl_on](../set/status_ssl_on.md) | What appears when server does ssl. |
| [set_status_umode](../set/status_umode.md) | What your user mode looks like. |
| [set_status_user](../set/status_user.md) | What %U looks like. |
| [set_status_voice](../set/status_voice.md) | What %@ looks like when you're a channel voice. |
| [set_status_window](../set/status_window.md) | What the window refnum looks like. |
| [set_switch_channels_between_windows](../set/switch_channels_between_windows.md) | Whether to allow switch windows to steal another window's channels. |
| [set_term_does_bright_blink](../set/term_does_bright_blink.md) | Whether the terminal does bright blink. |
| [set_user_information](../set/user_information.md) | Text returned by the supplied CTCP USERINFO responder. |
| [set_verbose_ctcp](../set/verbose_ctcp.md) | Script-provided setting. Whether to tell you if someone [ctcp](../command/ctcp.md)s you. |
| [set_word_break](../set/word_break.md) | What characters constitute breaks between words. |
| [set_wserv_path](../set/wserv_path.md) | Where to find the wserv program. |
| [set_wserv_type](../set/wserv_type.md) | Whether wserv should create gnu screens or xterms. |
| [set_xterm](../set/xterm.md) | Which program you use as xterm (ie, rxvt) |
| [set_xterm_options](../set/xterm_options.md) | What options you needed passed to your xterm. |
| [setenv](../command/setenv.md) | Change an environment variable. |
| [shift_command](../command/shift.md) | Remove the first word from a variable. |
| [shook](../command/shook.md) | Dispatch any arbitrary hook event. |
| [sleep](../command/sleep.md) | Blocking sleep of the client. |
| [stack](../command/stack.md) | Save and restore copies of an alias, assign, on, set, etc |
| [stub](../command/stub.md) | On-demand [load](../command/load.md)ing for an alias or assign. |
| [subpackage](../command/subpackage.md) | Add a segment to the namespace for stuff you [load](../command/load.md). |
| [switch](../command/switch.md) | Select a command block by wildcard pattern. |
| [silence](../command/silence.md) | Server-side ignores (not on all servers) |
| [timer](../command/timer.md) | Run a command later. |
| [type](../command/type.md) | Pretend the user just typed a string. |
| [unclear](../command/unclear.md) | Pull down the scrollback so it fills the screen. |
| [unless](../command/unless.md) | Reverse of [if](../command/if.md). |
| [unload](../command/unload.md) | Remove alias, assigns, ons, sets, etc from a [package](../command/package.md). |
| [unshift_command](../command/unshift.md) | Add a word to the start of a variable. |
| [until](../command/until.md) | Reverse of [while](../command/while.md). |
| [usleep](../command/usleep.md) | Blocking sleep of the client, less than a second. |
| [wait](../command/wait.md) | Nonblocking suspending of execution until previous server request finished. |
| [which](../command/which.md) | Find the full path of a [load](../command/load.md)ed file. |
| [while](../command/while.md) | Execute a block while some expression is true. |
| [window](../command/window.md) | Manipulate the EPIC on-screen display areas known as "windows". |
| [window add](../window/add.md) | Add a nickname to your query list. |
| [window back](../window/back.md) | Go back to the previous current window, swapping it in if necessary. |
| [window balance](../window/balance.md) | Make all the windows the same size. |
| [window beep_always](../window/beep_always.md) | Beep even if the window is hidden. |
| [window channel](../window/channel.md) | Change the current channel. |
| [window clear](../window/clear.md) | Scroll down so nothing shows in the window. |
| [window create](../window/create.md) | Create a new screen. |
| [window delete](../window/delete.md) | Remove a screen you don't want any more. |
| [window describe](../window/describe.md) | Let me tell you about your window. |
| [window discon](../window/discon.md) | Disassociate the window from its server. |
| [window double](../window/double.md) | Turn on the double status bar. |
| [window echo](../window/echo.md) | Output something to the window. |
| [window fixed](../window/fixed.md) | Forbid changing the window's size. |
| [window flush](../window/flush.md) | Delete the scrollback below what you see. |
| [window flush_scrollback](../window/flush_scrollback.md) | Delete the entire scrollback. |
| [window goto](../window/goto.md) | Switch to the window, counting from the top of screen |
| [window grow](../window/grow.md) | Increase the size of the window. |
| [window hide](../window/hide.md) | Remove a window from the screen. |
| [window hide_others](../window/hide_others.md) | Make this window the only one on the screen. |
| [window hold_interval](../window/hold_interval.md) | How often the status bar updates when holding stuff in this window. |
| [window hold_mode](../window/hold_mode.md) | Stop displaying stuff to the window, but save it in the scrollback. |
| [window hold_slider](../window/hold_slider.md) | How much to scroll down when you hit <enter>. |
| [window indent](../window/indent.md) | Overrule [set indent](../set/indent.md) for this window. |
| [window kill](../window/kill.md) | Delete a window you don't want any more. |
| [window kill_all_hidden](../window/kill_all_hidden.md) | Delete all of the hidden (invisible) windows. |
| [window kill_others](../window/kill_others.md) | Make this the only window left for the whole client. |
| [window killable](../window/killable.md) | Control whether the window may be killed. |
| [window killswap](../window/killswap.md) | Kill this window, and swap in an invisible window in its place. |
| [window last](../window/last.md) | Go back to the previous current window, but not if it's hidden. |
| [window lastlog](../window/lastlog.md) | How many logical lines of output to save. |
| [window lastlog_level](../window/lastlog_level.md) | What levels of output should be saved to the lastlog. |
| [window level](../window/level.md) | What levels of output should be sent to this window. |
| [window list](../window/list.md) | Describe all the windows. |
| [window log](../window/log.md) | Turn on or off the window's log file. |
| [window logfile](../window/logfile.md) | Change the window's log filename. |
| [window move](../window/move.md) | Move the window up or down on the screen. |
| [window move_to](../window/move_to.md) | Move the window to the Nth place, counting from the top of the screen. |
| [window name](../window/name.md) | Change the window's name. |
| [window new](../window/new.md) | Create a new window, splitting a visible window in half. |
| [window new_hide](../window/new_hide.md) | Create a new hidden window. |
| [window next](../window/next.md) | Swap the current window with the hidden window with the next higher refnum. |
| [window noserv](../window/noserv.md) | Disassociate the window from the server. |
| [window notified](../window/notified.md) | Toggle whether the window is notifying that it has output since it's been hidden. |
| [window notify](../window/notify.md) | Toggle whether the window should notify you when it has output while it's hidden. |
| [window notify_level](../window/notify_level.md) | Toggle what types of output cause the window to notify you while it's hidden. |
| [window notify_name](../window/notify_name.md) | What the window's name looks like on the status bar when it's notifying you. |
| [window number](../window/number.md) | Change the window's refnum. |
| [window pop](../window/pop.md) | Go back to the window you last [window push](../window/push.md)ed. |
| [window previous](../window/previous.md) | Swap the current window with the hidden window with the next lower refnum. |
| [window push](../window/push.md) | Save the current window's refnum onto a stack. |
| [window query](../window/query.md) | Change the window's current query target. |
| [window rebuild_scrollback](../window/rebuild_scrollback.md) | Throw away the scrollback buffer, and rebuild it from the lastlog. |
| [window refnum](../window/refnum.md) | Change the current window to another visible window. |
| [window refnum_or_swap](../window/refnum_or_swap.md) | Change the current window to another visible window, swapping it in if necessary. |
| [window refresh](../window/refresh.md) | Redraw the window. |
| [window rejoin](../window/rejoin.md) | Join a channel on a window's server, putting it in whichever window claims it. |
| [window remove](../window/remove.md) | Remove a nick from the window's query list. |
| [window scrolladj](../window/scrolladj.md) | Whether to insert space at the bottom, or pull scrollback back down from the top when a window grows in size. |
| [window scrollback](../window/scrollback.md) | How big the window's scrollback buffer should be. |
| [window scroll_backward](../window/scroll_backward.md) | Go back some number of lines in scrollback. |
| [window scroll_end](../window/scroll_end.md) | Go to the end (newest) of the scrollback. |
| [window scroll_forward](../window/scroll_forward.md) | Go forward some number of lines in scrollback. |
| [window scroll_start](../window/scroll_start.md) | Go to the start (oldest) of the scrollback. |
| [window search_back](../window/search_back.md) | Go backwards in scrollback to find a string. |
| [window search_forward](../window/search_forward.md) | Go forwards in scrollback to find a string. |
| [window server](../window/server.md) | Change which server this window is associated with. |
| [window show](../window/show.md) | Make a hidden window visible (by splitting a visible window) |
| [window show_all](../window/show_all.md) | Make all hidden windows visible (by splitting visible windows) |
| [window shrink](../window/shrink.md) | Make a window smaller |
| [window size](../window/size.md) | Set the window size to an absolute value. |
| [window skip](../window/skip.md) | Can [bind next_window](../bind/next_window.md) move to this window? |
| [window stack](../window/stack.md) | Show the refnums saved on the stack. |
| [window status_format](../window/status_format.md) | The status line for a single line status bar. |
| [window status_format1](../window/status_format1.md) | The bottom line of a double line status bar. |
| [window status_format2](../window/status_format2.md) | The top line of a double line status bar. |
| [window status_special](../window/status_special.md) | What %. should be on this window's status bar. |
| [window swap](../window/swap.md) | Make this window invisible, and make a hidden window visible, taking its place. |
| [window swappable](../window/swappable.md) | Change you change the visibility of this window? (Ie, hide a visible window) |
| [window topline](../window/topline.md) | Set the text of a selected topline. |
| [window toplines](../window/toplines.md) | Set how many toplines a window reserves. |
| [window unclear](../window/unclear.md) | Push down the scrollback so it's visible in the window. |
| [xdebug](../command/xdebug.md) | Change some internal debugging flags. |
| [xecho](../command/xecho.md) | Output to a window, with flags |
| [xeval](../command/xeval.md) | Run some commands, with flags. |
| [xquote](../command/xquote.md) | Send a string to the server, with flags. |
| [xtype](../command/xtype.md) | Type some text, with flags. |


## Functions

| Reference | Description |
| --- | --- |
| [abs](../function/abs.md) | Absolute Value of number |
| [acos](../function/acos.md) | Arc Cosine of number |
| [acosh](../function/acosh.md) | Inverse Hyperbolic Cosine of number |
| [after](../function/after.md) | Return string after a character |
| [afterw](../function/afterw.md) | Return words in list after a word. |
| [aliasctl](../function/aliasctl.md) | Low level manipulation on aliases and assigns. |
| [ascii](../function/ascii.md) | Convert strings to codepoints (numbers). |
| [asciiq](../function/asciiq.md) | Convert url-encoded strings to codepoints. |
| [asin](../function/asin.md) | Arc Sine of number |
| [asinh](../function/asinh.md) | Inverse Hyperbolic Sine of number |
| [atan](../function/atan.md) | Arctangent of number |
| [atanh](../function/atanh.md) | Inverse Hyperbolic Sine of number. |
| [b64decode](../disambiguation/b64decode.md) | Script-provided function. Convert Base64 into a string. |
| [b64encode](../disambiguation/b64encode.md) | Script-provided function. Covnert a string into Base64. |
| [before](../function/before.md) | Return string before a character. |
| [beforew](../function/beforew.md) | Return words in list before a word. |
| [bindctl](../function/bindctl.md) | Low level manipulation of keybindings. |
| [builtin_expando](../function/builtin_expando.md) | Call a builtin-expando directly. |
| [ceil](../function/ceil.md) | Ceiling of number |
| [center](../function/center.md) | Pad a string with spaces to center it. |
| [cexist](../function/cexist.md) | Does a command exist? |
| [chanmode](../function/chanmode.md) | What is the mode of a channel? |
| [channel](../function/channel.md) | Summarize users on channel (op, voice, nick) |
| [chanusers](../function/chanusers.md) | Who is on a channel? |
| [chanwin](../function/chanwin.md) | What window is this channel in? |
| [chmod](../function/chmod.md) | Change a file's permissions. |
| [chngw](../function/chngw.md) | Change a word in a word list. |
| [chop](../function/chop.md) | Remove chars from end of string. |
| [chops](../function/chops.md) | Who is a chanop on a channel? |
| [chr](../function/chr.md) | Convert codepoints (numbers) into strings. |
| [chrq](../function/chrq.md) | Convert codepoints (numbers) into url-encoded strings. |
| [cipher](../function/cipher.md) | What cipher is the (ssl) server connection using? |
| [close](../function/close.md) | Close an [open](../function/open.md) file. |
| [cofilter](../function/cofilter.md) | Return words from 2nd variable, based on which words in 1st variable aren't matched by a pattern. |
| [common](../function/common.md) | Return words common to two word lists. |
| [convert](../function/convert.md) | Convert a hostname to paddr, or paddr to hostname. |
| [copattern](../function/copattern.md) | Return words from 2nd variable, based on which words in 1st variable are matched by a pattern. |
| [corfilter](../function/corfilter.md) | Return words from 2nd variable, based on which patterns in 1st variable don't match a string. |
| [corpattern](../function/corpattern.md) | Return words from 2nd variable, based on which patterns in 1st variable match a string. |
| [cos](../function/cos.md) | Cosine of number. |
| [cosh](../function/cosh.md) | Hyperbolic Cosine of number. |
| [count](../function/count.md) | Count the number of instances of character in string. |
| [cparse](../function/cparse.md) | Convert markup codes into color codes. |
| [curcmd](../function/curcmd.md) | The current ircII command or alias that is running. |
| [curpos](../function/curpos.md) | Where the cursor is in $L (the input line) |
| [currchans](../function/currchans.md) | All current channels for the server. |
| [dbmctl](../function/dbmctl.md) | External hash table support. |
| [decode](../disambiguation/decode.md) | Script-provided function. Recover a string passed to [encode](../disambiguation/encode.md). |
| [delarray](../function/delarray.md) | Delete an entire Karll array. |
| [delitem](../function/delitem.md) | Remove an item from a Karll array by item number. |
| [delitems](../function/delitems.md) | Remove items from a Karll array by item numbers. |
| [deuhc](../function/deuhc.md) | Remove the wildcard part of a nick!user@host string. |
| [diff](../function/diff.md) | Return the words that exist only in one of two word lists. |
| [encode](../disambiguation/encode.md) | Script-provided function. Convert any string into something you can use in a variable name. |
| [eof](../function/eof.md) | Is the [open](../function/open.md) file at end-of-file? |
| [epic](../function/epic.md) | Returns 1, because you're using epic! |
| [exec](../function/exec.md) | Run a unix command in a subshell, returning three [open](../function/open.md) fds. |
| [exp](../function/exp.md) | Exponent operation (x `**` y) |
| [ferror](../function/ferror.md) | Does the [open](../function/open.md) file have an error condition? |
| [fexist](../function/fexist.md) | Does a filename exist? |
| [filter](../function/filter.md) | Return all words that don't match a pattern. |
| [finditem](../function/finditem.md) | The item number of any instance of an item in a Karll array. |
| [finditems](../function/finditems.md) | The item number of all instances of an item in a Karll array. |
| [findw](../function/findw.md) | Return the first [word](../function/word.md) index of a word in a list. |
| [findws](../function/findws.md) | Return all of the [word](../function/word.md) indexes of a word in a list. |
| [fix_arglist](../function/fix_arglist.md) | Convert a string into something you can use as an arglist to an alias or on. |
| [floor](../function/floor.md) | Largest integral number less than or equal to number. |
| [fnexist](../function/fnexist.md) | Does a built in function exist? |
| [frewind](../function/frewind.md) | Reset an [open](../function/open.md) file back to the beginning. |
| [fromw](../function/fromw.md) | Return a words in a list starting with a word. |
| [fseek](../function/fseek.md) | Change the read/write position of an [open](../function/open.md) file. |
| [fsize](../function/fsize.md) | How many bytes big is a file? |
| [fskip](../function/fskip.md) | Skip lines in an [open](../function/open.md) file. |
| [ftell](../function/ftell.md) | Where in an [open](../function/open.md) file am I? |
| [ftime](../function/ftime.md) | When was a file last modified? (mtime) |
| [ftruncate](../function/ftruncate.md) | Delete the contents of a file, but not the file itself. |
| [functioncall](../function/functioncall.md) | Is this alias being called as a function or as a command? |
| [geom](../function/geom.md) | What is the size of the screen? |
| [getarrays](../function/getarrays.md) | Get the name of all active Karll arrays. |
| [getcap](../function/getcap.md) | Low-level capability information. |
| [getcommands](../function/getcommands.md) | Pattern match command names. |
| [getenv](../function/getenv.md) | Get an environment variable. |
| [getfunctions](../function/getfunctions.md) | Pattern match function names. |
| [getgid](../function/getgid.md) | What is my primary user group? (GID) |
| [getitem](../function/getitem.md) | Get an item number from a Karll array. |
| [getlogin](../function/getlogin.md) | What username am I running under? |
| [getmatches](../function/getmatches.md) | A word list of all item numbers that match in a Karll array of strings. |
| [getopt](../function/getopt.md) | Process command line arguments. |
| [getpgrp](../function/getpgrp.md) | What process group am I in? |
| [getrmatches](../function/getrmatches.md) | A word list of all item numbers that match in a Karll array of patterns. |
| [getserial](../function/getserial.md) | Get a serial number that isn't in use. |
| [getset](../function/getset.md) | Get the value of a [set](../command/set.md). |
| [getsets](../function/getsets.md) | Pattern match set names. |
| [gettmatch](../function/gettmatch.md) | Return the best item match from a Karll array. |
| [getuid](../function/getuid.md) | What is my user id? (UID) |
| [glob](../function/glob.md) | Pattern match filenames. |
| [hash_32bit](../function/hash_32bit.md) | Convert a string to a 32 bit integer. |
| [hookctl](../function/hookctl.md) | Low-level manipulation of your [on](../command/on.md)s. |
| [idle](../function/idle.md) | How many seconds since a key was last pressed? (Same as $E) |
| [ifindfirst](../function/ifindfirst.md) | Return the **first** item number of an item in a Karll array. |
| [ifinditem](../function/ifinditem.md) | The index number of the first instance of an item in a Karll array. |
| [ifinditems](../function/ifinditems.md) | The index number of all instances of an item in a Karll array. |
| [igetitem](../function/igetitem.md) | Get an index number from a Karll array. |
| [igetmatches](../function/igetmatches.md) | A word list of all index numbers that match in a Karll array of strings. |
| [igetrmatches](../function/igetrmatches.md) | A word list of all index numbers that match in a Karll array of patterns. |
| [index](../function/index.md) | Return the position of a char in a string. |
| [indextoitem](../function/indextoitem.md) | Convert a Karll array index number to an item number. |
| [indextoword](../function/indextoword.md) | What word in list contains the 'index'th character? |
| [info](../function/info.md) | Return structured information about the client. |
| [insert](../function/insert.md) | Insert a word into a string at the "index"th character. |
| [insertw](../function/insertw.md) | Insert a word into a list. |
| [iptolong](../function/iptolong.md) | Convert a p-addr to a 32 bit long integer (for dcc). |
| [iptoname](../function/iptoname.md) | Resolve the canonical hostname of a p-addr. |
| [irclib](../function/irclib.md) | Where is the standard irc library directory? |
| [isalpha](../function/isalpha.md) | Does this string start with an a-z A-Z character? |
| [isaway](../function/isaway.md) | Am I away on a server? |
| [ischannel](../function/ischannel.md) | Is this a valid channel name on a server? |
| [ischanop](../function/ischanop.md) | Is this person a chanop (+o) on a channel? |
| [ischanvoice](../function/ischanvoice.md) | Is this person a channel voice (+v) on a channel? |
| [isconnected](../function/isconnected.md) | Am I registered to this server? |
| [iscurchan](../function/iscurchan.md) | Is this channel a current channel on this server? |
| [isdigit](../function/isdigit.md) | Does this string start with a digit? |
| [isdisplaying](../function/isdisplaying.md) | Is output being suppressed (ie, with `^)?` |
| [isencrypted](../function/isencrypted.md) | Am I connected to this server using ssl? |
| [isfilevalid](../function/isfilevalid.md) | Can I use this fd in file manipulation functions? |
| [ishalfop](../function/ishalfop.md) | Is this person a channel half-op (+h) on a channel? |
| [isnumber](../function/isnumber.md) | Is this string a number that is valid in this base? |
| [itemtoindex](../function/itemtoindex.md) | Convert a Karll array item number to an index number. |
| [jn](../function/jn.md) | Bessel function of the first kind of the order N.  Um, yea. |
| [joinstr](../function/joinstr.md) | Create a word list by joining words in each of 2 variables. |
| [jot](../function/jot.md) | Create a list of numbers, suitable for iterating over. |
| [json_error](../function/json_error.md) | Return error string set by the last call to [json_explode](../function/json_explode.md). |
| [json_explode](../function/json_explode.md) | Parse a JSON string and expand it into an assign variable structure. |
| [json_implode](../function/json_implode.md) | Serialise an assign variable structure into a JSON string. |
| [key](../function/key.md) | What is the channel key of a channel? |
| [killpid](../function/killpid.md) | Kill a unix process. |
| [lastlog](../function/lastlog.md) | Search the lastlog and return matching lines as values I can pass to [line](../function/line.md). |
| [left](../function/left.md) | Return the first N characters of a string. |
| [leftpc](../function/leftpc.md) | Return the longest initial part of the string that contains N printable characters. |
| [leftw](../function/leftw.md) | Return the first N words of a word list. |
| [levelctl](../function/levelctl.md) | Low-level manipulation of window/lastlog/flood/ignore levels. |
| [levelwindow](../function/levelwindow.md) | Which window owns this level? |
| [line](../function/line.md) | Return a line from the lastlog. |
| [listarray](../function/listarray.md) | Describe the contents of a Karll array. |
| [loadinfo](../function/loadinfo.md) | What file is loading right now? |
| [log](../function/log.md) | Natural logarithm of a number. |
| [log10](../function/log10.md) | Base-10 logarithm of a number. |
| [logctl](../function/logctl.md) | Low-level manipulation of logfiles. |
| [longtoip](../function/longtoip.md) | Convert a 32 bit integer (from DCC) into a p-addr. |
| [mask](../function/mask.md) | Normalize a string into a nick!user@host pattern for banning. |
| [match](../function/match.md) | Return the string that is best matched by a pattern. |
| [matchitem](../function/matchitem.md) | The item number of the best string match in a Karll array. |
| [maxlen](../function/maxlen.md) | Return the [strlen](../function/strlen.md) of the longest word in list. |
| [metric_time](../function/metric_time.md) | Return the current time in (days, millidays) |
| [mid](../function/mid.md) | Return a substring of a string. |
| [midw](../function/midw.md) | Return a subset of the words in a list. |
| [mkdir](../function/mkdir.md) | Make a directory. |
| [mktime](../function/mktime.md) | Convert (Year,month.day.hour.minute.second) to a [time](../function/time.md). |
| [msar](../function/msar.md) | Multiple Search And Replace on a string. |
| [mychannels](../function/mychannels.md) | What channels am I on this server? |
| [myservers](../function/myservers.md) | What severs am I connected to? |
| [nametoip](../function/nametoip.md) | Convert a hostname to its canonical p-addr (ip address) |
| [nochops](../function/nochops.md) | Who is not a channel operator? |
| [nohighlight](../function/nohighlight.md) | Convert highlight characters to reverse chars, the way it's done on the input prompt. |
| [notifywindows](../function/notifywindows.md) | Which hidden windows are notifying they have output? |
| [notw](../function/notw.md) | Remove a word from a list. |
| [numarrays](../function/numarrays.md) | How many Karll arrays are active? |
| [numitems](../function/numitems.md) | The number of items in a Karll array. |
| [numlines](../function/numlines.md) | How many lines on the display would this string take up if you [echo](../command/echo.md)d it? |
| [numonchannel](../function/numonchannel.md) | How many people are on the channel> |
| [numsort](../function/numsort.md) | Sort a string, honoring numerical order. |
| [numwords](../function/numwords.md) | How many words are in this word list? |
| [onchannel](../function/onchannel.md) | Is this person on the channel? |
| [open](../function/open.md) | Open a file for reading or writing. |
| [outputinfo](../function/outputinfo.md) | What is the current output target and output level? |
| [pad](../function/pad.md) | Add chars to a string to make it a certain length. |
| [pass](../function/pass.md) | Remove all but certain characters from a string. |
| [pattern](../function/pattern.md) | Return all words from list that are matched by pattern. |
| [pid](../function/pid.md) | What is the process id? |
| [pop](../function/pop.md) | Remove the last word from a variable. |
| [ppid](../function/ppid.md) | What is my parent's process id? |
| [prefix](../function/prefix.md) | What is the common leading substring on all of the words in a list? |
| [printlen](../function/printlen.md) | How many columns on the screen does this string take up? |
| [push](../function/push.md) | Add a word to the end of a variable. |
| [querywin](../function/querywin.md) | Which window claims this nick as a query? |
| [qword](../function/qword.md) | Get a word from a list as a qword (so it can be used as a dword) |
| [rand](../function/rand.md) | Get a random number. |
| [randread](../function/randread.md) | Read a random line from a file. |
| [read](../function/read.md) | Read a line from an [open](../function/open.md) file. |
| [realpath](../function/realpath.md) | What is the canonical pathname for this file? |
| [regcomp](../function/regcomp.md) | Compile a regular expression. |
| [regcomp_cs](../function/regcomp_cs.md) | Compile a regular expression, case insensitively. |
| [regerror](../function/regerror.md) | Did this regular expression fail? |
| [regexec](../function/regexec.md) | Match a compiled regular expression against a string. |
| [regfree](../function/regfree.md) | Release a compiled regular expression. |
| [regmatches](../function/regmatches.md) | Match a compiled regular expression against a string, returning all backreferences. |
| [remw](../function/remw.md) | Remove a certain word from a word list. |
| [remws](../function/remws.md) | Remove several certain words from a word list. |
| [rename](../function/rename.md) | Rename a file. |
| [repeat](../function/repeat.md) | Repeat a string several times. |
| [rest](../function/rest.md) | Return a string starting with a certain character position. |
| [restw](../function/restw.md) | Return a word list starting with a certain word. |
| [reverse](../function/reverse.md) | Reverse the order of characters in a string. |
| [revw](../function/revw.md) | Reverse the order of words in a string. |
| [rfilter](../function/rfilter.md) | Return all of the patterns from a list that don't match a string. |
| [right](../function/right.md) | Return the last few characters in a string. |
| [rightw](../function/rightw.md) | Return the last few words in a word list. |
| [rindex](../function/rindex.md) | Return the character position of the last instance of a char in a string. |
| [rmatch](../function/rmatch.md) | Return the best pattern from a list that matches a string. |
| [rmatchitem](../function/rmatchitem.md) | The item number of the best pattern in a Karll array. |
| [rmdir](../function/rmdir.md) | Remove a directory. |
| [rpattern](../function/rpattern.md) | Return all of the patterns from a list that matches a string. |
| [rsubstr](../function/rsubstr.md) | Find the last instance of a substring in a larger string. |
| [sar](../function/sar.md) | Search And Replace a string in a larger string. |
| [serverctl](../function/serverctl.md) | Low-level manipulation of servers. |
| [serverwin](../function/serverwin.md) | What is the current window for a server? |
| [servports](../function/servports.md) | Return the remote and local portnum for a server connection. |
| [setitem](../function/setitem.md) | Set an item in a Karll Array. |
| [sha256](../disambiguation/sha256.md) | Script-provided function. SHA256 message digest of a string (Strong crypto hashing). |
| [shift](../function/shift.md) | Remove the first word from a variable. |
| [shiftbrace](../function/shiftbrace.md) | Remove and return the {...} at the start of a variable. |
| [sin](../function/sin.md) | Sine of number. |
| [sinh](../function/sinh.md) | Hyperbolic Sine of number. |
| [sort](../function/sort.md) | Sort a word list case insensitively. |
| [splice](../function/splice.md) | Remove some words, and insert new words, into a word list. |
| [split](../function/split.md) | Convert characters to spaces in a string. |
| [ssl](../function/ssl.md) | Was this client compiled with ssl support? |
| [startupfile](../function/startupfile.md) | What file did the client load at startup? |
| [stat](../function/stat.md) | Return info about a file. |
| [status](../function/status.md) | Get the status bar. |
| [stime](../function/stime.md) | Human readable form of the time. |
| [strftime](../function/strftime.md) | Format the current time any way you want. |
| [strptime](../function/strptime.md) | Convert a string into a unix timestamp. |
| [strip](../function/strip.md) | Remove characters from a string. |
| [stripansi](../function/stripansi.md) | Convert codepoints 14-33 except 15 and 22 in a string to "safe" codepoints. |
| [stripansicodes](../function/stripansicodes.md) | The same as $stripcrap(NORMALIZE $*) |
| [stripc](../function/stripc.md) | The same as $stripcrap(COLOR $*) |
| [stripcrap](../function/stripcrap.md) | [Mangle](mangle_types.md) a string. |
| [strlen](../function/strlen.md) | The number of characters in a string. |
| [strtol](../function/strtol.md) | Convert a baseN number to base10, 2 <= N <= 36. |
| [substr](../function/substr.md) | Find a substring in a larger string. |
| [symbolctl](../function/symbolctl.md) | Low level manipulation of aliases, assigns, builtin commands, builtin functions, builtin expandos, and builtin variables ([set](../command/set.md)s). |
| [tan](../function/tan.md) | Tangent of number. |
| [tanh](../function/tanh.md) | Hyperbolic Tangent. |
| [tdiff](../function/tdiff.md) | Number converted to hours-minutes-seconds (long form) |
| [tdiff2](../function/tdiff2.md) | Number converted to hours-minutes-seconds (short form) |
| [time](../function/time.md) | What is the current time, in whole seconds? |
| [timerctl](../function/timerctl.md) | Low-level manipulation of [timer](../command/timer.md)s. |
| [tobase](../function/tobase.md) | Convert a base10 number to another base. |
| [tolower](../function/tolower.md) | Convert a string to lowercase. |
| [toupper](../function/toupper.md) | Convert a string to uppercase. |
| [tow](../function/tow.md) | Return a word list up to and including a word. |
| [tr](../function/tr.md) | Change characters in a string. |
| [trunc](../function/trunc.md) | Round a floating point numbers to a certain number of decimal places. |
| [ttyname](../function/ttyname.md) | What tty am I using? |
| [twiddle](../function/twiddle.md) | Expand a pathnames that contains a ~ for homedirs. |
| [umask](../function/umask.md) | Change the default umask for newly created files. |
| [uname](../function/uname.md) | Tell me about the unix I'm using. |
| [uniq](../function/uniq.md) | Remove duplicates from a word list. |
| [unlink](../function/unlink.md) | Remove a file. |
| [unshift](../function/unshift.md) | Add a string to the start of a string. |
| [unsplit](../function/unsplit.md) | Convert a dword list into a uword list using a seperator. |
| [urldecode](../disambiguation/urldecode.md) | Script-provided function. Convert a string from url format into normal. |
| [urlencode](../disambiguation/urlencode.md) | Script-provided function. Convert a string into url format. |
| [userhost](../function/userhost.md) | What is the userhost of a nickname or current message? |
| [usermode](../function/usermode.md) | What is my usermode? |
| [usetitem](../function/usetitem.md) | Set an item in a Karll array (faster) |
| [utime](../function/utime.md) | What is the current time, including usec? |
| [version](../function/version.md) | What is the server version? |
| [which](../function/which.md) | Path search for a file. |
| [winchan](../function/winchan.md) | Translate between current channel and window refnum. |
| [windowctl](../function/windowctl.md) | Low-level manipulation of windows. |
| [word](../function/word.md) | Get a word from a word list. |
| [wordtoindex](../function/wordtoindex.md) | Which [index](../function/index.md) position does this word start at? |
| [write](../function/write.md) | Write a line to an [open](../function/open.md) file. |
| [writeb](../function/writeb.md) | Write some binary data to an [open](../function/open.md) file. |
| [xdebug](../function/xdebug.md) | Manipulate the xdebug flags. |
| [xform](../function/xform.md) | Transform a string from one form to another. |
| [yn](../function/yn.md) | Bessel function of the second kind for integer order n. |


## Scripts

| Reference | Description |
| --- | --- |
| [2.8script](../scripts/2.8script.md) | Join/leave compatibility aliases and a numeric 367 handler; the leave alias calls an unavailable command. |
| [activity](../scripts/activity.md) | An example of how to use generalized activity handling. |
| [addset](../scripts/addset.md) | Create and destroy your own [set](../command/set.md)s. |
| [altchan](../scripts/altchan.md) | Implement <alt>-<number> window switching like bx. |
| [autojoin](../scripts/autojoin.md) | Automatically join channels when you (re-)connect to server. |
| [autoquery](../scripts/autoquery.md) | Automatically create a new querywin when someone msgs you. |
| [builtins](../scripts/builtins.md) | Compatibility aliases, settings, and supporting scripts; some historical helpers depend on removed facilities. |
| [chanmonitor](../scripts/chanmonitor.md) | Displays output of non-current channels in hidden windows to a special visible window. |
| [commandqueues](../scripts/commandqueues.md) | Time-delay processing queues. |
| [country](../scripts/country.md) | Convert between country codes and country names. |
| [data_array](../scripts/data_array.md) | This is a work in progress. |
| [data_struct](../scripts/data_struct.md) | This is a work in progress. |
| [debug.irc](../scripts/debug.irc.md) | Aliases to help you debug/tune your script. |
| [dump](../scripts/dump.md) | Script-defined cleanup of aliases, variables, hooks, and related script state. |
| [edit_topic](../scripts/edit_topic.md) | Edit the topic of the current channel. |
| [files](../scripts/files.md) | Examples of what you can do with [open](../function/open.md) files. |
| [floodprot](../scripts/floodprot.md) | Implement outbound flood protection. |
| [functions](../scripts/functions.md) | Utility commands and aliases, including historical helpers with removed dependencies. |
| [global](../scripts/global.md) | Default startup setup used when no readable personal startup file is selected. |
| [grep](../scripts/grep.md) | An example of how to grep a file with [open](../function/open.md). |
| [guh](../scripts/guh.md) | A few aliases for userhost, ison, and channels. |
| [highlight](../scripts/highlight.md) | Imlement something like the old "highlight ignores". |
| [history](../scripts/history.md) | Script-provided command history and navigation. |
| [hold_mode](../scripts/hold_mode.md) | Fully enable ircII-like hold mode behavior. |
| [ison](../scripts/ison.md) | Low-level interface to the ison queue. |
| [less](../scripts/less.md) | Peruse a file page by page. |
| [less-pipe](../scripts/less-pipe.md) | Peruse an [exec](../disambiguation/exec.md) process output page by page. |
| [loadformats](../scripts/loadformats.md) | A theming facility. |
| [local.examp](../scripts/local.examp.md) | An example of the local customization file. |
| [mail](../scripts/mail.md) | Check multiple mboxes at once. |
| [map](../scripts/map.md) | A client-side implementation of the [map](../scripts/map.md) command. |
| [meta-compat](../scripts/meta-compat.md) | Backwards compatibility for scripts that bound META keybindings. |
| [motd_script](../scripts/motd.md) | A client side message-of-the-day script. |
| [netsplit](../scripts/netsplit.md) | Handle netsplits and netjoins without flooding your screen. |
| [newaway](../scripts/newaway.md) | Only see other people's away messages once. |
| [newnick](../scripts/newnick.md) | Automatically generate new nicknames when server requires you to change your nickname. |
| [nickcomp](../scripts/nickcomp.md) | Automatic nickname completion for channel text. |
| [nopaste](../scripts/nopaste.md) | Prohibit accidental paste flooding. |
| [notify](../scripts/notify.md) | Nickname monitoring through the server’s MONITOR facility. |
| [paste](../scripts/paste.md) | Allow a special paste mode for paste flooding. |
| [pipe](../scripts/pipe.md) | Implement the function [pipe](../disambiguation/pipe.md) that returns the output from an [exec](../disambiguation/exec.md) command. |
| [reconnect](../scripts/reconnect.md) | Automatically reconnect to servers when disconnected. |
| [renumber](../scripts/renumber.md) | Automatically renumber your window refnums so there are no gaps. |
| [save](../scripts/save.md) | Save your settings to a file you can [load](../command/load.md) later. |
| [scan](../scripts/scan.md) | Summarize the current channel. |
| [screen](../scripts/screen.md) | Switch between windows like gnu screen does. |
| [slowcat](../scripts/slowcat.md) | Dump a file to current target, very slowly. |
| [snip](../scripts/snip.md) | Remove substrings from the start or end of a string. |
| [sping](../scripts/sping.md) | Ping a server. |
| [suppressmotd](../scripts/suppressmotd.md) | Don't be bothered with the server's motd. |
| `tabkey.ce` | Crazyeddy's and Fudd's tabkey script. |
| [tabkey.jm](../scripts/tabkey.jm.md) | Jm's tabkey script. |
| [utime](../scripts/utime.md) | Functions for manipulating [utime](../scripts/utime.md)s. |


## Special Topics

| Reference | Description |
| --- | --- |
| [about_epic](about_epic.md) | Information about the EPIC project and software. |
| [arglist](arglist.md) | How alias argument lists look and work. |
| [arrays](arrays.md) | How Karll arrays work. |
| [atomic_scope](atomic_scope.md) | Atomic scope and local variables. |
| [block](block.md) | The basis of ircII syntax is the block. |
| [command_line](command_line.md) | What options can I pass at the command line? |
| [commands_overview](commands_overview.md) | What are all the commands? |
| [compile_opts](compile_opts.md) | How can I tell what options were set at compiled time? |
| [copyright](copyright.md) | What is the copyright and license for the client? |
| [debugging](debugging.md) | How do I debug my script? |
| [default_keybindings](default_keybindings.md) | Information about what [BIND](../command/bind.md) -DEFAULT does |
| [disambiguation](disambiguation.md) | A template file we use for disambiguation pages. |
| [environment_variables](environment_variables.md) | What environment variables does EPIC honor? |
| [etiquette](etiquette.md) | How should I behave on irc? |
| [expando_substitution](expando_substitution.md) | How do $'s get expanded? |
| [expandos](expandos.md) | Even more about how $'s get expanded. |
| [expressions](expressions.md) | How math expressions work. |
| [functions_overview](functions_overview.md) | What are the built in functions? |
| [glossary](glossary.md) | This is a work in progress. |
| [graphics_chars](graphics_chars.md) | How to use alternate character set to echo box chars |
| [input_handling](input_handling.md) | How the client handles your keypresses. |
| [introduction](introduction.md) | A crash course on using irc. |
| [ipv6](ipv6.md) | Things you need to know about using ipv6. |
| [ircii_syntax](ircii_syntax.md) | How the ircII language works. |
| [ircuser](ircuser.md) | Why can't I just set my username to anything I want? |
| [karll_arrays](karll_arrays.md) | What karll arrays are and how they work. |
| [key_bindings](key_bindings.md) | How you can represent keybindings. |
| [levels](levels.md) | All about window/lastlog/ignore/flood levels. |
| [lval](lval.md) | About lvalues, things you can assign values to (variable names) |
| [mangle_types](mangle_types.md) | All about removing highlights in strings. |
| [math_operators](math_operators.md) | All operators and their priority and associativity |
| [memory_usage](memory_usage.md) | What causes high memory usage and what you can do about it. |
| [new_user](new_user.md) | A crash course to the absolute beginner to irc. |
| [output-help](output-help.md) | How the client sends output to your emulator. |
| [pass-through_command](pass-through_command.md) | Commands that are set to the server directly. |
| [patterns](patterns.md) | How wildcard pattern matching works. |
| [pf_loader](pf_loader.md) | All about using the pf (pre-formatted) loader. |
| [programming](programming.md) | A crash course in ircII programming. |
| [quoting_hell](quoting_hell.md) | What is quoting hell and how do I make it work for me? |
| [random_numbers](random_numbers.md) | How the client generates random numbers. |
| [regex](regex.md) | How regular expressions work in EPIC. |
| [referring_to_servers](referring_to_servers.md) | How am I allowed to refer to servers? |
| [removed_in_epic5](removed_in_epic5.md) | Historical EPIC4-to-EPIC5 compatibility lists. |
| [removed_in_epic6](removed_in_epic6.md) | Removed interfaces and scripts with retired dependencies. |
| [rules_about_number_arguments](rules_about_number_arguments.md) | How numbers passed to built-in functions are handled. |
| [security](security.md) | Thinking about security in your script. |
| [serial_numbers](serial_numbers.md) | How serial numbers work for on hooks. |
| [server_description](server_description.md) | What constitutes a server description? |
| [server_list](server_list.md) | How to build your own server list file. |
| [server_numerics](server_numerics.md) | How the client handles server numerics. |
| [server_state](server_state.md) | All about the various server status states. |
| [signals](signals.md) | Signals that the client handles and what they do. |
| [space_character](space_character.md) | What constitutes a space character? |
| [special_vars](special_vars.md) | Info about $ expandos, and a list of the inline expandos. |
| [standard_loader](standard_loader.md) | All about using the std (standard) loader. |
| [start](help_root.md) | This comprehensive index. |
| [status_line](status_line.md) | All you need to know about the status bar. |
| [text_hilight](text_hilight.md) | Bold, and Underline, and Color, and Reverse, oh my! |
| [using_symbolctl](using_symbolctl.md) | Create your own sets, command completion, other neat stuff |
| [welcome](welcome.md) | Welcome to EPIC! |
| [what_is_a_word](what_is_a_word.md) | When something is a "word", what does that mean? |
| [window_activity_handling](window_activity_handling.md) | How hidden windows decide when to tell you they have output. |
| [window_targets](window_targets.md) | What is a "target" and how do windows use them? |


## Disambiguation

| Reference | Description |
| --- | --- |
| [alias](../disambiguation/alias.md) | Alias definitions and symbol-table operations. |
| [away](../disambiguation/away.md) | Away messages and stored away-state values. |
| [channel](../disambiguation/channel.md) | Channel commands, membership queries, and window associations. |
| [connect](../disambiguation/connect.md) | IRC server-link requests and the former direct-socket function. |
| [exec](../disambiguation/exec.md) | Launching external programs and accessing their streams. |
| [fe](../disambiguation/fe.md) | Iteration and rewriting of word lists. |
| [info](../disambiguation/info.md) | IRC server information requests and local client build information. |
| [lastlog](../disambiguation/lastlog.md) | Recalling stored output and querying its records. |
| [list](../disambiguation/list.md) | IRC channel listings. |
| [local](../disambiguation/local.md) | Local variable declarations and scope. |
| [log](../disambiguation/log.md) | Selective logging, logarithms, and other logging controls. |
| [map](../disambiguation/map.md) | Server mapping through the server command or a client-side script. |
| [motd](../disambiguation/motd.md) | IRC server MOTD requests and the local file-display script. |
| [notify](../disambiguation/notify.md) | Script-provided nickname monitoring through the server’s MONITOR facility. |
| [pipe](../disambiguation/pipe.md) | Script-provided function for collecting an external command’s output. |
| [pop](../disambiguation/pop.md) | Remove the last word from a variable. |
| [prefix](../disambiguation/prefix.md) | Find a common word prefix or complete partial input. |
| [push](../disambiguation/push.md) | Append data to a variable. |
| [reconnect](../disambiguation/reconnect.md) | Retry a server connection or configure script-based reconnection. |
| [repeat](../disambiguation/repeat.md) | Repeat commands or construct repeated text. |
| [shift](../disambiguation/shift.md) | Remove the first word from a variable. |
| [stat](../disambiguation/stat.md) | Query local filesystem metadata. |
| [time](../disambiguation/time.md) | Server time requests and local timestamp values. |
| [unshift](../disambiguation/unshift.md) | Prepend data to a variable. |
| [userhost](../disambiguation/userhost.md) | Request userhosts from the server or read cached userhost values. |
| [utime](../disambiguation/utime.md) | Microsecond timestamp values and script helpers. |
| [version](../disambiguation/version.md) | Server-version requests and system-version information. |
| [which](../disambiguation/which.md) | Display a script file or locate a file in a search path. |
| [window](../disambiguation/window.md) | Window commands, events, and programmatic controls. |
| [xdebug](../disambiguation/xdebug.md) | Inspect or change debugging and parser flags. |


## Source references

- [source/commands.c](../../source/commands.c): `irc_command` registration.
- [source/functions.c](../../source/functions.c): `built_in_functions` registration and disabled raw-connection stubs.
- [source/vars.c](../../source/vars.c): `init_variables_stage1()` registration, rather than retained identifiers alone.
- [source/hook.c](../../source/hook.c): `hook_function_templates`.
- [source/keys.c](../../source/keys.c): `init_binds()` and the special NOTHING selector.
- [source/window.c](../../source/window.c): `windowcmd_options`.
- [script](../../script): retained files and explicit alias/addset definitions; generated definitions and dependencies require the individual script reference.
- [KNOWNBUGS](../../KNOWNBUGS) and [UPDATES](../../UPDATES): retired facilities and interface changes.
