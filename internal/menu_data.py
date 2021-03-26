from dataclasses import dataclass


@dataclass()
class MenuData:
    nth_day: int
    menu: str
    price: int
