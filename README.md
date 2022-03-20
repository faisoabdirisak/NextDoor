# NextDoor


## Author  
  
[Github](https://github.com/faisoabdirisak)

# Description  

This is a web application that shows the number of neighbours around you including their business and location.


##  Live Link
 Click [View Site](https://morning-ocean-92442.herokuapp.com/)  to visit the site.

 ## User Story
* Sign in with the application to start using.
* Set up a profile about me and a general location and my neighborhood name.
* Find a list of different businesses in my neighborhood.
* Find Contact Information for the health department and Police authorities near my neighborhood.
* Create Posts that will be visible to everyone in my neighborhood.
* Change My neighborhood when I decide to move out.
* Only view details of a single neighborhood.

## Setup and Installation  

To get the project .......  
  
    
##### Cloning the repository:  
 ``` 
git clone https://github.com/faisoabdirisak/NextDoor.git
```
##### Navigate into the folder 
 ``` 
cd NextDoor
```
##### Install and activate Virtual  
 ``` 
- python3 -m venv virtual - source virtual/bin/activate  
```  

##### Install Dependencies  
 ``` 
 pip install -r requirements.txt 
```  
 ##### Setup Database  
  SetUp your database User,Password, Host then make migrate  
 ``` 
python manage.py makemigrations 
 ``` 
 Now Migrate  
 ```
 python manage.py migrate 
```

##### Run the application  
 ``` 
 python manage.py runserver 
``` 
##### Running the application  
 ``` 
 python manage.py server 
```
##### Testing the application  
 ``` 
 python manage.py test 
```
Open the application on your browser `127.0.0.1:8000`. 


## How the app works
A user needs to log in if they have na existing account
A user can sign up f they do not have an account
A user then can be able to view a persons profile and their neighbours.

## Technology used  
  
* python3.8  
* Django 4.1
* Html
* CSS
* Javascript
* Heroku
* Bootstrap


## Known Bugs  
* There are no known bugs 
  
## Licence

MIT License    [MIT](https://choosealicense.com/licenses/mit/)


Copyright (c) [2022] [Faiso Abdirisak]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
