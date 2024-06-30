from ultralytics import YOLO
import os

dir = os.getcwd()
video_path = os.path.join(dir, 'data/input_video.mp4')
bytetrack_yaml_path = os.path.join(dir, 'bytetrack.yaml')

model = YOLO('yolov8n.pt')

results = model.track(source=video_path, persist=True, tracker=bytetrack_yaml_path)

print(results)