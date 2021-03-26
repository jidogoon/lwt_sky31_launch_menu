import camelot
from PyPDF2 import PdfFileReader
from camelot.core import TableList
from pandas import DataFrame

from internal.menu_data import MenuData
from internal.sky31_abc import SKY31ABC
from internal.util import Util


class SKY31PDF(SKY31ABC):
    def __init__(self, pdf_file: str):
        super().__init__()
        self._file_to_open = pdf_file

    def _load_menus(self):
        self._get_menu_tables()

    def _get_menu_tables(self):
        pdf_tables = self._get_pdf_tables()
        df = self._prepare_table(pdf_tables)
        self._parse_table(df)
        self._clear_prev_month()

    def _prepare_table(self, pdf_tables: TableList):
        df = None
        for pdf_table in pdf_tables:
            if None is df:
                df = pdf_table.df
                continue
            df = df.append(pdf_table.df, ignore_index=True)
        return df

    def _parse_table(self, df: DataFrame):
        for r_index, row in df.iterrows():
            if not row[0].endswith('주차'):
                continue
            for c_index, cell in row.iteritems():
                if self._is_ignore_cell(c_index):
                    continue
                self._find_menu(c_index, cell, df, r_index)

    def _find_menu(self, c_index: int, cell: str, df: DataFrame, r_index: int):
        for i in range(1, 4):
            menu_text = df[c_index][r_index + i].replace('\x0b', '\n').strip()
            if '' is menu_text:
                continue
            nth_day = Util.only_num(cell)
            menu_text_spt = menu_text.split('\n')
            if len(menu_text_spt) < 2:
                continue
            self._append_menu(menu_text_spt, nth_day)
            if len(menu_text_spt) > 3:
                self._append_menu(menu_text_spt, nth_day, moremenu=True)

    def _append_menu(self, menu_text_spt: [], nth_day: int, moremenu: bool = False):
        offset = 2 if moremenu else 0
        price = Util.only_num(menu_text_spt[1 + offset])
        if None is price:
            return
        self._menus.append(MenuData(nth_day=nth_day,
                                    menu=menu_text_spt[0 + offset],
                                    price=price))

    def _is_ignore_cell(self, c_index: int) -> bool:
        return c_index < 1

    def _get_pdf_tables(self):
        pdf = PdfFileReader(open(self._file_to_open, 'rb'))
        page_size = pdf.getNumPages()
        page_params = []
        for i in range(1, page_size + 1):
            page_params.append(str(i))
        page_param = ','.join(page_params)
        return camelot.read_pdf(self._file_to_open, pages=page_param)
