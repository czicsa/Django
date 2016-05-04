@echo off
set /p appname="Az app neve: "
@echo on
python manage.py startproject %appname%