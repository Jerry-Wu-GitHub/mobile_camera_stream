# 手机摄像头视频流

本仓库用于记录：如何把手机摄像头的画面传给电脑。

- 使用局域网
- 使用 Python 的 OpenCV 库

## 开始

### 手机端

1. 下载并安装 XAPK Installer 到手机，如 https://www.appinn.com/xapk-installer ，待会用于安装 `.xapk` 文件。

2. 下载 [IP Webcam](https://captain-droid.com/zh/apps/video/ip-webcam/) ，会得到一个 `.xapk` 文件，用 XAPK Installer 安装到手机。

3. 打开安装好的 IP Webcam ，点右上角的三个点，点“开启服务器”，授予访问摄像头等权限。在打开的页面的底部有局域网址，格式为

    ```
    IPv4: http://192.168.xxx.xxx:8080
    IPv4: https://192.168.xxx.xxx:8080
    IPv6: ...
    ```

4. 用在同一局域网下的设备访问 `http://192.168.xxx.xxx:8080` ，如果成功的话应该能打开一个网页，上面是手机摄像头画面。

### 电脑端

克隆本仓库：

```bash
git clone https://github.com/Jerry-Wu-GitHub/mobile_camera_stream.git
cd mobile_camera_stream
```

安装依赖：

```bash
pip install -r requirements.txt
```

设置环境变量：在根目录里新建一个 `.env` 文件，向文件里写入：

```
# 手机上显示的 IP Webcam 服务器 URL
BASE_URL = "https://192.168.xxx.xxx:8080"
```

运行 `example.py` ：

```bash
python example.py
```

如果成功的话，这应该会打开一个窗口，实时显示手机摄像头的画面。