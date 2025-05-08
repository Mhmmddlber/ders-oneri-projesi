from django.urls import path
from .views import kategori_listesi, ders_listesi, ders_detay, recommend_courses,konu_basliklari,konuya_gore_dersler
from . import views
from django.conf.urls.static import static  # BU KISIM EKSİKTİ
from django.conf import settings  # Bunu eklemelisin
from .views import ders_ara  # ✅ Burada fonksiyonu import ettik
from django.http import JsonResponse


urlpatterns = [
    path('', kategori_listesi, name='kategori_listesi'),
    path('ders_listesi/<str:kategori>/', ders_listesi, name='ders_listesi'),
    

    path('ders/<str:kategori>/<str:ders_kodu>/', ders_detay, name='ders_detay'),
    path('tavsiye/<str:kategori>/', views.recommend_courses, name='recommend_courses'),
    path('ders_ara/', ders_ara, name='ders_ara'),
     path('konu_basliklari/<str:kategori>/', konu_basliklari, name='konu_basliklari'),
    path('ders_konulari/<str:kategori>/<str:konu>/', konuya_gore_dersler, name='konuya_gore_dersler'),


]
# Statik ve medya dosyalarını ekleyelim
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)