import pygame
import time

def play_music(soundPorCausaDele):
    try:
        # Inicializar o pygame e o mixer de áudio
        pygame.init()
        pygame.mixer.init()

        # Carregar música
        pygame.mixer.music.load(sound_PorCausaDele)

        # Reproduzir música
        pygame.mixer.music.play()

        print('OBRIGADO POR FICAR ATÉ AQUI!')

        # Manter o programa em execução enquanto a música estiver sendo reproduzida
        while pygame.mixer.music.get_busy():
            time.sleep(1)

    except pygame.error as e:
        print(f'Erro ao reproduzir a música: {e}')

    finally:
        # Limpar o pygame ao finalizar
        pygame.quit()

# Arquivo de música
sound_PorCausaDele = 'PorCausaDele.mp3'

# Chamar a função para reproduzir a música
play_music(sound_PorCausaDele)
