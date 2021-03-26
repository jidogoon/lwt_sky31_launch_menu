from abc import ABC, abstractmethod
from datetime import date


class SKY31ABC(ABC):
    def __init__(self):
        self._menus = []

    def get_today_menus(self) -> []:
        self._load_menus()
        nth_day = date.today().day
        today_menus = list(filter(lambda m: m.nth_day == nth_day, self._menus))
        return today_menus

    def get_monthly_menus(self):
        self._load_menus()
        return self._menus

    @abstractmethod
    def _load_menus(self):
        pass

    def _clear_prev_month(self):
        first_day = 1
        last_day = 1
        for menu in self._menus:
            if menu.nth_day < last_day:
                first_day = menu.nth_day
                break
            last_day = menu.nth_day
        first_item = next(filter(lambda m: m.nth_day == first_day, self._menus), None)
        first_item_index = 0 if first_item is None else self._menus.index(first_item)
        self._menus = self._menus[first_item_index:]
