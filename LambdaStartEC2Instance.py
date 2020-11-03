import boto3
tagName='Development'

def lambda_handler(event, context):
   ec2_con_re=boto3.resource(service_name='ec2',region_name='us-east-1')
   test_env_filter={'Name':'tag:Environmet','Values':[tagName]}
   for each in ec2_con_re.instances.filter(Filters=[test_env_filter]):
       each.start()
