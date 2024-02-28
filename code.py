import matplotlib.pyplot as plt

date = "2022-09-01"
file = f"./Images/{date}/social_media-amazon.com-{date}.png"

img = plt.imread(file)
# img = img[50:280, 90:1180]
# Convert to the Gray-scale
# img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Erode
# img = cv2.erode(img, kernel, iterations=1)
plt.imshow(img)
plt.show()