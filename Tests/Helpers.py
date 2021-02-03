
def MakeSpreadSheet(SpreadSheetString):
    #Makeing a spreadsheet from a test case file
    List = []
    NumberOfColumnsTemp = []
    SpreadSheetList = SpreadSheetString.split('\n')
    for i in range(len(SpreadSheetList)):
        NumberOfColumnsTemp.append(len(SpreadSheetList[i].split(',')))
        List.append(list(map(str,SpreadSheetList[i].split(','))))
    return List