<div align="center"> 
  <img src="https://firebasestorage.googleapis.com/v0/b/projectbucket-52626.appspot.com/o/Stegnographer.svg?alt=media&token=56be60ca-5002-4dc0-b015-a36ddcb59e3c" height="105"/>

> This is a web based application which enables users to hide 1 image into another without destroying any of the 2 images.
> Also, to seperate out hidden image, we have decryption alogorithm also.
> Live demo [_here_](https://gameostash.herokuapp.com/).

- Provide general information about your project here.<br/><br/>
- Many a times we want to hide a particular image but due to security issues we are not able to do so. Due to this fact(and yes we have lot's of images we don't want to show and neither want to store somewhere), hiding it seemed a better option.<br/><br/>
- We created this project to learn how tasks and other manupulations could be done without paying much attention to dependencies and creating containers to ship our product<br/><br/><br/>

<img src="https://firebasestorage.googleapis.com/v0/b/projectbucket-52626.appspot.com/o/TechStackUsed.svg?alt=media&token=1c472635-f3a9-4164-bec0-4e1284951343" height="75"/><br/><br/>

- Django - v3.7.1
- Postgresql
- Pillow for image manupulation - v8.3.1
  <br/><br/>

<img src="https://firebasestorage.googleapis.com/v0/b/projectbucket-52626.appspot.com/o/Features.svg?alt=media&token=5b1dbffb-030c-4ec7-806d-22428c37ec03" height="75"/><br/><br/>

- Hide 1 image inside another.
- Retrieve hidden image back without compromising with quality of the 2 images used.<br/><br/>

<img src="https://firebasestorage.googleapis.com/v0/b/projectbucket-52626.appspot.com/o/Gallery.svg?alt=media&token=cb18a1d8-53bd-48c3-8584-0b4710f2ff60" height="75"/><br/><br/>

![Home Screen](./static/images/screenshot_1.png)

<strong><h2 style="color:#364547">Setup for running it Locally</h2></strong>

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
<br/><br/>

Run server on port 8000 by using

```
waitress-serve --port=8000 stegnographer.wsgi:application
```

<br/><br/>
<strong><h2 style="color:#364547">Room for Improvement </h2></strong>

- Stability and efficiency of hidding image
- User interface
- Scalability of this app

<br/><br/>
<strong><h2 style="color:#364547">To Do </h2></strong>

- Loading css

<br/><br/>
<img src="https://img.shields.io/badge/Contributors-black?logo=Github&style=for-the-badge" height="55"/>

  <table>
<tr align="center">
 <td>
<!-- Here I am writing my own code -->
Om Mukherjee

<p align="center">
<img src = "https://avatars.githubusercontent.com/Oyum2814"  height="120" alt="Om">
</p>

<p align="center">
<a href = "https://github.com/Oyum2814"><img src = "https://logos-download.com/wp-content/uploads/2016/09/GitHub_logo.png" width="36" height = "36"/></a>
<a href = "https://www.linkedin.com/in/om-mukherjee-b842b9212/">
<img src = "https://www.pikpng.com/pngl/m/57-572097_linkedin-transparent-icon-linked-in-logo-with-white.png" width="36" height="36"/>
</a>
</p>
    <strong>Frontend <br/> &<br/>Algorithm Generator<strong>
</td>

<td>
  
Achyut Shukla

<p align="center">
<img src = "https://avatars.githubusercontent.com/Achyut-0705"  height="120" alt="Achyut">
</p>
<p align="center">
<a href = "https://github.com/Achyut-0705"><img src = "https://logos-download.com/wp-content/uploads/2016/09/GitHub_logo.png" width="36" height = "36"/></a>
<a href = "https://www.linkedin.com/in/achyut-shukla-070502/">
<img src = "https://www.pikpng.com/pngl/m/57-572097_linkedin-transparent-icon-linked-in-logo-with-white.png" width="36" height="36"/>
</a>
</p>
  <strong>Backend <br/>&<br/> Hosting<strong>
</td>
  
  </table>
</tr>
</div>
  <br>
</div>
