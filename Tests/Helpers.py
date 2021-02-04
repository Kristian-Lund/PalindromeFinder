
def MakeTestCaseList(TestCaseListStr):
    #Makeing a spreadsheet from a test case file
    TestCaseList = []
    NumberOfColumnsTemp = []
    TestCaseListStrSplitted = TestCaseListStr.split('\n')
    for i in range(len(TestCaseListStrSplitted)):
        Case = TestCaseListStrSplitted[i].split('\t')
        if(len(Case) == 2 and (Case[1].lower() == "true" or Case[1].lower() == "false")):
            TestCaseList.append(list(map(str, Case)))
    return TestCaseList