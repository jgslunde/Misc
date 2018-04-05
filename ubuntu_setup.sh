
declare -A installs

echo "Insert chosen installs"
echo ""
echo "1)  __SUBLIME__"
echo "1a Install Sublime"
echo "1b Load Custom Sublime Macros"
echo ""
echo "2)  Install Ranger File Viwer"
echo ""
echo "3)  Install/Update pip & pip3"
echo ""
echo "4)  Install/Update lots of Python packages"
echo ""
echo "5)  Set up ap2 and ap3 runfiles"
echo ""
echo "6)  __Install TexLive (Full)__"
echo "6a: Core only"
echo ""

read -a chosen_installs


for install in ${chosen_installs[*]}
    do
        installs[$install]=true
    done



sudo apt-get update
sudo apt-get upgrade



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



if [ ${installs["6"]} ]
    then
        sudo -H apt-get install texlive-full
    fi



if [ ${installs["6a)"]} ]
    then
        sudo -H apt-get install texlive-core
    fi
