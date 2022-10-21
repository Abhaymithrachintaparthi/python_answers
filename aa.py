import pandas as pd

# read by default 1st sheet of an excel file
df = pd.read_excel('a.xlsx')
d = df.sort_values('Years of Experience', ascending=False)


print(d)
#output:
'''sl.no   First Name  Last Name  Years of Experience        Country Date of birth
4    Nereida    Magwood                   11  United States    1989-08-16
3   Kathleen     Hanner                    9  United States    1991-10-15
2     Philip       Gent                    6         France    1994-05-21
0      Dulce      Abril                    4  United States    1996-10-15
1       Mara  Hashimoto                    3  Great Britain    1997-08-16'''
