# [The iSpinalCordToolbox project](https://github.com/neuropoly/spinalcordtoolbox_web) #

This project is awesome.

-------
TODO:
Missing pieces to get out of beta mode:
	- A module queueing system to restrinct the number of running process
	- A database or file system organisation to store info including logs of every running jobs
	- A view that shows all the jobs sent by a user

	** Extra feature
	- An Angular JS layer for brain browser 
-------

# Setting Up

## Contents

 - client - the AngularJS frontend of the webapp
 - server - the Pyramid backend of the webapp

## How to install it

###Presteps
 - Set up virtualenv and activate it
 - Install npm

###Build Client side
```
[Install NPM]
cd client
npm install
```

###Install Client side as Package
```
[Activate a virtualenv]
cd client
python setup.py install
```

### Serving Client Side w/ Pyramid Dev Server

Setup, see routes, and serve pyramid app
```
cd ../server/
python setup.py develop
proutes development.ini
pserve development.ini --reload
```

Try URLs on localhost
- [The Client App](http://localhost:6543/)
- [The Server Root](http://localhost:6543/home)

##Some tricks 

### How to create a new page in the client Angular App
Presteps
 - install yeoman
 ```
 npm install -g yo
 npm install -g generator-angular
 ```

Call Yo to create your new page
```
yo angular:route mynewroute
```

###Create a soft link to auto-update your changes
```
[Activate a virtualenv]
cd ../*your_virtualenv*/lib/python3.4/site-packages/app-0.1-py3.4.egg/
```
Delete the app directory or rename it
```
ln -s ../../../../../client/app app
```

If bower_components are missing, do not forget to run bower in the `client/` dir:

```
cd client
bower install
``` 


Some library are needed to have the server running they are include in the setup.py file
Runnig 'python setup.py develop' should install all that you need in your virtual environement
Did not forget to add the package you add for additional developpement in the setup.py file


You need nodeJS to be installed so potential js goodies will work, the database is sqlite3, do not forget to have that install too.


lib that need to be there to compyle numpy, scipy, matplotlib...
libfreetype6 
libfreetype6-dev
lapack
gfortran
gcc
etc...
would be good to hav a .deb that do all that

