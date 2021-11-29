<h1 align="center">
    Fostress
</h1>
<p align="center">
<a href="https://github.com/ameliiams/Fostress/blob/main/LICENSE">
    <img src="https://img.shields.io/badge/license-Apache--2.0-blue.svg"alt="Fostress is released under the Apache 2.0 license." />
    <img src="https://img.shields.io/github/last-commit/ameliiams/fostress">
</a>
</p>

A free open-source social platform that was built with the goal of gaining a deeper understanding of the impact of social media on mental health. 

This app is based on Python with Django and SQLite. 

## Features
* Easy setup
* Supports user sign in & sign up
* Support for both text and image posts

## Get Started

First, create a virtual environment 

``` 
# Unix / MacOS
python3 -m venv fostress
source fostress/bin/activate
```

``` 
# Windows
python3 -m venv fostress
fostress/Scripts/activate.bat
```
Then, clone the project repository
```
git clone https://github.com/ameliiams/Fostress.git ./fostress/Fostress
```
Install dependencies
```
python3 -m pip install -r fostress/Fostress/requirements.txt
```
And run the server
```
python3 fostress/Fostress/site/manage.py migrate
python3 fostress/Fostress/site/manage.py runserver
```

## Screenshots

![Signup Page](https://github.com/ameliiams/Fostress/blob/main/screenshots/example-signup.gif?raw=true)
![Login Page](https://github.com/ameliiams/Fostress/blob/main/screenshots/example-login.gif?raw=true)
![Example image post](https://github.com/ameliiams/Fostress/blob/main/screenshots/example-imagepost.png?raw=true)
![Example text post](https://github.com/ameliiams/Fostress/blob/main/screenshots/example-textpost.png?raw=true)


## To Do
- [ ] Add support for comments
- [ ] Add user profile pictures
- [ ] Add page for user settings

## License
This project is licensed under the [Apache 2.0 License](https://github.com/ameliiams/Fostress/blob/main/LICENSE)
