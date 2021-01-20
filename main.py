# https://finreg.kz/index.cfm?docid=3227&switch=russian&organization=&organizationid=&organizationtypeid=&typeid=&kindid=&startdate=&enddate=&npatypeid=&sourceid=&view=new&start=1
# https://finreg.kz/index.cfm?docid=3227&switch=russian&organization=&organizationid=&organizationtypeid=&typeid=&kindid=&startdate=&enddate=&npatypeid=&sourceid=&view=new&start=101


import urllib.request

start = 1
end = 16595
step = 100
for i in range(start, end, step):
    print(i)
    fileName = str(i) + ".xlsx"
    fileDirectory = "./sanction/" + fileName
    url = f"https://finreg.kz/index.cfm?docid=3227&switch=russian&organization=&organizationid=&organizationtypeid=&typeid=&kindid=&startdate=&enddate=&npatypeid=&sourceid=&start={i}&excel"
    urllib.request.urlretrieve(url, fileDirectory)
    if i == 16501:
        fileName = "16595.xlsx"
        fileDirectory = "./sanction/" + fileName
        url = f"https://finreg.kz/index.cfm?docid=3227&switch=russian&organization=&organizationid=&organizationtypeid=&typeid=&kindid=&startdate=&enddate=&npatypeid=&sourceid=&start=16595&excel"
        urllib.request.urlretrieve(url, fileDirectory)
