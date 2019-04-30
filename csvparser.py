import csv
from datetime import datetime


class CSVParser:

    def __init__(self, filename):
        self.data = self.reader(filename)
        self.header = next(self.data)  # get csv header
        self.col_size = len(self.header)
        self.bad_data = []

    def parse(self):
        """
        Method for getting and saving data from CVS file
        """
        # list(map(self.store_data, self.data)) 

        # [self.store_data(entry) for entry in self.data]

        for entry in self.data:
            self.store_data(entry)
        self.write_bad_data()

    def store_data(self, entry):
        """
        Method for verification and saving entry to database
        :param entry: list
        """
        if len(entry) != self.col_size:
            self.bad_data.append(entry)
            return
        self.save(entry)

    def write_bad_data(self):
        """
        Method for writing unusual data to CVS file
        """
        timestamp = datetime.now().strftime('%Y-%b-%d-%H-%M')
        file_name = f'bad-data-{timestamp}.csv'
        with open(file_name, 'w', encoding='utf8') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerows(self.bad_data)

    def save(self, entry):
        pass

    @staticmethod
    def reader(csv_file):
        """
        Generator
        :param csv_file: file object
        :return: generator
        """
        datareader = csv.reader(csv_file)
        # yield next(datareader)  # yield the header row
        for row in datareader:
            yield row
