import menu
import fileOperation

def create():
    csv_data = fileOperation.readCSV("data/menu.csv")
    # element = indicator, title, xlabel, ylabel
    element_num = 4

    if element_num == len(csv_data[0]) == len(csv_data[1]) == len(csv_data[2]) == len(csv_data[3]):
        menu_list = []
        for index in range(len(csv_data)):
            item = menu.Menu()
            item.setValue(csv_data[index][0], csv_data[index][1], csv_data[index][2], csv_data[index][3])
            menu_list.append(item)
    else:
        pass
    return menu_list

