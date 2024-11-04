
#final

import cv2
import numpy as np
import os

def create_binary_mask(image_pass, output_folder, threshold=200):
    img = cv2.imread(image_pass)

    
    mask = np.zeros_like(img)
    mask[(img[:, :, 0] > threshold) & (img[:, :, 1] > threshold) & (img[:, :, 2] > threshold)] = 255

    
    white_pixel_count = np.sum(mask == 255)

    
    filename_without_ext = os.path.splitext(os.path.basename(image_pass))[0]
    output_path = os.path.join(output_folder, f"{filename_without_ext}_mask.png")
    cv2.imwrite(output_path, mask)

    return white_pixel_count

def main():
    input_dir = "C:\\Users\\dharani\\python projects\\Online-test\\"
    output_dir = "C:\\Users\\dharani\\python projects\\Online-test\\thresholded_images"

    os.makedirs(output_dir, exist_ok=True)

    image_folder = [
        os.path.join(input_dir, "faroe_island_1.png"),
        os.path.join(input_dir, "faroe_island_2.jpg"),
        os.path.join(input_dir, "faroe_island_3.jpg")
    ]

    total_white_pixels = 0
    for image_pass in image_folder:
        white_pixels = create_binary_mask(image_pass, output_dir)
        total_white_pixels += white_pixels
        print(f"White pixels in {image_pass}: {white_pixels}")

    print(f"Total white pixels in all images: {total_white_pixels}")

if __name__ == "__main__":
    main()