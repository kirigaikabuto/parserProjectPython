from bs4 import BeautifulSoup
import requests
import json
import pandas as pd
import datetime

dateStr = str(datetime.datetime.now()).replace(" ", "_").split(".")[0].replace(":", "_").replace("-", "_")

folderName = "./sanctions"
fileNameJson = "data" + dateStr + ".json"
fileNameXlsx = "data" + dateStr + ".xlsx"
fileNameXml = "data.xml"
absoluteDirectoryJson = folderName + "/" + fileNameJson
absoluteDirectoryXlsx = folderName + "/" + fileNameXlsx
absoluteDirectoryXml = folderName + "/" + fileNameXml


def parsePage(url):
    pageData = []
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    th = soup.findAll("th")
    columns = []
    for i in th:
        column = i.text.strip()
        columns.append(column)
    table = soup.find("table", {"class": "dataTable hover"})
    tr = table.findAll("tr")

    for i in range(1, len(tr)):
        td = tr[i].findAll("td")
        rows = []
        for j in td:
            row = j.text.strip()
            rows.append(row)
        counter = 0
        d = {}
        for j in columns:
            d[j] = rows[counter]
            counter += 1
        pageData.append(d)
    return pageData


def parseSanctions(start, end, step):
    allData = []
    for i in range(start, end + 1, step):
        print(i)
        url = f"https://www.finreg.kz/index.cfm?docid=3227&switch=russian&organization=&organizationid=&organizationtypeid=&typeid=&kindid=&startdate=&enddate=&npatypeid=&sourceid=&view=list&start={i}"
        temp = parsePage(url)
        allData += temp
    print(len(allData))
    jsonData = json.dumps(allData, indent=4, ensure_ascii=False)
    file = open(absoluteDirectoryJson, "w", encoding='utf-8')
    file.write(jsonData)
    file.close()


def saveToExcell(fileJson, fileXlsx):
    df = pd.read_json(fileJson, )
    print(df.head())
    df.to_excel(fileXlsx)


start = 1
end = 16696
step = 100
parseSanctions(start, 301, step)
saveToExcell(absoluteDirectoryJson, absoluteDirectoryXlsx)
# saveToXml(absoluteDirectoryJson, absoluteDirectoryXml)
