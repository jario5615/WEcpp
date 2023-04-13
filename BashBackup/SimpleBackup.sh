#! /bin/bash

read -p "Enter path to source from " source
read -p "Enter destination path " destination
if [[ ! -d $source ]]
then
	echo "WARN: Source directory does not exist"
else
	if [[ ! -d $destination ]]
	then
		mkdir $destination
	fi
	tar cfz "${destination}/backup.tar.gz" $source
	echo "Backup created successfully"
fi
