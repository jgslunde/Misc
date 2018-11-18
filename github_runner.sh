cd ..
for directory in */
do
    echo
    echo
    echo "################### ENTERING $directory ###################"
    cd $directory
    git status
    echo "####################################################################"
    echo
    cd ..
done