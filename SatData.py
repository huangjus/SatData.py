# Author: Justin Huang
# GitHub username: huangjus
# Date: 5/2/23
# Description: This code defines a class called SatData that reads a JSON file containing 2010 SAT results for
# New York City and writes the data to a text file in CSV format. The class has an __init__ method that reads the
# file and stores the data in a private data member. It also has a method named save_as_csv that takes a list of DBNs
# and saves a CSV file with rows corresponding to the DBNs in the list, sorted in ascending order by DBN.
# The CSV file is named output.csv


import json


class SatData:
    """
    A class to read SAT data from a JSON file and write selected rows to a CSV file.
    """

    def __init__(self):
        """
        Constructor that reads the JSON file and stores the data in a private data member.
        """

        self.__sat_data = []
        with open("sat.json", "r") as file:
            self.__sat_data = json.load(file)

    def save_as_csv(self, dbns):
        """
        A method that takes a list of DBNs and saves a CSV file with rows corresponding to the DBNs in the list.
        """

        filtered_data = [row for row in self.__sat_data if row["DBN"] in dbns]
        sorted_data = sorted(filtered_data, key=lambda x: x["DBN"])

        with open("output.csv", "w") as csv_file:
            csv_file.write("DBN,School Name,Number of Test Takers,Critical Reading Mean,"
                           "Mathematics Mean,Writing Mean\n")

            # Write the rows corresponding to the provided DBNs
            for row in sorted_data:
                school_name = f'"{row["School Name"]}"' if "," in row["School Name"] else row["School Name"]
                csv_file.write(f"{row['DBN']},{school_name},{row['Number of Test Takers']},"
                               f"{row['Critical Reading Mean']},{row['Mathematics Mean']},{row['Writing Mean']}\n")
