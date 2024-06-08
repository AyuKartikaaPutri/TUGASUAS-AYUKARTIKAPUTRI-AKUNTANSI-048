import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Membuat DataFrame penjualan cake
data_cake = pd.DataFrame({
    'jenis': ['Chocolate', 'Vanilla', 'Red Velvet', 'Cheesecake', 'Black Forest'],
    'jumlah': [150, 200, 120, 180, 140],
    'harga': [20, 18, 25, 22, 24]
})

# Membuat DataFrame penjualan pastry
data_pastry = pd.DataFrame({
    'jenis': ['Croissant', 'Danish', 'Muffin', 'Strudel', 'Pie'],
    'jumlah': [170, 160, 180, 150, 190],
    'harga': [15, 14, 18, 20, 22]
})

# Membuat DataFrame penjualan per bulan
data_bulanan = pd.DataFrame({
    'bulan': ['January', 'February', 'March', 'April', 'May'],
    'penjualan_cake': [500, 600, 550, 620, 590],
    'penjualan_pastry': [480, 560, 520, 580, 610]
})

# Menampilkan lima baris pertama data
print("Data penjualan cake:")
print(data_cake.head())
print("\nData penjualan pastry:")
print(data_pastry.head())
print("\nData penjualan bulanan:")
print(data_bulanan.head())

# Visualisasi Scatter Plot (Jumlah vs Harga Cake)
plt.figure(figsize=(14, 10))
plt.subplot(3, 2, 1)
sns.scatterplot(x='jumlah', y='harga', data=data_cake, hue='jenis', s=100, palette='viridis')
plt.title('Scatter Plot (Jumlah vs Harga Cake)')
plt.xlabel('Jumlah')
plt.ylabel('Harga')

# Visualisasi Histogram (Harga Pastry)
plt.subplot(3, 2, 2)
plt.hist(data_pastry['harga'], bins=5, color='skyblue', edgecolor='black')
plt.title('Histogram Harga Pastry')
plt.xlabel('Harga')
plt.ylabel('Frekuensi')

# Visualisasi Pie Chart (Penjualan Cake)
plt.subplot(3, 2, 3)
plt.pie(data_cake['jumlah'], labels=data_cake['jenis'], autopct='%1.1f%%', colors=sns.color_palette('viridis', len(data_cake)))
plt.title('Pie Chart Penjualan Cake')

# Visualisasi Bar Chart (Penjualan Pastry)
plt.subplot(3, 2, 4)
sns.barplot(x='jenis', y='jumlah', data=data_pastry, palette='viridis')
plt.title('Bar Chart Penjualan Pastry')
plt.xlabel('Jenis Pastry')
plt.ylabel('Jumlah')

# Visualisasi Line Chart (Penjualan Bulanan)
plt.subplot(3, 2, 5)
plt.plot(data_bulanan['bulan'], data_bulanan['penjualan_cake'], marker='o', label='Cake', color='blue')
plt.plot(data_bulanan['bulan'], data_bulanan['penjualan_pastry'], marker='s', label='Pastry', color='green')
plt.title('Line Chart Penjualan Bulanan')
plt.xlabel('Bulan')
plt.ylabel('Penjualan')
plt.legend()

# Visualisasi Box Plot (Harga Cake dan Pastry)
plt.subplot(3, 2, 6)
sns.boxplot(data=[data_cake['harga'], data_pastry['harga']], palette='viridis')
plt.title('Box Plot Harga Cake dan Pastry')
plt.xticks([0, 1], ['Cake', 'Pastry'])
plt.ylabel('Harga')

# Menampilkan semua visualisasi dalam satu window
plt.tight_layout()
plt.show()
