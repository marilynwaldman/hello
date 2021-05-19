# hello

## Create a directory - hello

From the terminal create a directory or from jupyterlab

```
mkdir hello
cd hello

```

## Create a repo on github from the directory hello

### Go to Github and create a repo, then copy and paste instructions

```
echo "# hello" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/     /hello.git
git push -u origin main

```

## create a hello.py file and change file permissions

`chmod +x hello.py`

## create a script file, run.sh and change file permissions.

`chmod +x run.sh`

## Say hello 

## Run the script file

`sh run.sh`

## push to github

```
git status
git add .
git commit -m "added hello.py and run.sh"
git push origin main

```


### Additional

https://stackoverflow.com/questions/46878457/adding-git-credentials-on-windows

## Do these steps

###  1.  Uninstall Ubuntu on Windows 10 - WLS2

How do I uninstall and reinstall Ubuntu WSL?
To uninstall Ubuntu, right-click the Ubuntu shortcut in your Start menu and click Uninstall.


### 2.  Install Ubuntu on Windows 10 - WLS2

##### Remember your root password

https://docs.microsoft.com/en-us/windows/wsl/install-win10


### 3.  Install git and configure github on WLS2 Ubuntu

https://docs.microsoft.com/en-us/windows/wsl/tutorials/wsl-git

### 4.  Install Anaconda on WLS2 Ubuntu

https://docs.anaconda.com/anaconda/install/linux/

https://docs.anaconda.com/anaconda/install/silent-mode/


```
cd
wget https://repo.anaconda.com/archive/Anaconda3-2021.05-Linux-x86_64.sh -O conda.sh
ls -l conda.sh
bash conda.sh  
```


You will be prompted to agree to terms and asked where to install. Say 'yes' and 'enter'

Do you accept the license terms? [yes|no]
[no] >>> 
Please answer 'yes' or 'no':'
>>> yes

Anaconda3 will now be installed into this location:
/home/ubuntu/anaconda3

  - Press ENTER to confirm the location
  - Press CTRL-C to abort the installation
  - Or specify a different location below

[/home/ubuntu/anaconda3] >>> 
PREFIX=/home/ubuntu/anaconda3

Reset the profile

```

source ~/.bashrc
which python

```


### Back to git

See this:  

Install git bash

https://www.youtube.com/watch?v=qdwWe9COT9k

https://git-scm.com/downloads

SSH KEY - windows

https://www.youtube.com/watch?v=WgZIv5HI44o


https://peteoshea.co.uk/setup-git-in-wsl/

https://docs.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent#adding-your-ssh-key-to-the-ssh-agent


https://github.com/desktop/desktop/issues/5454







