#!/bin/bash
mysql -uroot -e "DROP database myproject;"
mysql -uroot -e "DROP USER 'box'@'localhost'"
mysql -uroot -e "FLUSH PRIVILEGES;"
