#!/bin/bash
Files="*.txt"
p=0
for i in $Files;
do
name=$i
echo $name
base=${name%.txt}
q=$p+1
sed -e :a -e N -e 's/\n/ /' -e ta $name >$base.$q."txt"
sed -i 's/ References.*,/,/'  $base.$q."txt"
sed -i 's/ Acknowledgments.*,/,/' $base.$q."txt"
sed -e 's/\(Abstract.*\)/\x03&/' -e 's/.*\x03//' $base.$q."txt">$base.$q.$p."txt"
#conv -c -f utf-8 -t ascii chec.txt>$base.$q.$p.".txt"
sed -i 's/([^()]*)//g' $base.$q.$p."txt"
sed -i 's/([^{}]*)//g' $base.$q.$p."txt"
sed -i 's/Table//g' $base.$q.$p."txt"
sed -i 's/Figure//g' $base.$q.$p."txt"
sed -i 's/[0-9]//g' $base.$q.$p."txt"
sed -i 's/`//g' $base.$q.$p."txt"
sed -i 's/#//g' $base.$q.$p."txt"
sed -i 's/%//g' $base.$q.$p."txt"
sed -i 's/~//g' $base.$q.$p."txt"
sed -i 's/- //g' $base.$q.$p."txt"
sed -i  's/,//g' $base.$q.$p."txt"
sed -i 's/+//g' $base.$q.$p."txt"
sed -i 's/=//g' $base.$q.$p."txt"
sed -i 's/;//g' $base.$q.$p."txt"
sed -i 's/([^[]]*)//g' $base.$q.$p."txt"
sed -i 's/〈//g' $base.$q.$p."txt"
sed -i 's/〉//g' $base.$q.$p."txt"
sed -i 's/?//g' $base.$q.$p."txt"
sed -i 's/://g' $base.$q.$p."txt"
sed -i 's/\///g' $base.$q.$p."txt"
sed -i 's/<//g' $base.$q.$p."txt"
sed -i 's/>//g' $base.$q.$p."txt"
sed -i 's/≤//g' $base.$q.$p."txt"
sed -i 's/,//g' $base.$q.$p."txt"
sed -e 's/[^[:alpha:]]/ /g' $base.$q.$p."txt" | tr '\n' " " |  tr -s " " | tr " " '\n'| tr 'A-Z' 'a-z' | sort | uniq -c | sort -nr | nl>"dict".$base.$q.$p."txt" 
done
