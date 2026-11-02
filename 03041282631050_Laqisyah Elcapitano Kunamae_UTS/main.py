data_level = [
    18, 25, 33, 41, 55, 62, 76, 84, 91, 47, 29, 38, 70, 82, 15,         #data inti
    20, 99, 45, 59, 28.8                                                #data tambahan saya
]

# Menghitung status level
def status_level(level):
    if level < 30:
        return "LOW"
    elif 30 <= level <= 80:
        return "NORMAL"
    else:
        return "HIGH"

# Menghitung jumlah kategori
def hitung_kategori(data):
    jumlah = {"LOW": 0, "NORMAL": 0, "HIGH": 0}
    for level in data:
        status = status_level(level)
        jumlah[status] += 1
    return jumlah

# Menghitung rata-rata
def rata_rata(data):
    return sum(data) / len(data)

# Menampilkan hasil monitoring
print("=== MONITORING ===")

for i, level in enumerate(data_level, start=1):
    print("Data ke-", i, "=", level, "% ->", status_level(level))

# Menghitung jumlah kategori
kategori = hitung_kategori(data_level)
low = kategori["LOW"]
normal = kategori["NORMAL"]
high = kategori["HIGH"]

# Menghitung rata-rata level
rata = rata_rata(data_level)
maksimum = max(data_level)
minimum = min(data_level)

# Menampilkan hasil akhir
print("\n=== RINGKASAN ===")
print("Jumlah data LOW    :", low)
print("Jumlah data NORMAL :", normal)
print("Jumlah data HIGH   :", high)
print("Rata-rata level    :", round(rata, 2), "%")
print("Maksimum           :", maksimum, "%")
print("Minimum            :", minimum, "%")
print("Total data         :", len(data_level))