import os
from dotenv import load_dotenv
from .common.database import test_db_setup

load_dotenv()

BASE_URL = os.getenv('BASE_URL')
db = test_db_setup()