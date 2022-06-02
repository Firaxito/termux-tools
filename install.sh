#!/bin/bash

# System update
apt update && apt upgrade

# Storage permissions
termux-setup-storage

# Package install
pkg install python git openssh

# Python dependencies
pip install wheel
