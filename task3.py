import requests
from bs4 import BeautifulSoup

def scrape_headlines(url, output_file="headlines.txt"):
    try:
        # Send GET request
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers)

        # Check if request was successful
        if response.status_code != 200:
            print(f"Failed to fetch page. Status code: {response.status_code}")
            return

        # Parse HTML
        soup = BeautifulSoup(response.text, "html.parser")

        # Extract headlines (adjust tag/class depending on site structure)
        headlines = []
        for h2 in soup.find_all("h2"):
            text = h2.get_text(strip=True)
            if text:
                headlines.append(text)

        # Save to file
        with open(output_file, "w", encoding="utf-8") as f:
            for hl in headlines:
                f.write(hl + "\n")

        print(f"Scraped {len(headlines)} headlines and saved to {output_file}")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    # Example: BBC News homepage (you can change this)
    url = "https://www.bbc.com/news"
    scrape_headlines(url)
