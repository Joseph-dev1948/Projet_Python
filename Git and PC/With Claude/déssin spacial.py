# hand_draw_turtle_neon.py
import cv2
import mediapipe as mp
import threading
import queue
import turtle
import time
import math

CAM_WIDTH, CAM_HEIGHT = 800, 800
TURTLE_WIDTH, TURTLE_HEIGHT = 800, 800
QUEUE_TIMEOUT = 0.02

# ---------- Utils ----------
def normalized_to_turtle(x, y, turtle_w, turtle_h):
    tx = (x - 0.5) * turtle_w
    ty = (0.5 - y) * turtle_h
    return tx, ty

# ---------- Turtle Thread ----------
def turtle_thread_func(pt_queue: queue.Queue):
    screen = turtle.Screen()
    screen.setup(width=TURTLE_WIDTH, height=TURTLE_HEIGHT)
    screen.title("Turtle Finger Neon Paint")
    screen.tracer(0)

    pen = turtle.Turtle()
    pen.hideturtle()
    pen.speed(0)
    pen.pensize(3)

    glow = turtle.Turtle()
    glow.hideturtle()
    glow.speed(0)
    glow.pensize(9)

    drawing = False
    current_color = "red"

    while True:
        try:
            data = pt_queue.get(timeout=QUEUE_TIMEOUT)
        except queue.Empty:
            screen.update()
            continue

        if data is None:
            break

        x, y, draw_flag, color = data
        current_color = color

        if draw_flag:
            if not drawing:
                pen.penup()
                glow.penup()
                pen.goto(x, y)
                glow.goto(x, y)
                pen.pendown()
                glow.pendown()
                drawing = True
            else:
                glow.color(color)
                pen.color(color)
                glow.goto(x, y)
                pen.goto(x, y)
        else:
            if drawing:
                pen.penup()
                glow.penup()
                drawing = False

        screen.update()

# ---------- Main ----------
def main():
    pt_queue = queue.Queue()
    t_thread = threading.Thread(target=turtle_thread_func, args=(pt_queue,), daemon=True)
    t_thread.start()

    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(
        max_num_hands=1,
        min_detection_confidence=0.6,
        min_tracking_confidence=0.5
    )
    mp_drawing = mp.solutions.drawing_utils

    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, CAM_WIDTH)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, CAM_HEIGHT)

    # Couleur selon le nombre de doigts levés
    color_map = {
        1: "red",
        2: "green",
        3: "blue",
        4: "yellow",
        5: "purple"
    }

    # Landmark des doigts
    finger_landmarks = [4, 8, 12, 16, 20]  # pouce, index, majeur, annulaire, auriculaire

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = hands.process(frame_rgb)

            draw_flag = False
            color = "red"

            if results.multi_hand_landmarks:
                lm = results.multi_hand_landmarks[0].landmark

                # Vérifier doigts levés
                fingers_up = [
                    lm[8].y < lm[6].y,   # index
                    lm[12].y < lm[10].y, # majeur
                    lm[16].y < lm[14].y, # annulaire
                    lm[20].y < lm[18].y  # auriculaire
                ]
                thumb_up = lm[4].x < lm[3].x

                total_up = sum(fingers_up) + (1 if thumb_up else 0)

                # Choix de la couleur selon nombre de doigts levés
                if total_up in color_map:
                    color = color_map[total_up]

                # Dessiner si au moins un doigt levé
                if total_up > 0:
                    draw_flag = True
                    # Identifier le doigt levé pour le dessin (prendre le premier levé)
                    finger_states = [thumb_up] + fingers_up
                    for i, up in enumerate(finger_states):
                        if up:
                            lm_idx = finger_landmarks[i]
                            finger_pos = (lm[lm_idx].x, lm[lm_idx].y)
                            break
                    tx, ty = normalized_to_turtle(finger_pos[0], finger_pos[1], TURTLE_WIDTH, TURTLE_HEIGHT)
                    pt_queue.put((tx, ty, draw_flag, color))

                # Affichage caméra
                h, w, _ = frame.shape
                for i, up in enumerate([thumb_up]+fingers_up):
                    cx, cy = int(lm[finger_landmarks[i]].x*w), int(lm[finger_landmarks[i]].y*h)
                    cv2.circle(frame, (cx, cy), 10, (0,255,0) if up else (0,0,255), -1)
                cv2.putText(frame, f"Color: {color}", (10,40),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)
                mp_drawing.draw_landmarks(frame, results.multi_hand_landmarks[0], mp_hands.HAND_CONNECTIONS)

            cv2.imshow("Neon Finger Paint - Camera", frame)
            key = cv2.waitKey(1) & 0xFF

            # Quitter
            if key == 27:
                break

            # Sauvegarder dessin
            if key == ord("s"):
                ts = int(time.time())
                turtle.getcanvas().postscript(file=f"drawing_{ts}.eps")
                print(f"Image sauvegardée: drawing_{ts}.eps")

    finally:
        cap.release()
        cv2.destroyAllWindows()
        pt_queue.put(None)
        time.sleep(0.1)

if __name__ == "__main__":
    main()