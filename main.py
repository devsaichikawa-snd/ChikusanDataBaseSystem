from pork_carcass_data.data_cleansing import cleansing_pork_carcass
from pork_carcass_data.data_download import download_zenno_data


def execute():
    """実行"""
    pass


def execute_pork_carcass():
    """実行"""
    file_date = download_zenno_data()
    cleansing_pork_carcass(file_date)


if __name__ == "__main__":
    print("----- 処理を開始しました。-----")
    execute_pork_carcass()
    print("----- 全ての処理が終了しました。-----")
