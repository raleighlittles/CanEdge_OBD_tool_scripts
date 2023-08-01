import re


# Steps to use:
# search for the UDS device identifier in the CSV file created from the raw (not extracted) transactions
# e.g. 241 157 for (0xF19D, ECU install date)
# Copy the rows containing those texts, into Google Sheets
# when pasting, right click, the "split text across columns" option
# then select the whole column containing each bracketed array, and paste it here

responses= """[ 31 112   0   0   0   0   0   0]
[ 4 65 60  2  8  0  0  0]
[  3 127  34  49   0   0   0   0]
[128 232  30 127 208   0  38   3]
[255 224   0  24   0  16 255 227]
[ 51 131  45   0   8 255 232   0]
[ 31 164  50 211  56   0  57  16]
[255   0   0   0   0  25  64 206]
[ 32  30  31 164   0   0   0 128]
[0 0 0 0 0 0 0 0]
[213 255   0   7 135 177  92   3]
[255  48 255   4 255 255   0   0]
[  0   1 207   0   0   0   0   0]
[64 64  0  0  0  0  0  0]
[101  70  84 170   0   0   0   0]
[  0   0   3 223 131 179 224   8]
[254  19  64   0  50   0   0   0]
"""

responses_filtered = re.sub(r'\W', " ", responses)

indiv_bytes = responses_filtered.split()

print(indiv_bytes)
print("----------")

bytes_as_ascii_str = ""

for b in indiv_bytes:
  bytes_as_ascii_str += chr(int(b))

print(bytes_as_ascii_str)