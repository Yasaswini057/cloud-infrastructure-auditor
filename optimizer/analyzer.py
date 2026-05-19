from optimizer.recommendations import generate_recommendations
from optimizer.cost_calculator import calculate_total_cost


def analyze_ec2_instances(ec2_data):
    """
    Analyze EC2 instances for optimization opportunities.
    """

    stopped_instances = []

    for instance in ec2_data:

        if instance.get("State", "").lower() == "stopped":

            stopped_instances.append(instance)

    return stopped_instances


def analyze_ebs_volumes(ebs_data):
    """
    Analyze EBS volumes for optimization opportunities.
    """

    unused_volumes = []

    for volume in ebs_data:

        if volume.get("State", "").lower() == "available":

            unused_volumes.append(volume)

    return unused_volumes


def analyze_elastic_ips(elastic_ip_data):
    """
    Analyze Elastic IPs for optimization opportunities.
    """

    unused_ips = []

    for ip in elastic_ip_data:

        if not ip.get("InstanceId"):

            unused_ips.append(ip)

    return unused_ips


def analyze_resources(resources):
    """
    Analyze all cloud resources and generate summary.
    """

    ec2_analysis = analyze_ec2_instances(
        resources.get("ec2", [])
    )

    ebs_analysis = analyze_ebs_volumes(
        resources.get("ebs", [])
    )

    elastic_ip_analysis = analyze_elastic_ips(
        resources.get("elastic_ips", [])
    )

    recommendations = generate_recommendations(resources)

    total_cost = calculate_total_cost(resources)

    analysis_result = {
        "stopped_ec2_instances": ec2_analysis,
        "unused_ebs_volumes": ebs_analysis,
        "unused_elastic_ips": elastic_ip_analysis,
        "estimated_monthly_cost": total_cost,
        "recommendations": recommendations
    }

    return analysis_result