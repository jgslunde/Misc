git config --global user.name asdfbat
git config --global user.email jonas.s.lunde@outlook.com

ssh-keygen -t rsa -b 4096
ssh-add ~/.ssh/id_rsa

sudo apt install xclip
xclip -sel clip < ~/.ssh/id_rsa.pub