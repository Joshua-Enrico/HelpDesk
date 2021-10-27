#!/usr/bin/env bash
pip install -r requirements.txt
sudo apt-get install python3-dev default-libmysqlclient-dev build-essential
sudo service mysql start
echo "ALTER USER 'root'@'localhost' IDENTIFIED BY '1';" | sudo mysql -u root -proot
echo "CREATE USER 'Helpdesk'@'localhost' IDENTIFIED BY 'Helpdesk';" | mysql -u root -p1
echo "grant usage on *.* to 'Helpdesk'@'localhost';" | mysql -u root -p1
echo "grant all privileges on HelpDesk.* to 'Helpdesk'@'localhost';" | mysql -u root -p1
sudo mysql -u root -p1 HelpDesk < HelpDesk.sql