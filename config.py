from dotenv import load_dotenv
import os

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

#print("API KEY:", GOOGLE_API_KEY)

#Why?

#Instead of reading the .env file everywhere, the rest of your project can simply import: