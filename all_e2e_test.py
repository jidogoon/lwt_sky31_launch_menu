import unittest
from datetime import date

from sky31 import SKY31


def get_monthly_menus(year: int, month: int) -> str:
    monthly_menu = SKY31(year=year, month=month).get_monthly_menus()
    result = f'========= {year}년 {month}월 =========\n'
    for m in monthly_menu:
        result += f'{year}년 {month}월 {m.nth_day}일 {m.menu} ({m.price:,d}원)\n'
    return result


class AllE2ETest(unittest.TestCase):
    def setUp(self):
        from internal.sky31_pptx import SKY31PPTX
        self.sky31_pptx = SKY31PPTX(pptx_file=None)

    def _get_test_result(self, year: int, month: int) -> str:
        yyyymm = date(year=year, month=month, day=1).strftime("%Y%m")
        with open(f'./test_files/{yyyymm}.txt', 'r', encoding='utf-8') as result_file:
            result = result_file.read()
            result_file.close()
        return result

    def _save_test_result(self, year: int, month: int):
        yyyymm = date(year=year, month=month, day=1).strftime("%Y%m")
        with open(f'./test_files/{yyyymm}.txt', 'w', encoding='utf-8') as result_file:
            result = get_monthly_menus(year, month)
            result_file.write(result)
            result_file.close()

    def test_monthly_results(self):
        print('testing...2020 10')
        self.assertEqual(get_monthly_menus(2020, 10), self._get_test_result(2020, 10))
        print('testing...2020 11')
        self.assertEqual(get_monthly_menus(2020, 11), self._get_test_result(2020, 11))
        print('testing...2020 12')
        self.assertEqual(get_monthly_menus(2020, 12), self._get_test_result(2020, 12))
        print('testing...2021 1')
        self.assertEqual(get_monthly_menus(2021, 1), self._get_test_result(2021, 1))
        print('testing...2021 2')
        self.assertEqual(get_monthly_menus(2021, 2), self._get_test_result(2021, 2))
        print('testing...2021 3')
        self.assertEqual(get_monthly_menus(2021, 3), self._get_test_result(2021, 3))
        print('testing...2021 4')
        self.assertEqual(get_monthly_menus(2021, 4), self._get_test_result(2021, 4))
        print('testing...2021 5')
        self.assertEqual(get_monthly_menus(2021, 5), self._get_test_result(2021, 5))

    def find_idx(self, text: str, word: str):
        all_positions = []
        next_pos = -1
        while True:
            next_pos = text.find(word, next_pos + 1)
            if next_pos < 0:
                break
            all_positions.append(next_pos)
        return all_positions

    def test_reduce_malformed_text(self):
        malformed_menu_text = '오색 비빔밥\n(8,000)\n\n해물 순두부 찌개(7,000)\n\n해물 순두부 찌개(7,000)해물 순두부 찌개(7,000)\n\n(8,000)'
        reduced_text = self.sky31_pptx._reduce_malformed_menu(malformed_menu_text)
        self.assertEqual(reduced_text, '오색 비빔밥\n(8,000)\n\n해물 순두부 찌개\n(7,000)\n\n해물 순두부 찌개\n(7,000)해물 순두부 찌개\n(7,000)\n\n(8,000)')

    def test_reduce_wellformed_text(self):
        malformed_menu_text = '오색 비빔밥\n(8,000)\n\n해물 순두부 찌개\n(7,000)\n\n해물 순두부 찌개\n(7,000)'
        reduced_text = self.sky31_pptx._reduce_malformed_menu(malformed_menu_text)
        self.assertEqual(reduced_text, malformed_menu_text)


if __name__ == '__main__':
    unittest.main()
