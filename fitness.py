import PySimpleGUI as sg
from datetime import datetime

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            last_node = self.head
            while last_node.next:
                last_node = last_node.next
            last_node.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

class FitnessTakipProgrami:
    def __init__(self):
        self.gunluk_antrenmanlar = LinkedList()

    def antrenman_girisi(self, tarih, antrenman_adı, set_sayisi, tekrar_sayisi):
        
        hedef_set_sayisi = sg.popup_get_text(f"{antrenman_adı} için hedef set sayısını girin:", "Antrenman Girişi")
        antrenman_verisi = {
            "Tarih": tarih,
            "Antrenman adı": antrenman_adı,
            "Set sayısı": set_sayisi,
            "Tekrar sayısı": tekrar_sayisi,
            "Hedef set sayısı": hedef_set_sayisi
        }
        self.gunluk_antrenmanlar.append(antrenman_verisi)
        print(f"Toplam Set Sayısı: {set_sayisi}, Toplam Tekrar Sayısı: {tekrar_sayisi}, Hedef Set Sayısı: {hedef_set_sayisi}")

    def ilerlemeyi_goruntule(self):
        try:
            aktivite_adi = sg.popup_get_text("İlerlemeyi görüntülemek istediğiniz aktiviteyi girin:", "İlerlemeyi Görüntüle")
            if aktivite_adi is None:
                print("İlerlemeyi görüntüleme iptal edildi.")
                return

            aktivite_adi = aktivite_adi.lower()
            toplam_set_sayisi= 0
            toplam_tekrar_sayisi = 0

            current = self.gunluk_antrenmanlar.head
            while current:
                if current.data["Antrenman adı"].lower() == aktivite_adi:
                    toplam_set_sayisi += int(current.data["Set sayısı"])
                    toplam_tekrar_sayisi += int(current.data["Tekrar sayısı"])
                current = current.next
            print(f"\nToplam Set Sayısı ({aktivite_adi}): {toplam_set_sayisi}")
            print(f"\nToplam Tekrar Sayısı ({aktivite_adi}): {toplam_tekrar_sayisi}")
            
        
            return

        except Exception as e:
            print(f"Hata oluştu: {e}")

    def istatistikleri_goruntule(self):
        try:
            toplam_antrenman_sayisi = 0
            toplam_set_sayisi = 0
            hedef_set_sayisi_toplam = 0
            girilen_set_sayisi_toplam = 0

            current = self.gunluk_antrenmanlar.head
            while current is not None:  # current None olana kadar döngüyü sürdür
                toplam_antrenman_sayisi += 1

            # Set sayısı alanını kontrol et
                if "Set sayısı" in current.data:
                  toplam_set_sayisi += int(current.data["Set sayısı"])
                else:
                  print("Hata: Antrenman verisinde 'Set sayısı' alanı bulunamadı.")

                if "Hedef set sayısı" in current.data:
                  hedef_set_sayisi_toplam += int(current.data["Hedef set sayısı"])
                  girilen_set_sayisi_toplam += int(current.data["Set sayısı"])

                current = current.next
            if toplam_antrenman_sayisi > 0:    

            # Hedef set sayısı ve girilen set sayısı arasındaki farkı hesapla
                kalan_set_sayisi = hedef_set_sayisi_toplam - girilen_set_sayisi_toplam
                print(f"Hedefe kalan set sayısı: {kalan_set_sayisi}")
            else:
                   print("Henüz antrenman girilmemiş.")

        except Exception as e:
          print(f"Hata oluştu: {e}")


    def son_antrenmani_goruntule(self):
        self.gunluk_antrenmanlar.display()

    def antrenman_sil(self, antrenman_adı):
        current = self.gunluk_antrenmanlar.head
        prev = None

        while current:
            if current.data["Antrenman adı"].lower() == antrenman_adı.lower() and current.data["Tarih"]==tarih:
                if prev:
                    prev.next = current.next
                else:
                    self.gunluk_antrenmanlar.head = current.next
                print(f"{antrenman_adı} adlı antrenman başarıyla silindi.")
                return
            prev = current
            current = current.next

        print(f"{antrenman_adı} adlı antrenman bulunamadı.")
# FitnessTakipProgrami sınıfını kullanarak programı başlat
fitness_programi = FitnessTakipProgrami()

# PySimpleGUI arayüzünü tasarla
layout = [
    [sg.Text("Fitness Takip Programı", font=("Helvetica", 16))],
    [sg.Button("Antrenman Girişi"), sg.Button("Son Antrenmanı Görüntüle"), sg.Button("Antrenman Sil"), sg.Button("İlerlemeyi Görüntüle"),sg.Button("İstatistikler")],
    [sg.Output(size=(60, 10))],
    [sg.Button("Çıkış", button_color=('white', 'red'))]
]

window = sg.Window("Fitness Takip Uygulaması", layout)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == "Çıkış":
        break
    elif event == "Antrenman Girişi":
        tarih = sg.popup_get_text("Antrenman tarihini girin (DD-MM-YYYY):", "Antrenman Girişi")
        antrenman_adı = sg.popup_get_text("Yapılan antrenmanı girin:", "Antrenman Girişi")
        set_sayisi = sg.popup_get_text("Yapılan set sayısını girin:", "Antrenman Girişi")
        tekrar_sayisi = sg.popup_get_text("Her sette yapılan tekrar sayısını girin:", "Antrenman Girişi")
        fitness_programi.antrenman_girisi(tarih, antrenman_adı, set_sayisi, tekrar_sayisi)
        print("Antrenman başarıyla kaydedildi.")
    elif event == "Son Antrenmanı Görüntüle":
        fitness_programi.son_antrenmani_goruntule()
    elif event == "İlerlemeyi Görüntüle":
        fitness_programi.ilerlemeyi_goruntule()
    elif event == "İstatistikler":
        fitness_programi.istatistikleri_goruntule()
    elif event == "Antrenman Sil":
        antrenman_adı = sg.popup_get_text("Silmek istediğiniz antrenmanın adını girin:", "Antrenman Sil")
        fitness_programi.antrenman_sil(antrenman_adı)

window.close()
