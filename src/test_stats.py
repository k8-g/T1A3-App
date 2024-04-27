import pytest 

from Stats import Stats


def test_load_stats():
    test_stats = Stats()
    test_stats._file_name = "test_file.csv"
    test_stats.load_stats()
    assert test_stats.get_wins() == 20
    assert test_stats.get_losses() == 45
