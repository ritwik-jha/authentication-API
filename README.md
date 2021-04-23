# Authentication API's

## Description
Here we have created a authentication system from scratch using Flask as framework and python language. 
The authentication system provides API's using which any user can register and authenticate. 
The system is hosted on aws cloud and can be accessed using the API's only. 


## Routes
The routes are as follows:

### To signup/register as a new user:
```
http://15.207.114.217:80/signup/<username>/<email_address>/<password>
```
The user needs to enter his/her credentials in the form shown above. This will register a new user in the database and the user can use these credentials to login. Note that the username and email should be unique.


### To login as a user:
The user can use his/her email address and password to login/authenticate. This will start a session.
```
http://15.207.114.217:80/login/<email_address>/<password>
```

### To logout from a session/user:
Logging out will terminate the established session and logout the user. 
```
http://15.207.114.217:80/logout
```

### To dump the entire user database:
Dumping the database is creating a backup of the data. Here we store the entire data in a csv file for backup. 
```
http://15.207.114.217:80/dump
```

### To show the backedup/dumped data:
```
http://15.207.114.217:80/showbackup
```

## Example Situation
A user named jack with email address jack@g.com wants to register in the system and then authenticate. 

To register in the system jack uses:
http://15.207.114.217:80/signup/jack/jack@g.com/some_random_password

Jack receives the following output:

![image](https://user-images.githubusercontent.com/59885389/115818507-84db4680-a41a-11eb-8707-402bdc88af5d.png)

Now to login/authenticate in the system jack uses:
http://15.207.114.217:80/login/jack@g.com/some_random_password

Logging in Jack receives the following output:

![image](https://user-images.githubusercontent.com/59885389/115818903-69247000-a41b-11eb-9167-736960748e48.png)

Now to logout and terminate the session jack uses:
http://15.207.114.217:80/logout

For logout jack receives the following output:

![image](https://user-images.githubusercontent.com/59885389/115819036-af79cf00-a41b-11eb-8a89-3b2049a6b912.png)

To dump the data:
http://15.207.114.217:80/dump

Output:

![image](https://user-images.githubusercontent.com/59885389/115819632-dc7ab180-a41c-11eb-9f01-d34017808b9a.png)

To retrieved the dumped data:
http://15.207.114.217:80/showbackup

Output:

![image](https://user-images.githubusercontent.com/59885389/115819985-92460000-a41d-11eb-9cfc-d5ce5a86bd5d.png)







