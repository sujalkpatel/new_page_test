## Purpose of the project

This project reads the provided xlsx file through command line argument, extracts data from the first sheet of that file which is in the format as provided in the excel file(Analytics Template for Exercise.xlsx), and writes the output to output.xlsx file in the format provided in the sheet 2 of the Analytics Template for Exercise.xlsx. It can work with multiple site data provided in one sheet of the input xlsx file. The instructions to install and run this project are provided here.

## Expected Input & Output

The input for this program has to be in the format of an excel file with the data in the format of sheet 1 of Analytics Template for Exercise.xlsx. The output file would be named as "output.xlsx" by default. You can provide output file name also while running the program. The format of output file data would be same as the sheet 2 of Analytics Template for Exercise.xlsx.

## Installation

```shell
$ pip3 install -r requirements.txt
```

To install the dependencies run the above command within this directory.

## Run the project

```shell
$ python3 main.py <input_excel_file> (optional<output_file_name>)
```

To run the project, execute the above command where input_excel_file is the file you want to provide as an input with data present in the sheet 1 of that file and in the required format. output_file_name is optional as shown. The default output file name is "output.xlsx"

## Run tests

```shell
$ pytest -v --cov=.
```

To run the tests, execute the above command from this directory. It will also display the test coverage on the console.

Alternatively you can run the tests in docker container, if you want with the following commands:

```shell
$ docker build -t newpage-test .
$ docker run -it newpage-test
```

## Use cases & Edge cases

I have tested the program with 1, 2 and 100 site data. I have tested the program with site data where some dates are missing from the provided date range.

## Limitations

- This program assumes that you provide a valid xlsx file. So if you provide something other than that it will fail.
- This program assumes that the format of input data would be exactly as provided in the sheet 1 of Analytics Template for Exercise.xlsx where site data are in this order ["Page Views", "Unique Visitors", "Total Time Spent", "Visits", "Average Time Spent on Site"]. If the data provided are not in this order, the program would not provide accurate output.
- If the data provided contains dates out of the range of columns A1-A2, those data would not be considered in the output file.
- If data of some dates are not provided, those dates will not be included in the output file.

## Note

- Input file: Analytics Template for Exercise.xlsx
- Output file: output.xlsx

### All the best!
