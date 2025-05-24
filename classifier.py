from ultralytics import YOLO
from multiprocessing import freeze_support

def main():
    # pretrained model YOLOv8
    model = YOLO("yolo11n.pt")

    # Train model on custom dataset
    results = model.train(data = "Datasets\drug-name-detection\data.yaml", epochs = 100, imgsz = 640)

if __name__ == "__main__":
    freeze_support()
    main()

