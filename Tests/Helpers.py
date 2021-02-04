
def MakeSpreadSheet(SpreadSheetString):
    #Makeing a spreadsheet from a test case file
    List = []
    NumberOfColumnsTemp = []
    SpreadSheetList = SpreadSheetString.split('\n')
    for i in range(len(SpreadSheetList)):
        Case = SpreadSheetList[i].split('\t')
        if(len(Case) == 2 and (Case[1].lower() == "true" or Case[1].lower() == "false")):
            #List.append(list(map(str,SpreadSheetList[i].split(','))))
            List.append(list(map(str, Case)))
    return List