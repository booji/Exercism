#!/usr/bin/env bash
set -o errexit
set -o nounset


main () {
    if ((${#} != 1)); then
        echo "Usage: pangram.sh <string>"
        exit 1
    fi

    allLower=$(echo "${1}" | tr '[:upper:]' '[:lower:]')
    alphabet=$(echo {a..z})
    alphabet="${alphabet// /}"

    allLower=${allLower//[ .!_,\"\-0123456789]/}

    for ((i=0; i<${#allLower}; i++)); do

        alphabet=${alphabet//${allLower:i:1}/}
    done

    if ((${#alphabet} == 0)); then
        echo 'true'
    else
        echo 'false'
    fi

}

main "$@"
