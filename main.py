
from time import sleep
import telepot
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

token = '5614224301:AAEz-FJX5gKMJQT05qtUt3vYnY4oQHJhg3s'

chat_id = -1001822973795

msg_entrada = "🔔 Entrada Confirmada 🔔\n" \
              "✅ Entrar Alto ✅ \n" \
              "🎰 Jogo: Jetx 🎰"

msg_possivel_entrada = "⚠️ Atenção Possivel Entrada ⚠️"

ultima_msg_possivel_entrada = None

bot = telepot.Bot(token)


def initialize_chrome_browser(options=None):
    options = options or webdriver.ChromeOptions()
    #options.add_argument(r'--user-data-dir=C:\\Users\\user\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 2')
    options.add_argument('--profile-directory=Default')
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-logging")
    options.add_argument("--disable-login-animations")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-default-apps")
    options.add_argument("--disable-popup-blocking")
    Navegador = webdriver.Chrome(options=options)
    return Navegador


def enviar_mensagem(token, chat_id, mensagem):
    msg = bot.sendMessage(chat_id, mensagem)
    return msg


def responder_green(msg):
    messageId = msg['message_id']
    bot.sendChatAction(chat_id, 'typing')
    bot.sendMessage(chat_id, '✅✅✅✅GREENNNN ✅✅✅✅✅✅✅', reply_to_message_id=messageId)


def responder_loss(msg):
    messageId = msg['message_id']
    bot.sendChatAction(chat_id, 'typing')
    bot.sendMessage(chat_id, '❌❌❌❌ LOSS ❌❌❌❌', reply_to_message_id=messageId)


def deletar_mensagem(msg):
    messageId = msg['message_id']

    if msg['text'] == '⚠️ Atenção Possivel Entrada ⚠️':
        bot.deleteMessage((chat_id, messageId))


def jogo():
    global msg
    wait = WebDriverWait(driver, 200)
    wait.until(EC.visibility_of_element_located(
        (By.CLASS_NAME, "game-started")))
    #print("Apareceu")

    wait.until(EC.invisibility_of_element_located(
        (By.CLASS_NAME, "game-started")))
    #print("Sumiu")

    div_last100Spins = driver.find_element(By.ID, "last100Spins")
    divs_numeros = div_last100Spins.find_elements(By.XPATH, ".//*")
    numeros = ["Baixo" if float(x) < 2.00 else "Alto" for x in
               [div.get_attribute("textContent") for div in divs_numeros]]
    print(f"\nResultados : \n{numeros}")

    
    if all(x == "Baixo" for x in numeros[0:10]):
        print("Possivel Estrategia 1")
        msg = enviar_mensagem(token, chat_id, msg_possivel_entrada)
        # return msg

    elif all(x == "Baixo" for x in numeros[0:7]):
        print("Possivel Estrategia 2")
        msg = enviar_mensagem(token, chat_id, msg_possivel_entrada)

    elif all(x == "Baixo" for x in numeros[0:6]):
        print("Possivel Estrategia 3")
        msg = enviar_mensagem(token, chat_id, msg_possivel_entrada)
        # return msg




    if numeros[0] == "Alto" and all(x == "Baixo" for x in numeros[1:11]):
        print("Estrategia 1 Bateu")
        deletar_mensagem(msg)
        msg = enviar_mensagem(token, chat_id, msg_entrada)
        return msg

    elif numeros[0] == "Alto" and all(x == "Baixo" for x in numeros[1:8]):
        print("Estrategia 2 Bateu")
        deletar_mensagem(msg)
        msg = enviar_mensagem(token, chat_id, msg_entrada)
        return msg

    elif numeros[0] == "Alto" and all(x == "Baixo" for x in numeros[1:7]):
        print("Estrategia 3 Bateu")
        deletar_mensagem(msg)
        msg = enviar_mensagem(token, chat_id, msg_entrada)
        return msg


    if numeros[0] == "Alto" and numeros[1] == "Alto" and all(x == "Baixo" for x in numeros[2:12]):
        print("Green Estrategia 1")
        messageId = msg['message_id']
        bot.sendChatAction(chat_id, 'typing')
        bot.sendMessage(chat_id, '✅✅✅✅GREENNNN ✅✅✅✅✅✅✅', reply_to_message_id=messageId)
        jogo()


    elif numeros[0] == "Alto" and numeros[1] == "Alto" and all(x == "Baixo" for x in numeros[2:9]):
        print("Green Estrategia 2")
        messageId = msg['message_id']
        bot.sendChatAction(chat_id, 'typing')
        bot.sendMessage(chat_id, '✅✅✅✅GREENNNN ✅✅✅✅✅✅✅', reply_to_message_id=messageId)
        jogo()


    elif numeros[0] == "Alto" and numeros[1] == "Alto" and all(x == "Baixo" for x in numeros[2:8]):
        print("Green Estrategia 3")
        messageId = msg['message_id']
        bot.sendChatAction(chat_id, 'typing')
        bot.sendMessage(chat_id, '✅✅✅✅GREENNNN ✅✅✅✅✅✅✅', reply_to_message_id=messageId)
        jogo()



    if numeros[0] == "Baixo" and numeros[1] == "Alto" and all(x == "Baixo" for x in numeros[2:12]):
        print("Loss Estrategia 1")
        messageId = msg['message_id']
        bot.sendChatAction(chat_id, 'typing')
        bot.sendMessage(chat_id, '❌❌❌❌ LOSS ❌❌❌❌', reply_to_message_id=messageId)
        jogo()


    elif numeros[0] == "Baixo" and numeros[1] == "Alto" and all(x == "Baixo" for x in numeros[2:9]):
        print("Loss Estrategia 2")
        messageId = msg['message_id']
        bot.sendChatAction(chat_id, 'typing')
        bot.sendMessage(chat_id, '❌❌❌❌ LOSS ❌❌❌❌', reply_to_message_id=messageId)
        jogo()


    elif numeros[0] == "Baixo" and numeros[1] == "Alto" and all(x == "Baixo" for x in numeros[2:8]):
        print("Loss Estrategia 3")
        messageId = msg['message_id']
        bot.sendChatAction(chat_id, 'typing')
        bot.sendMessage(chat_id, '❌❌❌❌ LOSS ❌❌❌❌', reply_to_message_id=messageId)
        jogo()

  



if __name__ == '__main__':
    driver = initialize_chrome_browser()
    driver.get("https://www.br4bet.com/")
    sleep(5)
    termos =  driver.find_element(By.XPATH,'//*[@id="__layout"]/main/div[4]/div/div/div[2]/button[2]')
    termos.click()
    sleep(2)
    email = driver.find_element(By.XPATH,'//*[@id="navbarTogglerDemo02"]/div/div[1]/form/div[1]/div/div/input')
    email.click()
    mensagem = "sonymarle"
    email.send_keys(mensagem)
    sleep(2)
    senha = driver.find_element(By.XPATH,'//*[@id="navbarTogglerDemo02"]/div/div[1]/form/div[2]/div/div/input')
    senha.click()
    mensagem = "Ad000000"
    senha.send_keys(mensagem)
    sleep(2)
    entrar = driver.find_element(By.XPATH,'//*[@id="navbarTogglerDemo02"]/div/div[1]/form/div[3]/button')
    entrar.click()
    sleep(5)
    

    driver.get("https://www.br4bet.com/casino/?cat=live&gameid=5944")
    
    frame = driver.find_element(By.XPATH, '//*[@id="__layout"]/main/div[3]/div[1]/div/div[2]/div[3]/div/iframe')
    wait = WebDriverWait(driver, 30)
    wait.until(EC.frame_to_be_available_and_switch_to_it(frame))
    sleep(5)
    frame2 = driver.find_element(By.XPATH, '//*[@id="game-frame"]')
    wait = WebDriverWait(driver, 30)
    wait.until(EC.frame_to_be_available_and_switch_to_it(frame2))
    print("Tudo certo")
    sleep(5)
    while True:
        jogo()

   