from typing import List
from dotenv import load_dotenv
import os

from models import Post

load_dotenv(dotenv_path='.env')

username = 'admin' #os.getenv('USERNAME')
password = 'admin' #os.getenv('PASSWORD')