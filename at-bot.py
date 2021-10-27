import selenium
import datetime
import time
import json
import os
import discord_webhook
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from discord_webhook import *

data = json.load(open("data.json"))

os.system('start chrome.exe -remote-debugging-port='+data["port"]+' --user-data-dir="C:\Selenium\AT BOT"')

# Debug Address
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:"+data["port"])
path = Service(data["path"])
driver = webdriver.Chrome(service = path, options = chrome_options)
driver.set_window_size(768, 768)
driver.set_window_position(0, 0)

# Header
print("""\033[92m
   █████╗ ████████╗    ██████╗  ██████╗ ████████╗
  ██╔══██╗╚══██╔══╝    ██╔══██╗██╔═══██╗╚══██╔══╝
  ███████║   ██║       ██████╔╝██║   ██║   ██║   
  ██╔══██║   ██║       ██╔══██╗██║   ██║   ██║   
  ██║  ██║   ██║       ██████╔╝╚██████╔╝   ██║   
  ╚═╝  ╚═╝   ╚═╝       ╚═════╝  ╚═════╝    ╚═╝   \033[33mV.1.4
\033[00m""", end="")
print("\033[92m─" * 56 +"\033[00m")
print("\n" + "PORT :", "\033[33m"+data["port"]+"\033[00m" + "\n")

# Login
driver.get(data["dashboard"])
driver.find_element(By.ID, "username").send_keys(data["username"])
driver.find_element(By.ID, "password").send_keys(data["password"], Keys.ENTER)

# Data
NIM = driver.find_element(By.ID, "fullName").get_attribute("value")
Name = driver.find_element(By.ID, "eMail").get_attribute("value").title()
Class = driver.find_element(By.ID, "addRess").get_attribute("value")
print("NIM      =", NIM)
print("Name     =", Name)
print("Class    =", Class)

# List Matkul
print("\nMatkul   :")
i = 0
for isi in data["matkul"]:
    i += 1
    print(i, isi)

# Pilih Matkul
pilih = int(input("\nPilih Matkul : "))
print("\033[33m─" * 56 + "\033[00m")

if pilih == 1:
    Matkul = data["matkul"][0]
    print(Matkul)
    driver.get(data["link"][0])
elif pilih == 2:
    Matkul = data["matkul"][1]
    print(Matkul)
    driver.get(data["link"][1])
elif pilih == 3:
    Matkul = data["matkul"][2]
    print(Matkul)
    driver.get(data["link"][2])
elif pilih == 4:
    Matkul = data["matkul"][3]
    print(Matkul)
    driver.get(data["link"][3])
elif pilih == 5:
    Matkul = data["matkul"][4]
    print(Matkul)
    driver.get(data["link"][4])
else:
    print("Pilih nomor yang benar!")
    exit()

# Refresh Page
while not driver.find_elements(By.XPATH, '//*[@class="btn btn-primary btn-rounded left"]'):
        dt = datetime.datetime.now()
        print(f"\r{dt.strftime('%A %d/%m/%Y %H:%M:%S')}", end="")
        driver.refresh()
        time.sleep(0.2)

# Absen
start_time = time.time()
driver.find_element(By.XPATH, '//*[@class="btn btn-primary btn-rounded left"]').click()
day = datetime.datetime.now()
print("\n" + NIM, "Absen at", day.strftime("%X"))

# Feedback
driver.find_element(By.XPATH, '//*[@class="form-control "]').send_keys(data["feedback"])

# Kirim Feedback
driver.find_element(By.XPATH, '//*[@class="btn btn-primary btn-rounded left mt-4"]').click()

# Timestamp
timestamp = time.time() - start_time
timeexecution = ("%.1f seconds" % (timestamp))
print("Time Execution =", timeexecution)
print("\033[33m─" * 56 + "\033[00m" + "\n")

# Webhook Discord
webhook = DiscordWebhook(url = data["webhook"], username = data["bot"])
embed = DiscordEmbed(color = 0x33FFFF)
embed.set_author(name = data["bot"], url = data["dashboard"], icon_url = data["icon"])
embed.add_embed_field(name = "NIM", value = NIM, inline = False)
embed.add_embed_field(name = "Name", value = Name, inline = False)
embed.add_embed_field(name = "Class", value = Class, inline = False)
embed.add_embed_field(name = "Matkul", value = Matkul, inline = False)
embed.add_embed_field(name = "Status", value = "☑️ Success", inline = True)
embed.add_embed_field(name = "Time", value = "🕖 "+day.strftime("%X"), inline = True)
embed.add_embed_field(name = "Execution", value = "⏱️ "+timeexecution, inline = True)
embed.set_footer(text = "✨ V.1.4 • Made with ☕ by Faiz")
embed.set_timestamp()
webhook.add_embed(embed)
webhook.execute()

# Loguot
driver.get(data["logout"])
