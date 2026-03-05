import numpy as np

simulasi = 10000

# Simulasi lemparan dua dadu
dadu1 = np.random.randint(1, 7, size=simulasi)
dadu2 = np.random.randint(1, 7, size=simulasi)

# Jumlah kedua dadu
jumlah = dadu1 + dadu2

# Hitung berapa kali jumlah = 7
jumlah_7 = np.sum(jumlah == 7)

# Hitung probabilitas
probabilitas = jumlah_7 / simulasi

print(f"Jumlah simulasi     : {simulasi}")
print(f"Jumlah muncul = 7   : {jumlah_7}")
print(f"Probabilitas        : {probabilitas:.4f}")
print(f"Probabilitas teoritis: {6/36:.4f}")