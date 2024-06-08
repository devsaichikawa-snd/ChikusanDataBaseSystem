"""Excel オペレーション"""

from openpyxl import load_workbook

from common.util import is_none_or_empty


def read_workbook(file_path):
    """指定したExcel Bookを読み込む"""
    wb = load_workbook(file_path)
    return wb


def save_and_close_book(wb, file_path=None, save_flag=False):
    """指定したExcel Bookを保存・閉じる"""
    if save_flag:
        wb.save(file_path)
    wb.close()


def read_sheet(wb, sheet_name=None):
    """指定したExcel Sheetを開く"""
    if sheet_name is None:
        ws = wb.active
    else:
        ws = wb[sheet_name]
    return ws


def read_cell(ws, row: int, column: int) -> str:
    """cellの値を取得する"""
    if row < 0 or column < 0:
        # row/columnがマイナス値の場合はエラーにする
        raise ValueError("引数を確認してください。")
    value = ws.cell(row=row, column=column).value
    if is_none_or_empty(value):
        # Noneまたは空文字の場合、空文字にする
        return ""
    return value


def write_cell(ws, row: int, column: int, value):
    """cellの値を書き込む"""
    ws.cell(row=row, column=column).value = value


def excel_to_pdf():
    """ExcelファイルをPDFファイルに変換する"""
    pass
