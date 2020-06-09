import fileOperation

def isExist(countries):
    csv_data = fileOperation.readCSV("data/country_code.csv")
    result = []
    for checked_country in countries:
        for search in csv_data:
            if checked_country == search[1]:
                # 引数のcountry-codeが、リスト(.csv)に存在すれば "True"
                result.append(True)
                break
    # 引数に含まれる全country-codeが "True" の場合のみ True をreturnする
    if len(result) == len(countries):
        return True
    else:
        return False

def isUnique(target_list):
    # set()は重複値を無視して値をセットするため、要素数の比較で重複チェックが可能
    return len(target_list) == len(set(target_list))
