#!/bin/bash

# Build script for CAMP package in ROS 2 Humble
# This script helps automate the build process

echo "Building CAMP package for ROS 2 Humble..."

# Check if we're in a ROS 2 workspace
if [ ! -f "src/camp/package.xml" ]; then
    echo "Error: This script should be run from the root of your ROS 2 workspace"
    echo "Make sure the camp package is in src/camp/"
    exit 1
fi

# Install dependencies
echo "Installing dependencies..."
rosdep install --from-paths src --ignore-src -r -y

# Build the package
echo "Building the camp package..."
colcon build --packages-select camp

# Check if build was successful
if [ $? -eq 0 ]; then
    echo "Build successful!"
    echo "Run 'source install/setup.bash' to source the workspace"
    echo "Then you can use the launch commands from the README"
else
    echo "Build failed! Check the error messages above."
    exit 1
fi
