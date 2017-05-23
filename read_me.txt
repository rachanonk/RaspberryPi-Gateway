installation step

#install nodejs for rpi2 or rpi3 against ARM v7
mkdir node
cd node
wget https://nodejs.org/dist/v6.2.0/node-v6.2.0-linux-armv7l.tar.xz
tar -xvf node-v6.2.0-linux-armv7l.tar.xz
cd node-v6.2.0-linux-armv7l
#copies also readme and other not required files
sudo cp -R * /usr/local/  

sudo reboot
node -v  
npm -v

#the console output should be for node v6.2.0 and npm 3.8.9

 	
# install pm2 globally, because we use it for all our NodeJS apps
sudo npm install -g pm2

#install mysql
sudo apt-get install mysql-server --fix-missing
sudo apt-get install mysql-client

#check if mySQL is Running and the version
mysql -u root -p -e 'SHOW VARIABLES LIKE "%version%";'

#console output should be MySQL Version 5.5.44

# install mysql nodeadmin - a ui for mysql instead phpmysql
mkdir nodeadmin
cd nodeadmin
npm install nodeadmin

# For starting Nodeadmin, we have to create a NodeJS App Starter
sudo nano nodeadmin.js #This one is on Git
# create middleware nodejs and run ---> url http://your-ip:3333/nodeadmin

pm2 start nodeadmin.js

# Inside the shell
cd /etc/init.d/
# Create a Nodeadmin Starter Script
sudo nano nodeadmin-init.sh //This one is also on git

# make the file executable
sudo chmod +x /etc/init.d/nodeadmin-init.sh
# register and update the booting queue
sudo update-rc.d -f nodeadmin-init.sh defaults
# after a lot install, lets restart our rPI
sudo reboot
