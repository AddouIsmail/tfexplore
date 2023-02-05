import json
import boto3
from tfstate_classes.tfstate_input import abstract_tfstate


class terraform_states(abstract_tfstate):

    def __init__(self, path_input: str):
        """
        path_input: s3 bucket name
        """
        super(terraform_states, self).__init__(path_input)

    def _get(self):
        for index, s3_key in enumerate(self.__get_files_s3_paths(self.path_input)):
            content = self.__get_json_from_s3(self.path_input, s3_key)
            content["graph_index"] = index
            self.tfstates[s3_key] = content
            self.mapping[index] = s3_key

    def __get_json_from_s3(self, bucket_name, key):
        s3 = boto3.client('s3')
        bucket = bucket_name

        response = s3.get_object(Bucket = bucket, Key = key)
        content = response['Body']
        jsonObject = json.loads(content.read())
        return jsonObject

    def __get_files_s3_paths(self, bucket_name):
        session = boto3.Session()
        s3 = session.resource('s3')
        my_bucket = s3.Bucket(bucket_name)
        for my_bucket_object in my_bucket.objects.all():
            yield my_bucket_object.key
