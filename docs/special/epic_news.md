# EPIC news archive

This page covers EPIC6 development news and historical EPIC4/EPIC5 announcements. The dated EPIC6 entries summarize [UPDATES](../UPDATES.md) and upstream commit history; links to individual references explain current behavior and requirements.

## EPIC6

### 2026-10-30: Authentication checks and scripting fixes

Upstream commit `70a655b6` (internal commit ID 3106) includes static-analysis fixes and these interface changes:

- The supplied `sasl` script checks TLS certificate verification before sending PLAIN credentials and accepts an optional certificate-hash exception. See [SSL connections](about_ssl_connections.md#sasl-plain-authentication).
- [Compiled-regex consumers](regex.md) validate Base85 decoding and decoded structure size. Capture extraction and cleanup accept current compiled strings.
- [`ctcpctl()`](../function/ctcpctl.md) returns empty for unknown getter names and supports `GET ... REPLACE_ARGS`. [`ecdsatool()`](../function/ecdsatool.md) operation names are case-insensitive.
- [`disconnect`](../command/disconnect.md) and [`reconnect`](../command/reconnect.md) correctly parse server selectors, quit reasons, and `-force`/`-safe`; reconnect safe mode refuses to reset a registered session.
- [`msg`](../command/msg.md) and [`notice`](../command/notice.md) split long text at approximately 440 encoded bytes. [`window topline`](../window/topline.md) stores slots 1 through 99, while display and `windowctl` access remain limited to nine.
- [Installation](installing.md) carries configured `CPPFLAGS` into compilation. The supplied scripts fix delayed argument expansion and Python startup code.

### 2026-08-30: Scripting additions and retired interfaces

These announcements cover changes made between December 17, 2025 and August 30, 2026.

- [`sortby()`](../function/sortby.md) adds custom word-list sorting, [`stricmp()`](../function/stricmp.md) compares two quoted words, and the `<=>` [sort operator](math_operators.md) performs case-insensitive string comparison. The swap operator is now `=>`.
- The `nicklist` and `nickcolor.irc` scripts add a channel nickname display and nickname-based colors.
- Hexadecimal constants are supported in integer contexts.
- Python 3.8 became the minimum supported version for [Python integration](using_python.md).
- [`IRCCHANNEL`](environment_variables.md) selects a channel to join after the initial server connection, like the `-c` command-line option.
- Server-password and operator-password prompting were retired. Termcap support was retired; terminal handling uses terminfo.
- The `suppress_from_remote_server` and `allow_c1_chars` settings, `uhc()`, `mesg`, `botmode`, and the `stop_irc` binding were retired. Use the startup `-b` option to launch in the background.
- The removed hooks include `encrypted_notice`, `encrypted_privmsg`, `flood`, `help`, `note`, `notify_signon`, `notify_signoff`, `redirect`, and `wall`.
- Static analysis with Cppcheck and Coverity led to bug fixes.

### 2025-12-17: Installation types

The `--with-installtype=prod` configure option installs the executable under its configured name without the commit-number suffix and symlink used by the default installation type. See [installing EPIC6](installing.md).

### 2025-08-18: Comma-separated level sets

[Level sets](levels.md) use comma-separated names rather than space-separated names, allowing a set to be passed as a single word to interfaces such as `window notify_level`.

### 2025-06-05: Compiled regular-expression encoding

[`regcomp()`](../function/regcomp.md) and related compiled-regex functions use Base85 for their encoded state.

### 2025-06-01: Base85 transformations

[`xform()`](../function/xform.md) gained the `B85` transformation for ASCII85 encoding and decoding, using the `<~...~>` wrapper.

### 2025-05-27: SASL mechanism names

SASL rules use the server’s exact mechanism spelling and case, such as `EXTERNAL`, `ECDSA-NIST256P-CHALLENGE`, `SCRAM-SHA-512`, and `PLAIN`. The supplied `sasl` script selects its best matching rule rather than trying multiple rules for a server.

### 2025-05-26: SCRAM authentication and output contexts

- The `sasl` script gained `SCRAM-SHA-512` support. [`scrambox()`](../function/scrambox.md) supplies its low-level SCRAM operations.
- [`on context`](../on/context.md) reports output-context creation, and [`shh`](../command/shh.md) can suppress display for the context’s lifetime.

### 2025-05-16: SASL, capability negotiation, and server properties

- The `sasl` script provides a unified place to configure supported authentication mechanisms.
- Capability discovery runs during connection setup. [`on cap`](../on/cap.md) exposes capability offers and acknowledgments; `serverctl`’s `cap_hold` field can delay the end of negotiation until a script releases its hold.
- [`serverctl()`](../function/serverctl.md) gained access to the server-description `port` and `cert` fields.

### 2025-05-12: ECDSA and vhost handling

[`ecdsatool()`](../function/ecdsatool.md) adds key generation, public-key extraction, and challenge signing. [Vhost handling](../command/hostname.md) caches resolved addresses; numeric addresses avoid hostname lookup, while a hostname can require a blocking lookup on first use.

### 2025-04-30: Socket and key-binding changes

Unix-domain-socket server connections were retired. Control-S is no longer bound to [`toggle_stop_screen`](../bind/toggle_stop_screen.md) by default.

### 2025-04-10: Compact JSON and connection policy

[`json_implode()`](../function/json_implode.md) defaults to compact output. The [`policy` server state](server_state.md), between `reconnect` and `dns`, provides a point to adjust a server description before connection work begins.

### 2025-03-08: EPIC6 direction

EPIC6’s development emphasizes simpler interfaces and retiring obsolete facilities. The announced retirements include C90-only environments, shebang startup, `redirect` and `flush`, CPU saver, incoming flood control, embedded Perl and Ruby, legacy encryption types, the old math parser, Shift-JIS handling, and termcap-only environments. Mail checking and nickname monitoring moved from built-ins to scripts. Unlimited input lines and mouse interaction are among the additions.

### 2025-02-17: Mouse support

[`set mouse`](../set/mouse.md) enables click-to-focus and scrollwheel handling on compatible terminals. Scrollwheel events affect the current input window. Mouse reporting can change the terminal’s text-selection behavior.

### 2024-12-12: Destructive token extraction

[`token()`](../function/token.md) returns the text before a literal delimiter and replaces the named variable with the text after it. When the delimiter is absent, it returns the whole value and clears the variable; spaces are ordinary characters.

### 2024-08-26: EPIC6 fork

EPIC6 forked from EPIC5.

## 2016-02-13: EPIC5 2.0 announcement

EPIC5 2.0 was announced on February 13, 2016. Its `epic5-2.0` tagged source records February 12, 2016, with `internal_version` `20160212`.

## 2014-04-13: EPIC5 1.1.10

EPIC5 1.1.10's source release date is April 13, 2014. Its release commit, `8390b7ef`, records internal commit ID **1781**.

EPIC5 1.1.9 had been withdrawn because of a serious bug. The 1.1.10 release highlights were:

- `$encodingctl()` supplied low-level control over `/encoding` rules.
- `$fix_width()` was rewritten to match its intended behavior.
- Most string-manipulation functions became UTF-8 aware, counting code points rather than bytes where applicable.
- `/xtype -L`, `$[num]var` padding/truncation, and `/fec` gained UTF-8 handling.
- Case-insensitive comparisons and matching, including `==` and `$rmatch()`, gained Unicode-aware behavior subject to locale support.
- The scripting environment's UTF-8 support was substantially expanded.

These were release highlights rather than guarantees that every string operation counted display columns or handled every Unicode text operation identically.

## 2014-04-04: EPIC5 1.1.8

EPIC5 1.1.8, internal commit ID 1775, was released on April 4, 2014. The announcement highlighted:

- UTF-8 support for the console, scripts, and IRC messages.
- Encoding conversion for messages sent to and received from IRC.
- 256-color support.
- UTF-8-aware string functions such as `$mid()` and `$split()`.
- Additional improvements recorded in the source history.

Available encodings and usable conversions depend on the system and EPIC’s conversion rules.

## 2014-03-31: EPIC4 2.10.5

EPIC4 2.10.5, internal commit ID 779, was released March 31, 2014, adding full Maildir support contributed by Jari Turkia.

## 2014-02-11: EPIC4 2.10.4

EPIC4 2.10.4, internal commit ID 778, was released February 11, 2014. Its changes included a new `unicode` script from |Rain| and a fix for `$(IP)` support taken from EPIC5 for FreeBSD porters.

## Source references

- Upstream commit `70a655b6` and [KNOWNBUGS](../KNOWNBUGS.md): October 30, 2026 changes, including authentication, regex consumers, command parsing, message splitting, and topline limits.
- [UPDATES](../UPDATES.md): dated EPIC6 development announcements from August 2024 through August 2026.
- Repository tag `epic5-2.0`, `source/irc.c`: version name, internal release date, and commit ID; tag commit `075087c1` records the release.
- Repository commit `8390b7ef`, `source/irc.c` and `UPDATES`: EPIC5 1.1.10 release identity and contemporary encoding/function changes.
- Repository commit `d0ac3ed1`, `source/irc.c`: EPIC5 1.1.8, release date `20140404`, and commit ID 1775.
- Repository commits `1ed00810`, `66d46a70`, `82e6832d`, and `7aa00123`: Unicode case handling, string functions, `encodingctl()`, and `fix_width()` changes leading to those releases.
