import requests
from textblob import TextBlob
import matplotlib.pyplot as plt
import seaborn as sns


def fetch_comments(url, params=None):
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  
        return response.json()  
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP hatası oluştu: {http_err}")
        print(f"API Yanıtı: {response.text}")  
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Bağlantı hatası oluştu: {conn_err}")
    except requests.exceptions.Timeout as timeout_err:
        print(f"Zaman aşımı hatası oluştu: {timeout_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Genel bir hata oluştu: {req_err}")
    return None


def analyze_sentiment(text):
    analysis = TextBlob(text)
    if analysis.sentiment.polarity > 0:
        return "Olumlu"
    elif analysis.sentiment.polarity < 0:
        return "Olumsuz"
    else:
        return "Nötr"


url = "https://api.stackexchange.com/2.3/comments"


params = {
    "site": "stackoverflow",
    "order": "desc",
    "sort": "creation",
    "filter": "withbody",  
    "pagesize": 100,  
    "key": "rl_9EoKsGALwrALrMpMe4Q35KuWV",  
    "tagged": "Python"  
}


toplam_yorum_sayisi = 0
olumlu_sayisi = 0
olumsuz_sayisi = 0
notr_sayisi = 0


for page in range(1, 16):  
    params["page"] = page  
    comments = fetch_comments(url, params)

    if comments and comments.get('items'):
        toplam_yorum_sayisi += len(comments['items'])  

        
        for comment in comments['items']:
            yorum_icerik = comment.get('body', '')
            sentiment = analyze_sentiment(yorum_icerik)

            if sentiment == "Olumlu":
                olumlu_sayisi += 1
            elif sentiment == "Olumsuz":
                olumsuz_sayisi += 1
            else:
                notr_sayisi += 1

    
    if not comments.get('has_more', False):
        break


def visualize_results(olumlu, olumsuz, notr):
    
    labels = ['Olumlu', 'Olumsuz', 'Nötr']
    sizes = [olumlu, olumsuz, notr]
    colors = ['#66b3ff', '#ff9999', '#99ff99']
    explode = (0.1, 0, 0)  

    
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
    plt.title('Python ile İlgili Yorumların Duygu Dağılımı (Pasta Grafiği)')

    
    plt.subplot(1, 2, 2)
    sns.barplot(x=labels, y=sizes, hue=labels, palette=colors, legend=False)
    plt.title('Python ile İlgili Yorumların Duygu Dağılımı (Bar Grafiği)')
    plt.xlabel('Duygu')
    plt.ylabel('Yorum Sayısı')

    
    plt.tight_layout()
    plt.show()

visualize_results(olumlu_sayisi, olumsuz_sayisi, notr_sayisi)


print(f"Toplam çekilen yorum sayısı: {toplam_yorum_sayisi}")
print(f"Olumlu yorum sayısı: {olumlu_sayisi}")
print(f"Olumsuz yorum sayısı: {olumsuz_sayisi}")
print(f"Nötr yorum sayısı: {notr_sayisi}")