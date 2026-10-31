# Removed in EPIC6

This historical index collects entries moved from the [root help index](help_root.md) for interfaces removed from EPIC6, retained compatibility placeholders, and scripts whose dependencies have been retired. These entries do not supply working versions of the former facilities; follow each reference for current availability and any replacements.

The unavailable `allocdump` and Tcl entries are also retained here. Their reference pages do not establish a retirement date, so their inclusion does not identify them as EPIC6 removals.

For earlier changes, see the [EPIC4-to-EPIC5 compatibility lists](removed_in_epic5.md).

DCC commands, DCC transports/events/settings, external message encryption, CPU saver, Perl, Ruby, and incoming flood detection have been removed. Entries describing them are historical. Current TLS server connections are a separate facility.


## Former common commands

| Reference | Description |
| --- | --- |
| [dcc](../disambiguation/dcc.md) | Removed direct-client-connection interface for communication outside IRC. |
| [dcc get](../disambiguation/ctcp_get.md) | Removed DCC command for accepting an offered file. |
| [dcc resume](../disambiguation/ctcp_resume.md) | Removed DCC command for resuming a partial download. |
| [dcc send](../disambiguation/ctcp_send.md) | Removed DCC command for offering a file to another client. |
| [encrypt](../disambiguation/encrypt.md) | Removed conversation-encryption interface. |
| [ignore](../disambiguation/ignore.md) | Unfinished script replacement for the removed ignore command; suppression is not dependable. |


## Other former IRC commands

| Reference | Description |
| --- | --- |
| [dcc chat](../disambiguation/ctcp_chat.md) | Removed DCC command for direct client-to-client chat. |
| [dcc close](../disambiguation/ctcp_close.md) | Removed DCC command for closing one connection. |
| [dcc closeall](../disambiguation/ctcp_closeall.md) | Removed DCC command for closing all connections. |
| [dcc list](../disambiguation/ctcp_list.md) | Removed DCC command for listing connections and transfers. |
| [dcc raw](../disambiguation/ctcp_raw.md) | Removed DCC command for writing to a raw socket connection. |
| [dcc rename](../disambiguation/ctcp_rename.md) | Removed DCC command for changing a connection’s associated nickname. |
| [flush](../disambiguation/flush.md) | Removed command for suppressing incoming server output during a flood. |
| [mesg](../disambiguation/mesg.md) | Removed command for changing terminal write permissions. |
| [redirect](../disambiguation/redirect.md) | Removed command for sending client output back over IRC. |


## Commands

| Reference | Description |
| --- | --- |
| [allocdump](../disambiguation/allocdump.md) | Unavailable allocation-debugging command. |
| [bind_cpu_saver](../disambiguation/bind_cpu_saver.md) | Removed binding for reducing housekeeping while idle. |
| [bind_quit_irc](../disambiguation/bind_quit_irc.md) | Removed binding for prompting before [exit](../command/exit.md). |
| [bind_stop_irc](../disambiguation/bind_stop_irc.md) | Removed binding for suspending the client with SIGTSTP. |
| [bind_transpose_characters](../disambiguation/bind_transpose_characters.md) | Removed binding for swapping adjacent input characters. |
| [botmode](../disambiguation/botmode.md) | Removed command for detaching a running client; use startup option `-b` instead. |
| [on_dcc_activity](../disambiguation/on_dcc_activity.md) | Removed event for DCC traffic. |
| [on_dcc_chat](../disambiguation/on_dcc_chat.md) | Removed event for incoming DCC chat messages. |
| [on_dcc_connect](../disambiguation/on_dcc_connect.md) | Removed event for DCC connection establishment. |
| [on_dcc_list](../disambiguation/on_dcc_list.md) | Removed event for [dcc list](../disambiguation/ctcp_list.md) entries. |
| [on_dcc_lost](../disambiguation/on_dcc_lost.md) | Removed event for DCC connection closure. |
| [on_dcc_offer](../disambiguation/on_dcc_offer.md) | Removed event for outgoing DCC offers. |
| [on_dcc_raw](../disambiguation/on_dcc_raw.md) | Removed event for raw DCC socket traffic. |
| [on_dcc_request](../disambiguation/on_dcc_request.md) | Removed event for incoming DCC offers. |
| [on_encrypted_notice](../disambiguation/on_encrypted_notice.md) | Removed event for incoming [encrypted](../disambiguation/encrypt.md) notices. |
| [on_encrypted_privmsg](../disambiguation/on_encrypted_privmsg.md) | Removed event for incoming [encrypted](../disambiguation/encrypt.md) messages. |
| [on_flood](../disambiguation/on_flood.md) | Removed event for incoming flood detection. |
| `on_help` | Removed help-browser event. |
| [on_mail](../disambiguation/on_mail.md) | Removed event for built-in mailbox notifications. |
| [on_note](../disambiguation/on_note.md) | Removed event for incoming offline notes. |
| [on_notify_signoff](../disambiguation/on_notify_signoff.md) | Removed event for built-in notify offline notifications. |
| [on_notify_signon](../disambiguation/on_notify_signon.md) | Removed event for built-in notify online notifications. |
| [on_redirect](../disambiguation/on_redirect.md) | Removed event for redirected outgoing IRC output. |
| [on_send_dcc_chat](../disambiguation/on_send_dcc_chat.md) | Removed event for outgoing [dcc chat](../disambiguation/ctcp_chat.md) messages. |
| [on_wall](../disambiguation/on_wall.md) | Removed event for incoming wall messages. |
| [perl](../disambiguation/perl.md) | Removed embedded Perl integration. |
| [ruby](../disambiguation/ruby.md) | Removed embedded Ruby integration. |
| [set_allow_c1_chars](../disambiguation/set_allow_c1_chars.md) | Removed C1 control-character filter setting. |
| [set_cpu_saver_after](../disambiguation/set_cpu_saver_after.md) | Removed idle threshold for CPU saver. |
| [set_cpu_saver_every](../disambiguation/set_cpu_saver_every.md) | Removed housekeeping interval for CPU saver. |
| [set_dcc_auto_send_rejects](../disambiguation/set_dcc_auto_send_rejects.md) | Removed setting for sending DCC rejection replies. |
| [set_dcc_dequote_filenames](../disambiguation/set_dcc_dequote_filenames.md) | Removed setting for decoding offered DCC filenames. |
| [set_dcc_long_pathnames](../disambiguation/set_dcc_long_pathnames.md) | Removed filename-display setting for [dcc list](../disambiguation/ctcp_list.md). |
| [set_dcc_sliding_window](../disambiguation/set_dcc_sliding_window.md) | Removed throughput setting for [dcc sends](../disambiguation/ctcp_send.md). |
| [set_dcc_store_path](../disambiguation/set_dcc_store_path.md) | Removed default directory setting for incoming DCC files. |
| [set_dcc_use_gateway_addr](../disambiguation/set_dcc_use_gateway_addr.md) | Removed gateway-address setting for DCC. |
| [set_do_notify_immediately](../disambiguation/set_do_notify_immediately.md) | Removed immediate [ison](../command/ison.md) polling control for the built-in notify list. |
| [set_flood_after](../disambiguation/set_flood_after.md) | Removed incoming flood-detection sample threshold. |
| [set_flood_ignore](../disambiguation/set_flood_ignore.md) | Removed automatic suppression setting for incoming floods. |
| [set_flood_maskuser](../disambiguation/set_flood_maskuser.md) | Removed sender-grouping setting for incoming flood detection. |
| [set_flood_rate](../disambiguation/set_flood_rate.md) | Removed incoming flood-rate numerator. |
| [set_flood_rate_per](../disambiguation/set_flood_rate_per.md) | Removed incoming flood-rate denominator. |
| [set_flood_users](../disambiguation/set_flood_users.md) | Removed limit on tracked incoming flood senders. |
| [set_flood_warning](../disambiguation/set_flood_warning.md) | Removed incoming flood-warning setting. |
| [set_high_bit_escape](../disambiguation/set_high_bit_escape.md) | Removed high-bit input-to-escape conversion setting. |
| [set_mail_type](../disambiguation/set_mail_type.md) | Removed built-in mailbox-format selector. |
| [set_mirc_broken_dcc_resume](../disambiguation/set_mirc_broken_dcc_resume.md) | Removed compatibility setting for [dcc resume](../disambiguation/ctcp_resume.md). |
| [set_no_ctcp_flood](../disambiguation/set_no_ctcp_flood.md) | Removed setting for throttling automatic CTCP replies. |
| [set_notify](../disambiguation/set_notify.md) | Removed built-in nickname-polling enable setting. |
| [set_notify_interval](../disambiguation/set_notify_interval.md) | Removed polling interval for the built-in [notify](../disambiguation/notify.md) list. |
| [set_notify_userhost_automatic](../disambiguation/set_notify_userhost_automatic.md) | Removed automatic userhost-lookup setting for built-in notify. |
| [set_old_math_parser](../disambiguation/set_old_math_parser.md) | Removed selector for the legacy math parser. |
| [set_random_source](../disambiguation/set_random_source.md) | Removed random-number-generator selector. |
| [set_realname](../disambiguation/set_realname.md) | Removed realname setting; see the linked page for the current interface. |
| [set_status_cpu_saver](../disambiguation/set_status_cpu_saver.md) | Removed CPU-saver status-line format. |
| [set_suppress_from_remote_server](../disambiguation/set_suppress_from_remote_server.md) | Removed setting for appending a remote-server suffix to numeric replies. |
| [set_translation](../disambiguation/set_translation.md) | Removed byte-translation-table selector. |
| [set_translation_path](../disambiguation/set_translation_path.md) | Removed translation-table search path. |
| [tcl](../disambiguation/tcl.md) | Unavailable embedded Tcl integration. |
| [window prompt](../disambiguation/window_prompt.md) | Removed per-window input prompt for [query](../command/query.md) conversations with [exec](../command/exec.md) processes. |


## Functions

| Reference | Description |
| --- | --- |
| [connect](../function/connect.md) | Compatibility placeholder for [dcc raw](../disambiguation/ctcp_raw.md) connections; returns empty without opening a socket. |
| [crypt](../disambiguation/crypt.md) | Removed Unix `crypt(3)` password-hashing function. |
| [dccctl](../disambiguation/dccctl.md) | Removed function for inspecting and changing DCC connections. |
| [encryptparm](../disambiguation/encryptparm.md) | Removed function for inspecting [crypt](../disambiguation/crypt.md) sessions. |
| [floodinfo](../disambiguation/floodinfo.md) | Removed function for querying incoming flood-tracking records. |
| [globi](../disambiguation/globi.md) | Removed case-insensitive filename-pattern function. |
| [ignorectl](../disambiguation/ignorectl.md) | Removed function for inspecting and changing [ignore](../disambiguation/ignore.md) rules. |
| [listen](../function/listen.md) | Compatibility placeholder; returns empty without opening a listening socket. |
| [notify](../disambiguation/notify.md) | Script-provided `notify()` currently returns empty without querying or changing the watch list. |
| [perl](../disambiguation/perl.md) | Removed embedded Perl integration. |
| [perlcall](../disambiguation/perlcall.md) | Removed function for simple embedded Perl subroutine calls. |
| [perlxcall](../disambiguation/perlxcall.md) | Removed function for embedded Perl calls exchanging array data. |
| [ruby](../disambiguation/ruby.md) | Removed embedded Ruby integration. |
| [sedcrypt](../disambiguation/sedcrypt.md) | Removed function for transforming strings through peer encryption. |
| [srand](../function/srand.md) | Compatibility placeholder for random-number seeding; returns empty without affecting the generator. |
| [tcl](../disambiguation/tcl.md) | Unavailable embedded Tcl integration. |
| [uhc](../disambiguation/uhc.md) | Removed function for completing partial nickname/user/host masks. |


## Scripts

| Reference | Description |
| --- | --- |
| [autoget](../disambiguation/scripts_autoget.md) | Historical automatic [dcc get](../disambiguation/ctcp_get.md) rules; requires removed DCC facilities. |
| [dcc_ports](../disambiguation/scripts_dcc_ports.md) | Historical port-range helper for removed [DCC](../disambiguation/dcc.md) connections. |
| [epic-crypt-gpg](../disambiguation/scripts_epic-crypt-gpg.md) | Removed helper for the former [crypt](../disambiguation/crypt.md) external-encryption interface. |
| [epic-crypt-gpg-aa](../disambiguation/scripts_epic-crypt-gpg-aa.md) | Removed ASCII-armored helper for the former [crypt](../disambiguation/crypt.md) external-encryption interface. |
| [help](../disambiguation/scripts_help.md) | Retired in-client help browser; its connection dependency is unavailable in EPIC6. |
| [man](../disambiguation/scripts_man.md) | Front end to the retired help command; does not provide a working EPIC6 browser. |
| [revdcc](../disambiguation/scripts_revdcc.md) | Historical reverse-DCC helper; requires removed DCC facilities. |
| [setmail](../disambiguation/scripts_setmail.md) | Historical mail-format helper; does not configure the current Boolean mailbox checker. |


## Special Topics

| Reference | Description |
| --- | --- |
| [flood_control](../disambiguation/special_flood_control.md) | Historical incoming flood-protection facility, removed from EPIC6. |
| [using_perl](../disambiguation/special_using_perl.md) | Historical embedded Perl interface, removed from EPIC6. |


## Disambiguation

| Reference | Description |
| --- | --- |
| [perl](../disambiguation/perl.md) | Removed embedded Perl integration. |
| [ruby](../disambiguation/ruby.md) | Removed embedded Ruby integration. |
| [tcl](../disambiguation/tcl.md) | Unavailable embedded Tcl integration. |


## Source references

- `source/commands.c`: `irc_command` registration.
- `source/functions.c`: `built_in_functions` registration and disabled raw-connection stubs.
- `source/vars.c`: `init_variables_stage1()` registration, rather than retained identifiers alone.
- `source/hook.c`: `hook_function_templates`.
- `source/keys.c`: `init_binds()` and the special NOTHING selector.
- `source/window.c`: `windowcmd_options`.
- `script`: retained files and explicit alias/addset definitions; generated definitions and dependencies require the individual script reference.
- [KNOWNBUGS](../KNOWNBUGS.md) and [UPDATES](../UPDATES.md): retired facilities and interface changes.
