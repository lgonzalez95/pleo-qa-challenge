echo 'Stage1'
jmeter -n -t file.jmx
echo 'Stage2'
newman -f file.json
echo 'Stach3'
mkdir results
cd results
echo 'no=results' >> results.json

