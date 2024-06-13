import sys

from common.util import create_timer
from controller.household_consumption_control import exec_household_consumption
from controller.pork_carcass_control import exec_pork_carcass_data


def execute():
    """メイン実行処理

    Note:
        ターミナルで実行するときのコマンド
        Excel取得→データクレンジング→DB取込: python main.py pork-carcass
        データクレンジングの単体実行: python main.py pork-carcass cleansing
            →手動でDLする場合
        データ取込の単体実行: python main.py pork-carcass dbinsert
    """
    args = sys.argv

    if args[1] == "pork-carcass":
        # 豚枝肉相場Excelのデータ取得→クレンジング→DB取込
        exec_pork_carcass_data(args)
    elif args[1] == "household_consumption":
        # (データクレンジング)→家計消費データのDB取込
        exec_household_consumption(args)
    else:
        pass


if __name__ == "__main__":
    print("----- 処理を開始しました。-----")
    start_time = create_timer()
    execute()
    finish_time = create_timer()
    rerult_time = finish_time - start_time
    print("----- 全ての処理が終了しました。-----")
    print(f"処理時間は{rerult_time}秒です。")
