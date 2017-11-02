import os
import sys
import subprocess
import ConfigParser
from datetime import datetime

config = ConfigParser.RawConfigParser()
config.read('config.py')

DB_USER = config.get('PostgreSQL', 'DB_USER')
DB_NAME = config.get('PostgreSQL', 'DB_NAME')
BACKUP_PATH = config.get('Backup', 'BACKUP_PATH') + DB_NAME
FILENAME_PREFIX = config.get('Backup', 'FILENAME_PREFIX')

def get_filename(args):
  now = datetime.now()
  today = now.strftime('%Y%m%d')  
  hour = now.strftime('%H')

  if args.backup_type == 'hourly':
    filename = '%s_%s_h_%s.dump' % (FILENAME_PREFIX, today, hour)
    return filename

  elif args.backup_type == 'daily':
    filename = '%s_%s.dump' % (FILENAME_PREFIX, today)
    return filename

  else:
    parser.error('Ivalid argument.')
    sys.exit(1)

def backup_db(destination):
  ps = subprocess.Popen(['pg_dump', '-U', DB_USER, '-Fc', DB_NAME, '-f', destination], stdout=subprocess.PIPE)
  output = ps.communicate()[0]
  
  for line in output.splitlines():
    print line

def remove_db_backup_from_os(backup_path):
  os.remove(backup_path)