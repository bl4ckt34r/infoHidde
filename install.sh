#!/bin/bash

echo "Hello" $USER "you are adding alias for infoHidde in your shell configuration"

if [ -f "/home/$USER/.zshrc_test" -o -f "/root/.zshrc_test" ]; then
    USRSHELL=".zshrc_test"
    SHELLNAME="zsh"
elif [ -f "~/.bashrc_test" -o -f "/root/.bashrc_test" ]; then
    USRSHELL=".bashrc_test"
    SHELLNAME="bash"
else
    echo "You are using an invalid shell for this script"
fi

echo $USRSHELL

if [ "$USER" != "root" ]; then
    {
        echo "alias infoHidde='python3 /home/$USER/Downloads/git/infoHidde/infoHidde.py'" >> /home/$USER/$USRSHELL
    }
else
    echo "alias infoHidde='python /root/$USER/Downloads/git/infoHidde/infoHidde.py'" >> /root/$USRSHELL
fi

echo "Script is end the taks, now have an alias 'infoHidde' in your $SHELLNAME shell"
