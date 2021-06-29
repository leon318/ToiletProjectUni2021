# How to Create a Virtual Environment

## Setup Virtual Environment 

Create a folder on your computer. Next, open up pycharm, go to file, open, and select the folder you created. It will open a new project.

Open a terminal window at the bottom of the project. See which python is installed on it.
Type:
```bash
virtualenv --python=path nameofenvironment
```

 To find the path, go to your root terminal and type:
which python3
This will give you for example:
```bash
/usr/bin/python3
```
Take this and paste it into the above command line:
```bash
virtualenv --python=/usr/bin/python3 nameofenvironment
```

Press enter and create the new environment. Open a new terminal window and type which python3 to check its location. It should say something along the line of:
```bash
/Users/Name/Documents/FirstFolder/SecondFolder/Projectname/bin/python
```
## Set up python version
Now to set the python version, go to bottom right-hand corner to change python in the virtual environment. Click on add interpreter, select existing interpreter and it should show the location of the python in the virtual environment. Click on that and hit Ok

##Check Python
Lastly, to check if you did this correctly, you can type
```bash
which python3
```
It will show you the python location.

To enter into the virtual environment terminal open a new terminal or type in
```bash
source .venv/bin/activate
```
To deactivate type:
``` bash
deactivate
```

# How to import from function libraries

```
 export PYTHONPATH=$PYTHONPATH:/Users/Leon/Documents/ToiletProjectUni2021

```
