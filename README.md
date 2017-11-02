# weather-station-db-backup
Backup weather station database and send file to AWS S3 from RaspberryPi.

This project uses the **ConfigParser** library, which reads variables from a configuration file. 

Add a `config.py` file to the root with the following variables (include headers in [ ]:

#### [PostgreSQL]
* DB\_USER
* DB\_NAME

#### [S3]
* BUCKET\_NAME
* KEY\_NAME

#### [Backup]
* BACKUP\_PATH
* FILENAME\_PREFIX