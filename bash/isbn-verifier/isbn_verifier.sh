#!/usr/bin/env bash
set -o errexit
set -o nounset

main() {
    declare -i res
    declare -i mul

    isbn=${1//-/}
    if ((${#isbn} != 10)); then
        echo "false"
        exit 0
    fi
    if [[ $isbn != [0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9X] ]]; then
        echo "false"
        exit 0
    fi

    for (( i = 0; i < 10; i++ )); do
        mul=$((10 - i))
        char="${isbn:i:1}"
        if [[ $char = 'X' ]]; then
          char=10
        fi
        res+=$((char * mul))
    done
    if ((res % 11 == 0)); then
        echo "true"
    else
        echo "false"
    fi
}

main "$@"
