from django.contrib import admin
from .models import MeslekiA, MeslekiB, SosyalSecmeli, UniversiteMeslekiSecmeli

@admin.register(MeslekiA)
class MeslekiAAdmin(admin.ModelAdmin):
    list_display = ('ders_adi', 'ders_kodu', 'on_kosullar', 'yariyil', 'dersin_dili', 
                    'dersin_seviyesi', 'ders_kategorisi', 'dersi_sunan_birim', 
                    'dersin_amaci', 'dersin_icerigi', 'ders_kitaplari', 'ders_ogrenim_ciktilari', 
                    'haftalik_konular', 'degerlendirme_sistemi')

@admin.register(MeslekiB)
class MeslekiBAdmin(admin.ModelAdmin):
    list_display = ('ders_adi', 'ders_kodu', 'on_kosullar', 'yariyil', 'dersin_dili', 
                    'dersin_seviyesi', 'ders_kategorisi', 'dersi_sunan_birim', 
                    'dersin_amaci', 'dersin_icerigi', 'ders_kitaplari', 'ders_ogrenim_ciktilari', 
                    'haftalik_konular', 'degerlendirme_sistemi')

@admin.register(SosyalSecmeli)
class SosyalSecmeliAdmin(admin.ModelAdmin):
    list_display = ('ders_adi', 'ders_kodu', 'on_kosullar', 'yariyil', 'dersin_dili', 
                    'dersin_seviyesi', 'ders_kategorisi', 'dersi_sunan_birim', 
                    'dersin_amaci', 'dersin_icerigi', 'ders_kitaplari', 'ders_ogrenim_ciktilari', 
                    'haftalik_konular', 'degerlendirme_sistemi')

@admin.register(UniversiteMeslekiSecmeli)
class UniversiteMeslekiSecmeliAdmin(admin.ModelAdmin):
    list_display = ('ders_adi', 'ders_kodu', 'on_kosullar', 'yariyil', 'dersin_dili', 
                    'dersin_seviyesi', 'ders_kategorisi', 'dersi_sunan_birim', 
                    'dersin_amaci', 'dersin_icerigi', 'ders_kitaplari', 'ders_ogrenim_ciktilari', 
                    'haftalik_konular', 'degerlendirme_sistemi')

from .models import Comment

admin.site.register(Comment)
