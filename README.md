# Setup project

## 1. Fork the project on GitHub

![](http://i.imgur.com/DLi2Nmb.png)

## 2. Download and set up the GitKraken Git client

Download from [gitkraken.com](https://www.gitkraken.com/)

## 3. Clone your forked repository

Open GitKraken, set up your GitHub login and clone your forked repository.

## 4. Setup virtualenv

`virtualenv venv`

## 5. Activate virtualenv

OS X / Linux:
`. venv/bin/activate`

Windows:
`venv\script\activate`

If success, prompt should start with: `(venv)`

## 6. Install Django and dependencies

`pip install -r requirements/local.txt`

## 7. Run Django

`cd project`

OS X / Linux:
`./manage.py runserver`

Windows:
`python manage.py runserver`


# Practice

Go to [Issues](https://github.com/Pylvax/django/issues) and do the ones starting with numbers.
