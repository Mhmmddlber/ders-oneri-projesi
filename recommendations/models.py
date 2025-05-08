from django.db import models

class MeslekiA(models.Model):
    ders_adi = models.CharField(max_length=255)
    ders_kodu = models.CharField(max_length=50, primary_key=True)
    on_kosullar = models.TextField(null=True, blank=True)
    yariyil = models.CharField(max_length=50)
    dersin_dili = models.CharField(max_length=50)
    dersin_seviyesi = models.CharField(max_length=50)
    ders_kategorisi = models.CharField(max_length=100)
    dersi_sunan_birim = models.CharField(max_length=100)
    dersin_amaci = models.TextField()
    dersin_icerigi = models.TextField()
    ders_kitaplari = models.TextField(null=True, blank=True)
    ders_ogrenim_ciktilari = models.TextField(null=True, blank=True)
    haftalik_konular = models.TextField(null=True, blank=True)
    degerlendirme_sistemi = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.ders_adi


class MeslekiB(models.Model):
    ders_adi = models.CharField(max_length=255)
    ders_kodu = models.CharField(max_length=50, primary_key=True)
    on_kosullar = models.TextField(null=True, blank=True)
    yariyil = models.CharField(max_length=50)
    dersin_dili = models.CharField(max_length=50)
    dersin_seviyesi = models.CharField(max_length=50)
    ders_kategorisi = models.CharField(max_length=100)
    dersi_sunan_birim = models.CharField(max_length=100)
    dersin_amaci = models.TextField()
    dersin_icerigi = models.TextField()
    ders_kitaplari = models.TextField(null=True, blank=True)
    ders_ogrenim_ciktilari = models.TextField(null=True, blank=True)
    haftalik_konular = models.TextField(null=True, blank=True)
    degerlendirme_sistemi = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.ders_adi


class SosyalSecmeli(models.Model):
    ders_adi = models.CharField(max_length=255)
    ders_kodu = models.CharField(max_length=50, primary_key=True)
    on_kosullar = models.TextField(null=True, blank=True)
    yariyil = models.CharField(max_length=50)
    dersin_dili = models.CharField(max_length=50)
    dersin_seviyesi = models.CharField(max_length=50)
    ders_kategorisi = models.CharField(max_length=100)
    dersi_sunan_birim = models.CharField(max_length=100)
    dersin_amaci = models.TextField()
    dersin_icerigi = models.TextField()
    ders_kitaplari = models.TextField(null=True, blank=True)
    ders_ogrenim_ciktilari = models.TextField(null=True, blank=True)
    haftalik_konular = models.TextField(null=True, blank=True)
    degerlendirme_sistemi = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.ders_adi


class UniversiteMeslekiSecmeli(models.Model):
    ders_adi = models.CharField(max_length=255)
    ders_kodu = models.CharField(max_length=50, primary_key=True)
    on_kosullar = models.TextField(null=True, blank=True)
    yariyil = models.CharField(max_length=50)
    dersin_dili = models.CharField(max_length=50)
    dersin_seviyesi = models.CharField(max_length=50)
    ders_kategorisi = models.CharField(max_length=100)
    dersi_sunan_birim = models.CharField(max_length=100)
    dersin_amaci = models.TextField()
    dersin_icerigi = models.TextField()
    ders_kitaplari = models.TextField(null=True, blank=True)
    ders_ogrenim_ciktilari = models.TextField(null=True, blank=True)
    haftalik_konular = models.TextField(null=True, blank=True)
    degerlendirme_sistemi = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.ders_adi




class Comment(models.Model):
    ders = models.CharField(max_length=50)  # Ders koduna referans
    yorum = models.TextField()  # Yorum içeriği
    created_at = models.DateTimeField(auto_now_add=True)  # Yorum tarihi

    def __str__(self):
        return f"{self.ders} - {self.created_at.strftime('%Y-%m-%d %H:%M')}"

  

class Ders(models.Model):
    ders_adi = models.CharField(max_length=255)
    ders_kodu = models.CharField(max_length=50, unique=True)
    ders_kategorisi = models.CharField(max_length=255)

    def __str__(self):
        return self.ders_adi

