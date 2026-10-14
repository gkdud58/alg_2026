from dataclasses import dataclass

@dataclass
class City:
    name: str
    x: int
    y: int
    index: int

c1 = City("Seoul", 37, 127, 1)
c2 = City(x=35, name = "Busan", y=129, index=2)

city_dicts = [
  {
    "name": "Clean",
    "x": 1336,
    "y": 536,
    "index": 0
  },
  {
    "name": "Prosy",
    "x": 977,
    "y": 860,
    "index": 1
  },
  {
    "name": "Rabbi",
    "x": 6,
    "y": 758,
    "index": 2
  }
  ]

cities = [City(**d) for d in city_dicts]

print(cities)