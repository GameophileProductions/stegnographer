# Stegnograper
> This is a web based application which enables users to hide 1 image into another without destroying any of the 2 images.
> Also, to seperate out hidden image, we have decryption alogorithm also.
> Live demo [_here_](https://gameostash.herokuapp.com/). 

## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Features](#features)
* [Screenshots](#screenshots)
* [Setup](#setup)
* [Usage](#usage)
* [Room for Improvement](#room-for-improvement)
* [Acknowledgements](#acknowledgements)
* [Credits](#credits)
* [Contact](#contact)


## General Information
- Provide general information about your project here.
- Many a times we want to hide a particular image but due to security issues we are not able to do so. Due to this fact(and yes we have lot's of images we don't want to show and neither want to store somewhere), hiding it seemed a better option.
- We created this project to learn how tasks and other manupulations could be done without paying much attention to dependencies and creating containers to ship our product


## Technologies Used
- Django - v3.7.1
- Postgresql
- Pillow for image manupulation - v8.3.1


## Features
- Hide 1 image inside another.
- Retrieve hidden image back without compromising with quality of the 2 images used.


## Screenshots
![Home Screen](./static/images/screenshot_1.png)


## Setup

To run this project, follow the steps listed below.

> Install Python v3.7 or above from [_here_](https://www.python.org/downloads/release/python-370/)

> Now once you have install python, create virtual enviroment or activate an existing one.
> To create a new virtual enviroment, follow the steps:

```
$ pip install virtualenv
```

Now check your installation

```
$ virtualenv --version
```

Create a virtual environment now,

```
$ virtualenv virtualenv_name
```

After this command, a folder named virtualenv_name will be created. You can name anything to it. If you want to create a virtualenv for specific python version, type

```
$ virtualenv -p /usr/bin/python3 virtualenv_name
```

or

```
$ virtualenv -p /usr/bin/python2.7 virtualenv_name
```

Now at last we just need to activate it, using command

```
$ source virtualenv_name/bin/activate
```

Clone this repo
 ```
 git clone https://github.com/GameophileProductions/stegnographer.git
 ```

 `cd stegnographer`

 and run
 ```
 pip install -r requirements.txt
 ```

 This will install all the dependencies 


## Usage

Run server on port 8000 by using

```
waitress-serve --port=8000 stegnographer.wsgi:application
```


## Room for Improvement

Room for improvement:
- Stability and efficiency of hidding image
- User interface 
- Scalability of this app

To do:
- Loading css


## Acknowledgements

- Many thanks to [_Om-Mukherjee_](https://github.com/Oyum2814) without whom this project could not be completed

## Credits

- Frontend and algorithm was done by [_Om-Mukherjee_](https://github.com/Oyum2814)
- Backend and hosting was done by [_Achyut_](https://github.com/Achyut-0705)

## Contact
Created by [@Achyut](https://github.com/Achyut-0705) and [@Om](https://github.com/Oyum2814) - feel free to contact me!