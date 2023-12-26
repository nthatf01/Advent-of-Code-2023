from PIL import Image

def count_black_pixels(image_path):
    # Open the image
    img = Image.open(image_path)

    # Convert the image to grayscale
    img_gray = img.convert('L')

    # Get the pixel data
    pixels = img_gray.load()

    # Count the black pixels
    black_pixel_count = sum(1 for x in range(img.width) for y in range(img.height) if pixels[x, y] == 0)

    return black_pixel_count

# Example usage
image_path = 'day_18_image.png'
black_pixels = count_black_pixels(image_path)

print(f"Number of black pixels: {black_pixels}")
