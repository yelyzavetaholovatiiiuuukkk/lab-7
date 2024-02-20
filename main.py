import matplotlib.pyplot as plt

# Przykładowe dane
kategorie = ['Samochody', 'Elektronika', 'Buty', 'Odzież']
ilosc_sprzedanych = [250, 130, 200, 210]

# Tworzenie wykresu słupkowego
plt.figure(figsize=(7, 5))
plt.bar(kategorie, ilosc_sprzedanych, color='purple')
plt.xlabel('Kategoria')
plt.ylabel('Ilość sprzedanych produktów')
plt.title('Ilość sprzedanych produktów w różnych kategoriach')
plt.show()