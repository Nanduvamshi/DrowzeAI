# modules/detection.py
def start_drowsiness_detection():
    import cv2, dlib, time, numpy as np, imutils, pyttsx3, os
    from imutils.video import VideoStream
    from imutils import face_utils
    from modules.EAR import eye_aspect_ratio
    from modules.MAR import mouth_aspect_ratio
    import threading

    engine = pyttsx3.init()
    def speak_alert(message):
        def speak():
            engine = pyttsx3.init()
            engine.say(message)
            engine.runAndWait()
        threading.Thread(target=speak).start()

    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor("modules/shape_predictor_68_face_landmarks (1).dat")

    vs = VideoStream(src=0).start()
    time.sleep(2.0)

    frame_width, frame_height = 640, 360
    EYE_AR_THRESH = 0.25
    MOUTH_AR_THRESH = 0.79
    DROWSY_EYE_TIME_THRESH = 3  # seconds
    YAWN_TIME_THRESH = 1         # seconds

    (lStart, lEnd) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
    (rStart, rEnd) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]
    (mStart, mEnd) = (49, 68)

    frame_count = 0
    rects = []

    eye_closed_start = None
    mouth_open_start = None

    while True:
        frame = vs.read()
        if frame is None:
            continue

        frame = imutils.resize(frame, width=frame_width, height=frame_height)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        frame_count += 1
        if frame_count % 5 == 0:
            rects = detector(gray, 0)

        for rect in rects:
            shape = predictor(gray, rect)
            shape = face_utils.shape_to_np(shape)

            # Eye detection
            leftEye = shape[lStart:lEnd]
            rightEye = shape[rStart:rEnd]
            ear = (eye_aspect_ratio(leftEye) + eye_aspect_ratio(rightEye)) / 2.0

            if ear < EYE_AR_THRESH:
                if eye_closed_start is None:
                    eye_closed_start = time.time()
                else:
                    closed_duration = time.time() - eye_closed_start
                    if closed_duration >= DROWSY_EYE_TIME_THRESH:
                        speak_alert("Driver seems drowsy. Eyes closed for too long.")
                        eye_closed_start = None
            else:
                eye_closed_start = None

            # Mouth detection
            mouth = shape[mStart:mEnd]
            mar = mouth_aspect_ratio(mouth)

            if mar > MOUTH_AR_THRESH:
                if mouth_open_start is None:
                    mouth_open_start = time.time()
                else:
                    yawn_duration = time.time() - mouth_open_start
                    if yawn_duration >= YAWN_TIME_THRESH:
                        speak_alert("Driver is yawning. Please stay alert.")
                        mouth_open_start = None
            else:
                mouth_open_start = None

        cv2.imshow("Drowsiness Detection", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cv2.destroyAllWindows()
    vs.stop()
