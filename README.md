# Udacity Item Catalog Project

### Project components
*static - The location of the CSS and Javascript files*
*templates - where all the HTML files are stored for the front-end*
*databasesetup.py - here are located database tables*
*ItemCatalog.db - Database of items that is processed by the Flask Application*
*project.py - The main application for this Flask app*
*bunchofitems.py - Fills in the ItemCatalog.db with sports gear*
*client_secret_8309 ... sercontent.com - Google API credentials*

### How to run the project:
The vagrant virtual machine can be installed by forking/cloning [THIS](https://github.com/udacity/fullstack-nanodegree-vm) repository.
Once this is completed, and the vagrant files are in [directory], the user can enter the following shell commands:
 ```sh
$ cd directory/vagrant
$ vagrant up
```

The following shell commands start up the virtual machine:
 ```sh
$ cd [directory]/vagrant
$ vagrant ssh
```
If the app is being run for the first time, the initial database can be filled with the following commands:
 ```sh
$ cd /vagrant/catalog
$ python bunchofitems.py
```
To start the app so it can be viewed in a browser, use the following:
 ```sh
$ cd /vagrant
$ python project.py
```
To view the site, enter "http://localhost:5000/" in your browser (preferably Chrome)

### Attributions
