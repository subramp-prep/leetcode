# Read from the file file.txt and print its transposed content to stdout.
col=`head -1 file.txt|awk '{print NF}'`
for((i=1;i<=$col;i++)) {
	awk '{print $($i) }' file.txt | tr '\n' ' ' 
	echo ''
}

