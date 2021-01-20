# https://finreg.kz/index.cfm?docid=3227&switch=russian&organization=&organizationid=&organizationtypeid=&typeid=&kindid=&startdate=&enddate=&npatypeid=&sourceid=&view=new&start=1
# https://finreg.kz/index.cfm?docid=3227&switch=russian&organization=&organizationid=&organizationtypeid=&typeid=&kindid=&startdate=&enddate=&npatypeid=&sourceid=&view=new&start=101


import urllib.request
import os
import pandas as pd


def downloadFromUrl(url, fileDirectory):
    urllib.request.urlretrieve(url, fileDirectory)


def downloadForSanctions(start, end, step, folderDirectory):
    for i in range(start, end, step):
        print(i)
        fileName = str(i) + ".xls"
        fileDirectory = folderDirectory + "/" + fileName
        url = f"https://finreg.kz/index.cfm?docid=3227&switch=russian&organization=&organizationid=&organizationtypeid=&typeid=&kindid=&startdate=&enddate=&npatypeid=&sourceid=&start={i}&excel"
        downloadFromUrl(url, fileDirectory)


def getExcellFiles(folderDirectory):
    filesPaths = os.listdir(folderDirectory)
    absolutePaths = []
    for i in filesPaths:
        path = folderDirectory + "/" + i
        absolutePaths.append(path)
    return absolutePaths


start = 1
end = 16595
step = 100
folderDirectory = "./sanctions"
# downloadForSanctions(start, 202, step, folderDirectory)
getExcellFiles(folderDirectory)
paths = getExcellFiles(folderDirectory)
for i in paths:
    print(i)
    data = pd.read_excel(i)
    print(data)
