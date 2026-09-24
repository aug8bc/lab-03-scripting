#!/bin/bash
set -euo pipefail
curl https://s3.amazonaws.com/ds2002-resources/labs/lab3-bundle.tar.gz
tar -zxvf lab3-bundle.tar.gz
awk '!/^[[:space:]]*$/' myfile.tsv > cleaned.tsv
cat myfile.tsv | tr -s '\n' > cleaned.tsv
tr '/t' ',' < input.txt > output.csv
data_lines=$(($(wc -l < output.csv) -1))
echo "Remaining lines of data: $data_lines"
tar -czvf converted-archive.tar.gz output.csv
