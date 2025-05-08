from django.shortcuts import render, get_object_or_404, redirect
from .models import MeslekiA, MeslekiB, SosyalSecmeli, UniversiteMeslekiSecmeli, Comment
from .forms import CommentForm
from sentence_transformers import SentenceTransformer
from sklearn.decomposition import TruncatedSVD
import torch
from django.http import JsonResponse

# 📌 Model yükle
model = SentenceTransformer('sentence-transformers/paraphrase-multilingual-mpnet-base-v2')

# 📌 **Modeli Yükleme**
model = SentenceTransformer('sentence-transformers/paraphrase-multilingual-mpnet-base-v2')

# 📌 **Ders Kategorileri ve Anahtar Kelimeler**
all_categories = {
    "sosyal_secmeli": {
        "keywords": {
            "Tarih ve Kültür": "tarih, kültür, uygarlık, coğrafya, geçmiş, toplum",
            "Spor ve Sağlık": "spor, sağlık, antrenman, egzersiz, kondisyon, fitness",
            "Genel Kültür": "genel, bilgi, kültür, toplum, eğitim, farkındalık",
            "Bilişim ve Teknoloji": "teknoloji, yapay zeka, metaverse, blockchain, yazılım",
            "Çevre ve Sürdürülebilirlik": "çevre, sürdürülebilirlik, ekoloji, doğa, planlama",
            "Yabancı Dil": "yabancı dil, almanca, fransızca, italyanca, çince, ispanyolca, japonca",
            "Dil ve Edebiyat": "edebiyat, şiir, yazı, hikaye, roman, anlatım",
            "Felsefe ve Sosyoloji": "felsefe, toplum, birey, sosyoloji, düşünce, analiz",
            "Sanat ve Müzik": "sanat, müzik, estetik, resim, heykel, tarih",
            "Hak ve Hukuk": "hak, hukuk, sorumluluk, insan hakları, kurallar"
        },
        "weights": {
            "Tarih ve Kültür": 1.0,
            "Spor ve Sağlık": 1.2,
            "Genel Kültür": 0.8,
            "Bilişim ve Teknoloji": 1.1,
            "Çevre ve Sürdürülebilirlik": 0.9,
            "Yabancı Dil": 1.5,
            "Dil ve Edebiyat": 1.0,
            "Felsefe ve Sosyoloji": 0.9,
            "Sanat ve Müzik": 1.3,
            "Hak ve Hukuk": 0.7
        }
    },
    "universite_mesleki_secmeli": {
        "keywords": {
            "Enerji ve Çevre": "enerji, sürdürülebilirlik, çevre, kaynak, planlama",
            "Bilim ve Teknoloji": "bilim, teknoloji, yenilik, araştırma, analiz, algoritma",
            "Mühendislik Ekonomisi ve Yönetimi": "ekonomi, yönetim, finans, maliyet, strateji",
            "Navigasyon ve Coğrafya": "navigasyon, coğrafya, yer, harita, pozisyon",
            "Tarih ve Kültür": "tarih, kültür, uygarlık, mekan, toplum, geçmiş",
            "Müzecilik ve Kültür Yönetimi": "müze, kültür, yönetim, tarih, miras",
            "Sağlık ve Biyoteknoloji": "sağlık, biyoteknoloji, sistem, kontrol, yaşam",
            "Matematik ve Modelleme": "matematik, modelleme, istatistik, analiz, optimizasyon",
            "Mekanik ve Malzeme": "mekanik, malzeme, üretim, sistem, tasarım",
            "İnşaat ve Mevzuat": "inşaat, mevzuat, yönetmelik, yapı, yasa",
            "Fizik ve Temel Bilimler": "fizik, temel bilimler, evrim, doğa, bilim",
            "Dil ve Edebiyat": "dil, edebiyat, yazı, roman, şiir",
            "Uluslararası İlişkiler": "uluslararası, ilişkiler, politika, kültür, yönetim"
        },
        "weights": {
            "Enerji ve Çevre": 1.0,
            "Bilim ve Teknoloji": 1.1,
            "Mühendislik Ekonomisi ve Yönetimi": 1.1,
            "Navigasyon ve Coğrafya": 1.0,
            "Tarih ve Kültür": 1.1,
            "Müzecilik ve Kültür Yönetimi": 1.2,
            "Sağlık ve Biyoteknoloji": 1.3,
            "Matematik ve Modelleme": 1.4,
            "Mekanik ve Malzeme": 1.2,
            "İnşaat ve Mevzuat": 1.0,
            "Fizik ve Temel Bilimler": 1.2,
            "Dil ve Edebiyat": 1.0,
            "Uluslararası İlişkiler": 1.0
        }
    },
    "mesleki_a": {
        "keywords": {
            "Yapay Zeka ve Veri Bilimi": "yapay zeka, öneri sistemleri, makine öğrenmesi, veri bilimi",
            "Mühendislik ve Malzeme Bilimi": "termodinamik, malzeme bilimi, mukavemet, üretim teknikleri",
            "İşletme ve Finans": "dijital pazarlama, finansal yönetim, pazarlama stratejileri, iş hukuku",
            "Yenilikçi Teknolojiler ve Uygulamalar": "sezgisel algoritmalar, yazılım uygulamaları, bulanık mantık",
            "Sistem Analizi ve Dinamikleri": "sistem dinamiği, sistem analizi, modelleme"
        },
        "weights": {
            "Yapay Zeka ve Veri Bilimi": 1.3,
            "Mühendislik ve Malzeme Bilimi": 1.2,
            "İşletme ve Finans": 1.1,
            "Yenilikçi Teknolojiler ve Uygulamalar": 1.0,
            "Sistem Analizi ve Dinamikleri": 1.2
        }
    },
    "mesleki_b": {
        "keywords": {
            "Üretim ve İmalat Yönetimi": "imalat, üretim, sistemleri, zeki, modern",
            "Bilgi Sistemleri ve Teknoloji Yönetimi": "bilgi sistemleri, teknoloji yönetimi, kurumsal, veritabanı",
            "Stratejik ve Operasyonel Yönetim": "stratejik yönetim, operasyonel, kriz yönetimi, proje yönetimi",
            "Veri Analizi ve Karar Verme": "veri analizi, karar verme, istatistik, optimizasyon",
            "Finans ve Muhasebe": "maliyet, muhasebe, finans, yönetim",
            "Yönetim ve Organizasyonel Gelişim": "insan kaynakları, organizasyonel psikoloji, davranış bilimleri",
            "İleri Mühendislik ve Teknoloji Uygulamaları": "endüstri 4.0, yapay zeka, otomatik kontrol, mühendislik",
            "Kalite ve Süreç İyileştirme": "kalite kontrol, süreç iyileştirme, sigma, yalın üretim"
        },
        "weights": {
            "Üretim ve İmalat Yönetimi": 1.0,
            "Bilgi Sistemleri ve Teknoloji Yönetimi": 1.1,
            "Stratejik ve Operasyonel Yönetim": 1.0,
            "Veri Analizi ve Karar Verme": 1.2,
            "Finans ve Muhasebe": 1.1,
            "Yönetim ve Organizasyonel Gelişim": 1.0,
            "İleri Mühendislik ve Teknoloji Uygulamaları": 1.3,
            "Kalite ve Süreç İyileştirme": 1.2
        }
    }
}


# 📌 Ana Sayfa
def kategori_listesi(request):
    return render(request, 'index.html')

# 📌 Kategoriye Ait Dersler
def ders_listesi(request, kategori):
    kategori_model_map = {
        'mesleki_a': MeslekiA,
        'mesleki_b': MeslekiB,
        'sosyal_secmeli': SosyalSecmeli,
        'universite_mesleki_secmeli': UniversiteMeslekiSecmeli,
    }

    model = kategori_model_map.get(kategori)
    dersler = model.objects.all() if model else []

    # 📌 Kategori Başlığını Belirle
    kategori_baslik = ""
    if kategori == "mesleki_a":
        kategori_baslik = "Mesleki A Dersleri"
    elif kategori == "mesleki_b":
        kategori_baslik = "Mesleki B Dersleri"
    elif kategori == "sosyal_secmeli":
        kategori_baslik = "Sosyal Seçmeli Dersleri"
    elif kategori == "universite_mesleki_secmeli":
        kategori_baslik = "Üniversite Mesleki Seçmeli Dersleri"

    return render(request, 'recommendations/ders_listesi.html', {
        'kategori': kategori,
        'dersler': dersler,
        'kategori_baslik': kategori_baslik,  # 🔥 Bunu da gönderdik!
    })


# 📌 Tek Bir Dersin Detayını Getir
def ders_detay(request, kategori, ders_kodu):
    kategori_mapping = {
        "mesleki_a": MeslekiA,
        "mesleki_b": MeslekiB,
        "sosyal_secmeli": SosyalSecmeli,
        "universite_mesleki_secmeli": UniversiteMeslekiSecmeli
    }
    model = kategori_mapping.get(kategori.lower())
    if not model:
        return render(request, '404.html', status=404)
    ders = get_object_or_404(model, ders_kodu=ders_kodu)
    yorumlar = Comment.objects.filter(ders=ders_kodu).order_by('-created_at')

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            yeni_yorum = form.save(commit=False)
            yeni_yorum.ders = ders_kodu
            yeni_yorum.save()
            return redirect('ders_detay', kategori=kategori, ders_kodu=ders_kodu)
    else:
        form = CommentForm()

    return render(request, 'recommendations/ders_detay.html', {
        'ders': ders,
        'kategori': kategori,
        'yorumlar': yorumlar,
        'form': form
    })

# 📌 İlgi Alanı ile Kategori Eşleştirme (Colab mantığı)
def match_category_with_embeddings(user_input, categories, weights):
    if not categories:
        return None
    input_embedding = model.encode(user_input, convert_to_tensor=True)
    category_scores = {}
    for category, keywords in categories.items():
        category_embedding = model.encode(keywords, convert_to_tensor=True)
        similarity_score = torch.matmul(input_embedding, category_embedding.T).item()
        weighted_score = similarity_score * weights.get(category, 1.0)
        category_scores[category] = weighted_score
    return max(category_scores, key=category_scores.get) if category_scores else None

# 📌 📢 GÜNCELLENEN: Ders Tavsiyesi Fonksiyonu
def recommend_courses(request, kategori):
    kategori_model_map = {
        'mesleki_a': MeslekiA,
        'mesleki_b': MeslekiB,
        'sosyal_secmeli': SosyalSecmeli,
        'universite_mesleki_secmeli': UniversiteMeslekiSecmeli,
    }
    if kategori not in kategori_model_map:
        return render(request, '404.html', status=404)

    user_interest = request.GET.get('ilgi_alani', '').strip()
    if not user_interest:
        return render(request, 'recommendations/recommendation.html', {'kategori': kategori})

    category_info = all_categories.get(kategori, {})
    best_category = match_category_with_embeddings(user_interest, category_info.get("keywords", {}), category_info.get("weights", {}))

    if not best_category:
        return render(request, 'recommendations/recommendation.html', {'kategori': kategori, 'user_interest': user_interest})

    dersler = kategori_model_map[kategori].objects.filter(ders_kategorisi=best_category)
    if not dersler.exists():
        return render(request, 'recommendations/recommendation.html', {'kategori': kategori, 'user_interest': user_interest})

    # 🔥 FULL TEXT oluştur
    course_texts = [
        f"{ders.ders_adi or ''} {ders.dersin_amaci or ''} {ders.dersin_icerigi or ''} {ders.ders_ogrenim_ciktilari or ''} {ders.haftalik_konular or ''}"
        for ders in dersler
    ]

    # 🔥 SBERT + LSA + Dot Product ile öneri
    course_embeddings = model.encode(course_texts, convert_to_tensor=False)
    lsa = TruncatedSVD(n_components=100)
    reduced_course_embeddings = lsa.fit_transform(course_embeddings)

    query_embedding = model.encode([user_interest], convert_to_tensor=False)
    reduced_query_embedding = lsa.transform(query_embedding)

    similarities = (reduced_query_embedding @ reduced_course_embeddings.T).flatten()

    recommended_courses = sorted(zip(dersler, similarities), key=lambda x: x[1], reverse=True)[:5]
    recommended_dersler = [{'ders_adi': d.ders_adi, 'ders_kodu': d.ders_kodu, 'score': s} for d, s in recommended_courses]


    return render(request, 'recommendations/recommendation.html', {
        'kategori': kategori,
        'best_category': best_category,
        'user_interest': user_interest,
        'dersler': recommended_dersler
    })

# 📌 Ders Arama
def ders_ara(request):
    ders_adi = request.GET.get('q', '').strip().lower()
    kategori_model_map = {
        "mesleki_a": MeslekiA,
        "mesleki_b": MeslekiB,
        "sosyal_secmeli": SosyalSecmeli,
        "universite_mesleki_secmeli": UniversiteMeslekiSecmeli
    }
    for kategori, model in kategori_model_map.items():
        ders = model.objects.filter(ders_adi__icontains=ders_adi).first()
        if ders:
            return JsonResponse({'success': True, 'kategori': kategori, 'ders_kodu': ders.ders_kodu})
    return JsonResponse({'success': False})

# 📌 Konu Başlıklarını JSON Döndür
def konu_basliklari(request, kategori):
    category_info = all_categories.get(kategori, {})
    if not category_info:
        return JsonResponse({'success': False, 'message': 'Kategori bulunamadı'}, status=404)
    topics = sorted(category_info.get("keywords", {}).keys())
    return JsonResponse({'success': True, 'topics': topics})

# 📌 Konuya Göre Dersleri Getir
def konuya_gore_dersler(request, kategori, konu):
    kategori_model_map = {
        "mesleki_a": MeslekiA,
        "mesleki_b": MeslekiB,
        "sosyal_secmeli": SosyalSecmeli,
        "universite_mesleki_secmeli": UniversiteMeslekiSecmeli
    }
    model = kategori_model_map.get(kategori)
    if not model:
        return JsonResponse({'success': False, 'message': 'Kategori bulunamadı'}, status=404)
    dersler = model.objects.filter(ders_kategorisi=konu)
    context = {
        "konu_baslik": konu,
        "kategori": kategori,
        "dersler": dersler
    }
    return render(request, "ders_konulari.html", context)