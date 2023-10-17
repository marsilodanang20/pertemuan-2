import tkinter as tk
from tkinter import messagebox

def hitung_nilai_akhir():
    try:
        nim = entry_nim.get()
        nama = entry_nama.get()
        nilai_kehadiran = float(entry_kehadiran.get())
        nilai_tugas = float(entry_tugas.get())
        nilai_uts = float(entry_uts.get())
        nilai_uas = float(entry_uas.get())

        nilai_akhir = (0.10 * nilai_kehadiran) + (0.20 * nilai_tugas) + (0.30 * nilai_uts) + (0.40 * nilai_uas)
        nilai_mutu = ""

        if nilai_akhir >= 85:
            nilai_mutu = "A"
        elif nilai_akhir >= 75:
            nilai_mutu = "B"
        elif nilai_akhir >= 55:
            nilai_mutu = "C"
        elif nilai_akhir >= 40:
            nilai_mutu = "D"
        else:
            nilai_mutu = "E"

        # Menampilkan hasil perhitungan di jendela baru
        hasil_window = tk.Toplevel(root)
        hasil_window.title("Hasil Perhitungan")
        hasil_window.geometry("300x200")
        
        hasil_label = tk.Label(hasil_window, text=f"Hasil Perhitungan untuk NIM {nim} - {nama}:", font=("Arial", 14))
        hasil_label.pack(pady=10)
        
        nilai_akhir_label = tk.Label(hasil_window, text=f"Nilai Akhir: {nilai_akhir:.2f}", font=("Arial", 12))
        nilai_akhir_label.pack(pady=5)

        nilai_mutu_label = tk.Label(hasil_window, text=f"Nilai Mutu: {nilai_mutu}", font=("Arial", 12))
        nilai_mutu_label.pack(pady=5)

    except ValueError:
        messagebox.showerror("Error", "Masukkan angka yang valid untuk nilai.")

# Membuat GUI
root = tk.Tk()
root.title("Aplikasi Penghitung Nilai Akhir")
root.geometry("400x300")
root.configure(bg='#f0f0f0')

# Label dan entry untuk NIM dan Nama
label_nim = tk.Label(root, text="NIM:", font=("Arial", 12), bg='#f0f0f0')
label_nim.grid(row=0, column=0, padx=10, pady=5)
entry_nim = tk.Entry(root, font=("Arial", 12))
entry_nim.grid(row=0, column=1, padx=10, pady=5)

label_nama = tk.Label(root, text="Nama:", font=("Arial", 12), bg='#f0f0f0')
label_nama.grid(row=1, column=0, padx=10, pady=5)
entry_nama = tk.Entry(root, font=("Arial", 12))
entry_nama.grid(row=1, column=1, padx=10, pady=5)

# Label dan entry untuk nilai
label_kehadiran = tk.Label(root, text="Nilai Kehadiran:", font=("Arial", 12), bg='#f0f0f0')
label_kehadiran.grid(row=2, column=0, padx=10, pady=5)
entry_kehadiran = tk.Entry(root, font=("Arial", 12))
entry_kehadiran.grid(row=2, column=1, padx=10, pady=5)

label_tugas = tk.Label(root, text="Nilai Tugas:", font=("Arial", 12), bg='#f0f0f0')
label_tugas.grid(row=3, column=0, padx=10, pady=5)
entry_tugas = tk.Entry(root, font=("Arial", 12))
entry_tugas.grid(row=3, column=1, padx=10, pady=5)

label_uts = tk.Label(root, text="Nilai UTS:", font=("Arial", 12), bg='#f0f0f0')
label_uts.grid(row=4, column=0, padx=10, pady=5)
entry_uts = tk.Entry(root, font=("Arial", 12))
entry_uts.grid(row=4, column=1, padx=10, pady=5)

label_uas = tk.Label(root, text="Nilai UAS:", font=("Arial", 12), bg='#f0f0f0')
label_uas.grid(row=5, column=0, padx=10, pady=5)
entry_uas = tk.Entry(root, font=("Arial", 12))
entry_uas.grid(row=5, column=1, padx=10, pady=5)

# Tombol untuk menghitung nilai akhir
hitung_button = tk.Button(root, text="Hitung Nilai Akhir", font=("Arial", 14), command=hitung_nilai_akhir, bg='#4CAF50', fg='white', padx=10, pady=5)
hitung_button.grid(row=6, column=0, columnspan=2, pady=20)

root.mainloop()