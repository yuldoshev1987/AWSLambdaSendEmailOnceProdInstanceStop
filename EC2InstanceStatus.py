import boto3
def lambda_handler(event, context):
   client=boto3.client('ec2')
   response = client.describe_instances()
   for data in response.get('Reservations'):
        flag=False
        for data2 in data.get('Instances'):
            State = data2['State']['Name']
            if State == 'stopped':
               flag=True
            if flag==True:
               for tags in data2['Tags']:
                   env=tags['Value']
                   if str(env).lower()=='production':
                       InstanceId = data2['InstanceId']
                       print('Instance state is :', State, 'Environment :', env,'InstanceId :',InstanceId)



