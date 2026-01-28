from PIL import Image

def image_to_ascii(image_path, width=100):
    
    img = Image.open(image_path)
    
    img = img.convert('L')
    
    aspect_ratio = img.height / img.width
    new_height = int(width * aspect_ratio * 0.55)  # 0.55 pour compenser la hauteur des caractères
    img = img.resize((width, new_height))
    
    
    pixels = img.getdata()
    ascii_str = ""
    
    for i, pixel in enumerate(pixels):
        if pixel < 128:  # Sombre = étoile
            ascii_str += "*"
        else:  # Clair = espace
            ascii_str += " "
        
        if (i + 1) % width == 0:
            ascii_str += "\n"
    
    return ascii_str

art = image_to_ascii("tête_de_mort.png", width=80)
print(art)