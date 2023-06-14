#NOTE:
Make sure to have the required libraries (cv2, mediapipe, pyautogui) installed before running the code.


# Virtual_Mouse2.0


Certainly! Here's an explanation of how the code works:

1. The code imports the necessary libraries: `cv2` for capturing and processing video, `mediapipe` for face mesh detection, and `pyautogui` for controlling the mouse cursor.
2. It sets up the video capture using the default camera (`0`).
3. The face mesh detector is initialized from the `mediapipe` library with the `refine_landmarks` parameter set to `True`.
4. The screen width and height are obtained using `pyautogui.size()`, which returns the dimensions of the screen.
5. The code enters an infinite loop to continuously process video frames.
6. Inside the loop, it reads a frame from the video capture and flips it horizontally to create a mirror effect.
7. The frame's height, width, and number of channels (color depth) are extracted.
8. The frame is converted from the BGR color space to RGB color space, as required by the face mesh detector.
9. The face mesh detector processes the RGB frame to detect facial landmarks, and the results are stored in the `output` variable.
10. The `output` object contains information about the detected face, including the face landmarks.
11. If face landmarks are detected (`landmark_points` is not None), the code extracts the landmarks for the first face.
12. The code iterates over specific landmarks (using indices 474 to 478) and calculates their coordinates in pixel space.
13. It draws a circle on each landmark position in green color.
14. If the landmark at index 1 is processed (the second landmark in the specified range), the code calculates its coordinates in screen space using the screen dimensions.
15. It moves the mouse cursor to the calculated screen position using `pyautogui.moveTo()`.
16. The code then extracts the landmarks for the left eye (using indices 145 and 159) from the face landmarks.
17. It iterates over the left eye landmarks and calculates their coordinates in pixel space.
18. It draws a circle on each left eye landmark position in yellow color.
19. The code checks if the vertical distance between the two left eye landmarks is smaller than a threshold (0.004).
20. If the distance is small, it performs a click action using `pyautogui.click()`.
21. The code displays the frame with the drawn landmarks in a window titled "Eye Controlled Mouse".
22. The code waits for a key press, and if the 'q' key is pressed, it breaks the loop.
23. Finally, the video capture is released, and all windows are destroyed.

This code utilizes the face mesh detection capabilities of the Mediapipe library to track specific facial landmarks and control the mouse cursor based on their positions. It provides a basic eye-controlled mouse functionality using the left eye blink gesture.
