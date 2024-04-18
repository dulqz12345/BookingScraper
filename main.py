from bs4 import BeautifulSoup
import requests


def scrape_booking(search_query):
    URL = f"https://www.booking.com/search.html?ss={search_query}"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/123.0.0.0 Safari/537.36'}
    response = requests.get(URL, headers=headers)

    if response.status_code == 200:
        print(response.url)

        booking_gdansk = response.text
        soup = BeautifulSoup(booking_gdansk, "html.parser")
        # print(soup.prettify())
        print(soup.title)
        hotel_names = [name.text.strip() for name in soup.find_all('span', class_='sr-hotel__name')]
        return hotel_names
    else:
        print("Failed to fetch page")
        return []


search_query = "Gdansk"  # Example search query
hotels_found = scrape_booking(search_query)
print(hotels_found)

# def inc(x):
#     return x + 1
#
#
# def test_answer():
#     assert inc(3) == 4
