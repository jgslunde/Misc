# Running and connecting to a remote Jupyter server
This guide demonstrates how to
1. Set up SSH keys to connect password-less to ITA resources.
2. Run a jupyter server on the ITA compute resources (beehive, owl, euclid, or your own stjerne computer). 
3. Remotely connect to this notebook from your personal computer.

Replace instances of [username] with your username, and [beehive] with whatever system you want to run your notebook on (like beehive20 or stjerne18). Remember to remove the [] brackets.

Step -1 only needs to be done once. It's also only for convenience, and can be skipped.\
Step 0 only needs to be done once.\
Step 1 needs to be done every time you want to start a new jupyter server.\
Step 2 needs to be done every time you wish to connect to a running jupyter notebook.



# -1. Setting up SSH key
If you complete the following section, you won't have to input your password when remotely accessing any of the ITA resources through SSH. This includes both starting and connecting to a jupyter server.

## Creating private-public key pair
If you already have a key-pair, skip this step.\
On your local machine, execute
```
ssh-keygen -t rsa
```
Use the default location, and insert a passphrase if you want. If you don't anyone with access to the private SSH key on your computer may access your UiO files and resources.

## Placing your public key on the ITA system
Your **public** key will now lie in `~/.ssh/id_rsa.pub`. Copy the entire content of the file.

Navigate into the ITA systems, e.g. by SSH:
```
ssh [username]@login.astro.uio.no
```
Open or create the file `~/.ssh/authorized_keys`, and paste your public key into a new line.

Finally, remove execution permission from the file by running the following command (while SSHed into your ITA system)
```
chmod 600 ~/.ssh/authorized_keys
```

# 0. Setup if you are outside eduroam
If you are outside the UiO eduroam network, you can't access the ITA systems (like the beehives), and will have to access through @login.astro.uio.no. With the following setup, this will happen automatically.

On your own computer, insert the following into the file `~/.ssh/config`. Create the file if it does not exist.
```
Host beehive* owl* euclid* stjerne*
    ForwardX11 yes
    User [username]
    ProxyCommand ssh -XYC [username]@login.astro.uio.no -W %h:%p
```

Finally, remove execution permission from the file by running the following command
```
chmod 600 ~/.ssh/config
```

# 1. Starting jupyter notebook
We're gonna run a jupyter notebook on a remote ITA computer, using "screen". Screen is a program which allows you to start terminals which don't shut down simply if you exit your terminal, shut down you computer, or lose internet connection.

SSH into an some remote computer
```
ssh [username]@[beehive].uio.no
```
This should work after performing step 0. If it does not, you can split the process into two:
```
ssh [username]@login.astro.uio.no
ssh [beehive]
```

Start a screen
```
screen
```

Start a jupyter notebook server on some port.
```
jupyter-notebook --port=8887 --no-browser
```

In the terminal there pops up a link that looks something like this `http://localhost:8887/?token=db9778d93010499994a82f231b1e897b383529d9e6a0c315`. Copy and save the bit after "token=". This is a sort of password for your jupyter server, and you will probably need it the first time you connect to it.

De-attach from the screen by pressing ctrl+a+d. The screen terminal will now run by itself on the owl. After you've attached from the screen, you can safely close your terminal window. You can always re-attach to the screened session with
```
screen -r
```
Just remember to SSH into the correct computer first.


# 2. Forward port from login to your computer
Finally we forward the 8887 port on the ITA login to the 8889 port on your computer.
```
ssh -N -L localhost:8889:localhost:8887 [username]@login.astro.uio.no
```
This terminal will need to stay open while your use your notebook. You can whenever you want close it and rerun the command, and should be back where you left. If you've done everything correctly, this should be everything you need to do next time you want to connect to your jupyter server.

Go to `http://localhost:8889` to access your notebook. The first time you connect to a new server, you probably need to insert the token you copied into the top right corner.

# Final notes
* Remember that even if you close the terminal in step 2, your jupyter server is still running on your detached screen. If one of your notebooks are consuming large amounts of memory, it would be polite to shut it down if you don't intend to use it for a few hours/days. You can check the memory usage of your notebook by SSHing into the [beehive] where the jupter is running, and using the command `htop`.