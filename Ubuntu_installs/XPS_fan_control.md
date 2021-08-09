# Install and configure i8k
http://keenformatics.blogspot.com/2013/06/how-to-solve-dell-laptops-fan-issues-in.html

https://askubuntu.com/questions/1094485/dell-xps-15-9570-how-to-control-the-fans

https://www.cyberciti.biz/faq/controlling-dell-fan-speeds-temperature-on-ubuntu-debian-linux/

Edit config file: `sudo nano /etc/i8kmon.conf`

Monitor i8k: `i8mon`

Set manual fan speed: `i8kfan 1 1`



# Clone and make bios fan disable tool
https://github.com/TomFreudenberg/dell-bios-fan-control

```
cd dell-bios-fan-control
make
sudo ./dell-bios-fan-control 0
sudo ./dell-bios-fan-control 1
```
