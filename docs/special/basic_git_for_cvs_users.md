# Keeping up with EPIC in Git

To obtain EPIC6, use `git clone`, the rough equivalent of `cvs co`:

```sh
git clone https://git.epicsol.org/epic6.git
cd epic6
```

For the older EPIC5 and EPIC4 generations, the repository addresses are:

```sh
git clone https://git.epicsol.org/epic5.git
git clone https://git.epicsol.org/epic4.git
```

To update, run this inside your checkout:

```sh
git pull
```

This is the closest counterpart to `cvs update`, but Git fetches and integrates changes into the current branch according to its upstream and pull configuration. Local changes or divergent history can require additional action; it is not a guarantee that every checkout can always update without intervention.

To produce a patch for unstaged changes to tracked files:

```sh
git diff --no-color
```

Git's normal patch format is already unified; `-u` is optional. Use `git diff --cached --no-color` for staged changes, or `git diff HEAD --no-color` for both staged and unstaged changes to tracked files. Untracked files do not appear in these diffs.
