import cv2
import mediapipe as mp
import moves


########## SOLUTIONS #########################################################
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_holistic = mp.solutions.holistic

cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 2000)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 2000)

########## INSTANCIANDO ######################################################

biceps_left = moves.BicepsLeft()
biceps_right = moves.BicepsRight()
stretched_left_arm = moves.StretchedLeftArm()
stretched_right_arm = moves.StretchedRightArm()
raised_left_arm = moves.RaisedLeftArm()
raised_right_arm = moves.RaisedRightArm()
rest_left_arm = moves.RestLeftArm()
rest_right_arm = moves.RestRightArm()
hand_touch = moves.HandTouch()
raised = moves.Raised()
lowered = moves.Lowered()
strong_left = moves.StrongLeft()
stretched_left_leg = moves.StretchedLeftLeg()
stretched_right_leg = moves.StretchedRightLeg()
hand_left_mouth = moves.LeftHandMouth()
hand_right_mouth = moves.RightHandMouth()
side = moves.Side()
rest = moves.Rest()
head_to_left = moves.HeadToLeft()
head_to_right = moves.HeadToRight()


poses = [
    biceps_left,
    biceps_right,
    stretched_left_arm,
    stretched_right_arm,
    raised_left_arm,
    raised_right_arm,
    rest_left_arm,
    rest_right_arm,
    hand_touch,
    raised,
    lowered,
    strong_left,
    stretched_left_leg,
    stretched_right_leg,
    hand_left_mouth,
    hand_right_mouth,
    side,
    rest,
    head_to_left,
    head_to_right,
]

########## MEDIAPIPE INSTANCE ################################################

with mp_holistic.Holistic(
    min_detection_confidence=.9,
    min_tracking_confidence=.9
) as holistic:

    while cap.isOpened():
        ret, frame = cap.read()

        # IMAGE TO RGB:
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # ENANTIMORFISMO ESPELHOS PLANOS:
        image = cv2.flip(image, 1)
        image.flags.writeable = False

        # MAKE DETECTIONS:
        results = holistic.process(image)

        # RECOLOR IMAGEM BACK TO BGR:
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

########## GET COORDINATES ###################################################

        # EXTRACT LANDMARKS
        try:
            landmarks = results.pose_landmarks.landmark

            left_wrist = [
                landmarks[mp_holistic.PoseLandmark.LEFT_WRIST.value].x,
                landmarks[mp_holistic.PoseLandmark.LEFT_WRIST.value].y
            ]

            right_wrist = [
                landmarks[mp_holistic.PoseLandmark.RIGHT_WRIST.value].x,
                landmarks[mp_holistic.PoseLandmark.RIGHT_WRIST.value].y
            ]

            left_shoulder = [
                landmarks[mp_holistic.PoseLandmark.LEFT_SHOULDER.value].x,
                landmarks[mp_holistic.PoseLandmark.LEFT_SHOULDER.value].y
            ]

            right_shoulder = [
                landmarks[mp_holistic.PoseLandmark.RIGHT_SHOULDER.value].x,
                landmarks[mp_holistic.PoseLandmark.RIGHT_SHOULDER.value].y
            ]

            left_elbow = [
                landmarks[mp_holistic.PoseLandmark.LEFT_ELBOW.value].x,
                landmarks[mp_holistic.PoseLandmark.LEFT_ELBOW.value].y
            ]

            right_elbow = [
                landmarks[mp_holistic.PoseLandmark.RIGHT_ELBOW.value].x,
                landmarks[mp_holistic.PoseLandmark.RIGHT_ELBOW.value].y
            ]

            left_hip = [
                landmarks[mp_holistic.PoseLandmark.LEFT_HIP.value].x,
                landmarks[mp_holistic.PoseLandmark.LEFT_HIP.value].y
            ]

            right_hip = [
                landmarks[mp_holistic.PoseLandmark.RIGHT_HIP.value].x,
                landmarks[mp_holistic.PoseLandmark.RIGHT_HIP.value].y
            ]

            right_index = [
                landmarks[mp_holistic.PoseLandmark.RIGHT_INDEX.value].x,
                landmarks[mp_holistic.PoseLandmark.RIGHT_INDEX.value].y
            ]

            left_index = [
                landmarks[mp_holistic.PoseLandmark.LEFT_INDEX.value].x,
                landmarks[mp_holistic.PoseLandmark.LEFT_INDEX.value].y
            ]

            left_ankle = [
                landmarks[mp_holistic.PoseLandmark.LEFT_ANKLE.value].x,
                landmarks[mp_holistic.PoseLandmark.LEFT_ANKLE.value].y
            ]

            right_ankle = [
                landmarks[mp_holistic.PoseLandmark.RIGHT_ANKLE.value].x,
                landmarks[mp_holistic.PoseLandmark.RIGHT_ANKLE.value].y
            ]

            mouth_left = [
                landmarks[mp_holistic.PoseLandmark.MOUTH_LEFT.value].x,
                landmarks[mp_holistic.PoseLandmark.MOUTH_LEFT.value].y
            ]

            mouth_right = [
                landmarks[mp_holistic.PoseLandmark.MOUTH_RIGHT.value].x,
                landmarks[mp_holistic.PoseLandmark.MOUTH_RIGHT.value].y
            ]

            nose = [
                landmarks[mp_holistic.PoseLandmark.NOSE.value].x,
                landmarks[mp_holistic.PoseLandmark.NOSE.value].y
            ]

            left_foot_index = [
                landmarks[mp_holistic.PoseLandmark.LEFT_FOOT_INDEX.value].x,
                landmarks[mp_holistic.PoseLandmark.LEFT_FOOT_INDEX.value].y
            ]

            right_eye_outer = [
                landmarks[mp_holistic.PoseLandmark.RIGHT_EYE_OUTER.value].x,
                landmarks[mp_holistic.PoseLandmark.RIGHT_EYE_OUTER.value].y
            ]

            left_eye_outer = [
                landmarks[mp_holistic.PoseLandmark.LEFT_EYE_OUTER.value].x,
                landmarks[mp_holistic.PoseLandmark.LEFT_EYE_OUTER.value].y
            ]

########## UPDATES ###########################################################

            biceps_left.update(
                left_shoulder, left_elbow, left_wrist
            )

            biceps_right.update(
                right_shoulder, right_elbow, right_wrist
            )
            stretched_left_arm.update(
                right_shoulder, left_shoulder, left_elbow, left_wrist
            )
            stretched_right_arm.update(
                left_shoulder, right_shoulder, right_elbow, right_wrist
            )
            raised_left_arm.update(
                left_hip, left_shoulder, left_elbow, left_wrist
            )
            raised_right_arm.update(
                right_hip, right_shoulder, right_elbow, right_wrist
            )
            rest_left_arm.update(
                left_hip, left_shoulder, left_elbow, left_wrist
            )
            rest_right_arm.update(
                right_hip, right_shoulder, right_elbow, right_wrist
            )
            hand_touch.update(
                right_index, left_index
            )
            raised.update(
                right_shoulder, left_shoulder
            )
            lowered.update(
                right_shoulder, left_shoulder
            )
            strong_left.update(
                left_shoulder, left_wrist, left_elbow
            )
            stretched_left_leg.update(
                right_hip, left_ankle, left_hip
            )
            stretched_right_leg.update(
                left_hip, right_ankle, right_hip
            )
            hand_left_mouth.update(
                left_index, mouth_left
            )
            hand_right_mouth.update(
                right_index, mouth_right
            )
            side.update(
                right_shoulder, left_shoulder
            )
            rest.update(
                nose, left_foot_index
            )
            head_to_left.update(
                mouth_right, [0, 0], mouth_left
            )

            head_to_right.update(
                mouth_left, [1, 0], mouth_right
            )

        except:
            pass

########## PLOT COUNTER ######################################################

        for index_pose_array, pose_array in enumerate(poses):
            cv2.putText(
                image,
                pose_array.get_label() + ': ' + str(pose_array.get_counter()),
                (15, 30 + (30 * index_pose_array)),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 0, 0),
                2,
                cv2.LINE_AA
            )

########## DRAW LANDMARKS ####################################################

        # MY CUSTOM DRAWINGSPEC
        COLOR = (0, 255, 0)
        THICKNESS = 2
        CIRCLE_RADIUS = 2

        # POSE CONNECTIONS
        mp_drawing.draw_landmarks(
            image,
            results.pose_landmarks,
            mp_holistic.POSE_CONNECTIONS,
            mp_drawing.DrawingSpec(COLOR, THICKNESS, CIRCLE_RADIUS),
            mp_drawing.DrawingSpec(COLOR, THICKNESS, CIRCLE_RADIUS)
        )

        # DISPLAY THE RESULTING FRAME:
        cv2.imshow('Mediapipe', image)
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break


cap.release()
cv2.destroyAllWindows()
