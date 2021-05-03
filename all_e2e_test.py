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
    def _get_test_result(self, year: int, month: int) -> str:
        yyyymm = date(year=year, month=month, day=1).strftime("%Y%m")
        with open(f'./test_files/{yyyymm}.txt', 'r') as result_file:
            result = result_file.read()
            result_file.close()
        return result

    def test_monthly_results(self):
        self.assertEqual(get_monthly_menus(2020, 10), self._get_test_result(2020, 10))
        self.assertEqual(get_monthly_menus(2020, 11), self._get_test_result(2020, 11))
        self.assertEqual(get_monthly_menus(2020, 12), self._get_test_result(2020, 12))
        self.assertEqual(get_monthly_menus(2021, 1), self._get_test_result(2021, 1))
        self.assertEqual(get_monthly_menus(2021, 2), self._get_test_result(2021, 2))
        self.assertEqual(get_monthly_menus(2021, 3), self._get_test_result(2021, 3))
        self.assertEqual(get_monthly_menus(2021, 4), self._get_test_result(2021, 4))


if __name__ == '__main__':
    AllE2ETest().test_monthly_results()
