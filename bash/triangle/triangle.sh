#!/usr/bin/env bash
set -o errexit
set -o nounset

is_triangle() {

    if [[ $( echo "$1 == 0" | bc ) -eq 1 || $( echo "$2 == 0" | bc ) -eq 1 || $( echo "$3 == 0" | bc ) -eq 1 ]]; then
        echo "false"
    elif ! [[ $( echo "$1 + $2 >= $3" | bc ) -eq 1 && $( echo "$1 + $3 >= $2" | bc ) -eq 1 && $( echo "$2 + $3 >= $1" | bc ) -eq 1 ]]; then
        echo "false"
    else
        echo 'true'
    fi
}

equilateral(){
    if [[ $( echo "$1 == $2" | bc ) -eq 1 && $( echo "$1 == $3" | bc ) -eq 1 ]]; then
        echo "true"
    else
        echo "false"
    fi
}


isosceles() {
    if [[ $( echo "$1 == $2" | bc ) -eq 1 || $( echo "$1 == $3" | bc ) -eq 1 || $( echo "$2 == $3" | bc ) -eq 1 ]]; then
        echo "true"
    else
        echo "false"
    fi
}

scalene() {
    if [[ $( echo "$1 != $2" | bc ) -eq 1 && $( echo "$2 != $3" | bc ) -eq 1 && $( echo "$1 != $3" | bc ) -eq 1 ]]; then
        echo "true"
    else
        echo "false"
    fi
}

main() {
    if (($# != 4)); then
        echo "Usage: triangle.sh <equilateral|isosceles|scalene> <num1> <num2> <num3>"
        exit 1
    fi

    if [[ $(is_triangle $2 $3 $4) == 'false' ]]; then
        echo "false"
        exit 0
    fi

    case $1 in
        equilateral)
            result=$(equilateral $2 $3 $4)
            ;;
        isosceles)
            result=$(isosceles $2 $3 $4)
            ;;
        scalene)
            result=$(scalene $2 $3 $4)
            ;;
    esac

    echo "$result"

}

main "$@"
