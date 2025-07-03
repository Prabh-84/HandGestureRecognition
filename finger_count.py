import cv2
import mediapipe as mp
import time  # ⬅️ For FPS

# Initialize MediaPipe
mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands=1)
mpDraw = mp.solutions.drawing_utils

# Finger tip landmarks IDs
tipIds = [4, 8, 12, 16, 20]

cap = cv2.VideoCapture(0)

# For FPS calculation
pTime = 0  # previous time
cTime = 0  # current time

while True:
    success, img = cap.read()
    if not success:
        break
    img = cv2.flip(img, 1)
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    lmList = []
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
            for id, lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append((id, cx, cy))

    if lmList:
        fingers = []

        # Thumb
        if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
            fingers.append(1)
        else:
            fingers.append(0)

        # Other 4 fingers
        for i in range(1, 5):
            if lmList[tipIds[i]][2] < lmList[tipIds[i] - 2][2]:
                fingers.append(1)
            else:
                fingers.append(0)

        totalFingers = fingers.count(1)

        # Show fingers count
        cv2.putText(img, f'Fingers: {totalFingers}', (20, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 0), 3)

        # Gesture recognition
        gesture = "Unknown"
        if totalFingers == 0:
            gesture = "Fist"
        elif totalFingers == 1:
            gesture = "One"
        elif totalFingers == 2:
            gesture = "Two"
        elif totalFingers == 3:
            gesture = "Three"
        elif totalFingers == 4:
            gesture = "Four"
        elif totalFingers == 5:
            gesture = "Five"

        cv2.putText(img, f'Gesture: {gesture}', (20, 100),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 0, 0), 3)
    else:
        # No hand detected
        cv2.putText(img, 'Gesture: None', (20, 100),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 255), 3)

    # ⏱️ FPS calculation and display
    cTime = time.time()
    fps = 1 / (cTime - pTime) if cTime - pTime != 0 else 0
    pTime = cTime

    cv2.putText(img, f'FPS: {int(fps)}', (450, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)

    cv2.imshow("Finger Counter", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
