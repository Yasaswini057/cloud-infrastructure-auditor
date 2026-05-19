def calculate_total_cost(resources):
    """
    Calculate estimated total monthly cost
    of all scanned cloud resources.
    """

    total_cost = 0

    # EC2 Costs
    for ec2 in resources.get("ec2", []):
        total_cost += ec2.get("monthly_cost", 0)

    # EBS Costs
    for ebs in resources.get("ebs", []):
        total_cost += ebs.get("monthly_cost", 0)

    # Elastic IP Costs
    for eip in resources.get("elastic_ips", []):
        total_cost += eip.get("monthly_cost", 0)

    return total_cost