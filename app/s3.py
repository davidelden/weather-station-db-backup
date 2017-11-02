import boto3
import pytz
from datetime import datetime, timedelta

def upload_backup_to_s3(file_location, filename, bucket_name, key_name):
  s3 = boto3.client('s3')
  s3.upload_file(file_location, bucket_name, key_name+filename)

def delete_expired_backups_from_s3(bucket_name, expiration_hours):
  s3 = boto3.resource('s3')
  bucket = s3.Bucket(bucket_name)
  utc = pytz.utc
  expiration = timedelta(hours=expiration_hours)

  for obj in bucket.objects.all():
    if obj.key.endswith('.dump'):    
      obj_age = datetime.now(utc) - obj.last_modified.replace(tzinfo=utc)
      obj_expired = obj_age >= expiration
      
      if obj_expired:        
        response = obj.delete()        
        print 'Response status: %s' % response['ResponseMetadata']['HTTPStatusCode']