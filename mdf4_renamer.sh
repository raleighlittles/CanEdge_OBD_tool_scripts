#!/usr/bin/env bash

## Renames all the CanEdge files in a directory to have the date they were created,
## plus an optional suffix.
## ie. `ABCDEF.MF4` becomes `20010911_<suffix>.MF4`

## The CanEdge usually creates one folder per 'session', underneath a top-level folder with the device ID,
## e.g. `<path-where-SD-card-is-mounted>/LOG/<device-id>` so to rename files from all sessions, you can do,
## $ for dirname in *; do ~/github/CanEdge_OBD_Organizer/mdf4_renamer.sh "$dirname"; done
## (run from the 'LOG' folder)

## $1 = input_directory

input_dir=$1
suffix="versa"

file_ext="MF4"

for filename in "$input_dir"/*"$file_ext"; do

	file_modified_date=$(date -r "$filename" "+%Y%m%d%H%M%S")
	mv -vn "$filename" "$file_modified_date"_"$suffix"."$file_ext"
	
done
