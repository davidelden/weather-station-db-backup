import s3
import ConfigParser
from backup_db import get_filename, backup_db, remove_db_backup_from_os, BACKUP_PATH, DB_NAME
from argparse import ArgumentParser

config = ConfigParser.RawConfigParser()
config.read('config.py')

bucket_name = config.get('S3', 'BUCKET_NAME')
key_name = config.get('S3', 'KEY_NAME')

def main():
  parser = ArgumentParser()
  parser.add_argument('-t', '--type', dest='backup_type', help="Specify either 'hourly' or 'daily'.")
  
  args = parser.parse_args()
  filename = get_filename(args)  
  
  destination = r'%s/%s' % (BACKUP_PATH, filename)

  print "Backing up database '%s' to %s" % (DB_NAME, destination)
  backup_db(destination)

  s3.upload_backup_to_s3(destination, filename, bucket_name, key_name)
  s3.delete_expired_backups_from_s3(bucket_name, 24)

  remove_db_backup_from_os(destination)