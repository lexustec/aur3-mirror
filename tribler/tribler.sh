#!/bin/sh

export PYTHONPATH="/usr/share/tribler:$PYTHONPATH"
cd /usr/share/tribler
python2 Tribler/Main/tribler.py "$@"
