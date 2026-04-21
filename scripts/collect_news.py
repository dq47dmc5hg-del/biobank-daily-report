import requests
from bs4 import BeautifulSoup

# Function to collect news articles

def collect_biobank_news():
    articles = []
    sources = [
        {"name": "PubMed", "url": "https://pubmed.ncbi.nlm.nih.gov/", "filter": "biobank"},
        {"name": "bioRxiv", "url": "https://www.biorxiv.org/", "filter": "biobank"},
        {"name": "Science News", "url": "https://www.sciencenews.org/", "filter": "biobank"}
    ]
    
    for source in sources:
        response = requests.get(source['url'])
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            # Extract articles based on specific HTML structures (to be implemented)
            # Placeholder: You will need to tailor these selectors to the website's actual structure.
            for item in soup.find_all('article')[:20]:
                article = {
                    "category": source['name'],
                    "title": item.find('h2').get_text() if item.find('h2') else 'No Title',
                    "summary": item.find('p').get_text() if item.find('p') else 'No Summary',
                    "source": source['name'],
                    "url": item.find('a')['href'] if item.find('a') else 'No URL',
                }
                articles.append(article)
                if len(articles) >= 20:
                    break
        
    return articles


if __name__ == '__main__':
    news_articles = collect_biobank_news()
    for article in news_articles:
        print(article)