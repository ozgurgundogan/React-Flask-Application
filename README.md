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

## How to install ?
* Clone the project from github.
```bash
git clone https://github.com/ozgurgundogan/COALITION-ASSIGNMENT.git
cd COALITION-ASSIGNMENT/
```
* Ubuntu Installer
```bash
sudo sh ubuntu_installer.sh
```

* MacOs Installer
```bash
sudo sh macos_installer.sh
```

[You can install step by step by yourself](https://github.com/ozgurgundogan/COALITION-ASSIGNMENT/blob/master/INSTALLER-README.md "")


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

## Note

To be able to login into admin panel, password is required. Password is "admin".
