#!/bin/bash
sudo mysql -uroot -pbox -e "DROP database myproject;"
sudo mysql -uroot -pbox -e "DROP USER 'box'@'localhost'"
sudo mysql -uroot -pbox -e "FLUSH PRIVILEGES;"
