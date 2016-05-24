#!/bin/bash
mysql -uroot -e "create database myproject;"
mysql -uroot -e "CREATE USER 'box'@'localhost' IDENTIFIED BY '';"
mysql -uroot -e "GRANT ALL PRIVILEGES ON myproject.* TO 'box'@'localhost' WITH GRANT OPTION;"
mysql -uroot -e "FLUSH PRIVILEGES;"
