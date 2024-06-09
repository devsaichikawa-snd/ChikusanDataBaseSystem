import re

from common.util import get_today, get_files, get_last_month
from pork_carcass_data.const import DOWNLOAD_DIR
from pork_carcass_data.data_cleansing import cleansing_pork_carcass
from pork_carcass_data.data_download import download_zenno_data


def exec_pork_carcass_data(args):
    """実行"""
    if args[2] == "cleansing":
        # データクレンジングのみ単独実行
        __execSingle_cleansing_pork_carcass()
        return "done"
    if args[2] == "dbinsert":
        # データ取込のみ単独実行
        pass

    # 一気通貫処理(※前月分を処理する)
    file_date = __exec_download_zenno_data()
    __exec_cleansing_pork_carcass(file_date)
    __exec_db_insert()


def __exec_download_zenno_data():
    """データダウンロード処理"""
    file_date = download_zenno_data()
    return file_date


def __exec_cleansing_pork_carcass(file_date):
    """データクレンジング処理"""
    cleansing_pork_carcass(file_date)


def __execSingle_cleansing_pork_carcass():
    """データクレンジング処理(単独実行)"""
    # 手動でDLをしているので、DLフォルダにあるファイルを全て実行する。
    files = get_files(DOWNLOAD_DIR, "*.xlsx")
    for file in files:
        file_date = __get_date_from_file_path(file)
        cleansing_pork_carcass(file_date)
        print(f"{file}のデータクレンジングが終了しました。")


def __exec_db_insert():
    """Summary→MySQLへのデータ取込処理"""
    pass


def __get_date_from_file_path(file_path):
    """データクレンジング処理単体実行用の日付取得処理"""
    pattern = r"(\d{6})"
    match = re.search(pattern, file_path)

    if match:
        yyyymm = match.group(1)
    else:
        print(
            "ファイル名からyyyymmが取得できませんでした。直接日付を取得します。"
        )
        yyyymm = get_last_month(get_today, "yyyymm")

    return yyyymm
