import cv2
import mediapipe as mp
import pyautogui

# Initialize video capture
cam = cv2.VideoCapture(0)

# Initialize face mesh
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)

# Get screen dimensions
screen_w, screen_h = pyautogui.size()

while True:
    # Read frame from video capture
    _, frame = cam.read()
    
    # Flip frame horizontally
    frame = cv2.flip(frame, 1)
    
    # Convert frame to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Process the frame with face mesh
    output = face_mesh.process(rgb_frame)
    
    # Get face landmarks
    landmark_points = output.multi_face_landmarks
    
    # Get frame dimensions
    frame_h, frame_w, _ = frame.shape
    
    if landmark_points:
        # Get the landmarks of the first face
        landmarks = landmark_points[0].landmark
        
        # Iterate over specific landmarks
        for id, landmark in enumerate(landmarks[474:478]):
            # Calculate the coordinates of the landmark in pixel space
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            
            # Draw a circle on the landmark position
            cv2.circle(frame, (x, y), 3, (0, 255, 0))
            
            if id == 1:
                # Calculate the coordinates of the landmark in screen space
                screen_x = screen_w * landmark.x
                screen_y = screen_h * landmark.y
                
                # Move the mouse cursor to the landmark position
                pyautogui.moveTo(screen_x, screen_y)
        
        # Get the landmarks for the left eye (using indices 145 and 159)
        left = [landmarks[145], landmarks[159]]
        
        for landmark in left:
            # Calculate the coordinates of the landmark in pixel space
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            
            # Draw a circle on the landmark position
            cv2.circle(frame, (x, y), 3, (0, 255, 255))
        
        # Check if the left eye is closed based on the vertical distance between landmarks
        if (left[0].y - left[1].y) < 0.004:
            # Perform a click action if the left eye is closed
            pyautogui.click()
            pyautogui.sleep(1)
    
    # Show the frame with the eye-controlled mouse
    cv2.imshow('Eye Controlled Mouse', frame)
    
    # Wait for key press and exit loop if 'q' is pressed
    if cv2.waitKey(1) == ord('q'):
        break

# Release video capture and destroy windows
cam.release()
cv2.destroyAllWindows()

