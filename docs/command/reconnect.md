# reconnect

Close the selected server connection and start another connection attempt.

## Synopsis

```text
/reconnect [-force|-safe] [<server> [<reason>]]
```

## Description

`reconnect` manages a server's connection state while keeping EPIC running. It uses the selected server, defaulting to the server associated with the current window, closes its connection, then tries the next address from any remaining cached DNS results. If that attempt cannot start, it sets the server to the reconnect state; a window associated with that server then initiates a fresh DNS lookup and connection sequence.

The command works on an already connected server as well as an unfinished or closed connection. `-safe` refuses to reconnect a registered session; `-force`, the default, allows it. It normally prints disconnection and reconnection notices. A registered open connection receives an attempted IRC quit message with the supplied reason, defaulting to `Reconnecting`, before it closes; the server determines how the departure is reported. A successful nonblocking connection start does not guarantee eventual connection or registration.

Closing clears tracked channels, their window affiliations, pending channel assignments, and confirmed/pending nickname state. The server record, configured connection information, and window/server association remain. This built-in does not preserve and rejoin your former channels itself.

## Arguments

`<server>` selects an existing server entry by refnum, name, or server description. An unknown entry reports `No such server!` and leaves connections unchanged. All text after the server argument is the quit reason; supply the server argument when specifying a reason. See [server descriptions](../special/server_description.md).

Flags precede the server argument and are case-insensitive. `-force` and `-safe` accept `-f` and `-s` respectively; the last flag wins. With `-safe`, an already registered server produces a diagnostic asking you to disconnect first, and no connection reset occurs. An unfinished or closed connection can still be retried.

If the current window has no valid server while another connection exists, the command reports an unknown-server error. With no connections and no valid selected server, the `disconnect` [on](on.md) hook can suppress the normal not-connected message. The command is always registered, returns no value, and does not wait for reconnection to finish.

## Related behavior and example

[disconnect](disconnect.md) uses the same close operation but does not request another connection attempt. The bundled [reconnect script](../scripts/reconnect.md) implements separate automatic reconnection and channel-rejoining policy after connection losses; loading or configuring that script is separate from running this built-in.

To restart the connection belonging to your current window:

```text
/reconnect
```

To retry an unfinished connection for server refnum 2 while refusing to reset an active registered session:

```text
/reconnect -safe 2
```

## History and source

`reconnect` first appeared in `plus-3`, after ircII and before EPIC.

Registration is in `source/commands.c`. `reconnectcmd`, the shared `user_reset_connection` parser, closing, cached-address attempts, and DNS bootstrapping are in `source/server.c`. Window/server association and reconnect-state processing are in `source/window.c`.
