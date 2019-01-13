# britetestproj

Deployment Steps
 
  1. Create a virtual Enviornment in which we can install required packages for this project. All changes will be done only in this Enviornment.
     `$ virtualenv venv`
  2. Activate newly created virtualenv for further installation and project deployment. Make sure file "./venv/bin/activate" should have executable permissions.
     `$. ./venv/bin/activate`
  3. Goto "src" directory of this project and execute following command.
    `$ pip install -r requirements.txt`
  4. Finally start project using following command. It will start a project on 80 port of your computer. 
     `$ python app.py`
  5. Access project from web browser by typing this address "localhost:80" or "<IP_address>:80"
  

Project Details
   1. Feature request : Employee can update details of client feature request using web address "localhost:80", but make sure that client is already registered.
   2. If client is not registered either click on "Add New Client" button or use web address "localhost:80/client".
   
  
