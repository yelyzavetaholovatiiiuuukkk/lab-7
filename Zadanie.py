import pandas as pd

# Tworzenie DataFrame z danymi studentów
data = {
'nr_albumu': [98763, 14769, 90876, 67845, 12769],
    'imię': ['Bożena', 'Yelyzaveta', 'Sebastian', 'Kamil', 'Yuliia'],
    'nazwisko': ['Jaskulka', 'Holovatiuk', 'Kużniar', 'Borucki', 'Milczanowska'],
    'oceny_z_kolokwium': [4, 5, 3, 6, 4],
    'wiek': [19, 19, 20, 20, 19]
}

df = pd.DataFrame(data)

# a. Wybierz studentów, którzy mają ocenę większą niż 4
oceny_wieksze_niz_4 = df[df['oceny_z_kolokwium'] > 4]

# b. Posortuj studentów według wieku
posortowani_studenci = df.sort_values(by='wiek')

# c. Zgrupuj studentów według ocen i oblicz średnią wieku w każdej grupie
srednia_wiek_w_grupach = df.groupby('oceny_z_kolokwium')['wiek'].mean()

# d. Utwórz ramkę danych protokołu ocen z poprawy a następnie połącz ją z ramką pierwszego terminu na podstawie wspólnego klucza (nr_albumu)
ramka_poprawy = pd.DataFrame({
    'nr_albumu': [98763, 14769, 90876],
    'oceny_z_poprawy': [5, 6, 3]
})