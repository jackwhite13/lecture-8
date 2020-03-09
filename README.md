# Lecture 8 - CYBR 2980

FileIO
## Objectives
- Strings and text files
- Manipulating files and directories, os and sys modules
- Text files: reading/writing text and numbers from/to a file
- Creating and reading a formatted file (csv or tab-separated)


### Opening & Closing Files
| Method | Use | Purpose |
| --- | --- | --- |
| open | open(filename, 'r') | Open a file called ***filename*** and use it for reading. This will return a reference to a file object. |
| open | open(filename, 'w') | Open a file called ***filename*** and use it for writing. This will return a reference to a file object. |
| close | fileVariable.close() | File use is complete. |

Files must be in the same folder as the python file you are running. If there is a path to the file, that must be included in the filename.

### os module
Part of writing to files is knowing what folder your code is running within. The **os** module is useful for this. There is far more to this module than we will cover, for more info check out the [os module python docs](https://docs.python.org/3/library/os.html)

A useful tool is to get the current working directory (CWD).
```
import os

print(os.getcwd())
```

This can be appended to the file name for the full file path if needed.
 
### Reading from a file
```
myFile = open("qbdata.txt", 'r')

for line in myFile:
  print(line)
```

In this example, you will iterate across every line. This is anything denoted by the **\n** character.

If we want to break the data down further, we would have to split the lines by some value.

```
for line in myFile:
  info = line.split()
  print(info[0], info[1], "had a rating of", info[10])
```

### Writing to a file
If your program has collected data that needs to be saved (like email addresses scraped from a web page) then we will need to be able to write to a file.

To write to a file, when we open it, we need to use a **w** as the second parameter.
```
import random

outFile = open("dice_rolls.txt", 'w')

die1 = random.randint(1,6)
die2 = random.randint(1,6)
total = die1 + die2

output = str(die1) + " " + str(die2) + " " + str(total)
outFile.write(output)

outFile.close()

```

- What does this datafile look like after we have written it?
- What happens when we run the code again?
- What happens if we loop the process?


### Examining a dataset
[Johns Hopkins COVID-19 Dataset](https://github.com/CSSEGISandData/COVID-19)
- Can you print all the data?
- Can you isolate one country?
- Can you find the sum total of cases by place?
- Are there any data anomalies you would need to consider?
