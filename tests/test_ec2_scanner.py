import unittest
from unittest.mock import patch

import boto3
from moto import mock_aws

from scanner.ec2_scanner import scan_ec2_instances


class TestEC2Scanner(unittest.TestCase):

    @mock_aws
    @patch("scanner.ec2_scanner.get_all_regions")
    @patch("scanner.ec2_scanner.create_aws_session")
    def test_scan_ec2(self, mock_session, mock_regions):

        # ----------------------------
        # MOCK AWS REGION
        # ----------------------------
        mock_regions.return_value = ["ap-south-1"]

        # ----------------------------
        # CREATE FAKE EC2 INSTANCE (MOTO)
        # ----------------------------
        ec2 = boto3.client("ec2", region_name="ap-south-1")

        ec2.run_instances(
            ImageId="ami-12345678",
            MinCount=1,
            MaxCount=1,
            InstanceType="t2.micro"
        )

        # ----------------------------
        # FORCE SCANNER TO USE MOTO EC2
        # ----------------------------
        mock_session.return_value.client.return_value = ec2

        # ----------------------------
        # RUN YOUR SCANNER
        # ----------------------------
        result = scan_ec2_instances()

        # ----------------------------
        # ASSERTIONS
        # ----------------------------
        self.assertIsInstance(result, list)
        self.assertGreaterEqual(len(result), 1)
        self.assertIn("InstanceId", result[0])

        print("✔ EC2 Scanner Test Passed")


if __name__ == "__main__":
    unittest.main()