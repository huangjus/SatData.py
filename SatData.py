# Author: Justin Huang
# GitHub username: huangjus
# Date: 5/2/23
# Description: This implementation of the `SatData` class has an `__init__` method to read the JSON file and store
# the data privately. The `save_as_csv` method takes a list of DBNs and saves a CSV file with corresponding rows,
# sorted by DBN. The code reads `sat.json`, filters by DBNs, and writes the output to `output.csv`.

import json


class SatData:
    """
    A class that reads a JSON file containing data on 2010 SAT results for New York City
    and writes the data to a text file in CSV format.
    """

    def __init__(self):
        """
        Initializes the SatData object by reading the JSON file and storing the data in a data member.
        """
        
        with open('sat.json') as f:
            self.data = json.load(f)

    def save_as_csv(self, dbns):
        """
        Writes a CSV file containing SAT data for the given DBNs.
        """
        
        rows = []
        headers = ['DBN', 'School Name', 'Number of Test Takers', 'Critical Reading Mean', 'Mathematics Mean',
                   'Writing Mean']
        rows.append(','.join(headers))
        for record in self.data:
            if record['DBN'] in dbns:
                row = [record['DBN'], record['School Name'], record['Number of Test Takers'],
                       record['Critical Reading Mean'], record['Mathematics Mean'],
                       record['Writing Mean']]
                row = ['"{}"'.format(x) if ',' in x else x for x in row]  # Handling commas in School Name
                rows.append(','.join(row))
        rows.sort()
        with open('output.csv', 'w') as f:
            f.write('\n'.join(rows))
