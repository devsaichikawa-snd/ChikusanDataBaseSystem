import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.engine.base import Engine
from sqlalchemy.orm import scoped_session, sessionmaker


# .envファイルを読み込む()
load_dotenv()

DIALECT = "mysql"
DRIVER = "mysqlconnector"
DB_USER_NAME = os.getenv("DB_USER_NAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
HOST = os.getenv("DB_HOST")
PORT = 3306
DATABASE_NAME = os.getenv("DATABASE_NAME")
CHARSET_TYPE = "utf8"
DB_URL = f"{DIALECT}+{DRIVER}://{DB_USER_NAME}:{DB_PASSWORD}@{HOST}:{PORT}/{DATABASE_NAME}?charset={CHARSET_TYPE}"


def get_db_engine() -> Engine:
    """データベースエンジンを作成"""
    return create_engine(DB_URL, echo=True)


def dispose_db_engine(engine: Engine) -> None:
    """DBエンジンを破棄して接続を解放する"""
    return engine.dispose()


def get_db_session() -> scoped_session:
    """データベースセッションを取得"""
    return scoped_session(
        sessionmaker(autocommit=False, autoflush=False, bind=get_db_engine())
    )
