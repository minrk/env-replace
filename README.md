# env-replace

Pipe commands that produce lots of output through `env-replace` to replace expanded environment variables
(especially prefix paths in build output) with the environment variables themselves.

Install:

```bash
python3 -m pip install env-replace
```

Usage:

```bash
export PREFIX="/super-long-prefix-path"
echo "cc -I$PREFIX/include -L$PREFIX/lib ..." | env-replace
```

reverses environment variable expansion so that the output is:

```
cc -I$PREFIX/include -L$PREFIX/lib ...
```

instead of

```
cc -I/super-long-prefix-path/include -L/super-long-prefix-path/lib ...
```
