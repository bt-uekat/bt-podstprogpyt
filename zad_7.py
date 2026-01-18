import requests


class Brewery:
    def __init__(self, name: str, city: str, brewery_type: str):
        self.name: str = name
        self.city: str = city
        self.brewery_type: str = brewery_type

    def __str__(self) -> str:
        return (
            f"Browar: {self.name} "
            f"Miasto: {self.city} Typ: {self.brewery_type}"
        )


url = "https://api.openbrewerydb.org/v1/breweries"
response = requests.get(url)
data = response.json()
brewery_list = []
for item in data[:20]:
    new_brewery = Brewery(
        name=item.get("name", "Unknown"),
        city=item.get("city", "Unknown"),
        brewery_type=item.get("brewery_type", "Unknown"),
    )
    brewery_list.append(new_brewery)
for brewery in brewery_list:
    print(brewery)
