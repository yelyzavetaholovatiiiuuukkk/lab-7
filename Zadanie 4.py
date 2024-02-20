import matplotlib.pyplot as plt

# Dane dotyczące ocen
oceny = [4, 5, 3, 5, 4, 2, 5, 3, 4, 4, 5, 3, 2, 4, 5, 3, 4, 5, 4, 5]

# Wygeneruj histogram
plt.figure(figsize=(8, 6))
plt.hist(oceny, bins=5, color='purple', edgecolor='black')
plt.title('Histogram rozkładu ocen')
plt.xlabel('Ocena')
plt.ylabel('Liczba studentów')
plt.grid(True)  
plt.show()
