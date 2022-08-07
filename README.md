

## Store Sales ML project.

### Software and account Requirement.

1. [Github Account](https://github.com)
2. [Heroku Account](https://dashboard.heroku.com/login)
3. [VS Code IDE](https://code.visualstudio.com/download)
4. [GIT cli](https://git-scm.com/downloads)
5. [GIT Documentation](https://git-scm.com/docs/gittutorial)


Creating conda environment
```
conda create -p venv python==3.7 -y
```
```
conda activate venv/
```
OR 
```
conda activate venv
```

```
pip install -r requirements.txt
```

To Add files to git
```
git add .
```

OR
```
git add <file_name>
```

> Note: To ignore file or folder from git we can write name of file/folder in .gitignore file


To check all version maintained by git
```
git log
```

To create version/commit all changes by git
```
git commit -m "message"
```

To send version/changes to github
```
git push origin main
```

To check remote url 
```
git remote -v
```

To setup CI/CD pipeline in heroku we need 3 information
1. HEROKU_EMAIL = bs485950@gmail.com
2. HEROKU_API_KEY = <>
3. HEROKU_APP_NAME = storesalespredictor

BUILD DOCKER IMAGE
```
docker build -t <image_name>:<tagname> .
```
> Note: Image name for docker must be lowercase


To list docker image
```
docker images
```

Run docker image
```
docker run -p 5000:5000 -e PORT=5000 f8c749e73678
```

To check running container in docker
```
docker ps
```

Tos stop docker conatiner
```
docker stop <container_id>
```



```
python setup.py install
```


Install ipykernel

```
pip install ipykernel
```


Data Drift:
When your datset stats gets change we call it as data drift



## Write a function to get training file path from artifact dir




# If using the Docker for the first time. Here are the step to install wsl and Docker.
Enable the Windows Subsystem for Linux
=> clk Start -> find Turn windows features on or of -> select Virtual machine platform and windows subsystem for linux (After this step RESTART MACHINE).

or

Open PowerShell as Administrator (Start menu > PowerShell > right-click > Run as Administrator) and enter this command:

-> dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart

(After this step RESTART MACHINE)

Install your Linux distribution(download Ubuntu any version but LTS - Long Term Support) of choice from Microsoft Store .

Download the Linux kernel update package

-> Go to this link and follow STEP-4

https://docs.microsoft.com/en-us/windows/wsl/install-manual#step-4---download-the-linux-kernel-update-package

Open windows Powershell in Admin mode and write the dollowing command to check that is docker is running or not
 docker --version
wsl -l -v
Congratulation Done .
========================= DOCKER STEPS END =================================

========================= DOCKER IMAGE START =================================

# DOCKER IMAGE DETAILS

# Create a Docker file in the main project folder

which OS we are using as a base layer in our docker image. (Define which python version we are using. )
Copy the whole project except the enviroment folder in the docker file .
create .dockerignore file in the main project.
the files which we dont want we will add in the .dockerignore file.(we don't require .gitignore, venv, .git) -> .git is a hidden file we directly have to mention it in .dockerignore file.
Now copping all the file and folder in the dockerfile we have to simply write the command

COPY . /app
Here COPY command is used to copy all the (code)file and folder and we have created a folder called app, here it is stored in that and (.) dot represent current directory.

Now change the directory from ML_Project directory to app dicrectory