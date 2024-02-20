import matplotlib.pyplot as plt

# Dane dotyczące sprzedaży w różnych kategoriach
kategorie = ['Elektronika', 'Odzież', 'Buty', 'Samochody']
sprzedaz = [2500, 3800, 4500, 3200]  # Sprzedaż w każdej kategorii

# Wygeneruj wykres kołowy
plt.figure(figsize=(7, 7))
plt.pie(sprzedaz, labels=kategorie, autopct='%1.1f%%', startangle=140)
plt.title('Udział kategorii w całkowitej sprzedaży')
plt.axis('equal')  # Ustawienie wykresu kołowego na kształt koła
plt.show()

