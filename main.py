import os
from dotenv import load_dotenv

api_key = os.getenv("str")
print(api_key)
print("Hello World")