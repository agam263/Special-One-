import sys
from PIL import Image

def make_white_transparent(image_path, output_path):
    img = Image.open(image_path).convert("RGBA")
    datas = img.getdata()
    
    newData = []
    # threshold for considering a color "white"
    threshold = 240
    for item in datas:
        # Check if the pixel is close to white
        if item[0] > threshold and item[1] > threshold and item[2] > threshold:
            newData.append((255, 255, 255, 0)) # transparent
        else:
            newData.append(item)
            
    img.putdata(newData)
    img.save(output_path, "PNG")
    print("Background removed successfully.")

if __name__ == "__main__":
    make_white_transparent(sys.argv[1], sys.argv[2])
