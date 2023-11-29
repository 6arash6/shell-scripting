#!/usr/bin/bash

if ! [[ -f first-engineer.sh ]]; then
    echo "missing file: first-engineer.sh"
    exit 1
fi

if ! [[ -f last-5-records.sh ]]; then
    echo "missing file: last-5-records.sh"
    exit 1
fi

if ! [[ -f num-doctors.sh ]]; then
    echo "missing file: num-doctors.sh"
    exit 1
fi


if ! [[ -f num-dr-smith.sh ]]; then
    echo "missing file: num-dr-smith.sh"
    exit 1
fi

../../tester/run-tests.sh
