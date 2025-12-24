# Python-for-DevOps

[![Python](https://img.shields.io/badge/Python-3.x-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![GitHub](https://img.shields.io/badge/GitHub-developedbyviv-lightgrey)](https://github.com/developedbyviv)

A comprehensive collection of Python scripts and programs designed to solve common DevOps challenges and automate system administration tasks.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Scripts](#scripts)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## 🎯 Overview

This repository contains practical Python solutions for DevOps professionals and system administrators. The scripts cover essential tasks including infrastructure monitoring, system health checks, backup validation, configuration management, and common programming challenges used in automation workflows.

Whether you're new to DevOps or an experienced engineer, these scripts serve as learning resources and can be directly integrated into your automation pipelines.

## ✨ Features

- **Server Health Monitoring**: Scripts to check server CPU usage and health status
- **Backup Management**: Automated backup validation and verification
- **Configuration Management**: Environment configuration handling using dictionaries
- **System Information**: Scripts to list running servers and monitor system status
- **Deployment Logic**: Decision-making logic for deployment scenarios
- **Basic Programming**: Fundamental Python patterns for DevOps use cases

## 📂 Scripts

### System Administration & Monitoring

| Script | Purpose |
|--------|----------|
| `serverHealthStatus.py` | Monitor server health based on CPU usage thresholds |
| `multipleServerStatus.py` | Check health status across multiple servers |
| `listOfRunningServers.py` | Display and manage running servers |

### Backup & Data Management

| Script | Purpose |
|--------|----------|
| `backupValidation.py` | Validate backup files and confirm availability |

### Configuration Management

| Script | Purpose |
|--------|----------|
| `environmentConfigurations.py` | Manage environment variables and configurations using dictionaries |
| `immutableConfig.py` | Handle immutable configuration patterns |

### Deployment & Operations

| Script | Purpose |
|--------|----------|
| `deploymentLogicDecision.py` | Decision logic for deployment scenarios |

### Basic Python Patterns

| Script | Purpose |
|--------|----------|
| `checkEvenOrOdd.py` | Identify even and odd numbers |
| `printOddNumberUntillValue.py` | Generate odd numbers up to a specified value |
| `findLargestOfTwoNumber.py` | Compare and find the larger of two numbers |
| `factorialOfValue.py` | Calculate factorial values |

## 🚀 Installation

### Prerequisites

- Python 3.6 or higher
- pip (Python package manager)
- Basic understanding of DevOps concepts

### Clone the Repository

```bash
git clone https://github.com/developedbyviv/Python-for-DevOps.git
cd Python-for-DevOps
```

### (Optional) Create a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\\Scripts\\activate
```

## 💻 Usage

Each script can be run independently from the command line:

```bash
python3 scriptName.py
```

### Example: Check Server Health

```bash
python3 serverHealthStatus.py
```

This will display the server's health status based on current CPU usage:
- **CPU < 50%**: Server is healthy
- **CPU 50-80%**: Server under moderate load
- **CPU > 80%**: High CPU usage, scaling required

### Example: Validate Backups

```bash
python3 backupValidation.py
```

Checks if backup files exist and reports their status.

### Example: Environment Configuration

```bash
python3 environmentConfigurations.py
```

Manages and displays environment-specific configurations.

## 📝 Script Details

### Monitoring Scripts

The monitoring scripts use conditional logic to evaluate system metrics and provide actionable insights. They're designed to integrate with larger monitoring systems or cron jobs.

### Configuration Scripts

Configuration scripts demonstrate best practices for managing environment-specific settings, which is crucial in DevOps workflows across development, staging, and production environments.

### Helper Scripts

Basic programming scripts provide foundational patterns used throughout DevOps automation, including:
- Conditional decision-making
- Data processing and transformation
- Loop iteration patterns
- Mathematical operations

## 🤝 Contributing

Contributions are welcome! If you'd like to improve these scripts or add new ones:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/improvement`)
3. Make your changes and test thoroughly
4. Commit with clear messages (`git commit -m 'Add new feature'`)
5. Push to the branch (`git push origin feature/improvement`)
6. Open a Pull Request

## 📄 License

This project is licensed under the MIT License. See the LICENSE file for details.

## 👨‍💻 Author

**Vivek Singh Bhandari**
- GitHub: [@developedbyviv](https://github.com/developedbyviv)
- DevOps Engineer | Full-Stack Developer

## 📞 Support

If you have questions or find issues:

1. Check existing [Issues](https://github.com/developedbyviv/Python-for-DevOps/issues)
2. Open a new Issue with detailed description
3. Include relevant script name and error messages

## 🔗 Related Resources

- [Python Documentation](https://docs.python.org/3/)
- [DevOps Best Practices](https://en.wikipedia.org/wiki/DevOps)
- [System Administration with Python](https://realpython.com/)

---

**Last Updated**: December 24, 2025

Made with ❤️ for the DevOps community
