# Python - Password Hash
- This script was made to easy show how to hash strings and also the nesting way to make it more challanging to decrypt.

## Requirements
- [Windows](https://www.microsoft.com/en-us/p/windows-10-home/d76qx4bznwk4?rtc=1&activetab=pivot%3aoverviewtab)
- [Python 2/3](https://www.python.org/) installed
- CMD or Terminal/[Powershell](https://docs.microsoft.com/en-us/powershell/scripting/install/installing-powershell?view=powershell-7.1)/[Windows Powershell](https://docs.microsoft.com/en-us/windows/terminal/get-started)

## Instructions

1. Install dependencies.
2. Create the script.
3. Run and test.

### 1. Install dependencies.
- Navigate to folder location where the script will be held.  Here you can also navigate in your "File Explorer", right click, select "New" and click on "Text Document".  Rename the file anything you wish, but make sure to change the extention file to ".py".  In this tutorial we will call it "Password Hash.py".
```PowerShell
PS > CD '.\Documents\Python\Password Hash\'
```

- Install **hashlib**.  Hashlib is the Hash Library where the module implements a common use to many different secure hash and message digested algorithms.  More information found below:
	- [hashlib — Secure hashes and message digests](https://docs.python.org/3/library/hashlib.html)
```PowerShell
PS > pip install hashlib
```

- Install **getpass**.  Getpass prompts the user's input to not be echoed ( invisible ).  More information found below:
	-   [getpass — Portable password input](https://docs.python.org/3/library/getpass.html)
```PowerShell
PS > pip install getpass
```

- Install **pyperclip**.  Pyperclip is a cross-platform Python module for copy and paste clipboard functions compatihle with Python 2 and 3.  More information found below:
	-   [pyperclip 1.8.1](https://pypi.org/project/pyperclip/)
```PowerShell
PS > pip install pyperclip
```

### 2. Create the script.
1. Import all dependencies that were installed in the beginning.
```python
import hashlib #The hashing library
import getpass #To make the typing invisible
import pyperclip #To Copy the string
```

- Get the "string" that will not show any text being typed in PowerShell.  The "> " marker is just for aesthetics.
```python
string = getpass.getpass('> ')
```

- Here we are setting the variable "hash" being equal to the "string. encoded()" into the "hexidigest" from the "hashlib" library into a "sha256" variable.  Now note, you can change here the "256" into a "512" or anything supported to get a different result.  This example is to show how mulitple hash runs can produce many different results.
```python
hash = hashlib.sha256(string.encode()).hexdigest()
```

- You can disregard this next line of code if you like.  It's added to show an extra form of hashing for testing purposes.
```python
hash = hashlib.sha512(hash.encode()).hexdigest()
```

- This line copies the variable called "hash" into your clipboard.  You can print it to see, but not recommended as it's made to be anonymous.
```python
pyperclip.copy(hash)
```

- Let you know it's done.
```python
print('Done.')
```

- Full code.
```python
import hashlib #The hashing library
import getpass #To make the typing invisible
import pyperclip #To Copy the string


string = getpass.getpass('> ')
hash = hashlib.sha256(string.encode()).hexdigest()
hash = hashlib.sha512(hash.encode()).hexdigest()
pyperclip.copy(hash)
print('Done.')
```

### 3. Run and test.
- Always want to test it to make sure it's in working order.
```PowerShell
PS > py '.\Password Hash.py'
```