from datetime import date
from pathlib import Path
from internal.sky31_pptx import SKY31PPTX
from internal.sky31_pdf import SKY31PDF


class SKY31:
    def __init__(self, year: int = None, month: int = None):
        self._file_to_open = self._find_menu_file(year, month)
        self._loader = SKY31PPTX(self._file_to_open) \
            if self._file_to_open.lower().endswith('pptx') else SKY31PDF(self._file_to_open)

    def _find_menu_file(self, year: int = None, month: int = None) -> str:
        if year is None or month is None:
            yyyymm = date.today().strftime("%Y%m")
        else:
            yyyymm = date(year=year, month=month, day=1).strftime("%Y%m")
        pptx_file = f'{yyyymm}.pptx'
        pdf_file = f'{yyyymm}.pdf'
        if Path(pdf_file).exists():
            return pdf_file
        if Path(pptx_file).exists():
            return pptx_file
        raise FileNotFoundError

    def get_today_menus(self) -> []:
        return self._loader.get_today_menus()

    def get_monthly_menus(self):
        return self._loader.get_monthly_menus()


def print_monthly_menus(year: int, month: int):
    monthly_menu = SKY31(year=year, month=month).get_monthly_menus()
    print(f'========= {year}년 {month}월 =========')
    for m in monthly_menu:
        print(f'{year}년 {month}월 {m.nth_day}일 {m.menu} ({m.price:,d}원)')


if __name__ == '__main__':
    today_menu = SKY31().get_today_menus()
    print('오늘의 SKY 31 점심메뉴')
    for menu in today_menu:
        print(f'{menu.menu} ({menu.price:,d}원)')

    print_monthly_menus(2020, 10)
    print_monthly_menus(2020, 11)
    print_monthly_menus(2020, 12)
    print_monthly_menus(2021, 1)
    print_monthly_menus(2021, 2)
    print_monthly_menus(2021, 3)
