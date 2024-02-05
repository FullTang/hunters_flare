tasklist /FO CSV /NH > Tasks.csv
python ./levenshteinTasks.py
chcp 65001
dir /B /S "C:/" > directoryListing.txt
chcp 1252
python ./ps1Files.py