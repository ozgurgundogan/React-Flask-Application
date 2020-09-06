sudo apt-get -y install nodejs
sudo apt-get -y install npm
sudo npm cache clean -f
sudo npm install -g n
sudo n stable
nodejs -v
node -v
sudo npm install -g yarn
sudo apt-get -y install python3-pip
sudo apt-get -y install python3-venv
cd ./react-flask-app/
yarn install --force
cd ../api
python3 -m venv react-flask-venv
. ./react-flask-venv/bin/activate
pip3 install -y -r requirements.txt
deactivate
