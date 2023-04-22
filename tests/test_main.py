import os
import sys
import pytest

from ..main import readFile, getRows, writeToFile, main


@pytest.fixture
def single_day_single_site_sheet():
    return readFile('tests/test_site_1_date_1.xlsx')


@pytest.fixture
def one_month_single_site_sheet():
    return readFile('tests/test_site_1_date_31.xlsx')


@pytest.fixture
def three_day_one_missing_single_site_sheet():
    return readFile('tests/test_site_1_date_3_missing_1.xlsx')


def test_readFile_file_not_present():
    with pytest.raises(SystemExit) as output:
        readFile('tests/abc.xlsx')

    assert output.type == SystemExit
    assert output.value.code == 1


def test_readFile(single_day_single_site_sheet):
    assert not single_day_single_site_sheet.empty


def test_getRows(single_day_single_site_sheet):
    rows = getRows(single_day_single_site_sheet)

    assert len(rows) == 2


def test_getRows_one_month(one_month_single_site_sheet):
    rows = getRows(one_month_single_site_sheet)

    assert len(rows) == 32


def test_getRows_one_day_missing(three_day_one_missing_single_site_sheet):
    rows = getRows(three_day_one_missing_single_site_sheet)

    assert len(rows) == 3


def test_writeToFile(single_day_single_site_sheet):
    rows = getRows(single_day_single_site_sheet)

    assert len(rows) == 2

    outputFilePath = 'tests/output.xlsx'
    writeToFile(outputFilePath, rows)

    assert os.path.isfile(outputFilePath)
    os.remove(outputFilePath)


def test_main():
    inputFilePath = 'tests/test_site_1_date_1.xlsx'
    outputFilePath = 'tests/output.xlsx'
    sys.argv = ['main.py', inputFilePath, outputFilePath]
    main()

    assert os.path.isfile(outputFilePath)
    os.remove(outputFilePath)


def test_main_input_file_absent():
    sys.argv = ['main.py']
    with pytest.raises(SystemExit) as output:
        main()

    assert output.type == SystemExit
    assert output.value.code == 1
