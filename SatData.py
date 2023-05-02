# Author: Justin Huang
# GitHub username: huangjus
# Date: 5/2/23
# Description: This implementation of the `SatData` class has an `__init__` method to read the JSON file and store
# the data privately. The `save_as_csv` method takes a list of DBNs and saves a CSV file with corresponding rows,
# sorted by DBN. The code reads `sat.json`, filters by DBNs, and writes the output to `output.csv`.

import json


class SatData:
    """
    This class reads a JSON file containing data on 2010 SAT results for
    New York City and writes the data to a text file in CSV format.
    """

    def __init__(self):
        """
        Initializes the SatData class by reading the JSON file and storing
        the data in a private data member.
        """

        with open("sat.json", "r") as file:
            self.__data = json.load(file)

    def save_as_csv(self, dbns):
        """
        Takes a list of DBNs (district bureau numbers) as a parameter and
        saves a CSV file with rows corresponding to the DBNs in the list.
        The rows in the CSV file are sorted in ascending order by DBN.
        """

        filtered_data = sorted([row for row in self.__data if row["DBN"] in dbns], key=lambda x: x["DBN"])

        with open("output.csv", "w") as csvfile:
            csvfile.write(
                "DBN,School Name,Number of Test Takers,Critical Reading Mean,Mathematics Mean,Writing Mean\n")

            for row in filtered_data:
                school_name = row["School Name"]
                if ',' in school_name:
                    school_name = f'"{school_name}"'

                csvfile.write(
                    f'{row["DBN"]},{school_name},{row["Number of Test Takers"]},'
                    f'{row["Critical Reading Mean"]},{row["Mathematics Mean"]},'
                    f'{row["Writing Mean"]}\n')
