import boto3
from .automl import AWS_ACC_KEY_ID, AWS_SEC_ACC_KEY

client_cb = boto3.client('codebuild',
						aws_access_key_id=AWS_ACC_KEY_ID,
						aws_secret_access_key=AWS_SEC_ACC_KEY,
						region_name='us-west-2')

FLASK_PROJECT 	= 'ALL_FLASK_Image_Builder'

def build_image(username, project_id):
	print(f"build_image : INFO : Building image for user: {username} and project: {project_id}...")
	image_tag = f'project_{project_id}'
	response = client_cb.start_build(
	    projectName=FLASK_PROJECT,
	    environmentVariablesOverride=[
	        {
	            'name': 'IMAGE_TAG',
	            'value': image_tag,
	            'type': 'PLAINTEXT'
	        },
			{
	            'name': 'USERNAME',
	            'value': username,
	            'type': 'PLAINTEXT'
	        },
			{
	            'name': 'PROJECT_ID',
	            'value': str(project_id),
	            'type': 'PLAINTEXT'
	        },
	    ]
	)
	print(f'build_image : INFO : Done!')
	if int(response['ResponseMetadata']['HTTPStatusCode']) == 200:
		return f'749868801319.dkr.ecr.us-west-2.amazonaws.com/flask_images:{image_tag}'
	else:
		return False
