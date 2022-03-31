# import io
# import json
# import logging
# import random
# import time
# import zipfile
import boto3
# from botocore.exceptions import ClientError

def main(event, context):
    try:
        response = lambda_client.create_function(
            FunctionName=function_name,
            Description="AWS Lambda demo",
            Runtime='python3.8',
            Role=iam_role.arn,
            Handler=handler_name,
            Code={'ZipFile': deployment_package},
            Publish=True)
        function_arn = response['FunctionArn']
        logger.info("Created function '%s' with ARN: '%s'.",
                    function_name, response['FunctionArn'])
    except ClientError:
        logger.exception("Couldn't create function %s.", function_name)
        raise
    else:
        return function_arn