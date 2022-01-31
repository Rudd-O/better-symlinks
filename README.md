# Better symlinks

This is a very simple program to manage symlinks in your information
collection or file systems.

## Usage and modes of operation

The program has various modes of operation.  All modes support `-n` / `--dry-run` to print what would happen without actually making any changes on disk.

### Diagnostic

Also known as `diagnose` mode.

`better-symlinks diagnose <path>` will output a list of symlinks that are broken under folder `path`.

### Symlink modification

Also known as `sed` mode.

`better-symlinks sed <expression> <path>` will use a sed extended regular expression script (typically a `s/` search and replace one) on every symlink under `path` and replace the target of the symlink with the results of the expression.  Very useful to mass rename targets of symlinks.  Suppose you have the following symlinks pointing to various targets:

* `/folder/symlink` -> `/oldfolder/target`
* `/folder/another symlink` -> `/oldfolder/target2`

and suppose that you renamed `/oldfolder` to `/newfolder`.  Now all your symlinks under `/folder` are broken.

This mode fixes that. Running `better-symlinks sed 's|/oldfolder|/newfolder|' /folder` should replace `/oldfolder` in the broken symlinks to `/newfolder`, yielding valid symlinks again.

### Relativization

Also known as `relativize` mode.

`better-symlinks relativize <path>` will make all symlinks under `path` into relative symlinks, irrespective of file system; this is in some sense better than what the standard `symlinks` tool does, since that tool ignores other file systems, and that behavior cannot be turned off in that tool.  The tool will not modify any symlinks that don't point to existing files.
