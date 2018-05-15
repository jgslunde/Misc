sudo apt-get update
sudo apt-get upgrade

declare -A installs

echo "Insert chosen installs (Numbers/letters with spaces in between.)"
echo ""
echo "1) __SUBLIME (All below)__"
echo "1a Only Install Sublime"
echo "1b Only Load Custom Sublime Macros"
echo ""
echo "2)  Install Ranger File Viwer"
echo ""
echo "3)  Install/Update pip & pip3"
echo ""
echo "4)  Install/Update lots of Python packages"
echo ""
echo "5)  Set up ap2 and ap3 runfiles"
echo ""
echo "6) __Setup GitHub__"
echo "6a Install GitHub"
echo "6b Setup GitHub username and email"
echo "6c Setup SSH-keys (just press enter when promted for path or password)"
echo ""
echo "7) Setup aliases p and p2 for Python3 and Python2"
echo ""
echo "99)  __Install TexLive (Full, 5GB)__"
echo "99a: Core only"
echo ""

read -a chosen_installs

for install in ${chosen_installs[*]}
do
    installs[$install]=true
done





if [ ${installs["1a"]} ] || [ ${installs["1"]} ]
then
    sudo wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-key add -
    sudo apt-get install apt-transport-https
    echo "deb https://download.sublimetext.com/ apt/stable/" | sudo tee /etc/apt/sources.list.d/    sublime-text.list
    echo "deb https://download.sublimetext.com/ apt/dev/" | sudo tee /etc/apt/sources.list.d/sublime-text.list
    sudo apt-get update
    sudo apt-get install sublime-text
fi



if [ ${installs["1b"]} ] || [ ${installs["1"]} ]
then
    if [ ! -d ~/.config/sublime-text-3/Packages/User/ ]
    then
        mkdir -p ~/.config/sublime-text-3/Packages/User/
    fi
    sudo wget 'https://raw.githubusercontent.com/asdfbat/Misc/master/sublime/Default%20(Linux).sublime-keymap'
    sudo mv 'Default (Linux).sublime-keymap' ~/.config/sublime-text-3/Packages/User/
    sudo wget 'https://raw.githubusercontent.com/asdfbat/Misc/master/sublime/Preferences.sublime-settings'
    sudo mv 'Preferences.sublime-settings' ~/.config/sublime-text-3/Packages/User/
fi



if [ ${installs["2"]} ]
then
    sudo apt-get install ranger
fi



if [ ${installs["3"]} ]
then
    sudo -H apt-get install python-pip
    sudo -H apt-get install python3-pip
    sudo -H pip install --upgrade pip
    sudo -H pip3 install --upgrade pip
fi



if [ ${installs["4"]} ]
then
    sudo -H pip install numpy sympy scipy pytest seaborn numba --upgrade
    sudo -H pip install matplotlib line_profiler --upgrade
    sudo -H pip3 install numpy sympy scipy pytest seaborn numba --upgrade
    sudo -H pip3 install matplotlib line_profiler --upgrade
fi



if [ ${installs["5"]} ]
then
    sudo wget -O ~/runpy3.sh 'https://raw.githubusercontent.com/asdfbat/Misc/master/runpy3.sh'
    sudo ln -s ~/runpy3.sh /usr/bin/ap3
    sudo chmod 777 /usr/bin/ap3
    sudo wget -O ~/runpy2.sh 'https://raw.githubusercontent.com/asdfbat/Misc/master/runpy2.sh'
    sudo ln -s ~/runpy2.sh /usr/bin/ap2
    sudo chmod 777 /usr/bin/ap2
fi



if [ ${installs["6a"]} ] || [ ${installs["6"]} ]
then
    sudo -H apt-get install git
fi



if [ ${installs["6b"]} ] || [ ${installs["6"]} ]
then
    read -p 'Please insert your GitHub username ' github_name
    read -p 'Please insert your GitHub email ' github_email
    git config --global user.name $github_name
    git config --global user.email $github_email
fi



if [ ${installs["6c"]} ] || [ ${installs["6"]} ]
then
    if [ ! -f ~/.ssh/id_rsa ]   # if SSH doesn't already exists.
    then
        ssh-keygen -t rsa -b 4096
        eval "$(ssh-agent -s)"
        ssh-add ~/.ssh/id_rsa
    fi
    sudo apt-get install xclip
    xclip -sel clip < ~/.ssh/id_rsa.pub
    echo ""
    echo "#########################################################"
    echo "##      Your SSH-key is copied to your clipboard.      ##"
    echo "## Please navigate to https://github.com/settings/keys ##"
    echo "##        and paste the key under 'new SSH-key'.       ##"
    echo "##               Press enter to proceed...             ##"
    read -p "#########################################################"
fi



if [ ${installs["7"]} ]
then
    echo "alias p='python3'" >> ~/.bashrc
    echo "alias p2='python2'" >> ~/.bashrc
    . ~/.bashrc
fi



if [ ${installs["99"]} ]
then
    sudo -H apt-get install texlive-full
fi



if [ ${installs["99a)"]} ]
then
    sudo -H apt-get install texlive-core
fi
