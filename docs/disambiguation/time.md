# Time

Do you mean:

- The [time command](../command/time.md), `/time [server-or-nickname]`, which requests an IRC server's local time? Target forms, permissions, timezone text, and reply formatting depend on the server.
- The [time function](../function/time.md), `$time()`, which returns the client host's current Unix timestamp in whole seconds? It queries the local system clock and ignores arguments.

The command replies asynchronously and does not return the function's timestamp or change the local clock. `/time nickname` is also different from a [CTCP](../command/ctcp.md) TIME request to another client.

For formatting a local timestamp, see [stime](../function/stime.md) and [strftime](../function/strftime.md). For subsecond timestamps, see [utime](../function/utime.md). Local wall-clock readings can jump when the system clock is adjusted; they are not a monotonic elapsed-time clock.

## Source references

- `source/commands.c`: `time` uses the generic protocol sender.
- `source/functions.c`: `time()` calls the system clock and returns epoch seconds.
