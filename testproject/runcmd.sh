#!/bin/sh
#
# Run ``test`` or any other Django custom management command for each
# available environment.
#
# Usage: runcmd.sh [<cmd>]
#

DIRNAME=`python -c 'import os, sys; print(os.path.abspath(os.path.dirname(sys.argv[1])));' $0`
cmd="$@"

for dir in $DIRNAME/env*/
do
    if [ ! -d "$dir" ]
    then
        continue
    fi

    echo "Working environment is '`basename $dir`'"
    echo "Django command is '$cmd'"
    echo

    source "$dir/bin/activate"
    python "$DIRNAME/manage.py" $cmd

    echo
    echo "--------------------------------------------------------------------"
    echo
done
