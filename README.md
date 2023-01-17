

## Prerequisites

Be sure you have the following installed on your development machine:

+ Python >= 3.7
+ Django-restframework
+ twilio
+ psycofg2
+ Django
+ Git
+ pip
+ Virtualenv (virtualenvwrapper is recommended)

## Install Requirements

Run the below statements
```bash
> pip install -r requirements.txt
```

## Project Installation

To setup a local development environment:

+ Create the database in postgresql as named world
+ If database name not world then configure the the database in settings.py
+ Perform the migration commands to create the table 
+ If you dont want to wish to create the database use the attached database for execution

```bash
    python manage.py makemigrations       
    python manage.py migrate  
```
+ Dumps(world.sql) databae to world database

+ For sending OTP please fallow the bellow steps

   A Twilio account (If you don't have one, sign up for a free account here.)

   https://www.twilio.com/try-twilio

   once the account created create the number for message to send the OTP


   add the bellow statements to settings.py to enable the otp triger

    ACCOUNT_SID='YOUR ACCOUNT SID'
    AUTH_TOKEN='YOUR AUTH TOKEN'
    COUNTRY_CODE='+country code of your choice'
    TWILIO_PHONE_NUMBER='number you get from Twilio'

+ Run the server

```bash
    python manage.py runserver  
```
+ click the bellow url to run the project 

http://127.0.0.1:8000/login/

