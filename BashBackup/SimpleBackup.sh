#! /bin/bash
if [[ $# -lt 2 ]]; then
    echo "Usage: $0 [source] [destination] [options]"
    exit 1
fi

source=$1
destination=$2

if [[ ! -d $source ]]; then
    echo "ERROR: Source directory does not exist"
    echo "Backup failed"
    exit 1
fi

if [[ ! -d $destination ]]; then
    read -p "$destination isn't an existing directory. Create new directory here? (y/n) " ans
    if [[ $ans != "y" ]]; then
        echo "Backup failed"    
        exit 1
	fi
fi

delete_old=0
compress=0

while getopts ":c:z" opt ${@:3}
do
    case $opt in
        c)
            delete_old=1
            shift
            if [ $OPTARG == "z" ]; then
                shift
            fi
            delete_before=${@:$OPTIND:2}
            ((OPTIND+=2))
            ;;
        z)
            compress=1
            ;;
        \?)
            echo "Invalid option: -$OPTARG"
            echo "Backup failed"
            exit 1
            ;;
    esac
done

if [ $delete_old -eq 1 ]; then
    # count the number of backups to be deleted
    num_backups=$(find $destination -depth -type d -name "[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]_[0-9][0-9]:[0-9][0-9]" ! -newermt "$delete_before" | wc -l)

    if (( num_backups > 0 )); then
        read -p "Are you sure you want to delete $num_backups backups from before $delete_before? (y/n) " ans
        if [ $ans != "y" ]; then
            echo "Backup failed"
            exit 1
        fi
        # delete old backups
        find $destination -depth -type d -name "[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]_[0-9][0-9]:[0-9][0-9]" ! -newermt "$delete_before" -exec rm -r {} \;
    else
        echo "No backups to delete before $delete_before"
    fi
fi

#create directory with current date and time of backup
destination="$destination/$(date +%Y-%m-%d_%H:%M)"
mkdir -p $destination

if [[ $compress -eq 1 ]]; then
    tar -czf "${destination}/backup.tar.gz" -C $(dirname "$source") $(basename "$source")
    echo "Compressed archive \"backup.tar.gz\" created in \"${destination}/backup.tar.gz\" successfully"
else
    tar -cf "${destination}/backup.tar" -C $(dirname "$source") $(basename "$source")
    echo "Uncompressed archive \"backup.tar\" created in \"${destination}/backup.tar.gz\" successfully"
fi


