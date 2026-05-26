import unittest
from unittest.mock import patch

from scanner.ec2_scanner import scan_ec2_instances


class TestEC2Scanner(unittest.TestCase):

    @patch("scanner.ec2_scanner.create_aws_session")
    @patch("scanner.ec2_scanner.get_all_regions")
    def test_scan_ec2(self, mock_regions, mock_session):

        mock_regions.return_value = ["ap-south-1"]

        mock_client = mock_session.return_value.client.return_value
        mock_client.describe_instances.return_value = {
            "Reservations": []
        }

        result = scan_ec2_instances()

        self.assertEqual(type(result), list)


if __name__ == "__main__":
    unittest.main()