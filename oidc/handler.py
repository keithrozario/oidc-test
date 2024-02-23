import json
from aws_lambda_powertools import Logger

logger = Logger()

@logger.inject_lambda_context
def hello(event, context):
    
    logger.info("Collecting payment")
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
