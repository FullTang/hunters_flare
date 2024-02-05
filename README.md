This uses the Damerau–Levenshtein distance to calculate the difference between a running task in Windows and a list of known good tasks and returns all hits with a distance of one. The Damerau–Levenshtein is a number representing how different two strings are. Each insertion, deletion, replacement, and transposition adds one the the number. Two strings with a difference of one only require one modification to change from one string to the other.

The Python script can reveal a stealthy task that has been given a name that is very similar to a known good task in order to remain hidden and avoid detection. Use the batch file in the same directory as the python script to save a list of the running tasks to disk and open the output text file for the results.

Examples: svchost.exe vs svhcost.exe
          nssm_64.exe vs nssn_64.exe
          hasplmv.exe vs hasplmu.exe

