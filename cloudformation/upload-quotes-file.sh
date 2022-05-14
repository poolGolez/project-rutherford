QUOTES_FILE_LOCATION=resources/quotes.json

aws s3api put-object --bucket project-rutherford-65819 --key quotes.json --body $QUOTES_FILE_LOCATION