#!/bin/bash

show_answer=true
from_fixtures=false

while [ $# -gt 0 ]; do
  	case "$1" in
    	-y|--no-confirm)
    	  	show_answer=false
      	    ;;
        -f|--from-fixtures)
            from_fixtures=true
      	    ;;
  	esac
	shift
done

if $show_answer ; then
	echo "WARNING!! This script REMOVE your Cinemair's database and you LOSE all the data."
	read -p "Are you sure you want to delete all data? (Press Y to continue): " -n 1 -r
	echo    # (optional) move to a new line
	if [[ ! $REPLY =~ ^[Yy]$ ]] ; then
		exit 1
	fi
fi


echo "-> Remove cinemair DB"
dropdb cinemair
echo "-> Create cinemair DB"
createdb cinemair

echo "-> Load migrations"
python manage.py migrate

echo "-> Populate the data base"
if $from_fixtures ; then
    python manage.py sampledata --from-fixtures --traceback
else
    python manage.py sampledata --traceback
fi
