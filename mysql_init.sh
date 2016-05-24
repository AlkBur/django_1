#!/bin/bash
mysql -uroot -pbox -e "create database myproject;"
mysql -uroot -pbox -e "CREATE USER 'box'@'localhost' IDENTIFIED BY 'box';"
mysql -uroot -pbox -e "GRANT ALL PRIVILEGES ON myproject.* TO 'box'@'localhost' WITH GRANT OPTION;"
mysql -uroot -pbox -e "FLUSH PRIVILEGES;"
