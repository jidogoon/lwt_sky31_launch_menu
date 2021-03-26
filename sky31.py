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


if __name__ == '__main__':
    today_menu = SKY31().get_today_menus()
    print(date.today().strftime("오늘의 SKY 31 점심메뉴 - %Y년 %m월 %d일"
                                .encode('unicode-escape').decode())
          .encode().decode('unicode-escape'))
    for menu in today_menu:
        print(f'{menu.menu} ({menu.price:,d}원)')

    monthly_menu = SKY31(year=2020, month=12).get_monthly_menus()
    print('========= 2020 12 =========')
    for m in monthly_menu:
        print(f'12월 {m.nth_day}일 {m.menu} ({m.price:,d}원)')

    monthly_menu = SKY31(year=2021, month=1).get_monthly_menus()
    print('========= 2021 01 =========')
    for m in monthly_menu:
        print(f'1월 {m.nth_day}일 {m.menu} ({m.price:,d}원)')

    monthly_menu = SKY31(year=2021, month=2).get_monthly_menus()
    print('========= 2021 02 =========')
    for m in monthly_menu:
        print(f'2월 {m.nth_day}일 {m.menu} ({m.price:,d}원)')

    monthly_menu = SKY31(year=2021, month=3).get_monthly_menus()
    print('========= 2021 03 =========')
    for m in monthly_menu:
        print(f'3월 {m.nth_day}일 {m.menu} ({m.price:,d}원)')

    monthly_menu = SKY31(year=2021, month=4).get_monthly_menus()
    print('========= 2021 04 =========')
    for m in monthly_menu:
        print(f'4월 {m.nth_day}일 {m.menu} ({m.price:,d}원)')
