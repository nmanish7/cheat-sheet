# Regular Expression
---
	Bash globbing is a pattern matching feature that allows the user to match filenames and other strings using wildcards.

## Expression Table
Expression | Description
---|---
\*|Represent 0 or more characters (Any number of characters)
?|Represent only one character
[ ] | Represent range of character
{ } | Match exaclty Listed Occurrences

### Expression Range Example

Expression | Description
--- | ---
[abc]| a or b or c
[!abc] | Any character except ( a, b and c)
[a-z] | Any lowercase alphabet
[A-Z] | Any uppercase alphabet
[A-Za-z] | Any alphabet character either lowercase or uppercase
[0-9] | Any digit from 0 to 9
[A-Za-z0-9] | Any alpha numeric characters
[!A-Za-z0-9] | Special Symbols like (! @ # $ etc)


###  POSIX Character Example

	POSIX : Portable Operating System Interface 
	- [:digit:] is a POSIX character class, used inside a bracket expression like 
	[x-z[:digit:]]. The POSIX character class names must be written all lowercase.

Expression | Description
---|---
\[[:lower:]] | Any lowercase alphabet
\[[:upper:]]|Any uppercase alphabet
\[[:alpha:]] | Any alphabet
\[[:digit:]] | Any digit from 0 to 9
\[[:alnum:]] | Any alphanumeric character
\[![:digit:]] | Any character except digit

### Environment Example:

```shell
touch {a..d}{a..d} file_{a..d}.{txt,java,py}
mkdir subdirectory
touch subdirectory/file_a.txt subdirectory/file_b.txt subdirectory/file_m.py subdirectory/file_n.py
```


## Practice Questions
---
1. **To list out all file present in the current working directory.**
	
	```shell
	ls *
	```

1. **To list out all files with same extensions.**
	```shell
	ls *.py
	```


1.  **To list all file start with 'f'**
	```shell
	ls [f]*
	ls f*
	```

1. **To list out all file start with 'f' and end with 'y'.**
	```shell
	ls f*y
	ls [f]*[y]
	```

1. **To list out all file where filename content only two characters and first character should be 'f'.**

	```shell
	ls f?
	```

1. **To list out all files where filename content only two character**
	```shell
	ls ??
	```

1. **To list out all file where filename content at least three character.**
	```shell
	ls ???*
	```

1. **To list out all files where filename start with 'a' or 'b', 'c' or 'f'.**
	```shell
	ls [abcf]*
	```
1. **To list out all files where filename should not start with 'a' or 'f'.**
	```shell
	ls [!af]*
	```
1. **To list out all files where filename start with lowercase alphabet character**
	```shell
	ls [a-z]*
	ls [[:lower:]]*
	```
1. **To list out all files where filename start with digit.**
	```shell
	ls [0-9]*
	ls [[:digit:]]*
	```
1. **To list out all files where first letter should be uppercase second letter should be digit and third letter should be lowercase alphabet.**
	```shell
	ls [A-Z][0-9][a-z]*
	ls [[:upper:]][[:digit:]][[:lower:]]*
	```
1. **To list out all files start with special symbol**
	```shell
	ls [!A-Za-z0-9]*
	ls [![:alnum:]]*
	```
1. **To list out all files with '.txt' or '.java' **
	```shell
	ls *.{txt,java}
	```
1. **Remove all files with '.txt' or '.java' **
	```shell
	rm -f *.{txt,java}
	```
1. **Remove all file start with 'f' end with 't'**
	```shell
	rm -f f*[ta]
	```
1. **List all files that begin with lowercase alphabet and has a letter 'I' in third character position and end with either 't' or 'y'**
	```shell
	ls [a-z]?l*[ty]
	```