import cv2
import numpy as np
import matplotlib.pyplot as plt

original_image = None
modified_image = None
history = []

def load_image(image_path):
  """Load an image from file."""
  img = cv2.imread(image_path)
  global original_image, modified_image
  if img is None:
    print(f"Error: Could not load image from {image_path}")
    return False
  original_image = img
  modified_image = img
  history.append(("Load", img.copy()))
  return True

def show_image():
  """Display the most recent image from history."""
  # Most recent image from history
  last_operation = history[-1]
  modified_image = last_operation[1]  # The modified image is the 2nd index

  # Create a side-by-side comparison
  plt.figure(figsize=(12, 6))
  
  # Original image
  plt.subplot(1, 2, 1)
  plt.imshow(cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB))
  plt.title("Original")
  plt.axis('off')
  
  # Modified image
  plt.subplot(1, 2, 2)
  plt.imshow(cv2.cvtColor(modified_image, cv2.COLOR_BGR2RGB))
  plt.title("Modified")
  plt.axis('off')
  
  plt.show()

# 1. Adjust Brightness
def adjust_brightness():
  """Adjust the brightness of the image."""

  global modified_image
  brightness = float(input("Enter the brightness factor (0.0 to 1.0): "))
  if brightness < 0.0 or brightness > 1.0:
    print("Invalid brightness factor. Please enter a value between 0.0 and 1.0.")
    return
  
  modified_image = cv2.convertScaleAbs(modified_image, alpha=1.0, beta=brightness * 255)
  history.append((f"Adjust Brightness {brightness}", modified_image.copy()))
  show_image()

# 2. Adjust Contrast
def adjust_contrast():
  """Adjust the contrast of the image."""

  global modified_image
  contrast = float(input("Enter the contrast factor (0.0 to 1.0): "))
  if contrast < 0.0 or contrast > 1.0:
    print("Invalid contrast factor. Please enter a value between 0.0 and 1.0.")
    return
  
  modified_image = cv2.convertScaleAbs(modified_image, alpha=contrast, beta=0)
  history.append((f"Adjust Contrast {contrast}", modified_image.copy()))
  show_image()

# 3. Convert to Grayscale
def convert_to_grayscale():
  """Convert the image to grayscale."""

  global modified_image
  modified_image = cv2.cvtColor(modified_image, cv2.COLOR_BGR2GRAY)
  history.append(("Convert to Grayscale", modified_image.copy()))
  show_image()

# 4. Add Padding
def add_padding():
  """Add padding to the image."""

  global modified_image

  # Ask for border type
  print("Select the border type:")
  print("1. Constant")
  print("2. Replicate")
  print("3. Reflect")
  print("4. Wrap")
  
  choice_type = int(input("Enter your choice: "))
  
  if choice_type == 1:
    padding_type = cv2.BORDER_CONSTANT
    border_value = [0, 0, 0]  # Black padding
  elif choice_type == 2:
    padding_type = cv2.BORDER_REPLICATE
    border_value = None
  elif choice_type == 3:
    padding_type = cv2.BORDER_REFLECT
    border_value = None
  elif choice_type == 4:
    padding_type = cv2.BORDER_WRAP
    border_value = None
  else:
    print("Invalid choice. Please try again.")
    return

  print("\nSelect the padding proportion:")
  print("1. Square")
  print("2. Rectangle")
  print("3. Custom Ratio (e.g., 4:5)")
  
  choice_proportion = int(input("Enter your choice: ")) 

  orig_height, orig_width = modified_image.shape[:2]  # Get current image height and width
  
  if choice_proportion == 1:
    # Square padding - add padding to top and bottom until the image is square
    target_ratio = 1
    current_ratio = orig_width / orig_height
    
    # image is tall, add padding to width
    if current_ratio < target_ratio:
      # Image is too tall, add width
      new_width = orig_height # new width is the height
      initial_padding = (new_width - orig_width) // 2 # initial padding is the difference between the new width and the original width divided by 2
      top = bottom = 0
      left = right = initial_padding
    else: # image is wide, add padding to height
      new_height = orig_width # new height is the width
      initial_padding = (new_height - orig_height) // 2
      top = bottom = initial_padding
      left = right = 0
      
  elif choice_proportion == 2:
    #  different padding for vertical and horizontal
    vertical_padding = int(input("Enter vertical padding size (pixels): "))
    horizontal_padding = int(input("Enter horizontal padding size (pixels): "))
    top = bottom = vertical_padding
    left = right = horizontal_padding
      
  elif choice_proportion == 3:
    print("Enter the desired ratio (ie. for 4:5 ratio, enter 4 and then 5)")
    width_ratio = int(input("Enter width ratio: "))
    height_ratio = int(input("Enter height ratio: "))
    
    # Calculate target ratio (width:height)
    target_ratio = width_ratio / height_ratio
    current_ratio = orig_width / orig_height
    
    # First, add padding to achieve the target ratio
    if current_ratio < target_ratio:
      # Image is too tall, add width
      new_width = int(orig_height * target_ratio) # new width is the height * target ratio
      initial_padding = int((new_width - orig_width) // 2)
      top = bottom = 0
      left = right = initial_padding
    else:
      # Image is too wide, add height
      new_height = int(orig_width / target_ratio) # new height is the width / target ratio
      initial_padding = int((new_height - orig_height) // 2)
      top = bottom = initial_padding
      left = right = 0

  else:
    print("Invalid choice. Please try again.")
    return

  # Apply the padding
  padded_image = cv2.copyMakeBorder(
    modified_image,
    top, bottom, left, right,
    padding_type,
    value=border_value if border_value else None
  )
  
  # Save to history and display
  history.append((f"Add Padding (top={top}, bottom={bottom}, left={left}, right={right}, type={padding_type})", padded_image.copy()))
  show_image()

# 5. Apply Thresholding
def apply_thresholding():
  """Apply thresholding to the image."""

  global modified_image

  print("Available threshold types ===")
  print("1. THRESH_BINARY") # Values above threshold become white, below become black
  print("2. THRESH_BINARY_INV") # Values above threshold become black, below become white
  
  choice = int(input("Enter your choice: "))
  
  if choice == 1:
    threshold_type = cv2.THRESH_BINARY
  elif choice == 2:
    threshold_type = cv2.THRESH_BINARY_INV
  else:
    print("Invalid choice. Please try again.")
    return
  
  threshold_value = int(input("Enter the threshold value (0-255): "))

  modified_image = cv2.threshold(modified_image, threshold_value, 255, threshold_type)[1]

  history.append(("Apply Thresholding", modified_image.copy()))
  show_image()

# 6. Blend with Another Image
def blend_with_another_image():
  global modified_image
  
  second_image = input("Enter the name of the second image: ")

  img1 = modified_image.copy()
  img2 = cv2.imread(second_image)

  if img2 is None:
    return

  alpha = float(input("Enter the alpha value (0 to 1): "))

  if alpha < 0 or alpha > 1:
    print("Invalid alpha value. Please enter a value between 0 and 1.")
    return
  
  # Blend the images using the formula and convert to uint8 type
  blend = (1 - alpha) * img1 + alpha * img2
  blend = np.clip(blend, 0, 255).astype(np.uint8)

  modified_image = blend

  history.append((f"Blend with Another Image: {second_image}", modified_image.copy()))
  show_image()

# 7. Undo Last Operation
def undo_last_operation():
  global history
  if not history:
    print("No operations have been performed yet.")
    return
  history.pop()
  show_image()

# 8. View History
def view_history():
  i = 1
  print("--------------------------------")
  print("History Log:")
  for operation, image in history:
    print(f"{i}. {operation}")
    i += 1
  print("--------------------------------")

# 9. Save and Exit
def save_and_exit():
  global original_image

  save_path = input("Enter the name of the image to save: ")

  # save the most recent image in history
  cv2.imwrite(save_path, history[-1][1])

  print(f"Image saved to {save_path}")

# Main function
def main():
  # image_path = input("Enter the name of the image: ")
  image_path = "dapper-ship.jpeg"

  if not load_image(image_path):
    return
  
  print("Image loaded successfully")
  
  while True:
    print("\n==== Mini Photo Editor ====")
    print("1. Adjust Brightness")
    print("2. Adjust Contrast")
    print("3. Convert to Grayscale")
    print("4. Add Padding")
    print("5. Apply Thresholding")
    print("6. Blend with Another Image")
    print("7. Undo Last Operation")
    print("8. View History")
    print("9. Save and Exit")
    print("0. Exit without Saving")
    
    choice = input("\nEnter your choice (0-9): ")
    
    if choice == "1":
      adjust_brightness()
    elif choice == "2":
      adjust_contrast()
    elif choice == "3":
      convert_to_grayscale()
    elif choice == "4":
      add_padding()
    elif choice == "5":
      apply_thresholding()
    elif choice == "6":
      blend_with_another_image()
    elif choice == "7":
      undo_last_operation()
    elif choice == "8":
      view_history()
    elif choice == "9":
      save_and_exit()
    elif choice == "0":
      return False
    else:
      print("Invalid choice. Please try again.")

if __name__ == "__main__":
  main()
