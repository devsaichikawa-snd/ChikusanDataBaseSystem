import re

from common.util import get_today, get_files, get_last_month, delete_file
from pork_carcass_data.const import DOWNLOAD_DIR, OUTPUT_PORK_CARCASS_DIR
from pork_carcass_data.data_cleansing import cleansing_pork_carcass
from pork_carcass_data.data_download import download_zenno_data
from pork_carcass_data.data_import import import_data


def exec_pork_carcass_data(args: list) -> None:
    """メインコントローラー"""
    if len(args) > 2:
        if args[2] == "cleansing":
            # データクレンジングのみ単独実行
            __execSingle_cleansing_pork_carcass()
            return
        if args[2] == "dbinsert":
            # データ取込のみ単独実行
            __execSingle_import_data()
            return
    else:
        # 一気通貫処理(※前月分を処理する)
        file_date = __exec_download_zenno_data()
        file_path = __exec_cleansing_pork_carcass(file_date)
        __exec_import_data(file_path)


def __exec_download_zenno_data() -> str:
    """データダウンロード処理"""
    file_date = download_zenno_data()
    return file_date


def __exec_cleansing_pork_carcass(file_date: str) -> str:
    """データクレンジング処理"""
    file_path = cleansing_pork_carcass(file_date)
    return file_path


def __execSingle_cleansing_pork_carcass():
    """データクレンジング処理(単独実行)"""
    # 手動でDLをしているので、DLフォルダにあるファイルを全て実行する。
    files = get_files(DOWNLOAD_DIR, "*.xlsx")
    for file in files:
        file_date = __get_date_from_file_path(file)
        cleansing_pork_carcass(file_date, file)
        print(f"{file}のデータクレンジングが終了しました。")

    # DLファイルを全て削除する
    delete_file(files)


def __exec_import_data(file_path):
    """Summary→MySQLへのデータ取込処理"""
    import_data(file_path)


def __execSingle_import_data():
    """Summary→MySQLへのデータ取込処理(単独実行)"""
    files = get_files(OUTPUT_PORK_CARCASS_DIR, "*.xlsx")
    for file in files:
        import_data(file)
        print(f"{file}のデータ取込が終了しました。")


def __get_date_from_file_path(file_path: str) -> str:
    """データクレンジング処理単体実行用の日付取得処理"""
    pattern = r"(\d{6})"
    match = re.search(pattern, file_path)

    if match:
        yyyymm = match.group(1)
    else:
        print(
            "ファイル名からyyyymmが取得できませんでした。直接日付を取得します。"
        )
        yyyymm = get_last_month(get_today(), "yyyymm")

    return yyyymm
