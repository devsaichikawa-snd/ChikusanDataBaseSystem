"""pork_carcass_dataのModel"""

from dataclasses import dataclass


@dataclass
class ExcelPorkCarcassSummaryModel:
    """月別豚枝肉サマリモデル"""

    # 全農値
    market_date: str = ""
    nationwide_slaughter: str = ""
    zennoh_high_price: str = ""
    zennoh_middle_price: str = ""
    # 東京
    tokyo_high_price: str = ""
    tokyo_middle_price: str = ""
    tokyo_ordinary_price: str = ""
    tokyo_outside_price: str = ""
    tokyo_head_count: str = ""
    # 埼玉
    saitama_high_price: str = ""
    saitama_middle_price: str = ""
    saitama_ordinary_price: str = ""
    saitama_outside_price: str = ""
    saitama_head_count: str = ""
    # 横浜
    yokohama_high_price: str = ""
    yokohama_middle_price: str = ""
    yokohama_ordinary_price: str = ""
    yokohama_outside_price: str = ""
    yokohama_head_count: str = ""
    # 大阪
    osaka_high_price: str = ""
    osaka_middle_price: str = ""
    osaka_ordinary_price: str = ""
    osaka_outside_price: str = ""
    osaka_head_count: str = ""
