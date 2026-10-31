# Functions

EPIC functions accept arguments and return a value. They can manipulate strings and word lists, perform calculations, inspect client state, or perform operations such as file I/O. A function call can have side effects; it is not necessarily a read-only query.

For a broader introduction, see [programming](programming.md). See [expressions](expressions.md) and [expando substitution](expando_substitution.md) for how function results fit into statements.

## Calling functions

In expanded text, write `$name(arguments)`. In an expression, write `name(arguments)` without the dollar sign. Arguments are text expanded before the call, usually separated by spaces rather than commas; each function defines its own argument and quoting rules. Empty parentheses supply an empty argument string.

```irc
alias measure { echo Length: $strlen($*) }
@ amount = abs(-12)
```

After defining the alias, `/measure hello` displays `Length: 5`. The expression assigns `12` to `amount`. Do not assume that a function's argument list is an arithmetic expression: use `${...}` explicitly when an argument needs calculation.

Names are case-insensitive. An ordinary call prefers a C built-in when a script alias has the same name. `$:name(arguments)` selects the script alias; `$::name(arguments)` selects the built-in. If the selected function does not exist, the dispatcher returns an empty string. Empty results can also be valid data or function-specific failures, so consult the individual page before treating an empty result as a success or error indicator.

Scripts define functions using aliases, optionally with an [argument list](arglist.md). `return value` supplies their result; a function alias starts with an empty return value. The [functions script](../scripts/functions.md) is a collection of helpers, not a prerequisite for calling C built-ins.

## Functions by domain

The groups below provide navigation through the current interfaces. Each linked page defines the actual arguments, return values, errors, side effects, and requirements. Similar names do not imply identical behavior. In particular, string positions, Unicode code points, display widths, and word indices are different units.

### Extracting substrings from strings

Extract, trim, or locate portions of text.

[after](../function/after.md), [before](../function/before.md), [chop](../function/chop.md), [left](../function/left.md), [leftpc](../function/leftpc.md), [mid](../function/mid.md), [rest](../function/rest.md), [right](../function/right.md).

### String operations

Transform text, inspect characters, and manage formatting.

[ascii](../function/ascii.md), [asciiq](../function/asciiq.md), [center](../function/center.md), [chr](../function/chr.md), [chrq](../function/chrq.md), [count](../function/count.md), [cparse](../function/cparse.md), [deuhc](../function/deuhc.md), [fix_width](../function/fix_width.md), [getopt](../function/getopt.md), [hex](../function/hex.md), [index](../function/index.md), [insert](../function/insert.md), [is8bit](../function/is8bit.md), [isalpha](../function/isalpha.md), [isdigit](../function/isdigit.md), [isnumber](../function/isnumber.md), [isutf8](../function/isutf8.md), [joinstr](../function/joinstr.md), [maxlen](../function/maxlen.md), [msar](../function/msar.md), [nohighlight](../function/nohighlight.md), [numlines](../function/numlines.md), [pad](../function/pad.md), [pass](../function/pass.md), [printlen](../function/printlen.md), [repeat](../function/repeat.md), [reverse](../function/reverse.md), [rgb](../function/rgb.md), [rindex](../function/rindex.md), [rsubstr](../function/rsubstr.md), [sar](../function/sar.md), [shiftbrace](../function/shiftbrace.md), [split](../function/split.md), [splitw](../function/splitw.md), [stricmp](../function/stricmp.md), [strip](../function/strip.md), [stripansi](../function/stripansi.md), [stripansicodes](../function/stripansicodes.md), [stripc](../function/stripc.md), [stripcrap](../function/stripcrap.md), [strlen](../function/strlen.md), [strtol](../function/strtol.md), [substr](../function/substr.md), [tolower](../function/tolower.md), [toupper](../function/toupper.md), [tr](../function/tr.md), [unicode](../function/unicode.md), [unsplit](../function/unsplit.md), [xform](../function/xform.md).

### Word operations

Extract and manipulate word lists; some functions change a named variable.

[afterw](../function/afterw.md), [beforew](../function/beforew.md), [chngw](../function/chngw.md), [common](../function/common.md), [diff](../function/diff.md), [findw](../function/findw.md), [findws](../function/findws.md), [fromw](../function/fromw.md), [indextoword](../function/indextoword.md), [insertw](../function/insertw.md), [leftw](../function/leftw.md), [midw](../function/midw.md), [notw](../function/notw.md), [numsort](../function/numsort.md), [numwords](../function/numwords.md), [pop](../function/pop.md), [prefix](../function/prefix.md), [push](../function/push.md), [qword](../function/qword.md), [remw](../function/remw.md), [remws](../function/remws.md), [restw](../function/restw.md), [revw](../function/revw.md), [rightw](../function/rightw.md), [shift](../function/shift.md), [sort](../function/sort.md), [sortby](../function/sortby.md), [splice](../function/splice.md), [tow](../function/tow.md), [uniq](../function/uniq.md), [unshift](../function/unshift.md), [word](../function/word.md), [wordtoindex](../function/wordtoindex.md).

### Math functions

Numeric calculations and conversions; domain and range behavior can depend on the platform math library.

[abs](../function/abs.md), [acos](../function/acos.md), [acosh](../function/acosh.md), [asin](../function/asin.md), [asinh](../function/asinh.md), [atan](../function/atan.md), [atanh](../function/atanh.md), [ceil](../function/ceil.md), [cos](../function/cos.md), [cosh](../function/cosh.md), [exp](../function/exp.md), [floor](../function/floor.md), [jn](../function/jn.md), [log](../function/log.md), [log10](../function/log10.md), [rand](../function/rand.md), [sin](../function/sin.md), [sinh](../function/sinh.md), [srand](../function/srand.md), [tan](../function/tan.md), [tanh](../function/tanh.md), [tobase](../function/tobase.md), [trunc](../function/trunc.md), [yn](../function/yn.md).

### Time info

Timestamps, date formatting and parsing, and elapsed-time formatting.

[metric_time](../function/metric_time.md), [mktime](../function/mktime.md), [stime](../function/stime.md), [strftime](../function/strftime.md), [strptime](../function/strptime.md), [tdiff](../function/tdiff.md), [tdiff2](../function/tdiff2.md), [time](../function/time.md), [utime](../function/utime.md).

### Pattern matching

Wildcard selection, filename globbing, and regular-expression handles.

[cofilter](../function/cofilter.md), [copattern](../function/copattern.md), [corfilter](../function/corfilter.md), [corpattern](../function/corpattern.md), [filter](../function/filter.md), [glob](../function/glob.md), [mask](../function/mask.md), [match](../function/match.md), [pattern](../function/pattern.md), [regcomp](../function/regcomp.md), [regcomp_cs](../function/regcomp_cs.md), [regerror](../function/regerror.md), [regexec](../function/regexec.md), [regfree](../function/regfree.md), [regmatches](../function/regmatches.md), [rfilter](../function/rfilter.md), [rmatch](../function/rmatch.md), [rpattern](../function/rpattern.md).

### Server operations

Inspect or control known server connections. Most information queries read cached client state; a control operation can initiate activity.

[cipher](../function/cipher.md), [isaway](../function/isaway.md), [isconnected](../function/isconnected.md), [isencrypted](../function/isencrypted.md), [myservers](../function/myservers.md), [serverctl](../function/serverctl.md), [serverwin](../function/serverwin.md), [servports](../function/servports.md), [ssl](../function/ssl.md), [usermode](../function/usermode.md), [version](../function/version.md).

### Channel info

Inspect locally known channel state. Results depend on the selected server and information received from it.

[chankey](../function/chankey.md), [chanlimit](../function/chanlimit.md), [chanmode](../function/chanmode.md), [channel](../function/channel.md), [chanusers](../function/chanusers.md), [chansyncing](../function/chansyncing.md), [chops](../function/chops.md), [ischannel](../function/ischannel.md), [ischanop](../function/ischanop.md), [ischanvoice](../function/ischanvoice.md), [iscurchan](../function/iscurchan.md), [ishalfop](../function/ishalfop.md), [key](../function/key.md), [mychannels](../function/mychannels.md), [nochops](../function/nochops.md), [numonchannel](../function/numonchannel.md), [onchannel](../function/onchannel.md), [userhost](../function/userhost.md).

### Display operations

Inspect windows, input, status lines, and retained output.

[chanwin](../function/chanwin.md), [curpos](../function/curpos.md), [currchans](../function/currchans.md), [geom](../function/geom.md), [getcap](../function/getcap.md), [inputctl](../function/inputctl.md), [isdisplaying](../function/isdisplaying.md), [lastlog](../function/lastlog.md), [levelwindow](../function/levelwindow.md), [line](../function/line.md), [notifywindows](../function/notifywindows.md), [outputinfo](../function/outputinfo.md), [querywin](../function/querywin.md), [status](../function/status.md), [status_oneoff](../function/status_oneoff.md), [winchan](../function/winchan.md), [windowctl](../function/windowctl.md).

### Array operations

Use the separate built-in indexed-array facility; see [arrays](arrays.md) for item numbers versus sorted indices.

[delarray](../function/delarray.md), [delitem](../function/delitem.md), [delitems](../function/delitems.md), [finditem](../function/finditem.md), [finditems](../function/finditems.md), [getarrays](../function/getarrays.md), [getitem](../function/getitem.md), [getmatches](../function/getmatches.md), [getrmatches](../function/getrmatches.md), [gettmatch](../function/gettmatch.md), [ifindfirst](../function/ifindfirst.md), [ifinditem](../function/ifinditem.md), [ifinditems](../function/ifinditems.md), [igetitem](../function/igetitem.md), [igetmatches](../function/igetmatches.md), [igetrmatches](../function/igetrmatches.md), [indextoitem](../function/indextoitem.md), [itemtoindex](../function/itemtoindex.md), [listarray](../function/listarray.md), [matchitem](../function/matchitem.md), [numarrays](../function/numarrays.md), [numitems](../function/numitems.md), [rmatchitem](../function/rmatchitem.md), [setitem](../function/setitem.md), [usetitem](../function/usetitem.md).

### File I/O

Open, read, write, seek, and inspect files through client-managed handles; open modes and failure values are function-specific.

[close](../function/close.md), [dbmctl](../function/dbmctl.md), [eof](../function/eof.md), [ferror](../function/ferror.md), [frewind](../function/frewind.md), [fseek](../function/fseek.md), [fsize](../function/fsize.md), [fskip](../function/fskip.md), [ftell](../function/ftell.md), [ftime](../function/ftime.md), [ftruncate](../function/ftruncate.md), [isfilevalid](../function/isfilevalid.md), [open](../function/open.md), [randread](../function/randread.md), [read](../function/read.md), [write](../function/write.md), [writeb](../function/writeb.md).

### Client operations

Inspect and control aliases, keybindings, hooks, timers, settings, output levels, logs, encoding, and CTCP handlers.

[aliasctl](../function/aliasctl.md), [bindctl](../function/bindctl.md), [builtin_expando](../function/builtin_expando.md), [cexist](../function/cexist.md), [check_code](../function/check_code.md), [ctcpctl](../function/ctcpctl.md), [curcmd](../function/curcmd.md), [encodingctl](../function/encodingctl.md), [epic](../function/epic.md), [execctl](../function/execctl.md), [fix_arglist](../function/fix_arglist.md), [fnexist](../function/fnexist.md), [functioncall](../function/functioncall.md), [getcommands](../function/getcommands.md), [getfunctions](../function/getfunctions.md), [getserial](../function/getserial.md), [getset](../function/getset.md), [getsets](../function/getsets.md), [hookctl](../function/hookctl.md), [iconvctl](../function/iconvctl.md), [idle](../function/idle.md), [info](../function/info.md), [irclib](../function/irclib.md), [levelctl](../function/levelctl.md), [loadinfo](../function/loadinfo.md), [logctl](../function/logctl.md), [sequence_point](../function/sequence_point.md), [startupfile](../function/startupfile.md), [symbolctl](../function/symbolctl.md), [tags](../function/tags.md), [timerctl](../function/timerctl.md), [xdebug](../function/xdebug.md).

### Network operations

Address conversion and name resolution; availability and returned addresses depend on the host network environment.

[convert](../function/convert.md), [iptolong](../function/iptolong.md), [iptoname](../function/iptoname.md), [longtoip](../function/longtoip.md), [nametoip](../function/nametoip.md).

### System operations

Filesystem and process operations, process environment, identity, and platform security interfaces.

[chmod](../function/chmod.md), [exec](../function/exec.md), [fexist](../function/fexist.md), [getenv](../function/getenv.md), [getgid](../function/getgid.md), [getlogin](../function/getlogin.md), [getpgrp](../function/getpgrp.md), [getuid](../function/getuid.md), [killpid](../function/killpid.md), [mkdir](../function/mkdir.md), [pid](../function/pid.md), [pledge](../function/pledge.md), [ppid](../function/ppid.md), [realpath](../function/realpath.md), [rename](../function/rename.md), [rmdir](../function/rmdir.md), [stat](../function/stat.md), [ttyname](../function/ttyname.md), [twiddle](../function/twiddle.md), [umask](../function/umask.md), [uname](../function/uname.md), [unlink](../function/unlink.md), [unveil](../function/unveil.md).

### Miscellanea

Structured data, cryptographic helpers, identifiers, and list generation.

[ecdsatool](../function/ecdsatool.md), [hash_32bit](../function/hash_32bit.md), [jot](../function/jot.md), [json_error](../function/json_error.md), [json_explode](../function/json_explode.md), [json_implode](../function/json_implode.md), [jsontest](../function/jsontest.md), [pbkdf2](../function/pbkdf2.md), [scrambox](../function/scrambox.md), [uuid4](../function/uuid4.md).

## Script-provided functions

Loading [builtins](../scripts/builtins.md) supplies compatibility helpers including `b64encode`, `b64decode`, `encode`, `decode`, `urlencode`, `urldecode`, and `sha256`, implemented through the C `xform` interface. They are script aliases even though the package is named `builtins`. Some helpers overlap names still present in C; ordinary-call dispatch continues to prefer the C function.

Other examples are [notify](../scripts/notify.md), [scan](../scripts/scan.md), and [pipe](../scripts/pipe.md). These require their scripts to be loaded, and their effects differ: `scan` formats channel information, while `pipe` captures command output. A script helper can itself rely on other scripts or on removed interfaces, so use its current documentation rather than assuming that every installed script is operational.

## External scripting languages and availability

[python](../function/python.md) and [pydirect](../function/pydirect.md) are registered when EPIC is built with Python support. Their availability and argument rules are separate from EPIC alias functions. Platform-dependent functions, database support, regular-expression backends, security calls, and individual `xform` transformations also have their own build or platform requirements.

`fnexist(name)` tests for a registered C built-in, not a script alias. `getfunctions()` lists built-in function names; `aliasctl` and `symbolctl` provide script-symbol inspection. Registration alone is not a guarantee of useful behavior for every argument or build: consult the function's page and check its result. Server-related operations are also subject to connection state and network policy.

## Source references

- `source/functions.c`: `built_in_functions[]`, conditional registrations, `call_function()`, and individual handlers.
- `source/alias.c`: built-in/script symbol lookup and introspection.
- `source/commands.c`: alias function calls and return values.
- `source/expr.c` and `source/expr2.c`: text and expression call syntax.
- `script/builtins` and the linked scripts: script-provided compatibility and utility functions.
