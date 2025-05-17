import boto3
import json
from datetime import datetime

# Set the region
region = 'us-east-1'

# Create clients
ec2_client = boto3.client('ec2', region_name=region)

# Fetch all VPCs
def fetch_vpcs():
    response = ec2_client.describe_vpcs()
    return response['Vpcs']

# Fetch all EC2 instances
def fetch_ec2_instances():
    response = ec2_client.describe_instances()
    instances = []
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instances.append(instance)
    return instances

# Save data to a file
def save_to_file(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4, default=str)

def main():
    timestamp = datetime.now().strftime('%Y%m%d-%H%M%S')

    # Get VPC details
    vpcs = fetch_vpcs()
    save_to_file(vpcs, f'vpcs_{timestamp}.json')
    print(f"[+] VPC details saved to vpcs_{timestamp}.json")

    # Get EC2 details
    ec2_instances = fetch_ec2_instances()
    save_to_file(ec2_instances, f'ec2_instances_{timestamp}.json')
    print(f"[+] EC2 instance details saved to ec2_instances_{timestamp}.json")

if __name__ == '__main__':
    main()
