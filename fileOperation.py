import csv

def readCSV(file_path):
    out_list = []
    with open(file_path, mode='r') as f:
        reader = csv.reader(f)
        for line in reader:
            out_list.append(line)
    return out_list
