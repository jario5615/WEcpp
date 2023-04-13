#! /bin/bash
if [[ $# -ne 2 ]]; then
    echo "Usage: $0 [source] [destination]"
    exit 1
fi

source=$1
destination=$2

if [[ ! -d $source ]]; then
    echo "ERROR: Source directory does not exist"
    exit 1
fi

if [[ ! -d $destination ]]; then
    read -p "$destination isn't an existing directory. Create new directory here? (y/n) " ans
    if [[ $ans -ne "y" ]]; then
        exit 1
	fi
fi
#create directory with current date and time of backup
destination="$destination/$(date +%Y-%m-%d_%H:%M)"
mkdir -p $destination

tar cfz "${destination}/backup.tar.gz" $source
echo "Backup created successfully"
