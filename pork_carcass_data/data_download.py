from common.selenium import (
    disconnect,
    get_web_driver,
    get_element_by_class,
    get_element_by_linktext,
    push_button_in_javascript,
    push_link_anchor_text,
    switch_browser_tabs,
)
from common.util import time_keeper, get_last_month, get_today
from pork_carcass_data.const import ZENNO_URL


def download_zenno_data() -> str:
    """JA全農ミートフーズの豚枝肉相場ExcelをDLする"""
    driver = get_web_driver(ZENNO_URL)
    time_keeper(2)

    today = get_today()
    # class属性からターゲット要素を絞り込む
    if today.month == 4:
        # 4月だけは昨年度の3月を取得することになるので、属性値を変更する
        target_elem = get_element_by_class(driver, "lastYear")
    else:
        target_elem = get_element_by_class(driver, "thisYear")

    # target_elemを整形する。→["4月", "5月", "6月", ..., "1月", "2月", "3月"]
    months = target_elem.text.split("\n")
    # 前月を取得する
    last_month = get_last_month(today, "m月")

    # monthsからターゲット月を取得する
    target_month = ""
    for month in months:
        if month == last_month:
            target_month = month
            break
        continue

    # ターゲットのリンクテキスト名の要素を取得し、クリックする
    target_link = get_element_by_linktext(driver, target_month)
    push_link_anchor_text(driver, target_link)
    time_keeper(2)

    # ブラウザのタブを切り替える(ページタブを切り替える)
    switch_browser_tabs(driver)
    time_keeper(2)

    # [Excel]ボタンの実行
    push_button_in_javascript(driver, "javascript:excelout()")
    time_keeper(5)

    print("Excelを取得しました。")

    disconnect(driver)

    # 戻り値に前月を返す(形式が異なるので、取り直す)
    last_month = get_last_month(today, "yyyymm")

    return last_month
