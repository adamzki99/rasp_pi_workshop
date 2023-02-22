#!/bin/bash

if [ $(basename $PWD) = "rasp_pi_workshop" ]; then
    cd prep
elif [ $(basename $PWD) = "prep" ]; then
    :
else
    echo "Please run this script from the rasp_pi_workshop directory"
    exit 1
fi

Test_Code="code4tests.txt" # code4tests.txt is the file containing the test code
Main_Line=$(($( grep -n "def main()" ../main.py | cut -d: -f1 )-1)) # get the line number of the main function
Timer="60s" # time limit for the test (will force the test to stop after 60 seconds)

rm -rf tmp # remove the temporary directory if it exists
mkdir tmp # create a temporary directory
mv ../main.py tmp # copy the main.py file to the temporary directory
cd tmp
split main.py a -l $Main_Line -d # split the main.py file into two files
tail -n +2 "a01" > "a01.tmp" && mv "a01.tmp" "a01" # remove the first line of the second file
cd ..
cat tmp/a00 >> ../main.py
cat $Test_Code >> ../main.py # add the test code to the main.py file
cat tmp/a01 >> ../main.py
timeout $Timer python3 ../main.py # run the main.py file with a time limit
rm ../main.py # remove the main.py file
mv tmp/main.py ../main.py # move the main.py file back to the root directory
rm -rf tmp # remove the temporary directory