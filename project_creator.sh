# Create React Front-End
#yarn create react-app react-flask-app
#cd react-flask-app
#ls -l

# Create Flask Back-end
#make sure pip installed
sudo apt-get install python3-pip
sudo apt-get install python3-venv

#create api directory
mkdir api
cd api

#create virtual env
python3 -m venv react-flask-venv
source react-flask-venv/bin/activate
pip3 install flask python-dotenv
cd ..

#update watcher counts
echo fs.inotify.max_user_watches=524288 | sudo tee -a /etc/sysctl.conf && sudo sysctl -p