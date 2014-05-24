#!/bin/sh

# Verify user wants to proceed
# http://stackoverflow.com/questions/1885525/how-do-i-prompt-a-user-for-confirmation-in-bash-script
read -p "Initiate setup [y/N]?" -n 1 -r
if [[ ! $REPLY =~ ^[Yy]$ ]]
then
    exit 1
fi

# Get sudo privileges at the beginning
sudo echo


# Identify the operating system
platform='unknown'
unamestr=`uname`

if [[ "$unamestr" == 'Linux' ]]; then
	platform='linux'
elif [[ "$unamestr" == 'Darwin' ]]; then
	platform='osx'
fi
echo "You are running $platform"

echo "Installing pip..."
if [[ $platform == 'linux' ]]; then
	apt-get install python-pip
elif [[ $platform == 'osx' ]]; then
	sudo easy_install pip
fi
echo "Pip installation complete"


# Setting up virtualenv
cd ..
virtualenv dotasite
echo "Virtualenv setup"
cd dotasite


# Install pip requirements
source bin/activate
pip install -r requirements.txt


echo "Setup script has completed"
