#!/usr/bin/env bash
set -o errexit
set -o nounset

main() {

    if ((${#1} == 11)); then
        datetime="${1%Z} 00:00:00Z"
    else
        datetime=$1
    fi

    #BSD date command not Linux
    shiftedDate=$(date -jf '%F %TZ' -v+$((10**9))S -u "$datetime")

    # echo "$shiftedDate"
    #"2011-04-25Z" -> Thu  1 Jan 2043 01:46:40 UTC
    #Converting to idiotic US time defaults
    IFS=' ' read -ra dateARR <<< "$shiftedDate"
    echo "${dateARR[0]} ${dateARR[2]} ${dateARR[1]} ${dateARR[4]} ${dateARR[5]} ${dateARR[3]}"

}

main "$@"
