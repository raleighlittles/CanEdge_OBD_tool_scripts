#!/usr/bin/env bash

## Renames all the CanEdge files in a directory to have the date they were created,
## plus an optional suffix.
## ie. `ABCDEF.MF4` becomes `20010911_<suffix>.MF4`

## The CanEdge usually creates one folder per 'session', underneath a top-level folder with the device ID,
## e.g. `<path-where-SD-card-is-mounted>/LOG/<device-id>`
## will have multiple directories underneath it for each session.
## This script accounts for that and can search this doubly-nested structure

## $1 = input_directory - the path to where the SD card is mounted
## $2 = output directory - path to where final-renamed MF4 files should be copied to

input_dir=$1
suffix="versa"
file_ext="MF4"

for dirname in "$input_dir"/LOG; do

	echo "Scanning for $file_ext files in $dirname"

	for filename in "$input_dir"/"$dirname"/*"$file_ext"; do

		file_modified_date=$(date -r "$filename" "+%Y%m%d%H%M%S")
		mv -vn "$filename" "$file_modified_date"_"$suffix"."$file_ext"
		
	done

done

# delete empty directories
find "$input_dir" -type d -empty -delete

# move to output location
output_dir=$2
mv -vn *."$file_ext" "$output_dir"