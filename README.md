# PetroTech

### Running project with virtual env

```Shell
pip install virtualenv
```
Windows setup:
```Shell
#creating the enviroment
python -m venv venv

#activating the enviroment
venv\Scripts\activate

#deactivating enviroment
deactivate
```
Linux and Mac setup:
```Shell
#creating the enviroment
python -m venv venv

#activating the enviroment
source venv/bin/activate

#deactivating enviroment
deactivate
```

then installing the requirements:

```Shell
pip install -r requirements.txt
```

### Running the Project
in order to run the project you need to use either ways below

default and development settings
```Shell
python manage.py runserver 
```

