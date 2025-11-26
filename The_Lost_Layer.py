import pygame
import keyboard
import time
import os

# -----------------------------------------
# CONFIGURACIÓN DE AUDIO
# -----------------------------------------
pygame.mixer.init()

# Ruta del archivo BASS
audio_path = r"C:\Users\Usuario\Music\The_lost_layer_v20\The_lost_layer_v2.0-vocals.wav"

if not os.path.exists(audio_path):
    print("ERROR: No se encontró el archivo:", audio_path)
    exit()

# Cargar en pygame.mixer.music (NO Sound)
pygame.mixer.music.load(audio_path)

# Volumen inicial
volume = 0.5
pygame.mixer.music.set_volume(volume)

print("🎧 Control de Audio – The Lost Layer")
print("------------------------------------")
print(" Q → Reproducir BASS")
print(" W → Stop")
print(" A → Subir volumen")
print(" S → Bajar volumen")
print(" Z → Retroceder 50 ms")
print(" CTRL + C → Salir\n")

# -----------------------------------------
# LOOP PRINCIPAL
# -----------------------------------------

last_z_state = False


while True:

    # Q = PLAY
    if keyboard.is_pressed("q"):
        pygame.mixer.music.play()
        print("▶ Reproduciendo BASS...")
        time.sleep(0.2)

    # W = STOP
    if keyboard.is_pressed("w"):
        pygame.mixer.music.stop()
        print("■ STOP")
        time.sleep(0.2)

    # A = SUBIR VOLUMEN
    if keyboard.is_pressed("a"):
        volume = min(1.0, volume + 0.05)
        pygame.mixer.music.set_volume(volume)
        print(f"🔊 Volumen: {round(volume, 2)}")
        time.sleep(0.1)

    # S = BAJAR VOLUMEN
    if keyboard.is_pressed("s"):
        volume = max(0.0, volume - 0.05)
        pygame.mixer.music.set_volume(volume)
        print(f"🔉 Volumen: {round(volume, 2)}")
        time.sleep(0.1)

        # Z = RETROCEDER 50 ms (solo una vez por toque)
    z_pressed = keyboard.is_pressed("z")

    if z_pressed and not last_z_state:
        pos_ms = pygame.mixer.music.get_pos()
        if pos_ms != -1:
            current_pos = pos_ms / 1000.0
            new_pos = max(0, current_pos - 0.01)
            pygame.mixer.music.play(start=new_pos)
            print(f"⏪ Retroceder a {round(new_pos, 3)} s")
        time.sleep(0.05)

    last_z_state = z_pressed


    time.sleep(0.01)
