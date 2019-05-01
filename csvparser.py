import csv
import logging

from datetime import datetime

from models import Table

logging.basicConfig(filename='files/csv_parser.log', level=logging.INFO)


class CSVParser:

    def __init__(self, csv_file, session):
        """
        :param csv_file: file object
        :param session: SQLalchemy session object
        """
        if not session:
            raise Exception('Session parameter is empty')
        self.session = session
        self.data = self.reader(csv_file)
        self.header = next(self.data)  # get csv header
        self.col_size = len(self.header)
        self.bad_data = []
        self.table_list = []
        self.successful = self.failed = 0
        # self.count = 0

    def parse(self):
        """
        Method for getting and saving data from CVS file
        """
        # list(map(self.store_data, self.data)) 

        # [self.store_data(entry) for entry in self.data]

        for entry in self.data:
            self.store_data(entry)
        self.write_bad_data()
        # self.session.add_all(self.table_list)
        self.session.commit()
        logging.info(f'{self.successful+self.failed} records received')
        logging.info(f'{self.successful} records successful')
        logging.info(f'{self.failed} records failed')

    def store_data(self, entry):
        """
        Method for verification and saving entry to database
        :param entry: list
        """
        if len(entry) != self.col_size:
            self.bad_data.append(entry)
            return
        self.save_one(entry)

    def write_bad_data(self):
        """
        Method for writing unusual data to CVS file
        """
        timestamp = datetime.now().strftime('%Y-%b-%d-%H-%M')
        file_name = f'files/bad-data-{timestamp}.csv'
        with open(file_name, 'w', encoding='utf8') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerows(self.bad_data)
            self.failed = len(self.bad_data)-1

    def save_one(self, entry):
        attr_with_data = dict(zip(self.header, entry))
        # self.table_list.append(Table(**attr_with_data))
        self.session.add(Table(**attr_with_data))
        self.successful += 1

    @staticmethod
    def reader(csv_file):
        """
        :param csv_file: file object
        :return: generator which return csv file line on each iteration
        """
        datareader = csv.reader(csv_file)
        # yield next(datareader)  # yield the header row
        for row in datareader:
            yield row
