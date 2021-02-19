# Intro
You can't directly SSH into the beehives/owls from outside the UiO network. Everything therefore needs to be routed through login.astro.uio.no.

As an additional note: Most of this stuff only needs to be done "once". You can shut down your computer and quickly get back up and running on your notebook. However, if you wish to shut down the notebook entirely, you'll have to redo this.

# 1. Starting jupyter notebook
We're gonna run a jupyter notebook on an owl, using "screen". Screen is a program which allows you to start terminals which don't shut down simply if you exit your terminal, shut down you computer, or lose internet connection.

1a. SSH into an owl
```
ssh jonassl@login.astro.uio.no
ssh owl20 
```

1b. Start a screen
```
screen
```

1c. Start a jupyter notebook server on some port.
```
jupyter-notebook --port=8887 --no-browser
```

1d. In the terminal there pops up a link that looks something like this `http://localhost:8887/?token=db9778d93010499994a82f231b1e897b383529d9e6a0c315`. Copy and save the bit after "token=". You will probably need it the first time you connect to your new jupyter server.

1e. De-attach from the screen by pressing ctrl+a+d. The screen terminal will now run by itself on the owl. You can close the terminal if you want. You can always re-attach to the screened session with
```
screen -r
```

# 2. Forwarding port from owl20 to login.astro.uio.no
We will now forward the 8887 port on the owl20 to the 8888 port on login.astro.uio.no.

2a. SSH into the ITA login:
```
ssh jonassl@login.astro.uio.no
```

2b. Start a screen (this is optional, but means you won't have to set it back of if you lose connection).
```
screen
```

2c. Set up a port forward from 8887 on owl to 8888 on login
```
ssh -N -L localhost:8888:localhost:8887 jonassl@owl20.uio.no
```

2d. De-attach from the screen by pressing ctrl+a+d. You can close this terminal if you want.

# 3. Forward port from login to your computer
3a. Finally we forward the 8888 port on the ITA login to the 8889 port on your computer.
```
ssh -N -L localhost:8889:localhost:8888 jonassl@login.astro.uio.no
```
3b. This terminal will need to stay open while your use your notebook. You can whenever you want close it and rerun the command, and should be back where you left. If you've done everything correctly, this should be everything you need to do next time you want to connect to your jupyter server.

3c. Go to `http://localhost:8889` to access your notebook. You probably need to insert the token you copied into the top right corner.

NB: Remember that even if you close the terminal in step 3, your jupyter server is still running. If one of your notebooks are consuming large amounts of memory, it would be polite to shut it down if you don't intend to use it for a few hours/days. 
