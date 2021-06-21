"""
File: blur.py
Name:
-------------------------------
This file shows the original image first,
smiley-face.png, and then compare to its
blurred image. The blur algorithm uses the
average RGB values of a pixel's nearest neighbors
"""

from simpleimage import SimpleImage


def blur(img):
    
# 宣告變數
    count = 0
    new_r = 0
    new_g = 0
    new_b = 0
    blur_img = img # 用來儲存新的圖片避免取代原本的數值

# 判斷圖片大小後並計算每個pixel旁邊3x3的大小的rgb值
    for row in range(img.height):
        for col in range(img.width):
            for x in range(-1,2): 
                for y in range(-1,2):
                    if((col + y) >= 0) and ((col + y) < img.width) and ((row + x) >= 0) and ((row +x) < img.height):
                        count = count + 1
                        new_r += img.get_pix(row + x, col + y)[0]
                        new_g += img.get_pix(row + x, col + y)[1]
                        new_b += img.get_pix(row + x, col + y)[2]
                    else:
                        continue
# 設定blur後的數值                       
            new_r = int(new_r / count)
            new_g = int(new_g / count)
            new_b = int(new_b / count)
            blur_img.set_rgb(row, col, new_r, new_g, new_b)
            count = 0
            new_r = 0
            new_g = 0
            new_b = 0

    return blur_img    
                        
                    
    
def main():
    """
    TODO:
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(5):
        blurred_img = blur(blurred_img)
    blurred_img.show()


if __name__ == '__main__':
    main()
