# EventStoreDB

This package manages booting up EventStoreDB.

## How to declare it in your flake

Check the latest tag of the definition repository: https://github.com/pythoneda-runtime-infrastructure-def/eventstoredb/tags, and use it instead of the `[version]` placeholder below.

```nix
{
  description = "[..]";
  inputs = rec {
    [..]
    pythoneda-runtime-infrastructure-eventstoredb = {
      [optional follows]
      url =
        "github:pythoneda-runtime-infrastructure-def/eventstoredb/[version]";
    };
  };
  outputs = [..]
};
```

If your project depends upon [https://github.com/nixos/nixpkgs](nixpkgs "nixpkgs") and/or [https://github.com/numtide/flake-utils](flake-utils "flake-utils"), you might want to pin them under the `[optional follows]` above.

The Nix flake is provided by the [https://github.com/pythoneda-runtime-infrastructure-def/eventstoredb](pythoneda-runtime-infrastructure-def/eventstoredb "pythoneda-runtime-infrastructure-def/eventstoredb") repository.
