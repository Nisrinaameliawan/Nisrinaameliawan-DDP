import tkinter as tk
from tkinter import ttk


def hitung_kalori():
    umur = int(combo_umur.get().split('-')[0])
    berat = float(entry_berat.get())
    if umur >= 0 and umur <= 3:
        kalori = (89 * berat - 100) + 175
    elif umur >= 4 and umur <= 6:
        kalori = (89 * berat - 100) + 56
    elif umur >= 7 and umur <= 12:
        kalori = (89 * berat - 100) + 22
    else:
        kalori = (89 * berat - 100) + 20
        
    label_hasil["text"] = f"Kalori harian: {kalori}"

def about():
    global label_hasil, combo_umur, entry_berat, about_frame

    about_window = tk.Toplevel(root)
    about_window.title("Kalkulator")
    
    about_frame = ttk.Frame(about_window, padding="10", style='TFrame')
    about_frame.grid()
    style = ttk.Style()
    style.configure('TFrame', background='pink')
    
    about_label = ttk.Label(about_frame, text="Aplikasi Kalkulator Kalori Harian Bayi")
    about_label.grid(column=0, row=0, columnspan=2, pady=10)

    label_umur = ttk.Label(about_frame, text="Pilih Umur:")
    label_umur.grid(column=0, row=1, sticky=(tk.W, tk.E))

    umur_options = ["0-3 bulan", "4-6 bulan", "7-12 bulan", "13-35 bulan"]
    combo_umur = ttk.Combobox(about_frame, values=umur_options)
    combo_umur.grid(column=1, row=1)

    label_berat = ttk.Label(about_frame, text="Berat Badan Bayi (kg):")
    label_berat.grid(column=0, row=2, sticky=(tk.W, tk.E))

    entry_berat = ttk.Entry(about_frame)
    entry_berat.grid(column=1, row=2)

    button_hitung = ttk.Button(about_frame, text="Hitung", command=hitung_kalori, style='TButton')
    button_hitung.grid(column=0, row=3, columnspan=2)
    style.configure('TButton', background='white', foreground='magenta')

    label_hasil = ttk.Label(about_frame, text="Kalori Harian: ", style='TLabel')
    label_hasil.grid(column=0, row=4, columnspan=2)
    style.configure('TLabel', foreground='magenta', background='white')

root = tk.Tk()
root.title("")

background_label = tk.Label(root, bg="pink")
background_label.place(relwidth=1, relheight=1)

welcome_label = tk.Label(root, text="Welcome Moms", font=("Arial", 18), bg="pink", fg="white")
welcome_label.place(relx=0.5, rely=0.5, anchor="center")

menubar = tk.Menu(root)
root.config(menu=menubar)

file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="Open", command=about)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

menubar.add_cascade(label="Masuk Kalkulator", menu=file_menu)

root.mainloop()
