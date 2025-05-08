import csv
from recommendations.models import MeslekiA

def load_mesleki_a_to_database(file_path):
    encoding_format = detect_encoding(file_path)  # Önce kodlamayı tespit edelim
    with open(file_path, newline='', encoding=encoding_format) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            MeslekiA.objects.create(
                ders_adi=row['Ders Adı'],
                ders_kodu=row['Ders Kodu'],
                on_kosullar=row['Ön Koşullar'],
                yariyil=row['Yarıyıl'],
                dersin_dili=row['Dersin Dili'],
                dersin_seviyesi=row['Dersin Seviyesi'],
                ders_kategorisi=row['Ders Kategorisi'],
                dersi_sunan_birim=row['Dersi Sunan Akademik Birim'],
                dersin_amaci=row['Dersin Amacı'],
                dersin_icerigi=row['Dersin İçeriği'],
                ders_kitaplari=row['Ders Kitapları'],
                ders_ogrenim_ciktilari=row['Ders Öğrenim Çıktıları'],
                haftalik_konular=row['Haftalık Konular'],
                degerlendirme_sistemi=row['Değerlendirme Sistemi']
            )
    print("Mesleki A verileri başarıyla yüklendi!")

def detect_encoding(file_path):
    import chardet
    with open(file_path, 'rb') as f:
        result = chardet.detect(f.read())
        return result['encoding']
