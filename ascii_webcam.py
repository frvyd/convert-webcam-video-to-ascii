# This code captures video from the camera, resizes the frames in a 3x4 ratio, converts them to greyscale, and then generates the ASCII image based on pixel brightness.

import cv2

# Set the desired screen size 
screen_width = 200
screen_height = 150

# Create a list of ASCII characters ordered by brightness. (Large characters such as A,B,C... $,&... 0,1,2... make the image appear to flicker.)
ascii_chars = "@%#*+=-:. "

# Initialize the camera
cap = cv2.VideoCapture(0)

while True:
    # Capture a frame from the camera
    ret, frame = cap.read()

    # Resize the frame to match the screen size
    frame = cv2.resize(frame, (screen_width, screen_height))

    # Convert the frame to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Initialize an empty ASCII art string
    ascii_art = ""

    # Loop through each pixel in the grayscale frame
    for row in gray_frame:
        for pixel_value in row:
            # Map pixel value to an ASCII character
            index = int(pixel_value / 255 * (len(ascii_chars) - 1))
            ascii_art += ascii_chars[index]

        # Add a newline character at the end of each row
        ascii_art += "\n"

    # Print the ASCII art to the console or display it in a GUI window
    print(ascii_art)

    # Exit the loop when the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close any open windows
cap.release()
cv2.destroyAllWindows()
