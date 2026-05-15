def analyze_ec2_instances(ec2_data):
    """
    Analyze EC2 instances for optimization opportunities
    """

    stopped_instances = []

    for instance in ec2_data:

        if instance["State"] == "stopped":

            stopped_instances.append(instance)

    return stopped_instances
def analyze_ebs_volumes(ebs_data):
    """
    Analyze EBS volumes for optimization opportunities
    """

    unused_volumes = []

    for volume in ebs_data:

        if volume["State"] == "available":

            unused_volumes.append(volume)

    return unused_volumes
def analyze_elastic_ips(elastic_ip_data):
    """
    Analyze Elastic IPs for optimization opportunities
    """

    unused_ips = []

    for ip in elastic_ip_data:

        if ip.get("AllocationId"):

            unused_ips.append(ip)

    return unused_ips