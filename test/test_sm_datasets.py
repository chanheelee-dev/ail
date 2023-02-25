import pytest

import pathlib

from data_science.data_acquisition import sm_datasets as sm
import pandas as pd


# Start of the Test
@pytest.fixture(autouse=True)
def guerry():
    return "HistData.Guerry"


# Test Cases
class TestGuerry:
    def test_download_guerry(self, guerry, tmp_path):
        filename = sm.rdata_path[guerry].name  # guerry.csv
        test_file = tmp_path / filename  # tmp_path / guerry.csv
        sm.download(guerry, test_file)
        assert test_file.exists()

    def test_read_guerry(self, guerry, tmp_path):
        filename = sm.rdata_path[guerry].name  # guerry.csv
        test_file = tmp_path / filename  # tmp_path / guerry.csv
        sm.download(guerry, test_file)
        df = sm.read(guerry, test_file)
        assert list(df.columns) == [
            "dept",
            "Region",
            "Department",
            "Crime_pers",
            "Crime_prop",
            "Literacy",
            "Donations",
            "Infants",
            "Suicides",
            "MainCity",
            "Wealth",
            "Commerce",
            "Clergy",
            "Crime_parents",
            "Infanticide",
            "Donation_clergy",
            "Lottery",
            "Desertion",
            "Instruction",
            "Prostitutes",
            "Distance",
            "Area",
            "Pop1831",
        ]


# End of the Test
