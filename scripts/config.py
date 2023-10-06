from dotenv import load_dotenv
import os

"""
Set up environment variables in .env file in the root directory
"""

load_dotenv()

ACCOUNT_USERNAME = os.getenv('USERNAME')
ACCOUNT_PASSWORD = os.getenv('PASSWORD')
