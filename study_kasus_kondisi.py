import tkinter as tk
from tkinter import messagebox

def hitung_nutrisi():
    try:
        nama_makanan = entry_makanan.get()
        kalori = float(entry_kalori.get())
        karbohidrat = float(entry_karbohidrat.get())
        protein = float(entry_protein.get())
        lemak = float(entry_lemak.get())

        kalori_total = kalori * (kalori / 100)
        karbohidrat_total = karbohidrat * (karbohidrat / 100)
        protein_total = protein * (protein / 100)
        lemak_total = lemak * (lemak / 100)

        hasil_window = tk.Toplevel(root)
        hasil_window.title("Hasil Perhitungan Nutrisi")
        hasil_window.geometry("300x200")
        
        hasil_label = tk.Label(hasil_window, text=f"Nutrisi untuk Makanan: {nama_makanan}", font=("Arial", 14))
        hasil_label.pack(pady=10)
        
        kalori_label = tk.Label(hasil_window, text=f"Kalori: {kalori_total:.2f} kal", font=("Arial", 12))
        kalori_label.pack(pady=5)
        
        karbohidrat_label = tk.Label(hasil_window, text=f"Karbohidrat: {karbohidrat_total:.2f} g", font=("Arial", 12))
        karbohidrat_label.pack(pady=5)
        
        protein_label = tk.Label(hasil_window, text=f"Protein: {protein_total:.2f} g", font=("Arial", 12))
        protein_label.pack(pady=5)
        
        lemak_label = tk.Label(hasil_window, text=f"Lemak: {lemak_total:.2f} g", font=("Arial", 12))
        lemak_label.pack(pady=5)
    except ValueError:
        messagebox.showerror("Error", "Masukkan angka yang valid untuk nutrisi.")

root = tk.Tk()
root.title("Kalkulator Nutrisi")
root.geometry("400x300")
root.configure(bg='#f0f0f0')

label_makanan = tk.Label(root, text="Makanan:", font=("Arial", 12), bg='#f0f0f0')
label_makanan.grid(row=0, column=0, padx=10, pady=5)
entry_makanan = tk.Entry(root, font=("Arial", 12))
entry_makanan.grid(row=0, column=1, padx=10, pady=5)

label_kalori = tk.Label(root, text="Kalori (per 100g):", font=("Arial", 12), bg='#f0f0f0')
label_kalori.grid(row=1, column=0, padx=10, pady=5)
entry_kalori = tk.Entry(root, font=("Arial", 12))
entry_kalori.grid(row=1, column=1, padx=10, pady=5)

label_karbohidrat = tk.Label(root, text="Karbohidrat (per 100g):", font=("Arial", 12), bg='#f0f0f0')
label_karbohidrat.grid(row=2, column=0, padx=10, pady=5)
entry_karbohidrat = tk.Entry(root, font=("Arial", 12))
entry_karbohidrat.grid(row=2, column=1, padx=10, pady=5)

label_protein = tk.Label(root, text="Protein (per 100g):", font=("Arial", 12), bg='#f0f0f0')
label_protein.grid(row=3, column=0, padx=10, pady=5)
entry_protein = tk.Entry(root, font=("Arial", 12))
entry_protein.grid(row=3, column=1, padx=10, pady=5)

label_lemak = tk.Label(root, text="Lemak (per 100g):", font=("Arial", 12), bg='#f0f0f0')
label_lemak.grid(row=4, column=0, padx=10, pady=5)
entry_lemak = tk.Entry(root, font=("Arial", 12))
entry_lemak.grid(row=4, column=1, padx=10, pady=5)

hitung_button = tk.Button(root, text="Hitung Nutrisi", font=("Arial", 14), command=hitung_nutrisi, bg='#4CAF50', fg='white', padx=10, pady=5)
hitung_button.grid(row=5, column=0, columnspan=2, pady=20)

root.mainloop()
