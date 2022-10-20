from sortirovka import sort,get_da
from file import get_number_operation,get_data
from proces import read_file,write_file
from vibor import sort_data


def button():
    return sort_data(get_number_operation,read_file,write_file,sort,get_da,get_data)