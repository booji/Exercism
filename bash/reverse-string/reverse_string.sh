#!/usr/bin/env bash

set -o errexit
set -o nounset

main() {
    input=$@
    reverse_string=""
    for ((i = ${#input}-1; i>=0; i--))
        do reverse_string="$reverse_string${input:$i:1}"
    done
    echo $reverse_string
    exit 0
}

main "$@"
