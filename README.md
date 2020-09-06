## Project File Structure
```bash
.
├── api
├── files
├── project_creator.sh
├── react-flask-app
```

#### api
The directory holds all backend (Flask) files.
#### files
The directory holds csv files provided by Coalition Inc.
#### react-flask-app
The directory holds all frontend (ReactJS) files.

## Install ?
* Clone the project from github.
```bash
git clone https://github.com/ozgurgundogan/COALITION-ASSIGNMENT.git
cd COALITION-ASSIGNMENT/
```

* Install required packages. Please note that "sudo apt-get update" exists. If you do not want to update your other libraries, SKIP update command.
```bash
sudo apt update
```

```bash
## PLEASE NOTE THAT NODEJS IS GOING TO INSTALLED IN GLOBAL PATH.
# install nodejs
sudo apt install nodejs
sudo apt install npm
sudo npm cache clean -f
sudo npm install -g n
sudo n stable
# This project is currently build with nodejs v8.10.0
nodejs -v
# This project is currently build with node v12.18.13
node -v
sudo npm install -g yarn
```


```bash
## PLEASE NOTE THAT PIP and VIRTUALENV IS GOING TO INSTALLED IN GLOBAL PATH.
# make sure pip and virtual enviroment installed
sudo apt-get install python3-pip
sudo apt-get install python3-venv
```


* Now let's build up a virtual enviroment for our Flask Backend.
```bash
# I want to virtual enviroment under api directory. So move there.
cd ./api

# And create a virtual enviroment that I named "react-flask-venv"
python3 -m venv react-flask-venv

# Make sure virtual enviroment created. 
# After the command below executed, you should see "(react-flask-venv)" at the beginning 
# of the next line in your bash file. If you see, then virtual enviroment created successfully.
source react-flask-venv/bin/activate

# Now let's install required python libraies.
pip3 install -r requirements.txt

# Now let's wake up our backend server. 
# PLEASE NOTE THAT Flask is using port=5000. If port=5000 is not available, then try to kill the process that using port=5000.
flask run

# If you see "* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit), then server is ON and waits for requests.

```
So far, we are done with backend.
```bash
# Please Press CTRL+C to quit in your terminal.

# Let's deactivate virtual enviroment for now.
deactivate

# (react-flask-venv) should be removed in your terminal.
```

Now let's continue with frontend.

```bash
# If you follow the steps above, you are supposed to be under /api/ directory. 
# If you are in /api/ directory, then move /react-flask-app/ directory.
cd ../react-flask-app/

# Install nodejs packages required for frontend. 
# Here, I am using --force parameters to force to re-install packages 
# because you might have some of dependencies in your computer and these might be broken. 
# Let's make sure, eveything is alright.
yarn install --force
```

## How to run ?
1. Running backend server<br/>
Open a new terminal and move to project directory.
```bash
cd ./path/to/project/
cd ./api/
flask run
```

2. Running frontend server<br/>
Open a new terminal and move to project directory.
```bash
cd ./path/to/project/
cd ./react-flask-app/
yarn start
```

If you do not have any errors in your terminal, a new webpage is going to pop up and directs you to frontend address.
