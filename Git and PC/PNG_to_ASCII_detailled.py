from PIL import Image

def image_to_ascii_detailed(image_path, width=100):
    img = Image.open(image_path).convert('L')
    
    aspect_ratio = img.height / img.width
    new_height = int(width * aspect_ratio * 0.55)
    img = img.resize((width, new_height))
    
    # Différents niveaux de densité avec des étoiles
    chars = [" ", ".", ":", "*", "#", "█"]  # Du plus clair au plus foncé
    
    pixels = img.getdata()
    ascii_str = ""
    
    for i, pixel in enumerate(pixels):
        # Choisir le caractère selon la luminosité
        char_index = int((pixel / 255) * (len(chars) - 1))
        ascii_str += chars[len(chars) - 1 - char_index]
        
        if (i + 1) % width == 0:
            ascii_str += "\n"
    
    return ascii_str

art = image_to_ascii_detailed("tête_de_mort.jpg", width=80)
print(art)