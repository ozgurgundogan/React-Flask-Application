* Install required packages. Please note that "sudo apt-get update" exists. If you do not want to update your other libraries, SKIP update command.
```bash
sudo apt update
```

```bash
## PLEASE NOTE THAT NODEJS IS GOING TO INSTALLED IN GLOBAL PATH.
# install nodejs

curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.35.2/install.sh | bash
nvm install 12.18.13 --reinstall-packages-from=6.13.4
nvm use 12.18.13
sudo npm install -g yarn
```


```bash
## PLEASE MAKE SURE PIP and VIRTUALENV IS GOING TO INSTALLED IN GLOBAL PATH.
# for ubuntu you can use the commands below
sudo apt-get install python3-pip
sudo apt-get install python3-venv

# for macos you can use Homebrew.
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
brew install python3
pip3 install virtualenv
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
