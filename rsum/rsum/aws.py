"""S3 hosting static files module config."""
import os

# The AWS region to connect to.
AWS_REGION = "us-west-2"
# The AWS access key to use.
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
# The AWS secret access key to use.
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
# The optional AWS session token to use.
AWS_SESSION_TOKEN = ""
