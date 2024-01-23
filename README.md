# boot

This package manages booting up PythonEDA domains.

## How to declare it in your flake

Check the latest tag of the definition repository: https://github.com/pythoneda-runtime-def/boot/tags, and use it instead of the `[version]` placeholder below.

```nix
{
  description = "[..]";
  inputs = rec {
    [..]
    pythoneda-runtime-boot = {
      [optional follows]
      url =
        "github:pythoneda-runtime-def/boot/[version]";
    };
  };
  outputs = [..]
};
```

If your project depends upon [https://github.com/nixos/nixpkgs](nixpkgs "nixpkgs") and/or [https://github.com/numtide/flake-utils](flake-utils "flake-utils"), you might want to pin them under the `[optional follows]` above.

The Nix flake is provided by the [https://github.com/pythoneda-runtime-def/boot](pythoneda-runtime-def/boot "pythoneda-runtime-def/boot") repository.
