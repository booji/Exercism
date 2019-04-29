#!/usr/bin/env bash
set -o errexit
set -o nounset

square_of_sum() {
    local result=0
    for ((i=1; i<(($1+1)); i++)); do
        result=$((result+i))
    done
    result=$((result ** 2))
    echo "${result}"
}

sum_of_squares() {
    result=0
    for ((i=1; i<(($1+1)); i++)); do
        result=$((result + i ** 2))
    done
    echo "${result}"
}

difference() {
    echo "$(($(square_of_sum "${1}") - $(sum_of_squares "${1}")))"
}

main() {
    if  ((${#} != 2)); then
        echo "Usage: difference_of_squares.sh <option> <int>"
        exit 1
    fi

    case "${1}" in
        sum_of_squares)
            res=$(sum_of_squares "${2}")
            echo "${res}"
            ;;
        square_of_sum)
            res=$(square_of_sum "${2}")
            echo "${res}"
            ;;
        difference)
            res=$(difference "${2}")
            echo "${res}"
            ;;
        *)
            echo "Invalid option! Valid: sum_of_squares, square_of_sum, difference"
            exit 1
            ;;
    esac
}

main "${@}"
