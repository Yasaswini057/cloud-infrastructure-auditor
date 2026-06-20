# Cloud Infrastructure Auditor & Cost Optimizer

A production-level Python CLI tool designed to scan AWS cloud infrastructure, detect underutilized resources, estimate cloud costs, and generate optimization reports for FinOps and DevOps teams.

---

# Features

- AWS Authentication Validation
- Multi-Region AWS Resource Scanning
- EC2 Instance Scanning
- EBS Volume Scanning
- Elastic IP Scanning
- CloudWatch CPU Utilization Analysis
- Underutilized EC2 Detection
- Optimization Recommendations
- Cost Estimation
- JSON Report Generation
- CSV Report Generation
- YAML Report Generation
- Typer-based CLI Commands
- Rich Terminal Table Outputs
- Cleanup Dry-Run & Execute Support
- Logging Support
- Moto-based AWS Mock Testing

---

# Project Architecture

CLI → AWS Authentication → Resource Scanners → CloudWatch Analysis → Optimizer → Report Generator → Output Reports

---

# Installation

```bash
git clone <repository-url>

cd cloud-infrastructure-auditor

python -m venv env

env\Scripts\activate

pip install -r requirements.txt
```

---

# Usage

## Validate AWS Credentials

```bash
python main.py auth
```

## Show Version

```bash
python main.py version
```

## Show Commands

```bash
python main.py help-command
```

## Scan AWS Resources

```bash
python main.py scan
```

## Cleanup Dry Run

```bash
python main.py cleanup --dry-run
```

## Cleanup Execute

```bash
python main.py cleanup --execute
```

---

# Generated Reports

The project generates:

- JSON Reports
- CSV Reports
- YAML Reports

Reports are automatically generated inside:

```plaintext
output/reports/
```

---

# Optimization Features

- Detect underutilized EC2 instances
- Detect unattached EBS volumes
- Detect unused Elastic IPs
- Estimate cloud resource costs
- Generate FinOps optimization summaries

---

# Technologies Used

- Python
- Boto3
- Typer
- Rich
- PyYAML
- Moto
- PyTest
- AWS CloudWatch

---

# Screenshots

## CLI Scan Output

(Add screenshot here)

## Rich Table Output

(Add screenshot here)

## Generated Reports

(Add screenshot here)

---

# Member Contributions

### Member 1 – CLI & Authentication (Yasaswini)

- Implemented Typer CLI structure
- Added authentication workflow
- Added cleanup commands
- Improved command handling and scan summaries

### Member 2 – AWS Scanner & Optimization (Hasini)

- Implemented EC2, EBS, and Elastic IP scanners
- Added CloudWatch CPU analysis
- Added underutilized resource detection
- Added optimization recommendation logic

### Member 3 – Reports & Documentation (Swetha)

- Implemented JSON, CSV, and YAML report exports
- Improved report generation workflow
- Enhanced README documentation
- Added output report formatting support

### Member 4 – Testing & Packaging (Asheela)

- Added PyTest test cases
- Implemented Moto AWS mocking
- Added setup.py packaging
- Generated standalone executable build

---

# Project Status

Project implementation completed successfully with AWS scanning, optimization analysis, reporting, testing, and CLI workflow integration.

# Cloud Infrastructure Auditor

AWS Cost Optimization CLI Tool

## Features

* AWS Authentication
* EC2 Instance Scanner
* EBS Volume Scanner
* Elastic IP Scanner
* CPU Utilization Analysis
* Underutilized EC2 Detection
* Cost Optimization Recommendations
* Cleanup Dry Run
* JSON Report Export
* Interactive CLI using Typer and Rich

## Commands

Validate AWS Credentials

python main.py auth

Scan AWS Infrastructure

python main.py scan

Cleanup EC2 Instance (Dry Run)

python main.py cleanup <instance_id>

Show Version

python main.py version

Show Help

python main.py help-command

## Output

* EC2 Scan Results
* EBS Scan Results
* Elastic IP Scan Results
* Infrastructure Summary
* Optimization Summary
* Cost Estimation
* JSON Report
* Updated project documentation
* Rectify Errors