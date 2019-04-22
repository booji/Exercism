#!/usr/bin/env bash
set -o errexit
set -o nounset

main() {
    if (( $# != 1 )) || [[ $1 = *[!0-9]* ]]; then
        echo "Usage: raindrops.sh <int>"
        exit 1
    fi

    if ! (($1%3)); then
        x=Pling
    fi
    if ! (($1%5)); then
        x+=Plang
    fi
    if ! (($1%7)); then
        x+=Plong
    fi

    echo "${x:-$1}"
}

main "$@"
