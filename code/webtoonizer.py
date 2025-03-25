import cv2
import numpy as np

def webtoonize_image(image_path, output_path, k=16, num_bilateral=4):
    # Read the input image
    img = cv2.imread(image_path)
    if img is None:
        raise FileNotFoundError(f"Image not found at {image_path}")
    
    # Apply bilateral filter multiple times for smoothing while preserving edges
    for _ in range(num_bilateral):
        img = cv2.bilateralFilter(img, d=9, sigmaColor=50, sigmaSpace=50)
    
    # Perform color quantization to reduce the number of colors
    # Reshape the image array and apply k-means clustering
    data = np.float32(img).reshape((-1, 3))
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 20, 0.001)
    _, labels, centers = cv2.kmeans(data, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    centers = np.uint8(centers)
    quantized = centers[labels.flatten()]
    quantized = quantized.reshape(img.shape)
    
    # Convert to grayscale and apply median blur
    gray = cv2.cvtColor(quantized, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 7)
    
    # Detect and enhance edges using adaptive threshold
    edges = cv2.adaptiveThreshold(gray, 255, 
                                 cv2.ADAPTIVE_THRESH_MEAN_C,
                                 cv2.THRESH_BINARY, 5, 7)
    
    # Convert edges to color and combine with quantized image
    edges = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
    webtoon = cv2.bitwise_and(quantized, edges)
    
    # Save the cartoonized image
    cv2.imwrite(output_path, webtoon)
    print(f"Webtoon image saved to {output_path}")

# Example usage
webtoonize_image('input.png', 'webtoon_output.png')