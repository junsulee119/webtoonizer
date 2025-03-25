# Webtoonizer

## Overview

Webtoonize is a Python script that transforms ordinary images into webtoon-like illustrations using image processing techniques. The script applies a series of image transformations to create a webtoon-like aesthetic.

## Features

- Color quantization to simplify color palette
- Edge preservation through bilateral filtering
- Adaptive edge detection and enhancement
- Simplified color representation
- Easy-to-use image conversion

## Dependencies

- OpenCV (cv2)
- NumPy

## Installation

```bash
pip install opencv-python numpy
```

## Usage

```python
from webtoonizer import webtoonize_image

# Basic usage
webtoonize_image('input.png', 'webtoon_output.png')

# Customizable parameters
webtoonize_image('input.png', 'webtoon_output.png', k=16, num_bilateral=4)
```

### Parameters
- `image_path`: Path to input image
- `output_path`: Path to save webtoonized image
- `k`: Number of colors for quantization (default: 16)
- `num_bilateral`: Number of bilateral filtering passes (default: 4)

## Demo Images

### Original Image
![Original Image](/demo/input.png)

### Webtoonized Result
![Webtoonized Image](/demo/webtoon_output.png)

## How It Works

The script transforms images through these key steps:
1. Apply bilateral filtering to smooth image while preserving edges
2. Reduce color palette using k-means clustering
3. Convert to grayscale and apply median blur
4. Detect and enhance edges with adaptive thresholding
5. Combine quantized image with edge map

## Customization Tips

- Adjust `k` to control color complexity
- Modify `num_bilateral` to change edge smoothness
- Experiment with different input images for unique results

## License

