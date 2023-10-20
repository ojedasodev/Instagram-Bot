from dotenv import load_dotenv
import os

"""
Create an .env file in the root directory
and set up env variables
"""

load_dotenv()

ACCOUNT_USERNAME = os.getenv('USERNAME')
ACCOUNT_PASSWORD = os.getenv('PASSWORD')
