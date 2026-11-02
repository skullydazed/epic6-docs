# set ssl_min_version

## Synopsis

```text
/set ssl_min_version [<version>]
/set -ssl_min_version
```

Default: `1.2`. With no value, [set](../command/set.md) displays the current value. The hyphen form clears the setting and restores the default.

## Description

Sets the minimum TLS version for new TLS server connections. The default, `1.2`, permits TLS 1.2 or newer. Set it to `1.3` to require TLS 1.3. TLS 1.0 and 1.1 are never used.

The spellings `TLSv1.2` and `TLSv1.3` are also accepted, without regard to case. Any other nonempty value produces a warning and uses `1.2`. If a server cannot negotiate the required version, its TLS handshake fails. The setting takes effect on the next connection; it does not change an established connection. If the linked OpenSSL does not support TLS 1.3, requesting `1.3` produces a warning and falls back to `1.2`.

## Example

```text
/set ssl_min_version 1.3
```

## Source references

- `source/ssl.c`: minimum TLS version selection and handshake configuration.
- `source/vars.c` and `include/config.h`: setting registration and default.
