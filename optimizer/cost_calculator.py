def calculate_total_cost(ec2_data):
    """
    Calculate total monthly EC2 cost
    """

    cost = 0.0

    for instance in ec2_data:

        if instance["State"] == "running":
            cost += 8.47

    return round(cost, 2)


def calculate_potential_savings(ec2_data):
    """
    Calculate savings from underutilized EC2 instances
    """

    savings = 0.0

    for instance in ec2_data:

        if instance.get("Underutilized", False):
            savings += 8.47

    return round(savings, 2)