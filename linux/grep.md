
## GREP
> It is a Linux command that searches for patterns in files or input and prints matching lines.

Command | Full Form
---|---
GREP| Global Regular Expression
EGREP|Extended Global Regular Expression
FSGREP | Fixed String Global Regular Expression Print


### GREP Options
---
****
Option| Description |Example
---|---|---
-i|	Perform a case-insensitive search | grep -i "hello" file.txt
-v|	Invert the search, returning lines that do not match | grep -v "hello" file.txt
-n|	Display the line number of each match | grep -n "hello" file.txt
-c|	Count the number of matches | grep -c "hello" file.txt
-e|	Search for multiple patterns at once | grep -e "hello" -e "world" file.txt
-l|	Display only the names of the files that contain matches | grep -l "hello" \*.txt
-w  | Match only whole words, not partial matches  |  grep -w "hello" file.txt
-B  |	Display n lines before each match | grep -B 3 "hello" file.txt
-A  |	Display n lines after each match | grep -A 3 "hello" file.txt
-C  |	Display n lines before and after each match | grep -C 3 "hello" file.txt
-f  |	Read the search patterns from a file | grep -f patterns.txt file.txt


### Practice text

> **file.txt**
```text
Hello world!
This is a test file for the grep command.
The command can be used to search for specific patterns in text files.
I like to eat apples and bananas.
Do you like cherries?
Or do you prefer strawberries?
The -i option makes the search case-insensitive.
The -v option returns all lines that do not match the pattern.
The -n option shows the line numbers of matching lines.
The -c option counts the number of matching lines.
The -e option allows multiple patterns to be searched for.
The -l option lists only the names of files that contain the pattern.
The -w option matches only whole words, not partial matches.
The -B option shows n lines before the matching line.
The -A option shows n lines after the matching line.
The -C option shows n lines before and after the matching line.
```
> **patterns.txt**

```text
apple
banana
cherry
```