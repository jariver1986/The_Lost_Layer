import pygame
import keyboard
import time
import os

# -----------------------------------------
# CONFIGURACIÓN DE AUDIO
# -----------------------------------------
pygame.mixer.init()

# Ruta del archivo BASS
#audio_path = r"C:\Users\Usuario\Music\The_lost_layer_v20\The_lost_layer_v2.0-bass.mp3"
audio_path = r"C:\Users\Usuario\Music\The_lost_layer_v20\The_lost_layer_v2.0-vocals.mp3"


if not os.path.exists(audio_path):
    print("ERROR: No se encontró el archivo:", audio_path)
    exit()

# Cargar sonido
bass_sound = pygame.mixer.Sound(audio_path)

# Volumen inicial
volume = 0.5
bass_sound.set_volume(volume)

print("🎧 Control de Audio – The Lost Layer")
print("------------------------------------")
print(" Q → Reproducir BASS")
print(" W → Stop")
print(" A → Subir volumen")
print(" S → Bajar volumen")
print(" CTRL + C → Salir\n")

channel = None

# -----------------------------------------
# LOOP PRINCIPAL
# -----------------------------------------
while True:
    # Q = PLAY
    if keyboard.is_pressed("q"):
        if channel is None or not channel.get_busy():
            channel = bass_sound.play()
            print("▶ Reproduciendo BASS...")
        time.sleep(0.2)

    # W = STOP
    if keyboard.is_pressed("w"):
        if channel:
            channel.stop()
            print("■ STOP")
        time.sleep(0.2)

    # A = SUBIR VOLUMEN
    if keyboard.is_pressed("a"):
        volume = min(1.0, volume + 0.05)
        bass_sound.set_volume(volume)
        print(f"🔊 Volumen: {round(volume, 2)}")
        time.sleep(0.1)

    # S = BAJAR VOLUMEN
    if keyboard.is_pressed("s"):
        volume = max(0.0, volume - 0.05)
        bass_sound.set_volume(volume)
        print(f"🔉 Volumen: {round(volume, 2)}")
        time.sleep(0.1)

    time.sleep(0.01)

    # Z = RETROCEDER 50 ms (0.05 segundos)
    if keyboard.is_pressed("z"):
        if channel and channel.get_busy():
            # Obtener tiempo actual de reproducción en segundos
            current_pos = channel.get_pos() / 1000.0  # pygame lo da en milisegundos

            # Nuevo punto de inicio
            new_start = max(0, current_pos - 0.05)

            # Reproducir nuevamente desde esta posición
            channel.stop()
            channel = bass_sound.play(start=new_start)
            print(f"⏪ Retrocediendo a {round(new_start, 3)} segundos")
        
        time.sleep(0.1)
