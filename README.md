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