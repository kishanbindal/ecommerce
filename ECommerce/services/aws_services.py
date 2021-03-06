import boto3
from botocore.client import Config
import dotenv
import os

base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
env_path = os.path.join(base, '.env')

dotenv.load_dotenv(dotenv_path=env_path)


class AwsServices:

    def __init__(self):
        self.s3_client = boto3.client('s3', config=Config(signature_version='s3v4'), region_name='ap-south-1')
        self.bucket = os.getenv('AWS_STORAGE_BUCKET_NAME')

    def _generate_url(self, object_name):
        url = f"https://f{self.bucket}s3.ap-south.amazonaws.com/{object_name}"
        return url

    def upload_img(self, img_file, object_name):
        # import pdb
        # pdb.set_trace()
        # if " " in object_name:
        #     obj_name = object_name.replace(" ", "_")
        # else:
        #     obj_name = object_name
        self.s3_client.upload_fileobj(img_file, self.bucket, object_name)
        url = self._generate_url(object_name)
        return url

    def get_presigned_url(self, object_name):

        presigned_url = self.s3_client.generate_presigned_url('get_object',
                                                              Params={
                                                                  'Bucket': self.bucket,
                                                                  'Key': object_name,
                                                              },
                                                              ExpiresIn=604800,)
        return presigned_url
