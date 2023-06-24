#!/usr/bin/env bash


## $1 = input_directory

input_dir=$1

file_ext="MF4"

for filename in "$input_dir"/*"$file_ext"; do

	file_modified_date=$(date -r "$filename" "+%Y%m%d%H%M%S")
	echo "$file_modified_date"
	mv -vn "$filename" "$file_modified_date"_versa."$file_ext"
done
