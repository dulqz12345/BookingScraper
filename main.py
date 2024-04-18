from bs4 import BeautifulSoup
import requests

URL = ('https://www.booking.com/searchresults.pl.html?ss=Gda%C5%84sk%2C+Polska&efdco=1&label=gen173nr'
       '-1FCAEoggI46AdIHlgEaLYBiAEBmAEeuAEXyAEM2AEB6AEB'
       '-AECiAIBqAIDuAK184SxBsACAdICJGM4MTZmMzk0LTYzZDMtNDQ2ZS05ZTI2LTYzYzUwN2E1NmZhZtgCBeACAQ&aid=304142&lang=pl&sb'
       '=1&src_elem=sb&src=index&dest_id=-501400&dest_type=city&checkin=2024-07-13&checkout=2024-07-21&group_adults=2'
       '&no_rooms=1&group_children=0')

response = requests.get(URL)
print(response.status_code)
print(response.url)
booking_gdansk = response.text

soup = BeautifulSoup(booking_gdansk, "html.parser")
#print(soup.prettify())
print(soup.title)

# def inc(x):
#     return x + 1
#
#
# def test_answer():
#     assert inc(3) == 4
