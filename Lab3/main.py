
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import Normalizer
from sklearn.preprocessing import PolynomialFeatures
import matplotlib.pyplot as plt
import seaborn as sns
from bokeh.plotting import figure, show
from bokeh.layouts import gridplot
from bokeh.io import export_png

my_list = [2, 5, 6, 7, 12, 1, 0, 9, 2, 2]

# my_list.index(a) - wyswietla pod ktorym indexem w liscie znajduje sie dana wartosc w liscie
print(my_list.index(12))

# my_list.count(a) - wyswietla ile razy dana wartosc wystepuje w liscie
print(my_list.count(2))

# my_list.sort() - sortuje liste
my_list.sort()
print(my_list)

# my_list.insert(0,'!') - umieszcza w wybranym miejscu w liscie odpowiednia wartosc
my_list.insert(1, 99)
print(my_list)

# my_array = np.array(my_list) - zmienia nasza liste w tablice
my_array = np.array(my_list)
print(my_array)

# a.shape - pokazuje wymiary naszej tablicy
print(my_array.shape)

# a.ndim - pokazuje ilosc wymiarow tablicy
print(my_array.ndim)

# a.datatype - pokazuje typ danych w tablicy
print(my_array.dtype)

# e.size - pokazuje ilosc elementow tablicy
print(my_array.size)

# a.sum() - suma wartosci w tablicy
print(my_array.sum())

x = 2
y = 8

# np.add(x,y) - dodawanie dwóch liczb
print(np.add(x, y))

# np.substract(x,y) - odejmowanie dwóch liczb
print(np.subtract(x, y))

# np.multiply(x,y) - mnożenie dwóch liczb
print(np.multiply(x, y))

# np.divide(x,y) - dzielenie dwóch liczb
print(np.divide(x, y))

# np.sqrt(x) - pierwiastek z liczby
print(np.sqrt(x))

A = np.matrix(np.random.random((2, 2)))
B = np.asmatrix(y)
C = np.mat(np.random.random((10, 5)))
D = np.mat([[11, 7], [22, 5]])

# np.add(A,B) - dodawanie macierzy
print(np.add(A, D))

# np.substract(A,B) - odejmowanie macierzy
print(np.subtract(A, D))

# A.T - transpozycja macierzy
print(A)
print(A.T)

# np.divide(A,B) - dzielenie macierzy
print(np.divide(D, A))

# np.multiply(A,B) - mnożenie macierzy
print(np.multiply(D, A))

series = pd.Series([6, 11, -4, 4], index=['a', 'b', 'c', 'd'])

# series.max() - zwraca największą wartość
print(series.max())

# series.min() - zwraca najmniejszą wartość
print(series.min())

# series.sum() - sumuje wartości
print(series.sum())

# series.mean() - średnia wartości
print(series.mean())

# series.describe() - opis dataframe
print(series.describe())

# k_means - tworzenie algorytmu k srednich
k_means = KMeans(n_clusters=3, random_state=0)

# uczenie i testowanie danych
X = np.random.random((8, 8))
y = np.array(['B', 'A', 'A', 'A', 'B', 'A', 'B', 'B'])

X_train, X_test, y_train, y_test = train_test_split(X, y)

# standaryzacja
scaler = StandardScaler().fit(X_train)
standardized_X = scaler.transform(X_train)
standardized_X_test = scaler.transform(X_test)

# normalizacja
scaler = Normalizer().fit(X_train)
normalized_X = scaler.transform(X_train)
normalized_X_test = scaler.transform(X_test)

# tworzenie wielomianu
poly = PolynomialFeatures(5)
poly.fit_transform(X)

x = np.linspace(0, 10, 100)
y = np.cos(x)

figure1 = plt.figure()
figure2 = plt.figure(figsize=plt.figaspect(2.0))

figure1.add_subplot()
ax1 = figure1.add_subplot(221)  # row-col-num
ax3 = figure1.add_subplot(212)
figure3, axes = plt.subplots(nrows=2, ncols=2)
figure4, axes2 = plt.subplots(ncols=3)
figure1, ax = plt.subplots()
ax.fill(x, y, color='blue')  # rysowanie wielokąta
axes[0, 0].bar([1, 2, 3], [3, 4, 5])  # pionowe prostokaty ze stala wysokoscia
axes[1, 0].barh([0.5, 1, 2.5], [0, 1, 2])  # poziome prostokąty ze stałą wysokością
axes[1, 1].axhline(0.45)  # linia pozioma przez osie
axes[0, 1].axvline(0.65)  # linia pionowa przez osie

iris = sns.load_dataset("iris")
titanic = sns.load_dataset("titanic")

# wykres słupkowy
sns.barplot(x="sex",
            y="survived",
            hue="class",
            data=titanic)

plt.show()

# wykres punktowy z jedną zmienną
sns.stripplot(x="species",
              y="petal_length",
              data=iris)

# ustawienie limitu osi y
plt.ylim(0, 100)

# ustawienie limitu osi x
plt.xlim(0, 10)

# tytuł wykresu
plt.title("Nowy Tytuł")

plt.show()

p = figure(tools='box_select')
x = np.linspace(0, 4 * np.pi, 100)
y = np.sin(x)
p.circle(x, y, legend_label="sin(x)")
p.circle(x, 2 * y, legend_label="2*sin(x)", color="orange")
p.circle(x, 3 * y, legend_label="3*sin(x)", color="green")
p.legend.title = "Przykładowy tytuł"

# umiejscowienie legendy
p.legend.location = 'bottom_left'

# obramówka i tło legendy
p.legend.border_line_color = "navy"
p.legend.background_fill_color = "white"

# orientacja legendy
# p.legend.orientation = "horizontal"
p.legend.orientation = "vertical"

show(p)
# układ typu grid
p1 = figure(plot_width=500, tools='pan,box_zoom')
p2 = figure(plot_width=500, plot_height=500,
            x_range=(0, 8), y_range=(0, 8))
p3 = figure()

row1 = [p1, p2]
row2 = [p3]
layout = gridplot([[p1, p2], [p3]])

# export do PNG
export_png(p, filename="plot.png")
