from PIL import Image, ImageDraw, ImageFont

def load_image(path):
    """Load an image from a file."""
    try:
        img = Image.open(path)
        print(f"Image loaded: {path}")
        return img
    except Exception as e:
        print(f"Error: {e}")
        return None

def save_image(img, path):
    """Save an image to a file."""
    try:
        img.save(path)
        print(f"Image saved: {path}")
    except Exception as e:
        print(f"Error: {e}")

def resize_image(img, width, height):
    """Resize the image."""
    return img.resize((width, height))

def crop_image(img, left, top, right, bottom):
    """Crop the image."""
    return img.crop((left, top, right, bottom))

def rotate_image(img, angle):
    """Rotate the image."""
    return img.rotate(angle)

def flip_image(img, mode):
    """Flip the image horizontally or vertically."""
    if mode == "horizontal":
        return img.transpose(Image.FLIP_LEFT_RIGHT)
    elif mode == "vertical":
        return img.transpose(Image.FLIP_TOP_BOTTOM)
    else:
        print("Invalid mode. Use 'horizontal' or 'vertical'.")
        return img

def apply_grayscale(img):
    """Convert the image to grayscale."""
    return img.convert("L")

def add_text(img, text, position, font_size=20, color="white"):
    """Add text to an image."""
    draw = ImageDraw.Draw(img)
    try:
        font = ImageFont.truetype("arial.ttf", font_size)
    except IOError:
        font = ImageFont.load_default()
    draw.text(position, text, font=font, fill=color)
    return img

def main():
    print("Basic Image Editor")
    print("===================")

    # Load an image
    path = input("Enter the path to your image: ")
    img = load_image(path)
    if img is None:
        return

    while True:
        print("\nOptions:")
        print("1. Resize Image")
        print("2. Crop Image")
        print("3. Rotate Image")
        print("4. Flip Image")
        print("5. Apply Grayscale Filter")
        print("6. Add Text")
        print("7. Save and Exit")

        choice = input("Choose an option (1-7): ")

        if choice == "1":
            width = int(input("Enter new width: "))
            height = int(input("Enter new height: "))
            img = resize_image(img, width, height)
            print("Image resized.")

        elif choice == "2":
            left = int(input("Enter left coordinate: "))
            top = int(input("Enter top coordinate: "))
            right = int(input("Enter right coordinate: "))
            bottom = int(input("Enter bottom coordinate: "))
            img = crop_image(img, left, top, right, bottom)
            print("Image cropped.")

        elif choice == "3":
            angle = int(input("Enter angle to rotate (in degrees): "))
            img = rotate_image(img, angle)
            print("Image rotated.")

        elif choice == "4":
            mode = input("Enter flip mode ('horizontal' or 'vertical'): ")
            img = flip_image(img, mode)
            print("Image flipped.")

        elif choice == "5":
            img = apply_grayscale(img)
            print("Grayscale filter applied.")

        elif choice == "6":
            text = input("Enter text to add: ")
            x = int(input("Enter x-coordinate for text: "))
            y = int(input("Enter y-coordinate for text: "))
            font_size = int(input("Enter font size (default is 20): "))
            color = input("Enter text color (default is white): ") or "white"
            img = add_text(img, text, (x, y), font_size, color)
            print("Text added.")

        elif choice == "7":
            save_path = input("Enter the path to save the image: ")
            save_image(img, save_path)
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()