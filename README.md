# Hunter's Flare - Python3

This uses the Damerau–Levenshtein distance to calculate the difference between a running task in Windows and a list of known good tasks and returns all hits with a distance of one. The Damerau–Levenshtein distance is a number representing how different two strings are. Each insertion, deletion, replacement, and transposition adds one the the number. Two strings with a difference of one only require one modification to change from one string to the other.

## Use

This can reveal a stealthy task that has been given a name that is very similar to a known good task to remain hidden and avoid detection. 
- HuntersFlare.exe is a standalone version for use on any Windows system.
- DamerauLevenshteinTasks.py is the source code.

## Detection Examples

- lsass.exe   vs lsasss.exe  *Insertion*
- spoolsv.exe vs spolsv.exe  *Deletion*
- hasplmv.exe vs hasplnv.exe  *Replacement*
- svchost.exe vs svhcost.exe  *Transposition*
