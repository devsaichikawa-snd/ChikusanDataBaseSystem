"""各プロジェクトにおいて、MySQLにテーブルを作成したいときに、単体でこのファイル実行すること
コマンド: python init_db.py
"""


def init_dev_chikusan_db():
    """豚枝肉データのテーブル作成を実行する"""
    from db.db_settings import get_db_engine
    from pork_carcass_data.model import BASE

    engine = get_db_engine()
    # Drop Table All
    BASE.metadata.drop_all(bind=engine)
    # Create Table All
    BASE.metadata.create_all(bind=engine)


if __name__ == "__main__":
    init_dev_chikusan_db()
