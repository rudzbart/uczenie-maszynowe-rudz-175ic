import pandas as pd
from pandasgui import show

s = pd.read_csv('samochody1tys.csv')
show(s)

#1 pd.melt(df) - zbiera wszystkie kolumny i ustawia je w wierszach
show(pd.melt(s))

#2 df.sort_values('mpg') - sortuje wiersze wedlug wartosci danej kolumny 'mpg' od najmniejszej do najwiekszej
show(s.sort_values('cena'))

#3 df.drop_duplicates() - usuwa wszystkie powtarzające się wiersze
show(s.drop_duplicates())

#4 df.head(n) - pokazuje n pierwszych wierszy
show(s.head(10))

#5 df.tail(n) - pokazuje n ostatnich wierszy
show(s.tail(10))

#6 df.sample(n=10) - pokazuje n losowych wierszy
show(s.sample(13))

#7 df.iloc[n:m] - pokazuje wiersze od pozycji n do m-1
show(s.iloc[18:27])

#8 df.nlargest(n, 'value') - pokazuje n najwiekszych wierszy dla danego value
show(s.nlargest(5,'cena'))

#9 df.nsmallest(n, 'value') - pokazuje n najmnijeszych wierszy dla danego value
show(s.nsmallest(3,'cena'))

#10 df.filter(regex = 'regex') - pokazuje jedynie wartosci wierszy dla danej kolumny
show(s.filter(regex = 'cena'))