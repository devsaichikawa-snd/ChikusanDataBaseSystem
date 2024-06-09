from common.excel import (
    read_workbook,
    read_sheet,
    read_cell,
)
from common.util import is_none_or_empty
from db.db_settings import get_db_engine, get_db_session, dispose_db_engine
from pork_carcass_data.model import PorkCarcassPrice


def import_data(file_path):
    """pork_carcass_priceテーブルにsummary結果を取り込む処理"""

    # Summaryファイルを開く
    wb = read_workbook(file_path)
    ws = read_sheet(wb)

    # DB接続
    engine = get_db_engine()
    session = get_db_session()

    # Summaryからデータを取得する
    for row in range(3, ws.max_row + 1):
        market_date = read_cell(ws, row, 1, for_database=True)

        if is_none_or_empty(market_date):
            break

        # 全農値
        nationwide_slaughter = read_cell(ws, row, 2, for_database=True)
        zennoh_high_price = read_cell(ws, row, 3, for_database=True)
        zennoh_middle_price = read_cell(ws, row, 4, for_database=True)
        # Tokyo
        tokyo_high_price = read_cell(ws, row, 5, for_database=True)
        tokyo_middle_price = read_cell(ws, row, 6, for_database=True)
        tokyo_ordinary_price = read_cell(ws, row, 7, for_database=True)
        tokyo_outside_price = read_cell(ws, row, 8, for_database=True)
        tokyo_head_count = read_cell(ws, row, 9, for_database=True)
        # Saitama
        saitama_high_price = read_cell(ws, row, 10, for_database=True)
        saitama_middle_price = read_cell(ws, row, 11, for_database=True)
        saitama_ordinary_price = read_cell(ws, row, 12, for_database=True)
        saitama_outside_price = read_cell(ws, row, 13, for_database=True)
        saitama_head_count = read_cell(ws, row, 14, for_database=True)
        # Yokohama
        yokohama_high_price = read_cell(ws, row, 15, for_database=True)
        yokohama_middle_price = read_cell(ws, row, 16, for_database=True)
        yokohama_ordinary_price = read_cell(ws, row, 17, for_database=True)
        yokohama_outside_price = read_cell(ws, row, 18, for_database=True)
        yokohama_head_count = read_cell(ws, row, 19, for_database=True)
        # Osaka
        osaka_high_price = read_cell(ws, row, 20, for_database=True)
        osaka_middle_price = read_cell(ws, row, 21, for_database=True)
        osaka_ordinary_price = read_cell(ws, row, 22, for_database=True)
        osaka_outside_price = read_cell(ws, row, 23, for_database=True)
        osaka_head_count = read_cell(ws, row, 24, for_database=True)

        model = PorkCarcassPrice(
            market_date=market_date,
            nationwide_slaughter=nationwide_slaughter,
            zennoh_high_price=zennoh_high_price,
            zennoh_middle_price=zennoh_middle_price,
            tokyo_high_price=tokyo_high_price,
            tokyo_middle_price=tokyo_middle_price,
            tokyo_ordinary_price=tokyo_ordinary_price,
            tokyo_outside_price=tokyo_outside_price,
            tokyo_head_count=tokyo_head_count,
            saitama_high_price=saitama_high_price,
            saitama_middle_price=saitama_middle_price,
            saitama_ordinary_price=saitama_ordinary_price,
            saitama_outside_price=saitama_outside_price,
            saitama_head_count=saitama_head_count,
            yokohama_high_price=yokohama_high_price,
            yokohama_middle_price=yokohama_middle_price,
            yokohama_ordinary_price=yokohama_ordinary_price,
            yokohama_outside_price=yokohama_outside_price,
            yokohama_head_count=yokohama_head_count,
            osaka_high_price=osaka_high_price,
            osaka_middle_price=osaka_middle_price,
            osaka_ordinary_price=osaka_ordinary_price,
            osaka_outside_price=osaka_outside_price,
            osaka_head_count=osaka_head_count,
        )

        session.add(model)
    session.commit()
    print("summaryのDBインサートが完了しました。")

    # Excelを閉じる
    wb.close()
    # DBと切断
    session.close()
    # エンジンの破棄
    dispose_db_engine(engine)
