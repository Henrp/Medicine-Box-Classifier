import os

def main():
    folder = "Datasets/drug-name-detection/train/labels"
    for count, filename in enumerate(os.listdir(folder)):
        name = f"Labels {str(count + 1)}.txt"
        
        # original name
        src = f"{folder}/{filename}"
        # new name
        dst = f"{folder}/{name}"
        if not os.path.exists(dst):
            os.rename (src, dst)

if __name__ == "__main__":
    main()