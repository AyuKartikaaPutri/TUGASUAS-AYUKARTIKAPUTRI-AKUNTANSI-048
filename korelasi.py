import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import linregress

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

# Menampilkan data
print("Data penjualan cake:")
print(data_cake)
print("\nData penjualan pastry:")
print(data_pastry)
print("\nData penjualan bulanan:")
print(data_bulanan)

# Regresi Linier antara penjualan bulanan cake dan pastry
slope, intercept, r_value, p_value, std_err = linregress(data_bulanan['penjualan_cake'], data_bulanan['penjualan_pastry'])

# Plot regresi linier
plt.figure(figsize=(14, 10))
plt.subplot(2, 2, 1)
sns.regplot(x='penjualan_cake', y='penjualan_pastry', data=data_bulanan, scatter_kws={'s':100, 'color':'blue'}, line_kws={'color':'red'})
plt.title('Regresi Linier Penjualan Bulanan Cake dan Pastry')
plt.xlabel('Penjualan Cake')
plt.ylabel('Penjualan Pastry')
plt.annotate(f'y = {slope:.2f}x + {intercept:.2f}', xy=(0.05, 0.95), xycoords='axes fraction', fontsize=12, color='red', ha='left', va='top')

# Analisis Korelasi antara harga dan jumlah penjualan
corr_cake = data_cake[['harga', 'jumlah']].corr()
corr_pastry = data_pastry[['harga', 'jumlah']].corr()

print("\nKorelasi antara harga dan jumlah penjualan cake:")
print(corr_cake)
print("\nKorelasi antara harga dan jumlah penjualan pastry:")
print(corr_pastry)

# Visualisasi Heatmap Korelasi Cake
plt.subplot(2, 2, 2)
sns.heatmap(corr_cake, annot=True, cmap='viridis', vmin=-1, vmax=1)
plt.title('Heatmap Korelasi Harga dan Jumlah Penjualan Cake')

# Visualisasi Heatmap Korelasi Pastry
plt.subplot(2, 2, 3)
sns.heatmap(corr_pastry, annot=True, cmap='viridis', vmin=-1, vmax=1)
plt.title('Heatmap Korelasi Harga dan Jumlah Penjualan Pastry')

# Visualisasi scatter plot dengan trendline untuk korelasi harga vs jumlah penjualan cake
plt.subplot(2, 2, 4)
sns.regplot(x='harga', y='jumlah', data=data_cake, scatter_kws={'s':100, 'color':'purple'}, line_kws={'color':'orange'})
plt.title('Scatter Plot dan Trendline Harga vs Jumlah Penjualan Cake')
plt.xlabel('Harga')
plt.ylabel('Jumlah')

# Menampilkan semua visualisasi dalam satu window
plt.tight_layout()
plt.show()
