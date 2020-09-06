# install nodejs required version and install yarn
curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.35.2/install.sh | bash
nvm install 12.18.13 --reinstall-packages-from=6.13.4
nvm use 12.18.13
sudo npm install -g yarn

# install front end dependencies
cd ./react-flask-app/
yarn install --force

# create virtual enviroment and install backend requirement
cd ../api
python3 -m venv react-flask-venv
. ./react-flask-venv/bin/activate
pip3 install -r requirements.txt
deactivate
