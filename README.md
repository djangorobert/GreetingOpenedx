# GreetingOpenedx
All the Technologys used can be found in the: requirements.txt file.
I used pipenv for this project.
I used tutor to download openedx platform. 

Steps to get this project to work on your own PC:

1.Do this in your command prompt: mkdir (projectname)

2.cd (projectname)

3.git clone https://github.com/djangorobert/GreetingOpenedx.git
  
4.cd Greetingopenedx
  
5.pipenv install -r requirements.txt
  
6.cd openedproject

7.If you want to use the Django Admin which does comes ready with this repo make sure to do this command: python manage.py createsuperuser (yournameofchoicehere)
then fill in the blanks it may ask for your email and password. to get to the admin go to: localhost:8000/admin then sign in but make sure to do the 
next step first which is step (8) because you need the Server running first ;).

8.python manage.py runserver

A Project that Includes OpenEdx Platform and a Django Application that Adds Greetings and orders them from newest to oldest. Also shows the newest greeting 
at the top header tab. I also added in a API with read only privelages. The Goal of this project was to install Openedx platform and yet still have the ability to add on 
extra apps that could be features or add ons. 


Here is the Finished Product Images of the Landing page(Home page), Built the API to provide a different endpoint to be consumed by a Frontend Framework like React but make sure if your going to do so to install the package django-cors-headers to allow django and react to work together. I alos added in the pics of the Django built in Admin.
![Alt text](openedx1.JPG?raw=true)
![Alt text](openedx2.JPG?raw=true)
![Alt text](openedx3.JPG?raw=true)
![Alt text](openedx4.JPG?raw=true)
![Alt text](openedx5.JPG?raw=true)
![Alt text](openedx6.JPG?raw=true)
![Alt text](openedx7.JPG?raw=true)
