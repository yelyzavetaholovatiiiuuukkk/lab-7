import pandas as pd
import matplotlib.pyplot as plt


data = {
    'student_id': [1, 2, 3, 4, 5],
    'termin1': [4, 5, 3, 5, 4],
    'termin2': [5, 6, 4, 6, 5],
    'termin3': [4, 5, 4, 5, 3]
}

df = pd.DataFrame(data)

# Tworzenie wykresów ocen z poszczególnych terminów
plt.figure(figsize=(10, 5))

# Wykres ocen z terminu 1
plt.plot(df['student_id'], df['termin1'], label='Termin 1', marker='o')

# Wykres ocen z terminu 2
plt.plot(df['student_id'], df['termin2'], label='Termin 2', marker='s')

# Wykres ocen z terminu 3
plt.plot(df['student_id'], df['termin3'], label='Termin 3', marker='^')

plt.title('Oceny z kolokwium w poszczególnych terminach')
plt.xlabel('Numer studenta')
plt.ylabel('Ocena')
plt.legend()
plt.grid(True)
plt.show()

# Tworzenie wykresu rozkładu ostatecznych ocen
plt.figure(figsize=(8, 6))

# Połącz oceny z poszczególnych terminów w jedną kolumnę (np. średnią)
df['ostateczne'] = df.mean(axis=1)

# Wykres rozkładu ostatecznych ocen
plt.hist(df['ostateczne'], bins=5, color='purple', edgecolor='black')
plt.title('Histogram ostatecznych ocen')
plt.xlabel('Ocena')
plt.ylabel('Liczba studentów')
plt.grid(True)
plt.show()
