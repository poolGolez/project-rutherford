STACK_NAME=project-rutherford-s3-stack
TEMPLATE_LOCATION=file://${PWD}/template/project-rutherford-s3-stack.yaml

aws cloudformation validate-template --template-body $TEMPLATE_LOCATION
aws cloudformation create-stack --stack-name $STACK_NAME --template-body $TEMPLATE_LOCATION
