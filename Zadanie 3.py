import matplotlib.pyplot as plt

# Dane dotyczące czasu i prędkości pojazdu
czas = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
predkosc = [20, 25, 30, 35, 40, 45, 50, 55, 60, 65]

# Wygeneruj wykres punktowy
plt.figure(figsize=(8, 6))
plt.plot(czas, predkosc, marker='o', linestyle='-', color='b')
plt.title('Wykres punktowy - Prędkość chwilowa pojazdu')
plt.xlabel('Czas (s)')
plt.ylabel('Prędkość (km/h)')
plt.grid(True)
plt.show()
