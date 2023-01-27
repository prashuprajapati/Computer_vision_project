import cv2
import mediapipe as mp # it is detect the face
import pyautogui
import time
cam=cv2.VideoCapture(0)
face_match=mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
screen_w,screen_h = pyautogui.size() # return the screen height and width
while True:
    _, frame=cam.read()
    frame=cv2.flip(frame, 1) # flip the eye and use for move the cursur
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # change the color of frame
    output = face_match.process(rgb_frame)             # output after the detect the image
    landmark_points=output.multi_face_landmarks      # return the landmarks(face) point in the form of neumeric value (x,y,z)
    frame_h, frame_w, _ = frame.shape   # return the height and width of frame
    if landmark_points:
        landmarks = landmark_points[0].landmark
        #print(landmarks)
        for id , landmark in enumerate(landmarks[474:478]): # it is range of right eye which is show
            x = int(landmark.x*frame_w)
            y = int(landmark.y*frame_h)
            cv2.circle(frame , (x, y),3,(0, 255, 0))  # it is take frame, frame(height,width),radius,color in rgb and it is detect all face
            if id==1:
                screen_x = int(screen_w/frame_w*x)
                screen_y = int(screen_h/frame_h*y)
                pyautogui.moveTo(screen_x,screen_y)
        left=[landmarks[145],landmarks[159]]  # it is given landmarks of left eyes
        for landmark in left:
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x, y), 3, (0, 255, 255)) # detect the left eyes
        if left[0].y-left[1].y<0.004:
            pyautogui.click()  # it is click the any button
            time.sleep(5)
    cv2.imshow('image is ', frame)
    cv2.waitKey(1)