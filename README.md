# Absortion Curve - Inverse Neuronal Network 


## 1. Dependencies

To run this project you need to install:
- [anaconda](https://www.anaconda.com/download/)

You must be able to run `conda` and `pip` from the command line. If not have pip installed, you can install it with:
```bash
conda install pip
```


## Install
Now you need open a conda console and run:
```bash
conda create -n ams-dj python=3.9.16
conda activate ams-dj
```
This will create a new conda environment and activate it. Now you need to install the dependencies:
```bash
```
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic
```
This will create a new conda environment and install all dependencies.

## Run the App

You need position yourself in the app folder, the one that contains the file `manage.py`. To run the app you need to activate the conda environment and run the server:
```bash
conda activate ams-dj
python manage.py runserver
```
This will run the server in [http://localhost:8000/](http://localhost:8000/). Click on the link to open the app.