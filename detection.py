import cv2 
import numpy as np
import datetime
import time

# Input video
cap = cv2.VideoCapture('vehicle.mp4')

# Video writer setup
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (frame_width, frame_height))

# Video writer setup
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (int(cap.get(3)), int(cap.get(4))))

# Constants
min_width_rectangle = 80
min_height_rectangle = 80
count_line_position = 550
offset = 6

# Counters
total_count = 0
car_count = 0
truck_count = 0
bike_count = 0

# Background subtractor
algo = cv2.bgsegm.createBackgroundSubtractorMOG()

# Detection list
detect = []
prev_time = 0

def center_point(x, y, h, w):
    cx = int(x + w/2)
    cy = int(y + h/2)
    return cx, cy

def get_vehicle_type(w, h):
    area = w * h
    ratio = w / float(h)
    if area > 30000 and ratio > 0.9:
        return "Truck"
    else:
        return "Car"

color_map = {
    "Car": (0, 255, 255),
    "Truck": (0, 0, 255)

}

while True:
    ret, frame1 = cap.read()
    if not ret:
        break

    grey = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(grey, (3, 3), 5)

    img_sub = algo.apply(blur)
    dilate = cv2.dilate(img_sub, np.ones((5, 5)))
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    feature = cv2.morphologyEx(dilate, cv2.MORPH_CLOSE, kernel)
    feature = cv2.morphologyEx(feature, cv2.MORPH_CLOSE, kernel)

    contours, _ = cv2.findContours(feature, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    cv2.line(frame1, (25, count_line_position), (1200, count_line_position), (255, 127, 0), 3)

    for c in contours:
        (x, y, w, h) = cv2.boundingRect(c)
        if w >= min_width_rectangle and h >= min_height_rectangle:
            cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)
            center = center_point(x, y, h, w)
            detect.append(center)
            cv2.circle(frame1, center, 4, (0, 0, 255), -1)

            vehicle_type = get_vehicle_type(w, h)
            cv2.putText(frame1, vehicle_type, (x, y - 10), cv2.FONT_HERSHEY_DUPLEX, 0.8, color_map[vehicle_type], 2)

            for (cx, cy) in detect:
                if count_line_position - offset < cy < count_line_position + offset:
                    total_count += 1

                    if vehicle_type == "Truck":
                        truck_count += 1
                    else:
                        car_count += 1

                    cv2.line(frame1, (25, count_line_position), (1200, count_line_position), (0, 127, 255), 3)
                    detect.remove((cx, cy))
                    print(f"Vehicle Count: {total_count} | Car: {car_count}, Truck: {truck_count}")

# RIGHT SIDEBAR PANEL
    sidebar_x = frame_width - 280
    cv2.rectangle(frame1, (sidebar_x, 80), (frame_width - 10, 250), (50, 50, 50), -1)
    cv2.putText(frame1, "Car  : " + str(car_count), (sidebar_x + 10, 120), cv2.FONT_HERSHEY_SIMPLEX, 0.7, color_map["Car"], 2)
    cv2.putText(frame1, "Truck : " + str(truck_count), (sidebar_x + 10, 160), cv2.FONT_HERSHEY_SIMPLEX, 0.7, color_map["Truck"], 2)
    cv2.putText(frame1, "Total  : " + str(total_count), (sidebar_x + 10, 210), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    # Title
    cv2.putText(frame1, 'VEHICLE COUNTER PROJECT', (400, 60), cv2.FONT_HERSHEY_TRIPLEX, 1, (255, 0, 255), 2)

    # Date and time
    current_time = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    cv2.putText(frame1, current_time, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 0), 2)

    # FPS
    new_time = time.time()
    fps = int(1 / (new_time - prev_time)) if new_time != prev_time else 0
    prev_time = new_time
    cv2.putText(frame1, f'FPS: {fps}', (1000, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

    out.write(frame1)
    cv2.imshow("Vehicle Counter", frame1)

    if cv2.waitKey(1) == 13:  # Enter key
        break

cap.release()
out.release()
cv2.destroyAllWindows()