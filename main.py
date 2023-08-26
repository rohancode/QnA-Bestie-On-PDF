import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access environment variables
api_key = os.getenv("API_KEY")
database_url = os.getenv("DATABASE_URL")
debug_mode = os.getenv("DEBUG")

# Print the values
print("API Key:", api_key)
print("Database URL:", database_url)
print("Debug Mode:", debug_mode)