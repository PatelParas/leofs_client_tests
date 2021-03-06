from boto.s3.connection import S3Connection, OrdinaryCallingFormat
from boto.s3.bucket import Bucket
from boto.s3.key import Key

AWS_ACCESS_KEY = "05236"
AWS_SECRET_ACCESS_KEY = "802562235"
BUCKET_NAME = "test"

conn = S3Connection(AWS_ACCESS_KEY,
    AWS_SECRET_ACCESS_KEY,
    host = "localhost",
    port = 8080,
    calling_format = OrdinaryCallingFormat(),
    is_secure = False
)

try:
    # Create bucket
    buckets = conn.create_bucket(BUCKET_NAME)
    print "Bucket Created Successfully"

    # Show buckets
    print "--------Bucket List------"
    for bucket in conn.get_all_buckets():
        print bucket
    
    # Get Bucket 
    bucket = conn.get_bucket(BUCKET_NAME,validate=False)
    print "Get Bucket Successfully"
    
    # Create object
    s3_object = bucket.new_key("text")
    s3_object.set_contents_from_string("This is a text.")
    print "File Created Successfully"

    # Get Object
    s3_object = bucket.get_key("text")
    print "Object Data is :"
    print s3_object

    # Read object
    print s3_object.read()

    # Write from file
    print "Uploading file.."
    s3_object = bucket.new_key("testFile")
    s3_object.set_contents_from_filename("../temp_data/testFile")
    
    # Print multipart_upload.upload()
    print "File uploaded Successfully"

    # File Download
    s3_object.get_contents_to_filename("testFile.copy")
    print "File Downloaded Successfully"
    
    # File copy
    bucket.copy_key( "testFile.copy", BUCKET_NAME, "testFile" )
    print "File copied successfully"

    # Show Objects
    print"--------------------------------List Objects-----------------------------------"
    for key in bucket.list():
        print key.name , "\t\t" , key.size , "\t\t" , key.last_modified

    # Delete objects
    print"--------------------------------Delete Objects---------------------------------"
    for key in bucket.list():
        print key.name , "Deleted Successfully", key.delete()

    # Get deleted key
    s3_object = bucket.get_key("testFile")
    
    # It should print None
    print s3_object
finally:
    
    # Delete Bucket
    bucket = conn.get_bucket(BUCKET_NAME,validate=False)
    bucket.delete()
    print "Bucket deleted Successfully \n"
