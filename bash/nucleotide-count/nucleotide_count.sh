#!/usr/bin/env bash
set -o errexit
set -o nounset

main() {
    if (( $# != 1 )) ; then
        echo "Usage: nucleotide_count.sh <string>"
        exit 1
    fi

    A=0
    C=0
    G=0
    T=0
    for ((i=0; i<${#1}; i++)); do
        if [[ "${1:$i:1}" == "A" ]]; then
            ((A+=1))
        elif [[ "${1:$i:1}" == "C" ]]; then
            ((C+=1))
        elif [[ "${1:$i:1}" == "G" ]]; then
            ((G+=1))
        elif [[ "${1:$i:1}" == "T" ]]; then
            ((T+=1))
        else
            echo "Invalid nucleotide in strand"
            exit 1
        fi


    done
    echo -e "A: $A\nC: $C\nG: $G\nT: $T"

}


main "$@"
