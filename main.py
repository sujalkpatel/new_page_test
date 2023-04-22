import sys
import os
import collections
from datetime import timedelta
import pandas as pd

columnHeader = ["Day of Month", "Date", "Site ID", "Page Views",
                "Unique Visitors", "Total Time Spent", "Visits", "Average Time Spent on Site"]


def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)+1):
        yield start_date + timedelta(n)


def getRowData(df_sheet, df_list, siteHeader, row):
    dateSiteDict = collections.defaultdict(list)

    for i in df_list:
        if i == siteHeader:
            continue

        date, val = df_sheet[i][row+1], df_sheet[i][row+2]
        dateSiteDict[date].append(val)

    return dateSiteDict


def transformRowData(siteName, startDate, endDate, dateSiteDict):
    rows = []
    for curDate in daterange(startDate, endDate):
        dateStr = curDate.strftime("%Y/%m/%d")
        if curDate not in dateSiteDict:
            print(dateStr, "not present for site:", siteName)
            continue
        row = []
        row.append(curDate.day)
        row.append(dateStr)
        row.append(siteName)
        row.extend(dateSiteDict[curDate])
        rows.append(row)
    return rows


def getRows(df_sheet):
    df_list = list(df_sheet)
    siteHeader = df_sheet.columns[0]
    startDate = siteHeader
    endDate = df_sheet.iat[0, 0]
    rowCount = len(df_sheet[siteHeader])
    outputRows = [columnHeader]

    for i in range(0, rowCount, 3):
        data = getRowData(df_sheet, df_list, siteHeader, i)
        rows = transformRowData(
            df_sheet[siteHeader][i+2], startDate, endDate, data)
        outputRows.extend(rows)

    return outputRows


def readFile(inputFilePath):
    if not os.path.isfile(inputFilePath):
        print(inputFilePath, "isn't a valid file.")
        sys.exit(1)

    return pd.read_excel(
        inputFilePath, sheet_name=0)


def writeToFile(outputFilePath, rows):
    df = pd.DataFrame(data=rows)
    df.to_excel(outputFilePath, index=False, header=False)


def main():
    n = len(sys.argv)
    if n < 2:
        print("Usage: python3 main.py <input_excel_file> (optional<output_file_name>)")
        sys.exit(1)

    inputFilePath = sys.argv[1]
    outputFilePath = 'output.xlsx'
    if n >= 3:
        outputFilePath = sys.argv[2]

    df_sheet = readFile(inputFilePath)

    rows = getRows(df_sheet)
    writeToFile(outputFilePath, rows)


if __name__ == "__main__":
    main()
