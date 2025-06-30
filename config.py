from typing import List
from dotenv import load_dotenv
import os
from models import Post


load_dotenv(dotenv_path='.env')

username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")