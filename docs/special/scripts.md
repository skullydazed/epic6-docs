# EPIC scripts

EPIC is a programmable IRC client in the ircII tradition. Scripts can define commands and event handlers and provide a different, more complete user experience.

Script packs differ because users want different experiences, and many offer customization. The EPIC5 listings below are historical; their target generation does not establish compatibility with EPIC6. Check a pack's own documentation before using it with this version.

## Scripts for EPIC5

- [Amnesiac](http://amnesiac.ircii.org/)
- [Darkstar](http://www.epicsol.org/~brian/darkstar/)
- [LiCe5](https://lice.muppetz.com/)

## Scripts for EPIC4

EPIC4 script packs target an older client generation. Check their dependencies and EPIC6 compatibility before using them.

## Current EPIC6 source references

The client registers [alias](../command/alias.md), [on](../command/on.md), and [load](../command/load.md) in [source/commands.c](../../source/commands.c). These support script-defined commands, event handlers, and script loading. The bundled [script directory](../../script/) contains individual scripts; [script/global](../../script/global) illustrates combining them into a setup. A bundled script collection and an external script pack can have different installation instructions and requirements.
