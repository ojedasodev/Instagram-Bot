import sys
import os

# Get the parent directory of the src directory
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Append the parent directory to the sys.path list
sys.path.append(parent_dir)
