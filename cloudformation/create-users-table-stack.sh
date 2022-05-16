STACK_NAME=project-rutherford-users-db-stack
TEMPLATE_LOCATION=file://${PWD}/template/project-rutherford-users-db-stack.yaml

aws cloudformation validate-template --template-body $TEMPLATE_LOCATION
aws cloudformation create-stack --stack-name $STACK_NAME --template-body $TEMPLATE_LOCATION
