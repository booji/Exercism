#!/usr/bin/env bash
set -o errexit
set -o nounset

main() {
    if  (($# != 1)) || [[ $1 = *[!0-9]* ]]; then
        echo "Usage: armstrong_numbers.sh <int>"
        exit 1
    fi

    declare -i sum
    declare -i temp
    sum=0
    temp=$1

    while (($temp >= 1)); do
        digit=$((temp % 10))
        sum+=$((digit ** ${#1}))
        temp=$((temp/10))
    done

    if ((sum == $1)); then
        echo "true"
    else
        echo "false"
    fi
}

main "$@"
