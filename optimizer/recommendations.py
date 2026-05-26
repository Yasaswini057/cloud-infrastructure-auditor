def generate_recommendations(resources_data):
    """
    Evaluates resource data and returns actionable cost optimization recommendations.
    """
    recommendations = []
    
    # 1. Evaluate EC2 Instances
    ec2_instances = resources_data.get("ec2", [])
    for instance in ec2_instances:
        # Check for the Underutilized flag set by Member 2
        if instance.get("Underutilized", False):
            recommendations.append(
                f"Instance {instance['InstanceId']} is underutilized (Average CPU: {instance['AverageCPU']}% over 14 days). "
                f"Action: Consider downsizing or stopping this instance."
            )
            
        # Check for stopped instances (if your analyzer sets a flag or state)
        elif instance.get("State") == "stopped":
            recommendations.append(
                f"Instance {instance['InstanceId']} is stopped. "
                f"Action: Consider terminating it if it's no longer needed to save on associated costs."
            )

    # 2. Evaluate EBS Volumes
    ebs_volumes = resources_data.get("ebs", [])
    for volume in ebs_volumes:
        if volume.get("State") == "available":  # 'available' means unattached
            recommendations.append(
                f"EBS Volume {volume['VolumeId']} is unattached (State: available). "
                f"Action: Delete this volume to avoid unnecessary storage fees."
            )

    # 3. Evaluate Elastic IPs
    elastic_ips = resources_data.get("elastic_ips", [])
    for ip in elastic_ips:
        # If an Elastic IP isn't associated with an instance, flag it
        if not ip.get("InstanceId") and not ip.get("AssociationId"):
            recommendations.append(
                f"Elastic IP {ip['PublicIp']} is unassociated. "
                f"Action: Release this IP to stop incurring hourly AWS idle charges."
            )

    return recommendations