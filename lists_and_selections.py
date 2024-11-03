import cv2
import pyautogui
import numpy as np

def find_image_on_screen(target_image_path, confidence=0.8):
    """
    Searches for a specific image on the screen.

    Parameters:
        target_image_path (str): The path to the target image file.
        confidence (float): The match confidence threshold (0 to 1).

    Returns:
        tuple or None: The (x, y) coordinates of the top-left corner of the image if found,
                       or None if not found.
    """
    # Take a screenshot of the current screen
    screenshot = pyautogui.screenshot()
    screen_array = np.array(screenshot)
    screen_array = cv2.cvtColor(screen_array, cv2.COLOR_RGB2BGR)

    # Load the target image
    target_image = cv2.imread(target_image_path)

    # Perform template matching
    result = cv2.matchTemplate(screen_array, target_image, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    # Check if the match meets the confidence threshold
    if max_val >= confidence:
        return max_loc  # Return the location of the top-left corner of the found image
    else:
        return None  # Image not found on the screen

# Example usage:
target_image_path = 'target_image.png'  # Path to your target image
location = find_image_on_screen(target_image_path)

if location:
    print(f"Image found at location: {location}")
else:
    print("Image not found on the screen.")
