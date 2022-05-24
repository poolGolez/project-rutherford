STACK_NAME=project-rutherford-email-db-stack
TEMPLATE_LOCATION=file://${PWD}/template/project-rutherford-email-db-stack.yaml

aws cloudformation validate-template --template-body $TEMPLATE_LOCATION
aws cloudformation create-stack --stack-name $STACK_NAME --template-body $TEMPLATE_LOCATION
