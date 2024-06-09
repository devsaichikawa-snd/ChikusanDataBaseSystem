import sys

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
    else:
        pass


if __name__ == "__main__":
    print("----- 処理を開始しました。-----")
    execute()
    print("----- 全ての処理が終了しました。-----")
