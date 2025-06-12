# my s3 bucket policy (JSON)
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PublicReadGetObject",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::toqeir-s3website-bucket/*"
        }
    ]
}

# my SNS topic policy (JSON)
{
  "Version": "2008-10-17",
  "Id": "__default_policy_ID",
  "Statement": [
    {
      "Sid": "__default_statement_ID",
      "Effect": "Allow",
      "Principal": {
        "AWS": "*"
      },
      "Action": [
        "SNS:GetTopicAttributes",
        "SNS:SetTopicAttributes",
        "SNS:AddPermission",
        "SNS:RemovePermission",
        "SNS:DeleteTopic",
        "SNS:Subscribe",
        "SNS:ListSubscriptionsByTopic",
        "SNS:Publish"
      ],
      "Resource": "arn:aws:sns:eu-west-2:200866909788:feedbackform",
      "Condition": {
        "StringEquals": {
          "AWS:SourceOwner": "200866909788"
        }
      }
    }
  ]
}

# AWS api lambda trigger (does require IAM policy)
# my api arn https://toqeirfeedbackapi.execute-api.region.amazonaws.com/prod/feedback
# example AWS s3 web link http://toqeir-s3website-bucket.s3-website.eu-west-2.amazonaws.com/index.html