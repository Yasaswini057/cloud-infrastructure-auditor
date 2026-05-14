def generate_recommendations(resources):
    """
    Generate optimization recommendations
    based on scanned cloud resources.
    """

    recommendations = []

    # EC2 Recommendations
    for ec2 in resources.get("ec2", []):

        state = ec2.get("state", "").lower()
        instance_id = ec2.get("instance_id", "Unknown")

        if state == "stopped":
            recommendations.append(
                f"EC2 Instance {instance_id} is stopped. Consider terminating unused instances."
            )

    # EBS Recommendations
    for ebs in resources.get("ebs", []):

        volume_id = ebs.get("volume_id", "Unknown")
        state = ebs.get("state", "").lower()

        if state == "available":
            recommendations.append(
                f"EBS Volume {volume_id} is unattached. Consider deleting unused volumes."
            )

    # Elastic IP Recommendations
    for eip in resources.get("elastic_ips", []):

        public_ip = eip.get("public_ip", "Unknown")

        if not eip.get("instance_id"):
            recommendations.append(
                f"Elastic IP {public_ip} is unassociated. Consider releasing it."
            )

    # No recommendations
    if not recommendations:
        recommendations.append(
            "No optimization recommendations found."
        )

    return recommendations