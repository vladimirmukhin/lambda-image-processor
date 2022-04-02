import boto3
from PIL import Image

def lambda_handler(event,context):
    s3 = boto3.client('s3')

    print("download file")
    s3.download_file(event["Records"][0]["s3"]["bucket"]["name"], event["Records"][0]["s3"]["object"]["key"], '/tmp/file')

    print("process file")
    image = Image.open('/tmp/file')
    data = list(image.getdata())
    image_without_exif = Image.new(image.mode, image.size)
    image_without_exif.putdata(data)
    image_without_exif.save('/tmp/file_without_exif.jpg')

    print("upload file")
    s3.upload_file('/tmp/file_without_exif.jpg', 'destination20220402', event["Records"][0]["s3"]["object"]["key"])

if __name__== "__main__":
    handler(None,None)
