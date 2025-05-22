# Week 0: Software Installation Guide

## Table of Contents

### 1. [ROS2 Installation](#1-ros2-installation)
- [System Requirements](#system-requirements)
- [Dual Boot/VM Options](#dual-bootvm-options)
- [Installation Steps (Windows)](#installation-steps-windows)
- [Installation Steps (Mac)](#installation-steps-mac)
- [Installation Steps (ARM)](#installation-steps-arm)
- [Testing Installation](#testing-installation)

### 2. [KiCAD, Proteus & STM32 Installation](#2-kicad-proteus--stm32-installation)
- [KiCAD Installation](#kicad-installation)
  - [Windows, macOS, Ubuntu](#windows-macos-ubuntu)
  - [System Requirements](#system-requirements-1)
  - [Installation Steps](#installation-steps)
- [Proteus Installation](#proteus-installation)
  - [Windows Only](#windows-only)
  - [Download and Setup](#download-and-setup)
- [STM32Cube Programmer](#stm32cube-programmer)
  - [Multi-platform Installation](#multi-platform-installation)
  - [USB Permissions Setup](#usb-permissions-setup)
  - [Troubleshooting](#troubleshooting)

### 3. [Fusion 360 Installation](#3-fusion-360-installation)
- [System Requirements](#system-requirements-2)
- [Installation Methods](#installation-methods)
  - [Windows Setup](#windows-setup)
  - [macOS Setup](#macos-setup)
  - [Ubuntu Setup (Community Methods)](#ubuntu-setup-community-methods)
- [Educational Access](#educational-access)
- [Troubleshooting Tips](#troubleshooting-tips)

### 4. [MATLAB & PyBullet Installation](#4-matlab--pybullet-installation)
- [MATLAB Setup](#matlab-setup)
  - [Windows Installation](#windows-installation)
  - [macOS Installation](#macos-installation)
  - [Ubuntu Installation](#ubuntu-installation)
- [PyBullet Setup](#pybullet-setup)
  - [Prerequisites](#prerequisites)
  - [Installation Steps](#installation-steps-1)
  - [Verification](#verification)
  - [Example Usage](#example-usage)

## Detailed Installation Guides

### 1. ROS2 Installation

#### System Requirements
- 64-bit Ubuntu 20.04 or later, or Windows 10 (1909 or later)
- At least 4 GB of RAM (8 GB recommended)
- Dual-core CPU or better
- Graphics card with OpenGL 2.1 support

#### Dual Boot/VM Options
- For dual boot, allocate at least 50 GB of space for Ubuntu.
- Recommended VM software: VirtualBox or VMware.
- Allocate at least 4 GB of RAM and 2 CPU cores to the VM.

#### Installation Steps (Windows)
1. Download the ROS2 installer for Windows.
2. Run the installer and follow the on-screen instructions.
3. Set up the environment variables as prompted.
4. Verify the installation by running `ros2 --version` in the command prompt.

#### Installation Steps (Mac)
1. Install Homebrew if not already installed.
2. Run `brew install ros2/ros2/ros2-desktop` in the terminal.
3. Source the ROS2 setup file: `source /opt/ros/foxy/setup.zsh`.
4. Verify the installation by running `ros2 --version` in the terminal.

#### Installation Steps (ARM)
1. Download the ARM version of ROS2.
2. Extract the files and navigate to the directory in the terminal.
3. Run `colcon build` to build the packages.
4. Source the setup file: `source install/setup.bash`.

#### Testing Installation
- Connect a ROS2 compatible device (e.g., robot, sensor).
- Run `ros2 topic list` to check if the device is detected.
- Publish and subscribe to a test topic to verify communication.

### 2. KiCAD, Proteus & STM32 Installation

#### KiCAD Installation

##### Windows, macOS, Ubuntu
- Download the latest version of KiCAD for your OS.
- Follow the installation wizard and select the default options.

##### System Requirements
- 64-bit processor
- At least 4 GB of RAM
- OpenGL 2.1 compatible graphics card

##### Installation Steps
- For Windows, run the installer and follow the prompts.
- For macOS, drag KiCAD to the Applications folder.
- For Ubuntu, run `sudo snap install kicad --classic`.

#### Proteus Installation

##### Windows Only
- Download the Proteus installer for Windows.
- Run the installer and follow the on-screen instructions.

##### Download and Setup
- Ensure you have a valid license for Proteus.
- During installation, select the components you wish to install.

#### STM32Cube Programmer

##### Multi-platform Installation
- Download the STM32Cube Programmer for your OS.
- Install it by following the provided instructions.

##### USB Permissions Setup
- On Linux, add your user to the `dialout` group: `sudo usermod -aG dialout $USER`.
- On Windows, install the ST-Link USB driver if prompted.

##### Troubleshooting
- If the programmer does not detect the STM32 device, check the USB connection and power supply.
- Ensure no other program is using the ST-Link interface.

### 3. Fusion 360 Installation

#### System Requirements
- 64-bit processor
- Windows 10 or later, macOS Mojave or later
- At least 4 GB of RAM (8 GB recommended)
- DirectX 11 compatible graphics card

#### Installation Methods

##### Windows Setup
1. Download the Fusion 360 installer for Windows.
2. Run the installer and follow the on-screen instructions.
3. Sign in with your Autodesk account to activate the software.

##### macOS Setup
1. Download the Fusion 360 installer for macOS.
2. Open the downloaded file and drag Fusion 360 to the Applications folder.
3. Sign in with your Autodesk account to activate the software.

##### Ubuntu Setup (Community Methods)
- Install Windows or macOS in a virtual machine.
- Follow the respective installation steps for Windows or macOS.

#### Educational Access
- Students and educators can get a free 1-year license.
- Sign up with a valid educational email on the Autodesk website.

#### Troubleshooting Tips
- For installation issues, check the Autodesk forums or contact support.
- Ensure your system meets the minimum requirements.

### 4. MATLAB & PyBullet Installation

#### MATLAB Setup

##### Windows Installation
1. Download the MATLAB installer for Windows.
2. Run the installer and follow the on-screen instructions.
3. Activate MATLAB using your MathWorks account.

##### macOS Installation
1. Download the MATLAB installer for macOS.
2. Open the downloaded file and drag MATLAB to the Applications folder.
3. Activate MATLAB using your MathWorks account.

##### Ubuntu Installation
1. Download the MATLAB installer for Linux.
2. Extract the files and navigate to the directory in the terminal.
3. Run `sudo ./install` and follow the prompts.

#### PyBullet Setup

##### Prerequisites
- Python 3.6 or later
- pip package manager

##### Installation Steps
1. Run `pip install pybullet` in the terminal or command prompt.
2. For GPU support, install the appropriate CUDA and cuDNN versions.

##### Verification
- Run `python -c "import pybullet as p; print(p.getPhysicsEngineVersion())"` to check the installation.

##### Example Usage
- Launch PyBullet GUI: `python -m pybullet_envs.examples.minitaur_gym_example`.
- Load and simulate a robot model in the PyBullet environment.

---

Ensure to follow each step carefully and refer to the official documentation of each software for more detailed instructions and troubleshooting.