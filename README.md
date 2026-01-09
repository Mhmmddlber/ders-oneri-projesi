# YTÜ Endüstri Mühendisliği - Akıllı Seçmeli Ders Öneri Sistemi

Bu repository, Yıldız Teknik Üniversitesi Endüstri Mühendisliği Bölümü bitirme tezi kapsamında geliştirilen, doğal dil işleme (NLP) tabanlı bir seçmeli ders öneri sistemini içermektedir. Sistem, öğrencilerin ilgi alanlarını serbest metin olarak analiz eder ve en uygun akademik içeriği saniyeler içinde sunar.

## Proje Özeti
Üniversite öğrencilerinin ders seçim süreçlerindeki zorlukları (içerik belirsizliği, uzmanlaşma hedefi karmaşası vb.) çözmek amacıyla geliştirilen bu sistem, anlamsal benzerlik (semantic similarity) metotlarını kullanarak kişiselleştirilmiş bir rehberlik sunar.

## Teknik Mimari ve Metodoloji
Sistem, basit anahtar kelime eşleşmesinin ötesine geçerek derin öğrenme modelleriyle çalışır:
- **Embedding (Vektörleştirme):** Çok dilli (Türkçe/İngilizce) ders dökümanlarını yüksek boyutlu anlamsal vektörlere dönüştürmek için **SBERT (Sentence-BERT)** modeli kullanılmıştır.
- **Boyut Azaltma (Dimensionality Reduction):** Hesaplama maliyetini düşürmek ve verideki gürültüyü temizlemek için **LSA (Latent Semantic Analysis)** uygulanmıştır.
- **Benzerlik Hesaplama:** Öğrenci girişi ile ders vektörleri arasındaki anlamsal yakınlık **Dot Product (Nokta Çarpımı)** yöntemiyle hesaplanarak en alakalı dersler sıralanmıştır.
- **Web Interface:** Kullanıcı dostu arayüz **Django (Python)** framework'ü ile geliştirilmiştir.

## Veri Seti ve Kapsam
Proje, YTÜ Endüstri Mühendisliği Bölümü'ne ait dört ana seçmeli ders grubunu kapsamaktadır:
- Mesleki Seçmeli A ve B
- Sosyal Seçmeli
- Üniversite Mesleki Seçmeli
Veriler, üniversitenin Bologna Bilgi Sistemi'nden; ders amaçları, içerikleri, öğrenim çıktıları ve haftalık konuları içerecek şekilde derlenmiştir.

## Öne Çıkan Özellikler
- **Doğal Dil Anlayışı:** "Yapay zeka ve veri analizi öğrenmek istiyorum" gibi doğal cümleleri anlar.
- **Duyarlı Filtreleme:** Sadece ilgili kategorideki dersleri akıllıca sıralar.
- **Kullanıcı Etkileşimi:** Öğrencilerin dersler hakkında yorum yapabileceği ve geçmiş deneyimleri paylaşabileceği bir panel içerir.

## 💻 Repository Yapısı
- **`engine/`**: SBERT ve LSA modellerinin entegre edildiği öneri motoru kodları.
- **`web_interface/`**: Django tabanlı web arayüzü dosyaları.
- **`data/`**: Bologna sisteminden derlenmiş ders veri setleri.
- **`docs/`**: "Banking CRM System - Undergraduate Graduation Thesis" başlıklı teknik rapor dökümanı.

---
*Bu çalışma Muhammed Dilber tarafından Prof. Dr. Alev TAŞKIN danışmanlığında hazırlanmış bir Lisans Bitirme Tezidir.*
