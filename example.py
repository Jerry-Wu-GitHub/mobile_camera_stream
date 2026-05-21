import cv2
from camera_stream import get_camera_stream

cap = get_camera_stream()

# 循环读取视频帧
print("按 'q' 键退出。")
while True:
    ret, frame = cap.read()
    if not ret:
        print("读取视频帧失败！")
        break

    # 在这里可以对每一帧进行处理，例如显示、保存或进行图像分析
    cv2.imshow('Phone Camera', frame)

    # 等待按键，按 'q' 键退出
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 释放资源并关闭窗口
cap.release()
cv2.destroyAllWindows()
