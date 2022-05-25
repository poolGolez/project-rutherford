STACK_NAME=project-rutherford-sqs-email-stack
TEMPLATE_LOCATION=file://${PWD}/template/project-rutherford-sqs-email-stack.yaml

aws cloudformation validate-template --template-body $TEMPLATE_LOCATION
aws cloudformation create-stack --stack-name $STACK_NAME --template-body $TEMPLATE_LOCATION
