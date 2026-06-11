import os
import sys
from PIL import Image

def process_forensics():
    try:
        # C#'tan gelen yolları al
        input_dir = sys.argv[1] if len(sys.argv) > 1 else ""
        output_dir = sys.argv[2] if len(sys.argv) > 2 else ""

        if not os.path.exists(input_dir):
            return

        for filename in os.listdir(input_dir):
            if filename.lower().endswith((".jpg", ".jpeg", ".png")):
                img_path = os.path.join(input_dir, filename)
                
                # Resmin verisini tamamen yeni bir dosyaya kopyalayarak EXIF'i yok et
                with Image.open(img_path) as img:
                    clean_img = Image.new(img.mode, img.size)
                    clean_img.putdata(list(img.getdata()))
                    
                    save_path = os.path.join(output_dir, "cleaned_" + filename)
                    clean_img.save(save_path)
    except Exception as e:
        # Hata olursa masaüstüne log bırakır
        desktop = os.path.join(os.path.expanduser('~'), 'Desktop')
        with open(os.path.join(desktop, "log.txt"), "a") as f:
            f.write(str(e) + "\n")

if __name__ == "__main__":
    process_forensics()
