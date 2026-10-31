# regfree function

## Synopsis

`$regfree(<compiled expression>)`

## Technical

Releases the library resources associated with a successfully compiled expression returned by [$regcomp()](regcomp.md) or [$regcomp_cs()](regcomp_cs.md). The first normal function word is taken as the compiled string; extra arguments are ignored.

The wrapper initializes a `regex_t` structure, decodes the string from Base85, and requires the decoded data to fill exactly that structure before calling the regex library's `regfree()`. Failed decoding or a wrong decoded size prints `First argument to $regfree() is not a value from $regcomp()` and frees no regex resources. These checks do not verify ownership or compilation status.

## Returns

Always the empty string, including missing input, rejected input, and the path that calls the library cleanup routine. The result therefore does not confirm that resources were released. Missing input produces no diagnostic. This operation does not change the shared error state queried by [$regerror()](regerror.md).

## Restrictions

When resources have actually been freed, do not free them again or use the compiled string with [$regexec()](regexec.md), [$regmatches()](regmatches.md), or `regerror`. Copies of the string share the same underlying resources and all become unusable together. Freeing does not erase the EPIC variable containing the string.

Use only an original compiled string from the current process; arbitrary, corrupted, or unsuccessfully compiled state is not a supported cleanup input. No IRC connection is required.

## Example

After successful compilation and all matching operations, `$regfree($pattern)` releases the expression stored in `pattern`, returning empty. Clear the variable afterward to avoid accidentally reusing the freed state.

## History

First appeared in epic4-1.029.

## Source

Registration, `function_regfree()`, and compilation encoding: [source/functions.c](../../source/functions.c). Base85 decoding: [source/ircaux.c](../../source/ircaux.c). Regex library selection: [include/irc_std.h](../../include/irc_std.h).
