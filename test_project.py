import pytest
import pandas as pd
from project import count_games_by_platform, count_games_by_genre, top_publishers

# test dataframe
test_data = pd.DataFrame({
    'Name': ['Game A', 'Game B', 'Game C', 'Game D'],
    'Platform': ['X360', 'PS3', 'X360', 'PC'],
    'Publisher': ['Ubisoft', 'EA', 'Ubisoft', 'EA'],
    'Genre': ['Action', 'Sports', 'Action', 'Shooter'],
    'Year': [2008, 2009, 2008, 2010],
    'Global_Sales': [1.5, 2.0, 3.0, 0.5]
})

def test_count_games_by_platform():
    result = count_games_by_platform(test_data)
    assert result['X360'] == 2
    assert result['PS3'] == 1
    assert result['PC'] == 1

def test_count_games_by_genre():
    result = count_games_by_genre(test_data)
    assert result['Action'] == 2
    assert result['Sports'] == 1
    assert result['Shooter'] == 1

def test_top_publishers():
    result = top_publishers(test_data, top_n=1)
    assert result.index[0] == 'Ubisoft'
    assert result['Ubisoft'] == 2
