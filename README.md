# Driver Drowsiness Detection System

Real-time driver drowsiness detection system using OpenCV and Haar Cascade.  
The system monitors eye closure and triggers an alert to prevent accidents caused by driver fatigue.

## Features
- Real-time face and eye detection using webcam
- Blink ignored to reduce false alerts
- Continuous alert sound if eyes remain closed beyond threshold
- Displays status: "AWAKE" or "EYES CLOSED"
- Simple Python code, easy to understand for students

## Technologies Used
- Python
- OpenCV
- Haar Cascade Classifier
- Winsound (Windows alarm)

## How it Works
1. Detects face using Haar Cascade.
2. Detects eyes within the face region.
3. Counts consecutive frames where eyes are closed.
4. Triggers a sound alert if eyes remain closed for more than the set duration.
5. Displays real-time status on video.

## Installation
```bash
# Clone the repository
git clone <your-repo-link>

# Install required packages
pip install opencv-python
