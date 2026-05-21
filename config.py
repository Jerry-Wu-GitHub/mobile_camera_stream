import os
from dotenv import load_dotenv


# 加载 .env 文件
load_dotenv()

# 获取变量 IP Webcam 服务器 URL
BASE_URL = os.getenv('BASE_URL')
assert BASE_URL, "缺少环境变量：BASE_URL"
