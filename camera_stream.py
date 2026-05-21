from typing import Optional
from urllib.parse import urljoin

import cv2

BASE_URL = None
try:
    from .config import BASE_URL
except ImportError:
    from config import BASE_URL


def get_camera_stream(base_url: Optional[str] = None) -> cv2.VideoCapture:
    """
    获取视频流。

    Args:
        base_url (str): IP Webcam 服务器 URL ，默认从环境变量读取。

    Returns:
        cv2.VideoCapture: 视频流对象。

    Example:

    ```python
    import cv2

    cap = get_camera_stream()
    ret, frame = cap.read()
    # type of `ret` is `bool`
    # type of `frame` is `numpy.ndarray`

    if ret:
        # 在这里可以对每一帧进行处理，例如显示、保存或进行图像分析
        cv2.imshow('Phone Camera', frame)
    else:
        print("读取视频帧失败！")

    # 释放资源并关闭窗口
    cap.release()
    cv2.destroyAllWindows()
    ```
    """
    if base_url is None:
        base_url = BASE_URL
    if not base_url:
        raise ValueError("缺少参数 `base_url`")

    url = urljoin(base_url, "/video")
    print(f"正在尝试连接: {url}")
    # 创建VideoCapture对象，并主动打开地址
    cap = cv2.VideoCapture(url)

    # 检查是否连接成功
    if not cap.isOpened():
        raise ConnectionError(f"连接到 {url} 失败。请检查IP地址和网络。")
    print("连接成功！")

    # 降低延迟的关键设置：将缓冲区大小设为1
    # 这样能确保程序总是拿到最新的一帧，避免画面越来越卡顿
    cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)

    return cap
