import pygame
import time
import random
from colorama import init, Fore, Back, Style

# Inicializar colorama
init(autoreset=True)

def reproducir_musica_con_control(ruta_audio, letras_y_tiempos, stickers):
    """
    Versión con control manual del tiempo de inicio:
    - Permite ingresar manualmente el segundo de inicio
    - Sincroniza las letras con el tiempo especificado
    - Mantiene todas las características de colores y stickers
    """
    # Separar letras y tiempos
    letras = [item[0] for item in letras_y_tiempos]
    tiempos = [item[1] for item in letras_y_tiempos]
    
    # Colores disponibles para las letras
    colores = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, 
               Fore.MAGENTA, Fore.CYAN, Fore.WHITE]
    
    # Solicitar segundo de inicio al usuario
    while True:
        try:
            # segundo_inicio = float(input(f"\n{Back.BLUE}⏰ Ingrese el segundo de inicio (0-{tiempos[-1]}): {Style.RESET_ALL}"))
            segundo_inicio = 82
            if 0 <= segundo_inicio <= tiempos[-1]:
                break
            else:
                print(f"{Fore.RED}❌ Por favor ingrese un valor entre 0 y {tiempos[-1]}{Style.RESET_ALL}")
        except ValueError:
            print(f"{Fore.RED}❌ Ingrese un número válido{Style.RESET_ALL}")
    
    pygame.mixer.init()
    
    try:
        print(f"\n{Back.BLUE}🎶 Reproduciendo desde el segundo {segundo_inicio}: {ruta_audio}{Style.RESET_ALL}\n")
        pygame.mixer.music.load(ruta_audio)
        pygame.mixer.music.play(start=segundo_inicio)
        
        inicio = time.time() - segundo_inicio  # Ajustamos el tiempo de referencia
        indice_letra = 0
        
        # Encontrar el primer índice de letra que corresponde al tiempo de inicio
        for i, t in enumerate(tiempos):
            if t >= segundo_inicio:
                indice_letra = i
                break
        
        while indice_letra < len(letras):
            tiempo_actual = time.time() - inicio
            
            if tiempo_actual >= tiempos[indice_letra]:
                # Seleccionar color y sticker aleatorio
                color = random.choice(colores)
                sticker = random.choice(stickers)
                
                # Mostrar letra con color y sticker
                print(f"{color}{letras[indice_letra]} {sticker}")
                indice_letra += 1
                
                # Pequeña pausa entre letras
                time.sleep(0.2)
            
            time.sleep(0.01)
        
        # Esperar a que termine la canción
        while pygame.mixer.music.get_busy():
            time.sleep(0.1)
            
    except Exception as e:
        print(f"{Fore.RED}❌ Error: {str(e)}{Style.RESET_ALL}")
    finally:
        pygame.mixer.quit()
        print(f"\n{Back.GREEN}✅ Reproducción finalizada{Style.RESET_ALL}")

# --------------------------------------------------
# CONFIGURACIÓN PERSONALIZADA
# --------------------------------------------------

# Archivo de audio
ruta_audio = "amordevago.mp3"

# Letras con tiempos (ocultos al usuario)
letras_y_tiempos = [
    ["El verdadero beso de vago", 82],
    ["Que no vas a olvidar jamás", 84],
    ["Es que me tiene loco su manera de mirarme", 86],
    ["Como ella le hace pa' llegarme", 89],
    ["Como lo hace tierno al amarme", 91],
    ["Sus ojos marrones con la luna brillan", 95],
    ["Segundecame hasta el mediodía", 98],
    ["Hasta que abra la panadería", 100],
    ["Pasamos el día con la fría", 103],
    ["Me rompo el asado y algo pa' tomar", 106],
    ["Es que corrugo la pasa' mejor", 109]
]

# Lista de stickers/emojis para mostrar aleatoriamente
stickers = ["💿", "🎤", "🔥", "✨", "🎶", "💖", "👏", "🎵", "💫", "👍"]

# Ejecutar reproducción con control manual
reproducir_musica_con_control(ruta_audio, letras_y_tiempos, stickers)