# Define the filename of the image
filename = "photo.jpeg"

# Check if the file has a valid image extension (.jpg, .png, .gif)
is_image = filename.endswith((".jpg", ".png", ".gif"))

# Output the result (True if the file is an image, otherwise False)
print(is_image)