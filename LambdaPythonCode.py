import boto3
import datetime

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    volume_id = 'vol-0b3c8675728114271'
    try:
        timestamp = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC')
        response = ec2.create_snapshot(
            VolumeId=volume_id,
            Description=f"Snapshot of {volume_id} created at {timestamp}",
            TagSpecifications=[
                {
                    'ResourceType': 'snapshot',
                    'Tags': [
                        {'Key': 'CreatedBy', 'Value': 'Lambda'},
                        {'Key': 'VolumeId', 'Value': volume_id},
                        {'Key': 'Timestamp', 'Value': timestamp}
                    ]
                }
            ]
        )
        snapshot_id = response['SnapshotId']
        print(f"Snapshot {snapshot_id} created successfully for {volume_id}.")
        return {
            'statusCode': 200,
            'body': f"Snapshot {snapshot_id} created successfully."
        }
    except Exception as e:
        print(f"Error creating snapshot: {str(e)}")
        return {
            'statusCode': 500,
            'body': f"Error creating snapshot: {str(e)}"
        }
