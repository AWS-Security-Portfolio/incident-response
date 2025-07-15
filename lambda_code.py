import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    
    # --- CHANGE THESE TO MATCH YOUR ENVIRONMENT ---
    instance_id = 'i-xxxxxxxxxxxxxxxxx'  # Replace with your EC2 instance ID
    vpc_id = 'vpc-xxxxxxxxxxxxxxxxx'     # Replace with your VPC ID
    
    # Create a new security group (if not already created)
    quarantine_sg_name = 'quarantine-sg'
    sg_response = ec2.create_security_group(
        GroupName=quarantine_sg_name,
        Description='Security group for quarantined instances',
        VpcId=vpc_id
    )
    quarantine_sg_id = sg_response['GroupId']
    
    # (Optional) Ensure no inbound rules exist (default for new SG)
    # You can explicitly remove all inbound rules if necessary:
    # ec2.revoke_security_group_ingress(GroupId=quarantine_sg_id, IpPermissions=[])
    
    # Attach the quarantine security group to the instance
    ec2.modify_instance_attribute(
        InstanceId=instance_id,
        Groups=[quarantine_sg_id]
    )
    
    return {
        'statusCode': 200,
        'body': f'Instance {instance_id} quarantined with security group {quarantine_sg_id}.'
    }
