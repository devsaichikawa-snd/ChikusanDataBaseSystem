"""よく使う便利関数を定義する"""

from datetime import date
import os
from pathlib import Path
import time
import shutil


def get_project_dir() -> Path:
    """プロジェクトDirを生成する"""
    return Path.cwd()


def is_none_or_empty(check_value) -> bool:
    """Noneと空文字の判定をする
    Noneまたは空文字: True、値判定あり: False
    """
    if check_value is None or check_value == "":
        return True
    return False


def get_today():
    """本日日付を取得する"""
    return date.today()


def get_last_month(today, flag: str):
    """前月日付を取得する
    Args:
        today(date): date.today()
        flag(str): "yyyymm"や"mm"などの年月日の形式
    """
    year = today.year
    month = today.month
    # 前月の計算
    if month == 1:
        # 1月の場合は前年の12月になる
        year -= 1
        month = 12
    else:
        month -= 1

    if flag == "yyyymm":
        previous_date = f"{year}{month:02}"
    elif flag == "mm":
        previous_date = f"{month:02}"
    else:
        ValueError("引数を確認してください。")

    return previous_date


def from_str_to_date(value: str):
    """日付の型変換(str → date)"""
    datetyep_value = date.fromisoformat(value)
    return datetyep_value


def time_keeper(seconds: int):
    """待機時間を発生させる"""
    time.sleep(seconds)


def remove_day_str(value: str):
    """「日」の文字を削除する"""
    result = value.replace("日", "")
    return result


def file_copy(original_file, copy_to):
    """File Copy"""
    shutil.copy2(original_file, copy_to)


def delete_file(file_path):
    """ファイルを削除する"""
    os.remove(file_path)
