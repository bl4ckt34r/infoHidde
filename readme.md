# infoHidde

---

## What is infoHidde

infoHidde is a tool, thats provide a very simple level of encryption, for hidde
information of users with low knowledge about computers or cybersecurity, it's
util to hidde information, with a cesar encryption method, this method provide
a simple encryption, only for hidde information, is not recomended for secure
information, because use a low level of encryption, there are safer methods.

## Download and use infoHidde

Execute the next command to create a new directory and change to this path:

    > $ mkdir ~/Downloads/git
    > $ cd ~/Downloads/git

For download this tools only need clone this repositorie, with the next command:
    
    > $ git clone https://github.com/bl4ckt34r/infoHidde.git

And move to the new directory with:
    
    > $ cd infoHidde

After this commands, you can execute this tool with two ways, you can execute
directly the python file, named `infoHidde.py`, with the next command:

    > $ python3 ./infoHidde.py

Or can execute the file `install.sh`, you need assign execution permissions for 
this file with the next command:

    > $ sudo chmod +x install.sh

Now you can execute the next command, to install the tool:

    > $ ./install.sh

This file will do add an alias in your shell configuration, after execute this 
file, you can call the tool from any path in your system.
If you decide, you can make a new form of execute the tool, or can add the alias
manually in your shell configuration. The script only works in bash and zsh
at the moment.

## Use the tool

1. At the moment of execution, at the first time, you need select, what do you
want to do with the tool, you can encrypt and decrypt data.

2. At the next step you need to say to the tool, where is your file, this tool
only works with text files (.txt), you can use the absolute path or use a
relative path, only can use the signs ~ and . for the relative path.

3. If you select the option of encrypt, you can tell the number of displace the
characters, for the encryption, for each line in your file, after the last line
your data are encrypted, now you can use the option to decrypt, when you need. 
Else you select the decrypt option, only need wait for the end of the proces.

Note: The modified data, overwrite the original data, please use this tool with
caution, and don't encrypt file of the system, and use only text files.
__**THIS TOOL DELETE THE ORIGINAL DATA AND WRITE THE NEW ENCRYPTED OR DECRYPTED DATA**__

TOOLS CREATED BY: BL4CKT34R
