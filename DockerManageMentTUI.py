import os
import getpass 

os.system("mode con cols=1000 line = 1000")


def intro():
	os.system("clear")
	os.system("tput setaf 1")
	print("\t\t\t\t\t\tDOCKER MANAGEMENT TUI ")
	os.system("tput setaf 7")
	print("\t\t\t------------------------------------------------------------------")
	os.system("tput setaf 2")
	print("\t\t\t\t#################     MENU    ####################")
	os.system("tput setaf 7")
	print("\t\t\t\tA Docker Project by : Aishwary Madiwale, Deepak Singh")

    

def dockerinstall():
    os.system(" echo -e '[DVD1]\nbaseurl=file:///run/media/root/RHEL-8-0-0-BaseOS-x86_64/AppStream\ngpgcheck=0\n[DVD2]\nbaseurl=file:///run/media/root/RHEL-8-0-0-BaseOS-x86_64/BaseOS\ngpgcheck=0\n[Docker]\nbaseurl=https://download.docker.com/linux/centos/7/x86_64/stable/\ngpgcheck=0' > /etc/yum.repos.d/dock.repo")
    os.system("yum install docker-ce --nobest ")
    os.system("systemctl start docker")
    os.system("systemctl enable docker")

def dockdelt():
	os.system("tput setaf 1")
	print(" Warning!!!!!! this action will remove docker from you system  and all the data assciated with it ")
	os.system("tput setaf 7")
	print("Are you sure you want to proceed with this yes or no ")
	ans=input()
	if ans == 'yes' or ans == 'y' or ans == 'Y':
		os.system("yum remove docker-ce")
		os.system("rm -rf /var/lib/docker")
	elif ans == 'no' or ans == 'n'or ans == 'N':
		print("Action Aborted")
		

def deletedockimage():
	print("Do you want to delete all the docker images  yes or no")
	ans=input()
	if ans == "yes" or ans == "y":
			os.system("docker rm -f $(docker ps -a )")
	elif ans == "no" or ans == "n":
			dockimg()
			print("Enter the name or pid of the docker image that u want to delete")
			dockerid=input()
			os.system("docker image  rm -f {}".format(dockerid))

def dockimg():
    os.system("sudo docker images")	


def image():
    print("Enter the name of os that you want to download")
    osname=input()
    print("Please Wait while the image is being downloaded")
    os.system("sudo docker pull {}".format(osname)) 

def dockmonitor():
    os.system("npm install -g dockly")
    os.system("dockly")

def dockver():
    os.system("docker --version")

def embyserver():
	print("Please Wait while the server is being setup")
	os.system("curl -L -m 10000 \"https://github.com/docker/compose/releases/download/1.25.5/docker-compose-$(uname -s)-$(uname -m)\" -o /usr/local/bin/docker-compose")
	os.system("chmod +x /usr/local/bin/docker-compose")
	os.system("docker-compose up")
	print("Server has be installed and you can visit this http://localhost:8096/web/home.html  page to complete the setup")

def dockcontstart() : 
	print("Enter the name for your container ")
	conname=input()
	print("Enter the name of the image you want to use for the container")
	imagename=input()
	print("Do You want the container to be run in background yes or no")
	option=input()
	if option == 'yes' or option == 'y':
		print("Please wait while we are launching the container ")
		os.system("docker container run -dit --name {} {}".format(conname,imagename))
	

		success=os.system("docker container  ls | grep {}".format(conname))
		if success != ' ' :
			print("Container has been launched")
		else :
			print("Error in launching container")
	elif option == 'no' or option == 'n':
		os.system("docker container run -it --name {} {}".format(conname,imagename))    
def wordpress():
	print ("How do you want to configure the server Manual or Automatic (M OR A)")
	ans = input()
	if ans == 'm' or  ans == 'M':
		print("Enter the username ")
		username=input()
		flag=True
		while flag:
			print("Enter the password")
			password = getpass.getpass()
			print("Confirm Your Password")
			cpass=getpass.getpass()
			if password == cpass:
				flag=False
				print("Print enter the database name ")
				dbname=input()
				print("Please Wait while the server is being setup")
				wordpressservername="wordpress:5.1.1-php7.3-apache"
				mysqlservername="mysql:5.7"
				os.system("iptables -F")
				os.system("iptables -P FORWARD ACCEPT")
				os.system("firewall-cmd --zone=trusted --change-interface=docker0 --permanent ")
				os.system("firewall-cmd --zone=trusted --add-masquerade --permanent ")
				os.system("firewall-cmd --add-port=3306/tcp")
				os.system("firewall-cmd --reload")
				os.system("systemctl restart docker")
				os.system("docker pull {}".format(wordpressservername))
				os.system("docker pull {}".format(mysqlservername)) 
				os.system("docker rm -f $(docker ps -a)")
				os.system("docker run -dit -e MYSQL_ROOT_PASSWORD=0000 -e MYSQL_USER={} -e MYSQL_PASSWORD={} -e MYSQL_DATABASE={} -v mysql_storage:/var/lib/mysql --name mydbos mysql:5.7.28".format(username,password,dbname))
				os.system("docker run -dit -e WORDPRESS_DB_HOST=mydbos -e WORDPRESS_DB_USER={} -e WORDPRESS_DB_PASSWORD={} -e WORDPRESS_DB_NAME={} -v wp_storage:/var/www/html --name wpos -p 8081:80 --link mydbos wordpress:5.1.1-php7.3-apache".format(username,password,dbname))
				os.system("tput setaf 1")
				print("Your wordpress has been succesfully installed and configured visit the following ip address to  start the wordpress")
				os.system("tput setaf 7")
				os.system("docker inspect wpos | grep 'IPAddress'")
			else:
				print("Passwords do not match \n Please Try again")
			
				
	elif ans == 'a' or ans == 'A':
		print("Please Wait while the server is being setup")
		wordpressservername="wordpress:5.1.1-php7.3-apache"
		mysqlservername="mysql:5.7"
		os.system("iptables -F")
		os.system("iptables -P FORWARD ACCEPT")
		os.system("firewall-cmd --zone=trusted --change-interface=docker0 --permanent ")
		os.system("firewall-cmd --zone=trusted --add-masquerade --permanent ")
		os.system("firewall-cmd --add-port=3306/tcp")
		os.system("firewall-cmd --reload")
		os.system("systemctl restart docker")
		os.system("docker pull {}".format(wordpressservername))
		os.system("docker pull {}".format(mysqlservername)) 
		os.system("docker rm -f $(docker ps -a)")
		os.system("docker run -dit -e MYSQL_ROOT_PASSWORD=0000 -e MYSQL_USER=user -e MYSQL_PASSWORD=password -e MYSQL_DATABASE=mydb -v mysql_storage:/var/lib/mysql --name mydbos mysql:5.7.28")
		os.system("docker run -dit -e WORDPRESS_DB_HOST=mydbos -e WORDPRESS_DB_USER=user -e WORDPRESS_DB_PASSWORD=password -e WORDPRESS_DB_NAME=mydb -v wp_storage:/var/www/html --name wpos -p 8081:80 --link mydbos wordpress:5.1.1-php7.3-apache")
		os.system(" echo -e 'Mysql credentials \n Name of the os:mydbos \nUsername :user \n Password: password\n database name:mydb\n MySQLversion:mysql:5.7 \n Wordpress credentials \n Name of the os:wpos \n Wordpress version:wordpress:5.1.1-php7.3-apache' > /root/Desktop/WordpressInstallationDetails")
		os.system("tput setaf 1")
		print("Your wordpress has been succesfully installed and configured visit the following ip address to  start the wordpress")
		os.system("tput setaf 7")
		os.system("docker inspect wpos | grep 'IPAddress'")
# start of the program
intro()


while True:
	intro()
	print("\tMenu")
	print("\t1.  Install Docker")
	print("\t2.  Check Docker Version")
	print("\t3.  Check all Docker Images")
	print("\t4.  Download Docker Images")
	print("\t5.  Start a docker container")
	print("\t6.  Set up a Wordpress server")
	print("\t7.  Start Emby Media Server")
	print("\t8.  Pull up Docker monitor")
	print("\t9.  Delete docker images")	
	print("\t10.  Uninstall  Docker ? ")
	print("\t11. Exit")
	m = int(input())
	if m == 1:
		dockerinstall()
	elif m == 2:
		dockver()
	elif m == 3:
		dockimg()
	elif m == 4:
		image()
	elif m == 5:
		dockcontstart()
	elif m == 6:
		wordpress()
	elif m == 7:
		embyserver()
	elif m == 8:
		dockmonitor()
	elif m == 9:
		deletedockimage()
	elif m == 10:
		dockdelt()
	elif m == 11:
		exit()
	else :
		print("Error invalid input")
		print("Please select the option from above menu only")
	input("Press Enter  to continue")
	os.system("clear")
	
    
