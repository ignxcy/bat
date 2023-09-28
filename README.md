# Bat 

Bat is a simple "package manager" that installs aur packages using git and makepkg, only supports installing. 

Example usage:
```bash
python3 main.py install neofetch-git
```
Or if you already have Bat installed:
```bash
bat install neofetch-git
```

Installation:
```bash
makepkg -sri 
```
Or with make:
```bash
sudo/doas make install 
```

# How does it work?

It first git clones the aur package's git url to ~/bat/{package}
<br>Then it cd's into the directory
<br>And then it runs makepkg -sri, and you're done! 
