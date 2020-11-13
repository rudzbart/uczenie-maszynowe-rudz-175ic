import numpy as np
from math import pi
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVC
from sklearn import neighbors
from sklearn.metrics import mean_absolute_error
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import seaborn as sns
from bokeh.plotting import figure
from bokeh.io import output_file, show
from bokeh.layouts import gridplot
from bokeh.models.widgets import Panel, Tabs
from bokeh.models import CategoricalColorMapper
from bokeh.plotting import figure

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

# A = np.matrix(np.random.random(a,b) - tworzy macierz z losowymy wartosciamy o wymiarach a, b
A = np.matrix(np.random.random((2, 2)))
print(A)

# A.I - odwraca macierz
print(A.I)

# A.T - transponuje macierz
print(A.T)

# D = np.mat([[3,4],[5,6]]) - tworzenie macierzy z wlasnymi wartosciami
D = np.mat([[3, 4], [5, 6]])
print(D)

# np.add(A,D) - dodawanie macierzy
print(np.add(A, D))

# df.iloc([0],[0]) - pokazuje wartosc z dataframe'a w danym wierszu i kolumnie
s = pd.read_csv('samochody1tys.csv')
#print(s.iloc(2, 2))

# df.ix[2] - pobiera pojedynczy wiersz danych
print(s.cena[2])

# df.info() - pokazuje informacje na temat dataframe'u
print(s.info())

# df.count() - pokazuje ilosc wszystkich nie nullowych wartosci
print(s.count())

# df.columns() - opisuje kolumny dataframe'u
#print(s.columns())

X = np.random.random((10,5))
y = np.array(['M', 'M', 'F', 'F', 'M', 'F', 'M', 'M', 'F', 'F', 'F'])
X[X < 0.7] = 0
X_train, X_test, y_train, y_test = train_test_split(X,
                                                    y,
                                                    random_state=0)

# tworzenie LinearRegression
lr = LinearRegression(normalize=True)

# tworzenie svc
svc = SVC(kernel='linear')

# tworzenie KNN
knn = neighbors.KNeighborsClassifier(n_neighbors=5)

# Standaryzacja
scaler = StandardScaler().fit(X_train)


# przewidywanie z svc
y_pred = svc.predict(np.random.random((2,5)))
print(y_pred)

# średni błąd absolutny
y_true = [3, -0.5, 2]
mean_absolute_error(y_true,y_pred)

x = np.linspace(0, 10, 100)
y = np.cos(x)
z = np.sin(x)

# tworzenie plota
fig = plt.figure()
fig2 = plt.figure(figsize=plt.figaspect(2.0))

# łączenie punktow markerem
fig, ax = plt.subplots()

# dodawanie legendy
ax.set(title='An Example Axes', ylabel='Y-Axis', xlabel='X-Axis')

# dodawanie textu do plota
ax.text(1, -2.1, 'Example Graph', style='italic')

# dodawanie adnotacji
ax.annotate("Sine", xy=(8, 0),
            xycoords='data', xytext=(10.5, 0),
            textcoords='data', arrowprops=dict(arrowstyle="->", connectionstyle="arc3"), )

tips = sns.load_dataset("tips")
sns.set_style("whitegrid")
g = sns.lmplot(x="tip",
               y="total_bill",
               data=tips,
               aspect=2)

g = (g.set_axis_labels("Tip","Total bill(USD)").
set(xlim=(0,10),ylim=(0,100)))

plt.title("plot2")
plt.show(g)

# defaultowe ustaiwenia seaborn
sns.set()

# wykres punktowy
titanic = sns.load_dataset("titanic")
sns.pointplot(x="class",
y = "survived",
hue = "sex",
data = titanic,
       palette = {"male": "g",
                  "female": "m"},
                 markers = ["^", "o"],
                           linestyles = ["-", "--"])


# wykres kolumnowy
sns.barplot(x="sex", y="survived", hue="class", data=titanic)

# wykres skrzypcowy
sns.violinplot(x="age",
y = "sex",
    hue = "survived",
          data = titanic)

# ustawienie oznaczenia osi y
g.set_ylabels("Survived")

# ustawienie oznaczen obu osi
g.set_axis_labels("Survived", "Sex")

x = [1, 2, 3, 4, 5]
y = [6, 7, 2, 4, 5]
p = figure(title="simple line example",
 x_axis_label='x',
 y_axis_label='y')
p.line(x, y, legend="Temp.", line_width=2)
output_file("lines.html")
show(p)
p1 = figure(plot_width=300, tools='pan,box_zoom')
p2 = figure(plot_width=300, plot_height=300,
            x_range=(0, 8), y_range=(0, 8))
p3 = figure()

# ustawianie siatki (grid)
row1 = [p1, p2]
row2 = [p3]
layout = gridplot([[p1, p2], [p3]])

# ustawienie layoutu z zakładkami
tab1 = Panel(child=p1, title="tab1")
tab2 = Panel(child=p2, title="tab2")
layout = Tabs(tabs=[tab1, tab2])

# kolorowanie punktow
color_mapper = CategoricalColorMapper(
    factors=['US', 'Asia', 'Europe'],
    palette=['blue', 'red', 'green'])

# usadowienie legendy
p.legend.location = 'bottom_left'

# ułozenie legendy - poziomo/pionowo
p.legend.orientation = "horizontal"
# lub
p.legend.orientation = "vertical"
