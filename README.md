# NBA_scraper
Python scraper for NBA.com that collects player data and loads it into a Pandas dataframe and writes to csv.

## Software Requirements
- Python 3
- Python modules (these can be PIP installed)
  * selenium
  * BeautifulSoup
  * html5lib
  * Pandas

## Data
Here is a small example of the player data:
```
In [5]: player_data_df
Out[5]: 
    rank            player_name team age  gp  ...   pf    fp dd2 td3 plusminus
0      1           James Harden  HOU  30  19  ...  3.1  59.2   6   0       7.8
1      2  Giannis Antetokounmpo  MIL  24  20  ...  3.3  60.4  19   2      10.3
2      3            Luka Doncic  DAL  20  18  ...  2.7  57.5  13   7       5.6
3      4           Kyrie Irving  BKN  27  11  ...  2.9  48.3   2   1      -0.8
4      5             Trae Young  ATL  21  19  ...  1.2  45.6   6   1      -6.9
..   ...                    ...  ...  ..  ..  ...  ...   ...  ..  ..       ...
452  440         Romeo Langford  BOS  20   1  ...  0.0   0.0   0   0       0.0
453  440        Sekou Doumbouya  DET  18   1  ...  0.0   0.0   0   0       3.0
454  440           Stanton Kidd  UTA  27   4  ...  0.8   0.8   0   0      -0.3
455  440          Vlatko Cancar  DEN  22   1  ...  0.0   0.0   0   0       1.0
456  440       Zach Norvell Jr.  LAL  21   2  ...  0.0   0.6   0   0      -2.0

[457 rows x 30 columns]
```
