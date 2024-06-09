"""pork_carcass_dataのModel"""

from dataclasses import dataclass
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, DateTime, Date


# モデルのベースクラスを定義。SQLAlchemyでテーブルを定義する際は、"BASE"を継承すること。
BASE = declarative_base()


class PorkCarcassPrice(BASE):
    """豚枝肉相場テーブル"""

    # テーブル名
    __tablename__ = "pork_carcass_price"
    # 主キー
    id = Column(Integer, primary_key=True, autoincrement=True)

    market_date = Column(Date, unique=True, nullable=False)
    nationwide_slaughter = Column(Integer, nullable=True)
    zennoh_high_price = Column(Integer, nullable=True)
    zennoh_middle_price = Column(Integer, nullable=True)
    # TOKYO
    tokyo_high_price = Column(Integer, nullable=True)
    tokyo_middle_price = Column(Integer, nullable=True)
    tokyo_ordinary_price = Column(Integer, nullable=True)
    tokyo_outside_price = Column(Integer, nullable=True)
    tokyo_head_count = Column(Integer, nullable=True)
    # SAITAMA
    saitama_high_price = Column(Integer, nullable=True)
    saitama_middle_price = Column(Integer, nullable=True)
    saitama_ordinary_price = Column(Integer, nullable=True)
    saitama_outside_price = Column(Integer, nullable=True)
    saitama_head_count = Column(Integer, nullable=True)
    # YOKOHAMA
    yokohama_high_price = Column(Integer, nullable=True)
    yokohama_middle_price = Column(Integer, nullable=True)
    yokohama_ordinary_price = Column(Integer, nullable=True)
    yokohama_outside_price = Column(Integer, nullable=True)
    yokohama_head_count = Column(Integer, nullable=True)
    # OSAKA
    osaka_high_price = Column(Integer, nullable=True)
    osaka_middle_price = Column(Integer, nullable=True)
    osaka_ordinary_price = Column(Integer, nullable=True)
    osaka_outside_price = Column(Integer, nullable=True)
    osaka_head_count = Column(Integer, nullable=True)
    created_at = Column(DateTime, default=datetime.now, nullable=False)
    updated_at = Column(DateTime, default=datetime.now, nullable=False)


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
