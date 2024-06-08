import re

from common.excel import (
    read_workbook,
    read_sheet,
    save_and_close_book,
    read_cell,
    write_cell,
)
from common.util import (
    is_none_or_empty,
    remove_day_str,
    from_str_to_date,
    file_copy,
    time_keeper,
    delete_file,
)
from pork_carcass_data.const import (
    DOWNLOAD_DIR,
    EXCEL_TEMPLATE_DIR,
    EXCEL_TEMPLATE_FILE_NAME,
    OUTPUT_PORK_CARCASS_DIR,
    DEFAULT_ROW_DLFILE,
    DEFAULT_ROW_SUMMARYFILE,
)
from pork_carcass_data.model import ExcelPorkCarcassSummaryModel


def cleansing_pork_carcass(file_date):
    """Cleansing"""
    # ダウンロードファイルを開く
    download_file_path = DOWNLOAD_DIR + f"豚肉相場一覧表_{file_date}.xlsx"
    wb = read_workbook(download_file_path)
    ws = read_sheet(wb)

    # DLファイルデータ→ExcelSummaryModelへの変換(読み込み)
    model_list = []
    model_list = __read_dl_file_data(file_date, ws, model_list)
    # DLファイルを閉じる
    save_and_close_book(wb)

    # Summaryのコピー(テンプレートを直接触らない)
    original_sammary_file_path = EXCEL_TEMPLATE_DIR + EXCEL_TEMPLATE_FILE_NAME
    file_copy(original_sammary_file_path, OUTPUT_PORK_CARCASS_DIR)
    time_keeper(2)

    # コピー先のSummaryファイルを開く
    copy_sammary_file_path = OUTPUT_PORK_CARCASS_DIR + EXCEL_TEMPLATE_FILE_NAME
    wb = read_workbook(copy_sammary_file_path)
    ws = read_sheet(wb)

    # ExcelSummaryModel→Summaryへの変換(書込み)
    __write_summary_file(ws, model_list)

    # 名前を付けて保存
    save_file_path = (
        OUTPUT_PORK_CARCASS_DIR + f"{file_date}_豚枝肉相場_Summary.xlsx"
    )
    save_and_close_book(wb, save_file_path, True)
    # コピーしたsummaryが邪魔なので削除する
    delete_file(copy_sammary_file_path)


def __read_dl_file_data(file_date, ws, model_list):
    """"""
    row = DEFAULT_ROW_DLFILE
    for _ in range(1, 30):
        cell_a_1_val = read_cell(ws, row, 1)

        if "全農建値" in cell_a_1_val:
            break
        if is_none_or_empty(cell_a_1_val):
            continue

        market_date = str(file_date) + remove_day_str(cell_a_1_val)
        model = ExcelPorkCarcassSummaryModel()
        model.market_date = market_date

        model_list.append(model)
        row += 1

    print("データ件数: {}件".format(len(model_list)))

    # DLデータの値を取得する
    row = DEFAULT_ROW_DLFILE
    for model in model_list:
        # 全農建値
        model.zennoh_high_price = read_cell(ws, row, 3)
        model.zennoh_middle_price = read_cell(ws, row, 5)
        model.nationwide_slaughter = __remove_date(read_cell(ws, row, 8))
        # Tokyo
        model.tokyo_high_price = read_cell(ws, row, 11)
        model.tokyo_middle_price = read_cell(ws, row, 13)
        model.tokyo_ordinary_price = read_cell(ws, row, 15)
        model.tokyo_outside_price = read_cell(ws, row, 17)
        model.tokyo_head_count = read_cell(ws, row, 19)
        # Saitama
        model.saitama_high_price = read_cell(ws, row, 22)
        model.saitama_middle_price = read_cell(ws, row, 24)
        model.saitama_ordinary_price = read_cell(ws, row, 26)
        model.saitama_outside_price = read_cell(ws, row, 28)
        model.saitama_head_count = read_cell(ws, row, 30)
        # Yokohama
        model.yokohama_high_price = read_cell(ws, row, 33)
        model.yokohama_middle_price = read_cell(ws, row, 35)
        model.yokohama_ordinary_price = read_cell(ws, row, 37)
        model.yokohama_outside_price = read_cell(ws, row, 39)
        model.yokohama_head_count = read_cell(ws, row, 41)
        # Osaka
        model.osaka_high_price = read_cell(ws, row, 44)
        model.osaka_middle_price = read_cell(ws, row, 46)
        model.osaka_ordinary_price = read_cell(ws, row, 48)
        model.osaka_outside_price = read_cell(ws, row, 50)
        model.osaka_head_count = read_cell(ws, row, 52)

        row += 1

    return model_list


def __write_summary_file(ws, model_list):
    """"""
    row = DEFAULT_ROW_SUMMARYFILE
    for model in model_list:
        __set_value_of_date(ws, row, 1, from_str_to_date(model.market_date))
        # 全農建値
        __set_converted_value(ws, row, 2, model.nationwide_slaughter)
        __set_converted_value(ws, row, 3, model.zennoh_high_price)
        __set_converted_value(ws, row, 4, model.zennoh_middle_price)
        # Tokyo
        __set_converted_value(ws, row, 5, model.tokyo_high_price)
        __set_converted_value(ws, row, 6, model.tokyo_middle_price)
        __set_converted_value(ws, row, 7, model.tokyo_ordinary_price)
        __set_converted_value(ws, row, 8, model.tokyo_outside_price)
        __set_converted_value(ws, row, 9, model.tokyo_head_count)
        # Saitama
        __set_converted_value(ws, row, 10, model.saitama_high_price)
        __set_converted_value(ws, row, 11, model.saitama_middle_price)
        __set_converted_value(ws, row, 12, model.saitama_ordinary_price)
        __set_converted_value(ws, row, 13, model.saitama_outside_price)
        __set_converted_value(ws, row, 14, model.saitama_head_count)
        # Yokohama
        __set_converted_value(ws, row, 15, model.yokohama_high_price)
        __set_converted_value(ws, row, 16, model.yokohama_middle_price)
        __set_converted_value(ws, row, 17, model.yokohama_ordinary_price)
        __set_converted_value(ws, row, 18, model.yokohama_outside_price)
        __set_converted_value(ws, row, 19, model.yokohama_head_count)
        # Osaka
        __set_converted_value(ws, row, 20, model.osaka_high_price)
        __set_converted_value(ws, row, 21, model.osaka_middle_price)
        __set_converted_value(ws, row, 22, model.osaka_ordinary_price)
        __set_converted_value(ws, row, 23, model.osaka_outside_price)
        __set_converted_value(ws, row, 24, model.osaka_head_count)

        row += 1


def __remove_date(value):
    """豚肉相場一覧表_yyyymm.xlsxの「全国と畜頭数」列の値が
    数値と日付の情報となっているので、日付を削除する処理

    Note:
        変更前: 68800 (2023/02/28)
        変更後: 68800
    """

    # 正規表現
    regex = r"\(\d{4}/\d{1,2}/\d{1,2}\)"
    # 正規表現で示して値だけ削除し、さらに空白を削除する
    removed_value = str.strip(re.sub(regex, "", value))

    return removed_value


def __type_conversion(value):
    """intに変換する"""
    if not is_none_or_empty(value):
        value = int(value)
    return value


def __set_converted_value(ws, row, column, value):
    """対象セルに値をセットする"""
    # 値を型変換するしてから、セルに書き込む
    converted_value = __type_conversion(value)
    write_cell(ws, row, column, converted_value)


def __set_value_of_date(ws, row, column, value):
    """対象セルに値をセットする(date型の値限定)"""

    write_cell(ws, row, column, value)
