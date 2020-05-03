# Docker-Management-TUI

Docker-Management-TUI is a simple Terminal User Interface program made using python for the novice users who want t use the docker for their projects but 
don't understand how to use it or are unfamilliar with installations process or are just lazy and want everything done at a push of a button.
Docker-Management-TUI will take care of all the things from installation of the docker or setting up a wordpress or a media server with minimum efforts needed.
It also provides the feature of monitoring the docker containers resource utilization with help of Dockly API module (Visit for more information on dockly module  https://github.com/lirantal/dockly)


With this repo you can Automatically:

1.Install Docker into your system

2.Download and use  Docker Images

3.Set up a Emby media server

4.Set up a Wordpress server

5.Monitor Container Stats 

# Built With
- RedHat Linux RHEL8
- Dockly
- Docker
- Emby Server
- Wordpress
- MYSQL

# Requirements 
Make sure that you have atleast python3 installed on your machine 

# Usage 

Just clone this repository on your machine and the use the command 
```
python3 DockerManagementTUI.py 
```

# User Interface 
![User Interface](Images/User%20Interface.png)

# Version Check
![Version check](Images/Version%20check.png)

# Wordpress Setup
![Wordpress server](Images/wordpress%20setup.png)

# Wordpress Server
![Wordpress server](Images/wordpress%20server.png)

# Emby Media  server
![Emby Media  server](Images/Emby%20server.png)

# Docker Monitor
![Docker Monitor](Images/Dockly%20Monitor.png)

 ## MySQL client
If you want to verify that your database folder has been created or not, install MySQL client software using yum install mysql. After installation run this command : 
   
    mysql -h 172.17.0.0/16 (your MySQL container IP) -u (username) -p

# Troublshooting the erros
Linux firewall won't allow to connect to MySQL database server and to outside world. Hence following commands should be implemented first in order to connect to server.
```
- selinux 0
- iptables -F
- iptables -P FORWARD ACCEPT
- firewall-cmd --zone=trusted --change-interface=docker0 --permanent (If there are any other networks for docker add them too like br-xxxxx)
- firewall-cmd --zone=trusted --add-masquerade --permanent
- firewall-cmd --add-port=3306/tcp
- firewall-cmd --reload
- systemctl restart docker
- Change your network settings to Bridge Adapter
```
# Authors
- [Aishwary Madiwale](https://github.com/lelouch885)
- [Deepak Singh](https://github.com/deepaksingh4)

# About
This is a docker project built for need of automation and maintaining the server database in cases when local system crashes, Docker is too fast in building OS i.e. in few seconds this will help owncloud to maintain file storage safe.

