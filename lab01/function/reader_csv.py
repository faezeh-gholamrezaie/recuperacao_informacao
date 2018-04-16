#coding: utf-8
import csv
def get_data(file_path):
    return csv.reader(open(file_path))