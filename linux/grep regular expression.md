# GREP Regular Expression

	Regular Expression: A regular expression is a sequence of characters that defines a pattern, used to search, match, and manipulate text data.

## CATEGRORY:
> Different types of patterns.
---

### Quantifier

 *Matches a certain number of occurrences of the preceding character or group.*

-   `*`: matches zero or more occurrences of the preceding character or group
-   `+`: matches one or more occurrences of the preceding character or group
-   `?`: matches zero or one occurrence of the preceding character or group
-   `{n}`: matches exactly n occurrences of the preceding character or group
-   `{n,}`: matches n or more occurrences of the preceding character or group
-   `{n,m}`: matches between n and m occurrences of the preceding character or group

### Wildcard

*Wildcard is a special characters that can match any character or set of characters.*
-   `.`: matches any single character

### Grouping and Ranges

*Groups characters together or creates a set of characters to match.*

-   `()`: groups characters together to create a subexpression
-   `[]`: creates a character set that matches any character in the set
-   `[^]`: creates a negated character set that matches any character not in the set
-   `-`: creates a range of characters within a character set

### Alternation

*Alternation is a regular expression feature that allows matching of either one pattern or another.*

 -   `|`: separates alternate expressions (matches either the left or right expression)

### Anchors
*An anchor in regular expressions is a character that matches a position instead of a character, such as the beginning or end of a line*

-   `^`: matches the beginning of a line
-   `$`: matches the end of a line


### Escape Characters

*An escape character is used to indicate that a special character should be treated as a literal character in a regular expression.*

 -   `\`: escapes special characters so they can be matched literally ( escape character, used to match a special character)


### Backreferences
*Backreferences are a feature in regular expressions that allow you to refer to a previously matched group within the pattern. This can be useful when you want to match something that is repeated later in the pattern, such as matching the same word twice in a row. By using a backreference, you can match the second occurrence of the word only if it is the same as the first occurrence. Backreferences are indicated using the \1, \2, etc. syntax, where the number corresponds to the order of the group in the pattern.*
-   `\1`, `\2`, etc.: matches the same text as previously matched by a capturing group

### POSIX
*Matches characters based on their POSIX character class.*
-   `[:alnum:]`: matches any alphanumeric character
-   `[:alpha:]`: matches any alphabetic character
-   `[:blank:]`: matches any whitespace character that is not a newline
-   `[:digit:]`: matches any digit character
-   `[:lower:]`: matches any lowercase alphabetic character
-   `[:punct:]`: matches any punctuation character
-   `[:space:]`: matches any whitespace character including newline
-   `[:upper:]`: matches any uppercase alphabetic character
-   `[:xdigit:]`: matches any hexadecimal digit character

### Character Classes
*Matches characters based on character class.*
-    `\b` : word boundary, matches the boundary between a word character and a non-word character
-   `\d` : digit character, equivalent to [0-9]
-   `\D` : non-digit character, equivalent to  \[^0-9]
-   `\w` : word character, equivalent to [a-zA-Z0-9_]
-   `\W` : non-word character, equivalent to \[^a-zA-Z0-9_]
-   `\s` : whitespace character, equivalent to \[\\t\\n\\r\\f\\v]
-   `\S` : non-whitespace character, equivalent to \[^\\t\\n\\r\\f\\v]

## Regular Expression Example
---
Expression | Description
---|---
\*| Zero or more occurrence of the previous character.
g*|g, gg, ggg
.| Single character (any character) without blank line
.* | Any number of character with blank line
\\+|One or more occurrence of the previous character
\\? | Zero or one occurrence of the previous character
\[^pqr] | A single character which is not 'p' or 'q' or 'r'
\[^a-zA-Z] | A non alphabetical character
\[^a-zA-Z0-9] | Special Characters
\^pat | Pattern 'pat' at the beginning of the line.
pat$ | Pattern 'pat' at the end of the line.
\^pat$ | Pattern 'pat' is the only word in the line.
\^$ | Empty line
<|Word begin with
\> | Word end with

## Regular Expression Exercise

> **Files**

- [Sample File 1](./data/Sample-1.txt)
- [Sample File 2](./data/Sample-2.txt)
---

***Follow Sample File 1***
1. To search for every line that contains the word ‘GNU’
	```shell
	grep -w 'GNU' sample1
	```
1. Search for each instance of the word ‘license’ (with upper, lower, or mixed cases)
	```shell
	grep -iw 'license' sample1
	```
2. Search for every line that does not contain the word ‘the’ and also specify the line No. 
	```shell
	grep -vn 'the' sample1
	```
5. Find lines where ‘GNU’ occurs at the very beginning of a line.
	```shell
	grep ^GNU sample1
	```
1. Match every line ending with the word ‘and’.
	```shell
	grep -w 'and$' sample1
	```
1. To match anything in the sample-1 file that has two characters and then the string ‘cept’.
	```shell
	grep ..cept sample1
	```
1. To find the lines that contain ‘too’ or ‘two’
	```shell
	grep -E 'too|two' sample1
	```
1. To find any line that begins with a capital letter and ends with a period.
	```shell
	grep '^[[:upper:]].*\.$' sample1
	```
1. Matches the string free plus one or more characters that are not white space characters.
	```shell
	grep 'free[[:alpha:]][[:alpha:]]*' sample1
	```
1. To find all of the lines in the sample-2 file that contain triple-vowels.
	```shell
	grep '[aeiou]\{3\}' sample1
	```
1. To match any words that have between 16 and 20 characters.
	```shell
	grep -w '\w\{16,20\}' sample1
	```
1. Find all patterns that has at least one but no more than 3, ‘a’
	```shell
	grep 'a\{1,3\}' sample1
	```

---
***Follow Sample File 2***

13. Print all lines that contain a phone number with an extension (the letter x or X followed by four digits).
	```shell
	grep -w 'x[[:digit:]]\{4\}' sample2
	```
1. Print all lines that contain a date. Hint: this is a very simple pattern. It does not have to work for any year before 2000.
	```shell
	grep '[[:alpha:]]\{3\}\.[[:blank:]]\+[[:digit:]]\{1,2\},[[:blank:]]\+[[:digit:]]\{4\}' sample2
	```
15. Print all lines containing a vowel (a, e, i, o, or u) followed by a single character followed by the same vowel again. Thus, it will find “eve” or “adam” but not “vera”. 
	```shell
	grep -E '([aeiou]).\1' sample2
	```
17. Print all lines that do not begin with a capital S.
	```shell
	grep '^[^S]' sample2
	```
19. Print all lines that contain CA in either uppercase or lowercase.
	```shell
	grep -i 'ca' sample2
	```
21. Print all lines that contain an email address (they have an @ in them.
	```shell
	grep '@' sample2
	```
1. Print all lines that do not contain the word ‘Sep.’ (including the period)
	```shell
	grep -wv 'Sep.' sample2
	```
1. Print all lines that contain the word ‘de’ as a whole word.
	```shell
	grep '\<de\>' sample2
	```
1. Find all subdirectories within a directory
	```shell
	ll -R <directory> | grep '^d' | grep -E '\w+$'
	ll -R <directory> | grep '^d' | grep -Eo '\w+$'
	```
1. List all files in the default directory that others can read or write
	```shell
	ll -l <directory> | grep '\S\{7\}rw-'
	```