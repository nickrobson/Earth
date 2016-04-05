#!/usr/bin/env bash

DIR="$HOME/.earth/source"

if ! [ -e "$DIR" ]; then
    git clone 'https://github.com/nickrobson/Earth/' "$DIR"
    cd "$DIR"
    pip install -r requirements.txt
elif [ "$0" = "update" ]; then
    cd "$DIR"
    git pull
    pip install -r requirements.txt
fi

"$DIR/earth.py" &
