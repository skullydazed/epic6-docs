# Removed in EPIC5

These historical EPIC4-to-EPIC5 compatibility lists were moved from the [root help index](help_root.md). They include obsolete names, script-provided replacements, and names without a separate help page. Follow the linked references for current availability and replacement behavior.

For later removals, see [removed in EPIC6](removed_in_epic6.md).

## Historical EPIC4-to-EPIC5 compatibility lists

### Help files exist for non-existent scripts

| Reference | Description |
| --- | --- |
| [alias_script](../disambiguation/alias.md) | Alias definitions and symbol-table operations. |
| `altchan.bj` | — |
| `autokick` | — |
| `autoop` | — |
| [away_script](../disambiguation/away.md) | Away messages and stored away-state values. |
| `basical` | — |
| `columns` | — |
| `dcc_spacefix` | — |
| `deban` | — |
| `dns` | — |
| `efnext` | — |
| `events.hop` | — |
| `events` | — |
| `fake-dcc` | — |
| [fe_script](../disambiguation/fe.md) | Iteration and rewriting of word lists. |
| `genalias` | — |
| `hybrid6` | — |
| `imap` | — |
| `ip-to-int` | — |
| `keybinds` | — |
| `killpath` | — |
| `kpstat` | — |
| `langtrans` | — |
| [list_script](../disambiguation/list.md) | IRC channel listings. |
| [local_script](../disambiguation/local.md) | Local variable declarations and scope. |
| `mkpdir` | — |
| `more` | — |
| `mudirc` | — |
| `netsplit.env` | — |
| `newformat` | — |
| `old-dcc` | — |
| [prefix_script](../disambiguation/prefix.md) | Find a common word prefix or complete partial input. |
| `recursion` | — |
| [repeat_script](../disambiguation/repeat.md) | Repeat commands or construct repeated text. |
| `scandir` | — |
| `sdiff` | — |
| `silent` | — |
| `sound` | — |
| `starutils` | — |
| [stat_script](../disambiguation/stat.md) | Query local filesystem metadata. |
| `status_lag` | — |
| `tabkey.th` | — |
| [time_script](../disambiguation/time.md) | Server time requests and local timestamp values. |
| `tls` | — |
| `vi-binds` | — |
| `webster` | — |
| `window_script` | — |


### Help files exist for non-existent commands

| Reference | Description |
| --- | --- |
| `bind_command_completion` | Command completion supplied by tabkey scripts. |
| `bind_backward_history` | Implemented by [history script](../scripts/history.md). |
| `bind_forward_history` | Implemented by [history script](../scripts/history.md). |
| `bind_shove_to_history` | Implemented by [history script](../scripts/history.md). |
| `bye` | Use [quit](../command/quit.md) instead. |
| `set_alt_charset` | Use [set mangle_display](../set/mangle_display.md) instead. |
| `set_auto_new_nick` | Use the [newnick](../scripts/newnick.md) script instead. |
| `set_auto_reconnect` | Implemented by [reconnect script](../scripts/reconnect.md). |
| `set_auto_reconnect_delay` | Implemented by [reconnect script](../scripts/reconnect.md). |
| `set_auto_rejoin` | Implemented by [builtins](../scripts/builtins.md). |
| `set_auto_rejoin_connect` | Unsupported legacy setting; see the [reconnect script](../scripts/reconnect.md) for reconnection behavior. |
| `set_auto_rejoin_delay` | Implemented by [builtins](../scripts/builtins.md). |
| `set_auto_unmark_away` | Implemented by [builtins](../scripts/builtins.md). |
| `set_auto_whowas` | Implemented by [builtins](../scripts/builtins.md). |
| `set_bad_style` | This was never implemented. |
| `set_beep_max` | Unsupported legacy bell-count setting. |
| `set_beep_on_msg` | The [builtins](../scripts/builtins.md) script implements this. |
| `set_beep_when_away` | Unavailable legacy setting; the supplied builtins script does not define it. |
| `set_blink_video` | Use [set mangle_display](../set/mangle_display.md) instead. |
| `set_bold_video` | Use [set mangle_display](../set/mangle_display.md) instead. |
| `set_color` | Use [set mangle_display](../set/mangle_display.md) instead. |
| `set_command_mode` | Implemented by [builtins](../scripts/builtins.md). |
| `set_connect_timeout` | Obsoleted by nonblocking connects. |
| `set_dcc_timeout` | Script-defined timeout for removed DCC facilities; see [builtins](../scripts/builtins.md). |
| `set_display_ansi` | Use [set mangle_display](../set/mangle_display.md) instead. |
| `set_display_pc_characters` | The client no longer supports non-8-bit terminals. |
| `set_eight_bit_characters` | The client no longer supports non-8-bit terminals. |
| `set_full_status_line` | Implemented by [builtins](../scripts/builtins.md). |
| `set_help_pager` | Legacy setting for the retired [help](../disambiguation/scripts_help.md) browser. |
| `set_help_path` | Legacy setting for the retired [help](../disambiguation/scripts_help.md) browser. |
| `set_help_prompt` | Legacy setting for the retired [help](../disambiguation/scripts_help.md) browser. |
| `set_help_window` | Legacy setting for the retired [help](../disambiguation/scripts_help.md) browser. |
| `set_highlight_char` | Use [set mangle_display](../set/mangle_display.md) instead. |
| [set_history](../scripts/history.md) | Script-provided command history and navigation. |
| `set_history_circleq` | Implemented by the [history](../scripts/history.md) script. |
| `set_input_aliases` | An obsolete setting. |
| `set_inverse_video` | Use [set mangle_display](../set/mangle_display.md) instead. |
| `set_max_reconnects` | An obsolete setting. |
| `set_meta_states` | An obsolete setting. |
| `set_nd_space_max` | Unsupported legacy setting. |
| `set_notify_handler` | An obsolete setting. |
| `set_random_local_ports` | An obsolete setting. |
| `set_reverse_status_line` | Unavailable legacy setting; the supplied [builtins](../scripts/builtins.md) script does not define it. |
| [set_scroll](../window/scroll.md) | An obsolete setting. |
| [set_security](security.md) | An obsolete setting. |
| `set_ssl_certfile` | This was never implemented. |
| `set_ssl_keyfile` | This was never implemented. |
| `set_ssl_path` | This was never implemented. |
| `set_status_truncate_rhs` | Unsupported legacy status-line truncation setting. |
| `set_suppress_server_motd` | Implemented by the [suppressmotd](../scripts/suppressmotd.md) script. |
| `set_switch_channel_on_part` | Channel stacking makes this a moot feature. |
| `set_tab` | Unsupported legacy setting. |
| `set_tab_max` | Unsupported legacy setting. |
| `set_underline_video` | Use [set mangle_display](../set/mangle_display.md) instead. |
| [window_bind](../command/bind.md) | Auto-rejoin feature no longer built-in |
| `window_unbind` | Auto-rejoin feature no longer built-in |
| [window_scratch](../window/scratch.md) | An obsolete operation.  All windows are scratch windows. |
| [window_scroll](../window/scroll.md) | An obsolete operation.  All windows are scrollable. |


### Help files exist for non-existent functions

| Reference | Description |
| --- | --- |
| `fabs` | Use [abs](../function/abs.md) instead. |
| `getppid` | Historical name; use [pid](../function/pid.md) for the client’s process ID or `ppid()` for its parent. |
| `igmask` | Compatibility helper for the removed [ignorectl](../disambiguation/ignorectl.md) interface; does not restore ignore support. |
| `igtype` | Compatibility helper for the removed [ignorectl](../disambiguation/ignorectl.md) interface; does not restore ignore support. |
| `lastserver` | Use [serverctl](../function/serverctl.md) instead. |
| `rigmask` | Compatibility helper for the removed [ignorectl](../disambiguation/ignorectl.md) interface; does not restore ignore support. |
| `rigtype` | Compatibility helper for the removed [ignorectl](../disambiguation/ignorectl.md) interface; does not restore ignore support. |
| `servergroup` | Use [serverctl](../function/serverctl.md) instead. |
| `servername` | Use [serverctl](../function/serverctl.md) instead. |
| `servernick` | Use [serverctl](../function/serverctl.md) instead. |
| `servernum` | Use [serverctl](../function/serverctl.md) instead. |
| `serverourname` | Use [serverctl](../function/serverctl.md) instead. |
| `servertype` | Use [serverctl](../function/serverctl.md) to inspect the connection type. |
| `winbound` | Auto-rejoin feature no longer built-in |
| `wincursorline` | Use [windowctl](../function/windowctl.md) instead. |
| `winlevel` | Use [windowctl](../function/windowctl.md) instead. |
| `winline` | Use [windowctl](../function/windowctl.md) instead. |
| `winnam` | Use [windowctl](../function/windowctl.md) instead. |
| `winnicklist` | Use [windowctl](../function/windowctl.md) instead. |
| `winnum` | Use [windowctl](../function/windowctl.md) instead. |
| `winquery` | Use [windowctl](../function/windowctl.md) instead. |
| `winrefs` | Use [windowctl](../function/windowctl.md) instead. |
| `winscreen` | Use [windowctl](../function/windowctl.md) instead. |
| `winscrollbacksize` | Use [windowctl](../function/windowctl.md) instead. |
| `winserv` | Use [windowctl](../function/windowctl.md) instead. |
| `winsize` | Use [windowctl](../function/windowctl.md) instead. |
| `winstatsize` | Use [windowctl](../function/windowctl.md) instead. |
| `winvisible` | Use [windowctl](../function/windowctl.md) instead. |
