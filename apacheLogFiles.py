# Author: Darren Ramsook
# Version: 1
# Find out more: www.DarrenR.co.tt
import re
import pandas as pd
import datetime as dt
import time
from .ipRequests import returnCountryCode
# Returns length of apl


def lineCounter(logfile):
    file = open(logfile, 'r')
    lines = file.readlines()
    return(len(lines))


# Returns list of logs from logfile
def logToList(logfile):
    file = open(logfile, 'r')
    lines = file.readlines()
    print("Number of lines in " + logfile + ": " + str(len(lines)))
    return(lines)


# Returns a Pandas dataframe from logfile
def dataframeLog(logfile, typeOfLog):
    file = open(logfile, 'r')
    dataList = []
    if (typeOfLog == 'access'):
        columnList = ["Ip", "RFC 1413", "UserID", "Timestamp",
                      "Request Line", "Status", "Size of Object", "Referer", "User-Agent"]
        for line in file:
            try:
                matches = None
                pattern = re.compile(
                    r'([A-Za-z0-9\.-_]+)\s(-|.+)\s(-|.+)\s(\[.+\])\s\"(.+)\"\s(-|\d+)\s(-|\d+)\s\"(-|.*)\"\s\"(-|.*)\"')
                matches = tuple(pattern.findall(line))[0]
                dataList.append(matches)
            except:
                print(line)
    if (typeOfLog == 'error'):
        pass
        #columnList = []

    df = pd.DataFrame(dataList, columns=columnList)
    return(df)


def requestSplitter(logfile, typeOfData):
    df = None
    if (typeOfData == 'CSV'):
        df = pd.read_csv(logfile)
    elif(typeOfData == 'dataframe'):
        df = logfile
    df["RequestType"] = ""
    df["RequestLink"] = ""
    pattern = re.compile(
        r'([A-Z]+|-)\s*\**\s*(.*)\s*')
    for index, row in df.iterrows():
        try:
            combinedResult = tuple(pattern.findall(row["Request Line"]))[0]
            df.at[index, "RequestType"] = combinedResult[0]
            df.at[index, "RequestLink"] = combinedResult[1]
        except:
            df.at[index, "RequestType"] = "Unk"
            df.at[index, "RequestLink"] = row["Request Line"]

    df = df[['Ip', 'Timestamp', 'RequestType', 'RequestLink', 'Status',
             'Size of Object', 'Referer', 'User-Agent']]
    return(df)


def timeConversion(logfile, typeOfData):
    df = None
    if (typeOfData == 'CSV'):
        df = pd.read_csv(logfile)
    elif(typeOfData == 'dataframe'):
        df = logfile
    for index, row in df.iterrows():
        df.at[index, 'Timestamp'] = dt.datetime.strptime(
            row["Timestamp"], "[%d/%b/%Y:%H:%M:%S +0000]")
    return(df)


def reverseIpLookup(df, key):
    ipDict = {}
    df["Country"] = ''
    for index, row in df.iterrows():
        if row["Ip"] in ipDict:
            row["Country"] = ipDict[row["Ip"]]
        else:
            time.sleep(0.65)
            countryCode = returnCountryCode(
                key, row["Ip"])
            ipDict[row["Ip"]] = countryCode
            row["Country"] = countryCode
            print(row["Ip"] + " : " + countryCode)
    return(df)


def completeParse(logfile):
    df = dataframeLog(logfile, 'access')
    df = requestSplitter(df, 'dataframe')
    df = timeConversion(df, 'dataframe')
    df.to_csv('./logFiles/test.csv', index=False)
    return(df)
