"""This is a sample code submitted for hackathon verification as requested by organizers. To prevent potential leaks, sensitive keys and methods are not shared
as i was told by the lead organiser that project leak can not be guaranteed."""

#importing libraries
import cv2
import time
from PIL import Image
import pyttsx3
import io
import base64

try:
    tts_engine = pyttsx3.init()
    tts_engine.setProperty('rate', 150)
    tts_engine.setProperty('volume', 0.8)
except Exception:
    tts_engine = None
    print("Text-to-speech not available")
    
#using TTS for audio or speech to text conversion 
def speak(text):
    
    if tts_engine:
        try:
            tts_engine.say(text)
            tts_engine.runAndWait()
        except:
            print("TTS error, printing instead:", text)#error catching in case of any issue 
    else:
        print("SPEAK:", text)

def capture_image(filename='capture.jpg'):
    """Capture an image from the webcam."""
    cap = cv2.VideoCapture(1)  # Try Logitech webcam
    if not cap.isOpened():
        print("Logitech webcam not found, trying default camera") #if not able to connect to logicam ,switch to laptop cam 
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            print("No webcam available")
            return None
    # Set basic resolution
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    time.sleep(2)  # Wait for camera to warm up
    ret, frame = cap.read()
    cap.release()
    if ret:
        cv2.imwrite(filename, frame)
        print("Image captured:", filename)#image captured confirmation on console 
        return filename
    print("Failed to capture image")
    return None

def encode_image(image_path):
    with Image.open(image_path) as img:
        buf = io.BytesIO()
        img.save(buf, format="JPEG")#converting the image to base64
    return base64.b64encode(buf.getvalue()).decode()

def detect_threats(image_path):
    """Simulate threat detection with dummy data."""
    # sample result after detection .
    weapons = [
        {
            "type": "rifle",
            "model": "AK-47",
            "range": "400m",
            "threat_level": "High"
        }
    ]
    crowd = {
        "total_people": 2,
        "armed_people": 2
    }
    print("Detected threats:", weapons, crowd)
    return weapons, crowd
#strategy and report to be provided to the officer and webapp
def create_report(weapons, crowd):
    weapon = weapons[0] if weapons else {}
    report = (     
        f"Weapon: {weapon.get('type', 'Unknown')} {weapon.get('model', 'unknown')}.\n"
    )
    print("Report:", report)
    return report

#survillence mode fucntion
def main():
    print("Starting security system")
    speak("Starting surveillance")
    
    # Capture image
    img_file = capture_image()
    if not img_file:
        speak("Cannot capture image")
        return
    
    # Encode image (for demo, not used in processing)
    encoded = encode_image(img_file)
    print("Image encoded (base64 length):", len(encoded))
    
    # Simulate threat detection
    weapons= detect_threats(img_file)#detecting the weapon using gemini api
    
    # Create and speak report
    report = create_report(weapons)
    speak(report)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Program stopped")
        speak("System stopped")
    finally:
        if tts_engine:
            tts_engine.stop()
        cv2.destroyAllWindows()
