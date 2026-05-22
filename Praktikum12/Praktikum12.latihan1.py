# Nama : Fuad Nizard Attaqi
# NIM : J0403251086
# Kelas : A1

# ==========================================================
# Latihan 1: Weighted Graph dan Perhitungan Jalur
# ==========================================================
# Representasi weighted graph menggunakan dictionary bersarang
graph = {
 'A': {'B': 4, 'C': 2},
 'B': {'D': 5},
 'C': {'D': 1},
 'D': {}
}
# Menghitung dua kemungkinan jalur dari A ke D
jalur_1 = graph['A']['B'] + graph['B']['D'] # A -> B -> D
jalur_2 = graph['A']['C'] + graph['C']['D'] # A -> C -> D
print("Jalur 1: A -> B -> D =", jalur_1)
print("Jalur 2: A -> C -> D =", jalur_2)
if jalur_1 < jalur_2:
    print("Jalur terpendek adalah A -> B -> D")
else:
    print("Jalur terpendek adalah A -> C -> D")

# ==========================================================
# Jawaban Analisis:
# ==========================================================
# 1. Berapa total bobot jalur A -> B -> D?
# Jawab: Total bobot jalur A -> B -> D adalah 9 (diperoleh dari 4 + 5).
#
# 2. Berapa total bobot jalur A -> C -> D?
# Jawab: Total bobot jalur A -> C -> D adalah 3 (diperoleh dari 2 + 1).
#
# 3. Jalur mana yang dipilih sebagai jalur terpendek?
# Jawab: Jalur A -> C -> D, karena memiliki total bobot yang paling kecil (3 dibandingkan 9).
#
# 4. Mengapa jalur terpendek tidak selalu ditentukan dari jumlah edge yang paling sedikit?
# Jawab: Karena pada weighted graph (graph berbobot), setiap hubungan antar node (edge) 
# memiliki nilai/bobot tertentu (seperti jarak, biaya, atau waktu). Oleh karena itu, 
# efisiensi jalur diukur berdasarkan total bobot minimum (akumulasi bobot) dari seluruh 
# edge yang dilalui, bukan berdasarkan jumlah langkah atau jumlah edge terkecil. Jalur 
# yang memiliki edge lebih banyak bisa saja lebih optimal jika total akumulasi bobotnya 
# lebih kecil daripada jalur dengan edge sedikit tetapi memiliki bobot edge yang sangat besar.