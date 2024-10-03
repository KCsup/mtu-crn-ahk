#! /usr/bin/env nix-shell
#! nix-shell -i bash -p bash python311

python3 -m http.server 6942
