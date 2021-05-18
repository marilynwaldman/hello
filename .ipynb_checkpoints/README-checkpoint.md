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


### Uninstall Ubuntu on Windows 10 - WLS2

How do I uninstall and reinstall Ubuntu WSL?
To uninstall Ubuntu, right-click the Ubuntu shortcut in your Start menu and click Uninstall.


### Install Ubuntu on Windows 10 - WLS2

https://docs.microsoft.com/en-us/windows/wsl/install-win10


### Install git and configure github on WLS2 Ubuntu

https://docs.microsoft.com/en-us/windows/wsl/tutorials/wsl-git

### Install Anaconda on WLS2 Ubuntu

https://docs.anaconda.com/anaconda/install/linux/

https://docs.anaconda.com/anaconda/install/silent-mode/


```
wget https://repo.anaconda.com/archive/Anaconda3-2021.05-Linux-x86_64.sh -O ~/conda.sh
bash ~/miniconda.sh -b -p $HOME/conda
```

```
bash Anaconda3-2020.02-Linux-x86_64.sh

````
or 

```
sh Anaconda3-2020.02-Linux-x86_64.sh
```
Reset the profile

```

source ~/.bashrc
which python

```






