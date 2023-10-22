# Informasi tentang makanan dalam bentuk dictionary
food_info = {
    "Apel": {
        "Kalori": 52,
        "Karbohidrat": 14,
        "Protein": 0.3,
        "Lemak": 0.2,
        "Serat": 2.4
    },
    "Pisang": {
        "Kalori": 105,
        "Karbohidrat": 27,
        "Protein": 1.3,
        "Lemak": 0.3,
        "Serat": 3.1
    },
    "Bakso": {
        "Kalori": 165,
        "Protein": 31,
        "Lemak": 3.6,
        "Karbohidrat": 0,
        "Serat": 0
    },
    "Salad": {
        "Kalori": 360,
        "Protein": 8,
        "Lemak": 36,
        "Karbohidrat": 4,
        "Serat": 2
    }
    
}

# Fungsi untuk mencetak informasi makanan
def print_food_info(food_name):
    food_name = food_name.capitalize()
    if food_name in food_info:
        print(f"Informasi gizi untuk {food_name}:")
        for nutrient, value in food_info[food_name].items():
            print(f"- {nutrient}: {value}g")
    else:
        print(f"Informasi gizi untuk {food_name} tidak ditemukan.")

# Menggunakan fungsi untuk mencetak informasi makanan
food_name = input("Masukkan nama makanan: ")
print_food_info(food_name)
