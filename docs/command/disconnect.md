# disconnect command

## Synopsis

```text
/disconnect [-force|-safe] [<server> [<reason>]]
```

## Description

`disconnect` closes the selected IRC connection without quitting EPIC. With no server argument, it uses the server associated with the current window. Other server connections are left alone. It normally reports `Disconnecting from server ...` and refreshes the status display.

For a registered connection, EPIC sends a QUIT message with the supplied reason, defaulting to `Disconnecting`, before closing the connection. The server controls how that departure is reported to others. The command does not wait for acknowledgement.

Joined channels and their window affiliations on that server are removed, along with pending channel assignments. The server record itself remains, so this is not deletion from the server list. Stored configuration and the requested away message are not removed by this close operation.

## Arguments

`<server>` selects an existing server entry by refnum, name, or server description. See [server descriptions](../special/server_description.md) for lookup syntax. An unknown entry reports `No such server!` and leaves connections unchanged. All text after the server argument is the quit reason; supply the server argument when specifying a reason.

The optional `-force` and `-safe` flags precede the server argument, are case-insensitive, and accept `-f` and `-s` respectively. The last flag wins; the default is `-force`. The safe-mode check applies only to [reconnect](reconnect.md), so `-safe` does not prevent disconnecting an active session.

The command is available in every build. If there is no valid current-window server and another connection exists, it reports an unknown-server error. When the client has no connections, a `disconnect` hook can handle or suppress the normal not-connected message. See [`on`](on.md).

## Technical

Closing an open connection passes through `closing` to `closed`. `disconnect` does not request a new connection or attempt another DNS address afterward. [`reconnect`](reconnect.md) uses the same shared connection-reset helper but performs an additional connection attempt; it is the command intended to try another available address while connecting.

If the server record has no open descriptor, the close helper still clears channel state and sets `closing`, but returns before setting `closed`. Thus the exact final state differs for an already closed or unfinished connection.

## Example

To disconnect from the server of your current window:

```text
/disconnect
```

To disconnect server refnum 2 with a custom quit reason:

```text
/disconnect 2 I'll be back later!
```

See [`window`](window.md) and [`server`](server.md) for window/server selection.

## History

The `disconnect` command first appeared in “plus 3” (post-ircII, pre-EPIC).

## Source

See [source/server.c](../../source/server.c) for `disconnectcmd()`, the shared `user_reset_connection()` helper, argument parsing, `server_close()`, and `server_close_internal()`. [source/commands.c](../../source/commands.c) registers the command; [source/window.c](../../source/window.c) supplies the current window's server and pending-channel cleanup.
