def estimate_ec2_cost(ec2_data):
    """
    Estimate EC2 monthly cost
    """

    total_cost = 0

    instance_prices = {
        "t3.micro": 8.47,
        "t2.micro": 8.47,
        "t3.small": 16.79
    }

    for instance in ec2_data:

        instance_type = instance.get(
            "Type",
            ""
        )

        total_cost += instance_prices.get(
            instance_type,
            0
        )

    return round(
        total_cost,
        2
    )


def calculate_total_cost(ec2_data):
    """
    Wrapper function for analyzer compatibility
    """

    return estimate_ec2_cost(
        ec2_data
    )