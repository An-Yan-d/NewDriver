import cv2

# 读取图像并转换为灰度图像
image = cv2.imread('View31.jpg')[260:420,:]
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 应用阈值化函数，将图像转换为二进制形式
thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

# 查找连通分量
connectivity = 8  # 8领域连接
num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(thresh, connectivity, cv2.CV_32S)

# 输出连通分量的数量
print(f"Number of connected components: {num_labels-1}")  # 减去背景
whratio=1
rec_i=0
for i in range(1,num_labels):
    print(i,stats[i])
    if stats[i][2]>70 and stats[i][2]/stats[i][3]>whratio:
        whratio=stats[i][2]/stats[i][3]
        rec_i=i
# 可以绘制标记的联通分量，使用以下代码
# img_with_labels = cv2.applyColorMap(labels.astype(np.uint8)*30, cv2.COLORMAP_JET)
# rec_i=5
print(rec_i)
mask = (labels == rec_i)
image[mask] = [0, 0, 255]  # 将连通分量用红色标记在原始图像上
cv2.imshow('Connected components', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
