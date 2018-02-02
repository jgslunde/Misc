sudo apt-get update
sudo apt-get upgrade
sudo apt-get install git


read -p 'Would you like to install Gnome Tweak Tool? (y/n) ' var10
if [ $var10 = 'y' ]
	then
	sudo apt-get install gnome-tweak-tool
	fi

read -p 'Would you like to install Google Chrome? (y/n) ' var
if [ $var = 'y' ]
	then
	read -p 'please go to https://www.google.com/chrome/browser/desktop/ and download the .deb file to your download folder. Press enter when you are finished.'
	sudo dpkg -i ~/Downloads/google-chrome-stable_current_amd64.deb
	fi


read -p 'Would you like to install Sublime? (y/n) ' var14
if [ $var14 = 'y' ]
	then
	sudo wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-key add -
	sudo apt-get install apt-transport-https
	echo "deb https://download.sublimetext.com/ apt/stable/" | sudo tee /etc/apt/sources.list.d/	sublime-text.list
	echo "deb https://download.sublimetext.com/ apt/dev/" | sudo tee /etc/apt/sources.list.d/sublime-text.list
	sudo apt-get update
	sudo apt-get install sublime-text
	fi

read -p 'Would you like to load custom Sublime macros? (y/n) ' var15
if [ $var15 = 'y' ]
	then
	sudo wget 'https://raw.githubusercontent.com/asdfbat/Misc/master/sublime/Default%20(Linux).sublime-keymap'
	sudo mv 'Default (Linux).sublime-keymap' ~/.config/sublime-text-3/Packages/User/
	fi



read -p 'Would you like to install Ranger file viewer? (y/n) ' var12
if [ $var12 = 'y' ]
	then
	sudo apt-get install ranger
	fi

#read -p 'Would you like to activate "minimize window on click"? (y/n) ' var2
#if [ $var2 = 'y' ]
#	then
#	gsettings set org.compiz.unityshell:/org/compiz/profiles/unity/plugins/unityshell/ #launcher-minimize-window true
#	fi


read -p 'Would you like to install/update pip? (y/n) ' var3
if [ $var3 = 'y' ]
	then
	sudo -H apt-get install python-pip
	sudo -H apt-get install python3-pip
	sudo -H pip install --upgrade pip
	sudo -H pip3 install --upgrade pip
	sudo -H pip install --upgrade virtualenv
	fi


read -p 'Would you like to install dropbox? (y/n) ' var4
if [ $var4 = 'y' ]
	then
	sudo -H apt-get install nautilus-dropbox
	fi


read -p 'Would you like to install lots of Python packages? (y/n) ' var5
if [ $var5 = 'y' ]
	then
	sudo -H install python-pip
	sudo -H apt-get install python-setuptools python-pip mercurial
	sudo -H pip install numpy sympy scipy nose pytest
	sudo -H pip install ipython --upgrade
	sudo -H pip install seaborn
	sudo -H pip install numba
	sudo -H pip install cPython
	sudo -H pip install line_profiler

	sudo -H install python3-pip
	sudo -H pip3 install matplotlib
	sudo -H pip3 install seaborn
	sudo -H apt-get install python3-tk
	sudo -H pip3 install numba
	sudo -H pip3 install sympy
	sudo -H pip3 install pytest
	sudo -H pip3 install cPython
	sudo -H pip3 install line_profiler
	fi


read -p 'Would you like to install Atom? (y/n) ' var7
if [ $var7 = 'y' ]
	then
	read -p 'please navigate to https://atom.io/ and download the .deb file to your Downloads folder. Press enter when done'
	sudo dpkg -i ~/Downloads/atom-amd64.deb
	sudo apt-get -f install
	fi

read -p 'Would you like to install spell check and syntax highlighting for Latex in Atom? (y/n) ' var8
if [ $var8 = 'y' ]
	then
	sudo apm install linter-spell
	sudo apm install linter-spell-latex
	sudo apm install language-latex
	fi


read -p 'Add command ap2 and ap3 for running all python files in a folder? (Will create files allepy3.sh and allepy2.sh in home directory) (y/n) ' var9
if [ $var9 = 'y' ]
	then
	sudo wget -O ~/runpy3.sh 'https://raw.githubusercontent.com/asdfbat/Misc/master/runpy3.sh'
	sudo ln -s ~/runpy3.sh /usr/bin/ap3
	sudo chmod 777 /usr/bin/ap3
	sudo wget -O ~/runpy2.sh 'https://raw.githubusercontent.com/asdfbat/Misc/master/runpy2.sh'
	sudo ln -s ~/runpy2.sh /usr/bin/ap2
	sudo chmod 777 /usr/bin/ap2
	fi


read -p 'Would you like to install TexLive full? (y/n) ' var6
if [ $var6 = 'y' ]
	then
	sudo -H apt-get install texlive-full
	fi


# Fixing broken packages:
#sudo apt-get clean
#sudo apt-get update
#sudo dpkg --configure -a
#sudo apt-get install -f
