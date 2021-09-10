import boto3
client = boto3.client('autoscaling')

response = client.describe_auto_scaling_groups()

res = [[i for i in response[x]] for x in response.keys()]
lst = res[0]
lst1 = []
lst2 = []
y = 0
for x in lst:
    try:
        print(f"AutoScaling group name: {x['AutoScalingGroupName']}")
        print(f"Launch Configuration Name: {x['LaunchConfigurationName']}")
        print(f"Termination Policy: {x['TerminationPolicies']}")
        while y < len(x['Instances']):
            lst1.append(x['Instances'][y]['InstanceId'])
            lst1.append(x['Instances'][y]['InstanceType'])
            lst1.append(x['Instances'][y]['LifecycleState'])
            lst1.append(x['Instances'][y]['HealthStatus'])
            y += 1
        print(f"{len(x['Instances'])} each of InstanceID, InstanceType, InstanceState, InstanceHealth: {lst1}")
        print("\n")
        y = 0
        lst1 = []
    except KeyError:
       print("\n")

#Output Example
'''
AutoScaling group name: madhu-asg
Launch Configuration Name: madhu-lc
Termination Policy: ['OldestLaunchConfiguration']
2 each of InstanceID, InstanceType, InstanceState, InstanceHealth: ['i-09b1256481', 'r5.xlarge', 'InService', 'Healthy', 'i-0d265796798845d', 'r5.xlarge', 'InService', 'Healthy']
'''
