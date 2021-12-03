# RSS Reader
A content aggregator web application built with Django Framework.

## General Info
A content aggregator, which displays the latest content from chosen podcasts or blogs.

## Technologies:
- Python
- Django
- JavaScript
- feedparser library
- django-apscheduler library
- HTML
- CSS

## Features:
- user authorization (register, login, logout, edit profile, change password, reset password)
- available channel list (all and by category)
- channels details view
- add channels in admin panel by providing the link to the feed
- parsing RSS feeds
- users can choose the channels to follow
- scheduling tasks with django-apscheduler
- use a custom django command to execute scripts
- tests in PyTest

## Setup

First you should clone this repository:
```
git clone https://github.com/JKK86/rss-reader.git
cd  rss-reader
```

To run the project you should have Python 3 installed on your computer. Then it's recommended to create a virtual environment for your projects dependencies. To install virtual environment:
```
pip install virtualenv
```
Then run the following command in the project directory:
```
virtualenv venv
```
That will create a new folder venv in your project directory. Next activate virtual environment:
```
source venv/bin/active
```
Then install the project dependencies:
```
pip install -r requirements.txt
```
Now you can run the project with this command:
```
python manage.py runserver
```
You can start executing scripts (fetch feeds) with this command:
```
python manage.py start_jobs
```

**Note** in the settings file you should complete your own database settings and secret key.

## Inspiration

This app is inspired by realpython.com

