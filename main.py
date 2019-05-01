import sys

from csvparser import CSVParser

# from models import Table
from utils import create_session

session = create_session('db.sqlite3')

FILE_NAME = sys.argv[1]

with open(FILE_NAME, 'r', encoding='utf8') as csv_file:
	csv_parser = CSVParser(csv_file, session=session)
	csv_parser.parse()

print('Done!')
