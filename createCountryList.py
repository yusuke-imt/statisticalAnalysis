import fileOperation

def create():
    csv_data = fileOperation.readCSV("data/country_code.csv")
    # element = name, code
    element_num = 2

    if element_num == len(csv_data[0]) == len(csv_data[1]):
        country_list = ""
        for index in range(len(csv_data)):
            country_list += csv_data[index][1] + " : " + csv_data[index][0] + "\n"
    else:
        pass
    return country_list
