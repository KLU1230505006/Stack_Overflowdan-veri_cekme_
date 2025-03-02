Python Yorumları Duygu Analizi

Bu proje, Stack Overflow'daki Python ile ilgili yorumları çekerek, duygu analizi yapmayı ve sonuçları görselleştirmeyi amaçlamaktadır. 
API'den alınan yorumlar, TextBlob kütüphanesi ile analiz edilir ve olumlu, olumsuz veya nötr olarak sınıflandırılır. Sonuçlar, pasta grafiği ve çubuk grafik şeklinde görselleştirilir.

Özellikler

Stack Overflow API'sinden Python ile ilgili yorumları çeker.
TextBlob kullanarak yorumların duygu analizini yapar.
Sonuçları pasta grafiği ve çubuk grafik ile görselleştirir.

Gereksinimler

Bu projeyi çalıştırmak için aşağıdaki Python kütüphanelerinin yüklü olması gerekmektedir:

requests,textblob,matplotlib,seaborn

Bu kütüphaneleri yüklemek için aşağıdaki komutu çalıştırabilirsiniz:

pip install requests textblob matplotlib seaborn

Ayrıca, TextBlob kütüphanesinin dil modeli için aşağıdaki komutu çalıştırmanız gerekebilir:

python -m textblob.download_corpora



Kurulum
Bu repoyu klonlayın:
git clone https://github.com/kullaniciadi/proje-adi.git

Proje klasörüne gidin:
cd proje-adi

Gerekli bağımlılıkları yükleyin:
pip install -r requirements.txt



Kullanım
Proje, Stack Overflow'dan yorumları çekip analiz eder ve sonuçları görselleştirir. Çalıştırmak için aşağıdaki komutu kullanabilirsiniz:

python sentiment_analysis.py

Çalıştırdıktan sonra, toplam yorum sayısı ve duygu analiz sonuçları terminalde görüntülenecek ve grafikler gösterilecektir.


API Anahtarı
Kodda kullanılan API anahtarı (key parametresi), Stack Overflow API'sine yapılan istekleri yönetmek için gereklidir.
Eğer API erişiminde bir sorun yaşarsanız, kendi Stack Exchange API Anahtarınızı alarak params sözlüğünde güncelleyebilirsiniz.
