import tkinter as tk

def hesapla():
    sayi1 = float(giris1.get())
    sayi2 = float(giris2.get())
    islem = secim.get()

    if islem == "Toplama":
        sonuc.set(sayi1 + sayi2)
    elif islem == "Çıkarma":
        sonuc.set(sayi1 - sayi2)
    elif islem == "Çarpma":
        sonuc.set(sayi1 * sayi2)
    elif islem == "Bölme":
        if sayi2 == 0:
            sonuc.set("Hata! Sıfıra bölme hatası.")
        else:
            sonuc.set(sayi1 / sayi2)

# Tkinter penceresini oluştur
root = tk.Tk()
root.title("Basit Hesap Makinesi")

# Ekranın genişliğini ve yüksekliğini al
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Pencerenin boyutunu ve konumunu ayarla
window_width = 300
window_height = 200
x_coordinate = (screen_width - window_width) // 2
y_coordinate = (screen_height - window_height) // 2

# Ana pencereyi konumlandır
root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_coordinate, y_coordinate))

# Diğer widget'ları oluştur ve ekrana yerleştir
giris1 = tk.Entry(root)
giris1.place(relx=0.5, rely=0.4, anchor="center")

secenekler = ["Toplama", "Çıkarma", "Çarpma", "Bölme"]
secim = tk.StringVar(root)
secim.set(secenekler[0])
secim_menu = tk.OptionMenu(root, secim, *secenekler)
secim_menu.place(relx=0.5, rely=0.5, anchor="center")

giris2 = tk.Entry(root)
giris2.place(relx=0.5, rely=0.6, anchor="center")

sonuc = tk.StringVar()
sonuc_label = tk.Label(root, textvariable=sonuc)
sonuc_label.place(relx=0.5, rely=0.7, anchor="center")

hesapla_button = tk.Button(root, text="Hesapla", command=hesapla)
hesapla_button.place(relx=0.5, rely=0.8, anchor="center")

# Pencereyi göster
root.mainloop()
