# env-replace

Pipe commands that produce lots of output through `env-replace` to replace expanded environment variables
(especially prefix paths in build output) with the environment variables themselves.

Usage:

```bash
export PREFIX="/super-long-prefix-path"
echo "$PREFIX/baz" | env-replace
```

reverses environment variable expansion so that the output is:

```
$PREFIX/baz
```
