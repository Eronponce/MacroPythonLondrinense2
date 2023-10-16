import pyautogui
import keyboard
largura_foto = 720
captura_vermelho =(624, 806, largura_foto,3 )
captura_preto
def identifica_vermelho(imagem):
    for x in range(0, largura_foto ):
        if imagem.getpixel((x , 2)) == (255, 0, 0):
            return(x)


ecra = pyautogui.screenshot(region=captura_vermelho)
ecra.save('ecra.png')
while (not (keyboard.is_pressed('m'))):
    cordenada_preta = 0
    cordenada_preta += 1
    cordenada_vermelho = identifica_vermelho(ecra)
    print(cordenada_vermelho)
    while cordenada_preta != cordenada_vermelho:
        pyautogui.moveTo(624, 806)
        pyautogui.mouseDown()
    pyautogui.mouseUp()



