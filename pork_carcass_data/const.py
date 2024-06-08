"""pork_carcass_dataの定数"""

from common.util import get_project_dir


# 全農ミートフーズのサイトURL
ZENNO_URL = "https://www.jazmf.co.jp/market/list.html"

# ディレクトリとファイルパス
PROJECT_DIR = str(get_project_dir())
DOWNLOAD_DIR = "C:\\Users\\daiko\\Downloads\\"
EXCEL_TEMPLATE_DIR = PROJECT_DIR + "\\excel_template\\"
OUTPUT_PORK_CARCASS_DIR = PROJECT_DIR + "\\output\\豚枝肉相場サマリ\\"
EXCEL_TEMPLATE_FILE_NAME = "豚枝肉相場_Summary.xlsx"

# Excel 行と列の固定番号
DEFAULT_ROW_DLFILE = 6
DEFAULT_ROW_SUMMARYFILE = 3
