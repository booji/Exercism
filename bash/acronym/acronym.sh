#!/usr/bin/env bash
set -o errexit
set -o nounset

main() {
    if (($# != 1)); then
        echo "Usage: acronym.sh <string>"
        exit 1
    fi

    string="${1//-/ }"
    acronym=''
    for word in $string; do
        acronym+="${word:0:1}"
    done

    echo ${acronym} | tr '[a-z]' '[A-Z]'

}

main "$@"
