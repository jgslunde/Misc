read -p 'Would you like to install Google Chrome? (y/n) ' var
if [ $var = 'y' ]
	then
	read -p 'please go to https://www.google.com/chrome/browser/desktop/ and download the .deb file to your download folder. Press enter when you are finished.'
	sudo dpkg -i ~/Downloads/google-chrome-stable_current_amd64.deb
	fi


read -p 'Would you like to activate "minimize window on click"? (y/n) ' var2
if [ $var2 = 'y' ]
	then
	gsettings set org.compiz.unityshell:/org/compiz/profiles/unity/plugins/unityshell/ launcher-minimize-window true
	fi


read -p 'Would you like to install/update pip? (y/n) ' var3
if [ $var3 = 'y' ]
	then
	sudo -H apt-get install python-pip python-dev build-essential
	sudo -H pip install --upgrade pip
	sudo -H pip install --upgrade virtualenv
	fi


read -p 'Would you like to install dropbox? (y/n) ' var4
if [ $var4 = 'y' ]
	then
	sudo -H apt-get install nautilus-dropbox
	fi


read -p 'Would you like to install lots of Python 2.7 packages? (y/n) ' var5
if [ $var5 = 'y' ]
	then
	sudo -H apt-get install python-setuptools python-pip mercurial
	sudo -H pip install numpy sympy scipy nose pytest
	sudo -H pip install ipython --upgrade
	fi


read -p 'Would you like to install Atom? (y/n)' var 7
if [ $var7 = 'y' ]
	then
	read -p 'please navigate to https://atom.io/ and download the .deb file to your Downloads folder. Press enter when done'
	sudo ~/Downloads/dpkg -i atom-amd64.deb
	sudo apt-get -f install

read -p 'Would you like to install TexLive full? (y/n) ' var6
if [ $var6 = 'y' ]
	then
	sudo -H apt-get install texlive-full
	fi


read -p 'Would you like to install spell check and syntax highlighting for Latex in Atom?' var8
if [ $var = 'y' ]
	then
	sudo apm install linter-spell
	sudo apm install linter-spell-latex
	sudo apm install language-latex

# Fixing broken packages:
#sudo apt-get clean
#sudo apt-get update
#sudo dpkg --configure -a
#sudo apt-get install -f
