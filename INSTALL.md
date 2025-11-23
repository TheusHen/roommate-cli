# Installation Guide

This guide provides detailed instructions for installing Roommate CLI on various platforms.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Quick Installation](#quick-installation)
- [Installation from Source](#installation-from-source)
- [Installation via pip (from GitHub)](#installation-via-pip-from-github)
- [Virtual Environment Setup](#virtual-environment-setup)
- [Platform-Specific Instructions](#platform-specific-instructions)
- [Verifying Installation](#verifying-installation)
- [Troubleshooting](#troubleshooting)

## Prerequisites

- **Python**: Version 3.8 or higher
- **pip**: Python package manager (usually comes with Python)
- **Git**: For cloning the repository (optional)

### Check Prerequisites

```bash
# Check Python version
python --version
# or
python3 --version

# Check pip version
pip --version
# or
pip3 --version
```

## Quick Installation

The fastest way to get started:

```bash
# Clone the repository
git clone https://github.com/TheusHen/roommate-cli.git
cd roommate-cli

# Install dependencies
pip install -r requirements.txt

# Run the application
python main.py
```

## Installation from Source

### Step 1: Clone the Repository

```bash
git clone https://github.com/TheusHen/roommate-cli.git
cd roommate-cli
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Run the Application

```bash
python main.py
```

## Installation via pip (from GitHub)

You can install directly from GitHub:

```bash
pip install git+https://github.com/TheusHen/roommate-cli.git
```

After installation, you can run the application using:

```bash
roommate
```

## Virtual Environment Setup

It's recommended to use a virtual environment to avoid dependency conflicts.

### Using venv (Recommended)

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Linux/Mac:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python main.py
```

### Using conda

```bash
# Create conda environment
conda create -n roommate python=3.12

# Activate environment
conda activate roommate

# Install dependencies
pip install -r requirements.txt

# Run the application
python main.py
```

## Platform-Specific Instructions

### Linux

```bash
# Install Python (if not already installed)
sudo apt-get update
sudo apt-get install python3 python3-pip git

# Clone and install
git clone https://github.com/TheusHen/roommate-cli.git
cd roommate-cli
pip3 install -r requirements.txt

# Run
python3 main.py
```

### macOS

```bash
# Install Homebrew (if not already installed)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Python
brew install python git

# Clone and install
git clone https://github.com/TheusHen/roommate-cli.git
cd roommate-cli
pip3 install -r requirements.txt

# Run
python3 main.py
```

### Windows

1. **Install Python**:
   - Download Python from [python.org](https://www.python.org/downloads/)
   - During installation, check "Add Python to PATH"

2. **Install Git** (optional):
   - Download from [git-scm.com](https://git-scm.com/download/win)

3. **Clone and Install**:
   ```cmd
   git clone https://github.com/TheusHen/roommate-cli.git
   cd roommate-cli
   pip install -r requirements.txt
   ```

4. **Run**:
   ```cmd
   python main.py
   ```

## Verifying Installation

After installation, verify that everything works:

```bash
# Check if dependencies are installed
pip list | grep rich
pip list | grep requests

# Try running the application
python main.py
```

You should see the Roommate banner and connection message.

## Development Installation

For contributors and developers:

```bash
# Clone the repository
git clone https://github.com/TheusHen/roommate-cli.git
cd roommate-cli

# Install in editable mode with development dependencies
pip install -e ".[dev]"

# Or use make
make dev-install
```

## Updating

To update to the latest version:

```bash
# If installed from source
cd roommate-cli
git pull origin main
pip install --upgrade -r requirements.txt

# If installed via pip
pip install --upgrade git+https://github.com/TheusHen/roommate-cli.git
```

## Uninstalling

To uninstall Roommate CLI:

```bash
# If installed via pip
pip uninstall roommate-cli

# If installed from source, just delete the directory
rm -rf roommate-cli
```

## Troubleshooting

### Common Issues

#### "python: command not found"

Try using `python3` instead of `python`.

#### "pip: command not found"

Try using `pip3` instead of `pip`, or install pip:

```bash
# Linux
sudo apt-get install python3-pip

# macOS
python3 -m ensurepip --upgrade
```

#### Permission Denied

If you get permission errors when installing, either:

1. Use a virtual environment (recommended)
2. Use the `--user` flag: `pip install --user -r requirements.txt`
3. Use `sudo` (not recommended): `sudo pip install -r requirements.txt`

#### Import Errors

If you get import errors for `rich` or `requests`:

```bash
pip install --force-reinstall -r requirements.txt
```

#### Connection Issues

If the app can't connect to the server:

1. Check your internet connection
2. Verify the API server is online
3. Try accessing https://roommate.theushen.me in your browser

## Getting Help

If you encounter any issues not covered here:

1. Check the [README](README.md) for general information
2. Search [existing issues](https://github.com/TheusHen/roommate-cli/issues)
3. Create a new issue with details about your problem

---

Happy chatting with your AI Roommate! 🏠
