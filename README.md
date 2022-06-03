# Prerequisites
> sudo apt install python3-pip python3-virtualenv  

# Install project:
Review setup.sh and execute it. The setup script executes the following functions:  
*Creates a virtual environment for the project.  
*Installs libraries to the virtual environment using PIP.  
*Generates a secret key for django.  
*Creates the project database.  
*Collects static files.  

Create a superuser:
> source env/bin/activate  
> python manage.py createsuperuser  
> deactivate  

# Run the server:  
The web server can now be started:  
> source env/bin/activate  
> python manage.py runserver 0:8000  
> deactivate  

Note that this is a development server. Some additional setup is required for production:  
*Debug mode should be disabled for a production server. It can be set in CONotesWiki/.env file.  
*Change ALLOWED_HOSTS to your domain name or IP address in CONotesWiki/.env file.  
*Use a production web server like Apache.  
