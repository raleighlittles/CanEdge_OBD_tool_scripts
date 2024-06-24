#!/usr/bin/env bash

set -e

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
output_dir=$2

for dirname in "$input_dir"/LOG/*; do

	#echo "Scanning for $file_ext files in $dirname"

	for subdir in "$dirname"/*; do

		#echo "Scanning subdir $subdir"

		for filename in "$subdir"/*$file_ext; do

			file_modified_date=$(date -r "$filename" "+%Y%m%d%H%M%S")
			new_filename="$file_modified_date"_"$suffix"."$file_ext"
			echo "Renaming $filename to '$new_filename'"
			mv -vn "$filename" "$output_dir"/"$new_filename"

		done
		
	done

done

# delete empty directories and temp files
find "$input_dir"/LOG -type d -empty -delete
find "$input_dir"/LOG -type f -iname "*.TMP"

# move to output location

# mv -vn *."$file_ext" "$output_dir"