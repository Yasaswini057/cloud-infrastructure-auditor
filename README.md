## Features

- AWS Authentication Validation
- EC2 Instance Scanning
- EBS Volume Scanning
- Elastic IP Scanning
- Optimization Recommendations
- JSON Report Generation
- CSV Report Generation
- Logging Support

## Run Project

```bash
python main.py auth
python main.py scan


## Member Contributions

### Member 1 – CLI & Authentication (Yasaswini)

Completed Tasks:
- Implemented CLI commands using Typer
- Added AWS Authentication command (`auth`)
- Added Version command (`version`)
- Added Help command (`help-command`)
- Improved scan progress messages
- Added authentication success/failure messages
- Added AWS Account ID and Region display
- Added scan completion summary
- Tested CLI commands and authentication workflow

## Usage

Validate AWS Credentials:

python main.py auth

Show Version:

python main.py version

Show Commands:

python main.py help-command

Scan AWS Resources:

python main.py scan