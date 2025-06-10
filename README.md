
# Vehicle Counter Project with OpenCV 🚗🚚

I have created Vehicle detection the main aim of this porject is to detect the vehicles that which one is car and which one is Truck.In this i have useed of OpenCV to detect and count vehicles.When displaying of the output it showing the counting of the each vehicle which passes though the detection line.After the detecting the vehicle that will be counted on the Sidebar. Eventhough time and date is also included along with FPs of the video fee.This is a beginner project which gives the solution for the traffice monitoring systems and also counting requirement.

## 🛠 Key Features:

1. Vehicle Detection: Used OpenCV's background subtractor MOG actually it identify the  moving objects in the video.

2. Vehicle Classification: Classifiy the vehicle wheather it is Cars 🚗 and Trucks 🚚,This will be identify based on their width ,height and rario.

3. RealTime Counting: It track the vehicles the update the total vehicle counts.

4. vehicle Count Display: The sidebar panel which shows the count of cars 🚗 and trucks 🚚 of their time.

5. Dynamic Display: It is used for the current date and time 🕒 also FPS of the video feed.


## Technologies Used:

- OpenCV 🖼: For real-time image processing and video analysis.

- Numpy 🔢: For matrix manipulation and array operations.

- Datetime 🗓: For displaying the current date and time in the video.

- Time ⏱: For calculating and displaying the frames per second (FPS).


## How it Works:

- Background Subtraction: It capture the background images and videos and  highlights moving vehicles.

- Contour Detection: Conting the vehicles from the processed video, representing moving vehicles.

- Bounding Box and Classification: For each contour, a bounding box is drawn around the detected vehicle.And clssify either it is car🚗 of truck🚚.
 
 User Interface: It displays  statistics such as vehicle type counts, the total vehicle count, current time 🕒, and also FPS 

💻 Output:

- After the displaying of the output you can check out for the  processed video which will be saved as output.avi 🎥.

- Vehicle count statistics will be displayed in real time on the video feed.


### 🙋‍♂️Author : Amit kumar
<img src="https://github.com/AmitAnant01/Vehicle-Detection-count/blob/main/detect.png" width="100%" />

