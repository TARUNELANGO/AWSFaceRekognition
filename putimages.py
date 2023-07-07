import boto3

s3 = boto3.resource('s3')

# Get list of objects for indexing
images=[('Amma2.jpg','Amma'),
      ('Tarun2.jpg','Tarun'),
      ('Nishok2.jpg','Nishok'),
      ('Vivek4.jpg','Vivek'),
      ('Maanu2.jpg','Maanu'),
      ('Tarun1.jpg','Tarun')
      ]

# Iterate through list to upload objects to S3   
for image in images:
    file = open(image[0],'rb')
    object = s3.Object('facecollection-bucket','index/'+ image[0])
    ret = object.put(Body=file,
                    Metadata={'FullName':image[1]})