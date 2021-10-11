import selenium
import datetime
import time
import discord_webhook
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from discord_webhook import *

# chrome.exe -remote-debugging-port=8901 --user-data-dir="C:\Selenium\EVRDS-8901"

# Login

# Debug Address
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:8901")
path = r"C:\Users\ASUS\Desktop\Learning\Python-Language\AT-BOT\chromedriver.exe"
driver = webdriver.Chrome(path, options = chrome_options)

# AT BOT
print("\n" + "=" * 40)
print("AT BOT".center(40))
print("=" * 40)

# Dashboard
Dashboard   = "http://elearning.bsi.ac.id/user/dashboard"
driver.get(Dashboard)

# Data
NIM         = driver.find_element_by_id("fullName").get_attribute('value')
Name        = driver.find_element_by_id("eMail").get_attribute('value').title()
Class       = driver.find_element_by_id("addRess").get_attribute('value')
Url         = "https://discord.com/api/webhooks/895862701799120926/PIdi5Gc0GOFsD0wexJYShpfbcKsu1DM0MD-Dbcd7M7Q8xHlZpqMwYjHKEi3oLLHG222r"
Icon        = "https://cdn.discordapp.com/attachments/778645573498175538/895915601678200872/AT_BOT.gif"
Username    = "AT BOT"

print("NIM      =", NIM)
print("Name     =", Name)
print("Class    =", Class)

# List Matkul
print("\nMatkul   :")
matkul      = ["1. Entrepreneurship", "2. Dasar Pemrograman", "3. Logika & Algoritma", "4. Pengantar TIK", "5. Bahasa Inggris"]
for isi in matkul:
	print(isi)

# Link Matkul
Entrepreneurship    = "http://elearning.bsi.ac.id/absen-mhs/eyJpdiI6ImVOdjQvNE94OWl1dFF2eUtyVkcvcnc9PSIsInZhbHVlIjoiak9ob3pMUk52bExoa2dxTTV0L21DSUVISU5YbjRJVDVibXlzYTAraGRNdjZzMEdSVzRqZ0NVSlArZ2lLVURmbXlRM2czOW13MTNkSjY4SmxVK0Rpc3c9PSIsIm1hYyI6IjQwNjZmODliNDNhYzkyOWE4MjViNDcwYTQ0NmY0ZGUxYWU1OGVkOTEyMzExMGM5OWY3NTUyM2EwNTlmY2Y5YTkifQ=="
Dasar_Pemrograman   = "http://elearning.bsi.ac.id/absen-mhs/eyJpdiI6IkRkQlJGcTB0aHZjT1kxblRPL1c0Smc9PSIsInZhbHVlIjoiQ3RRS0U2TGtyQW9YVUNsVjVnY1NsQ2l1NnR1c2NwMWJBMkZhc0Y4T3gzRk14MTJpdUhFWWVjZ1FUQ1hNVmdpd2Nkc3JQQ2lYSmcwMzJ5cUZxVnJ6T1pST2FvVm5Ma2JialNyZ2p4djc4b009IiwibWFjIjoiNmJiNmViNjJmY2NiNWVmN2ZhYTNkNDRlMWY4ODM1NTVmNDUyMzIzYTgzMWJkOThkNDA3NTQyNGJjNGM1OGI5NCJ9"
Logika_Algoritma    = "http://elearning.bsi.ac.id/absen-mhs/eyJpdiI6IkV6WkRjSnpIaVkxV08rbzRZdVFTMkE9PSIsInZhbHVlIjoiNlNVZDg0Q1lpMkk1SFlkclo4Zjlrc0ZFcXRaREhLdmZmRjdaSGp1dmNnMi9pYzNGanBObU1aeVRXQjlwNTZ6akJaTlZsb0Y4MVJOSExTVXY1WnA5Snc9PSIsIm1hYyI6ImQ3Nzg5MWE3NGNjYmZlODAzMDRjMzUwZDgzNDI5MTA1ZmNlM2VlZmIxNzc3N2FlZTQ2NWU4MTdlNjc5NGExYTYifQ=="
Pengantar_TIK       = "http://elearning.bsi.ac.id/absen-mhs/eyJpdiI6InN4c2tNMXkrMmtUMlBLcjJUSEhiWXc9PSIsInZhbHVlIjoiNlNEZkFkclVSdUVyR2RwaXp6N0VUUXR0V09aZmFhTUJPT1lFLzlCUlhYc0ZzZGpITStQY1hJZUprTXZLOWxrd0o4RURTZWEwcjFFVFhNZ0VkQUx2UFVHTiswNVlNYVNtTHozZVBoL2hGVGg2VGFuL3JxT2kyTDdNdzhzTFBXQU0iLCJtYWMiOiI0NmM1OTVlOGQ2YzVmNzdkNjM3MmU1Y2VlZTVmMmY4NDMwMTk1NTYwOTNmNTBiNmU4YTc4NDE2OGM3YmNlNDU5In0="
Bahasa_Inggris      = "http://elearning.bsi.ac.id/absen-mhs/eyJpdiI6Imtnazk2eGx2Tkdvc240ZjVDUEtROXc9PSIsInZhbHVlIjoiSXBkKzB5Yk44a1J5bllqaXdaMzlpV1UrMUI1VS9WejV2eWFSYzdYL2FOM0xneDY3bkhtTEE3NG9zVTdQbTNoV3JqYTFIaWpUckFYZ0QyMUU0Z2lsRkE9PSIsIm1hYyI6IjYyZmMwOTcwYzllZTk1NzUzZjUyM2Y0OWYyZjU0YmNjNmZhNjg3Y2JhZmFkMjUwMjE0OTkxNWU1ZTlhM2ZiNDMifQ=="

# Pilih Matkul
pilih = int(input("\nPilih Matkul : "))

if pilih == 1:
    Matkul = "Entrepreneurship"
    print(Matkul)
    driver.get(Entrepreneurship)
elif pilih == 2:
    Matkul = "Dasar Pemrograman"
    print(Matkul)
    driver.get(Dasar_Pemrograman)
elif pilih == 3:
    Matkul = "Logika & Algoritma"
    print(Matkul)
    driver.get(Logika_Algoritma)
elif pilih == 4:
    Matkul = "Pengantar TIK"
    print(Matkul)
    driver.get(Pengantar_TIK)
elif pilih == 5:
    Matkul = "Bahasa Inggris"
    print(Matkul)
    driver.get(Bahasa_Inggris)
else:
    print("Pilih nomor yang benar !")
    exit()

# Refresh Page
while not driver.find_elements_by_xpath('//*[@class="btn btn-primary btn-rounded left"]'):
        dt = datetime.datetime.now()
        print(f"\r{dt.strftime('%A %d/%m/%Y %H:%M:%S')}", end=" ")
        driver.refresh()
        time.sleep(0.2) #0.3

# Absen
start_time = time.time()
absen = driver.find_element_by_xpath('//*[@class="btn btn-primary btn-rounded left"]')
absen.click()
day = datetime.datetime.now()
print("\n" + "-" * 40)
print(NIM, "Absen at", day.strftime("%X"))

# Feedback
feedback = driver.find_element_by_xpath('//*[@class="form-control "]')
feedback.send_keys("Pengajaran Sesuai")

# Kirim Feedback
kirim = driver.find_element_by_xpath('//*[@class="btn btn-primary btn-rounded left mt-4"]')
kirim.click()

# Timestamp
timestamp = time.time() - start_time
timeexecution = ("%.1f Second" % (timestamp))
print("Time Execution = " ,timeexecution)
print("-" * 40 + "\n")

# Webhook Discord
webhook = DiscordWebhook(url=Url, username=Username)
embed = DiscordEmbed(color = 0x33FFFF)
embed.set_author(name=Username, url=Dashboard, icon_url=Icon)
embed.add_embed_field(name="NIM", value=NIM, inline=False)
embed.add_embed_field(name="Name", value=Name, inline=False)
embed.add_embed_field(name="Class", value=Class, inline=False)
embed.add_embed_field(name="Matkul", value=Matkul, inline=False)
embed.add_embed_field(name="Status", value="☑️ Success", inline=True)
embed.add_embed_field(name="Time", value="🕖 "+day.strftime("%X"), inline=True)
embed.add_embed_field(name="Execution", value="⏱️ "+timeexecution, inline=True)
embed.set_footer(text="✨ V.1.3 • Made with ☕ by Faiz")
embed.set_timestamp()

webhook.add_embed(embed)
webhook.execute()
