import json
import boto3

sns = boto3.client('sns')

def lambda_handler(event, context):
    body = json.loads(event['body'])

    message = f"""
    New Feedback Received:

    First Name: {body.get('firstname')}
    Last Name: {body.get('lastname')}
    Email: {body.get('email')}
    Country: {body.get('country')}
    Message: {body.get('subject')}
    """

    # Replace TopicArn with your SNS Topic ARN
    response = sns.publish(
        TopicArn='arn:aws:sns:eu-west-2:200866909788:feedbackform',
        Message=message,
        Subject='New Feedback Form Submission'
    )

    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Feedback submitted successfully!'})
    }