import boto3

ec2 = boto3.resource('ec2')
#instance = ec2.Instance('id')
client = boto3.client('ec2')

response = client.describe_instance_status(
)
res = [[i for i in response[x]] for x in response.keys()]
mylist = []
for x in res:
    mylist.append(x)
for y in mylist[0]:
    instance = ec2.Instance(y['InstanceId'])
    for tag in instance.tags:
        if tag["Key"] == 'Name':
            instancename = tag["Value"]
    print(f"Private, Public IP, InstanceType, InstanceState, KeyName, InstanceName, InstanceIDs: {instance.private_ip_address} | {instance.public_ip_address}| {instance.instance_type} | {instance.state['Name']} | {instance.key_name} | {instancename} | {y['InstanceId']}")





#Output
'''
Private, Public IP, InstanceType, InstanceState, KeyName, InstanceName, InstanceIDs: 10.7.0.54 | 13.59.6.92| r5.xlarge | running | terraform-1521082690-region | ImageEngine-frontend-green | i-0927d7e1ef08c7cd7
'''
