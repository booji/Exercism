#!/usr/bin/env bash
set -o errexit
set -o nounset


main() {
    if (($# == 0)); then
         echo ""
         exit 0
    fi
    if  [[ $1 = *[!GCTA]* ]]; then
        echo "Invalid nucleotide detected."
        exit 1
    fi

    echo "${1}" | tr 'GCTA' 'CGAU'

}

main "$@"
