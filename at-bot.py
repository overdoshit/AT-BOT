import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains 
import datetime
import time
import schedule
# chrome.exe -remote-debugging-port=8901 --user-data-dir="C:\Selenium\EVRDS-8901"

# Debug Address
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:8901")
driver = webdriver.Chrome(options=chrome_options)

# Dashboard
Dashboard = "http://elearning.bsi.ac.id/user/dashboard"
driver.get(Dashboard)

# List Matkul
matkul = ["1. Entrepreneurship", "2. Dasar Pemrograman", "3. Logika & Algoritma", "4. Pengantar TIK", "5. Bahasa Inggris"]
for isi in matkul:
	print(isi)

# Link Matkul
Entrepreneurship = "http://elearning.bsi.ac.id/absen-mhs/eyJpdiI6ImVOdjQvNE94OWl1dFF2eUtyVkcvcnc9PSIsInZhbHVlIjoiak9ob3pMUk52bExoa2dxTTV0L21DSUVISU5YbjRJVDVibXlzYTAraGRNdjZzMEdSVzRqZ0NVSlArZ2lLVURmbXlRM2czOW13MTNkSjY4SmxVK0Rpc3c9PSIsIm1hYyI6IjQwNjZmODliNDNhYzkyOWE4MjViNDcwYTQ0NmY0ZGUxYWU1OGVkOTEyMzExMGM5OWY3NTUyM2EwNTlmY2Y5YTkifQ=="
Dasar_Pemrograman = "http://elearning.bsi.ac.id/absen-mhs/eyJpdiI6IkRkQlJGcTB0aHZjT1kxblRPL1c0Smc9PSIsInZhbHVlIjoiQ3RRS0U2TGtyQW9YVUNsVjVnY1NsQ2l1NnR1c2NwMWJBMkZhc0Y4T3gzRk14MTJpdUhFWWVjZ1FUQ1hNVmdpd2Nkc3JQQ2lYSmcwMzJ5cUZxVnJ6T1pST2FvVm5Ma2JialNyZ2p4djc4b009IiwibWFjIjoiNmJiNmViNjJmY2NiNWVmN2ZhYTNkNDRlMWY4ODM1NTVmNDUyMzIzYTgzMWJkOThkNDA3NTQyNGJjNGM1OGI5NCJ9"
Logika_Algoritma = "http://elearning.bsi.ac.id/absen-mhs/eyJpdiI6IkV6WkRjSnpIaVkxV08rbzRZdVFTMkE9PSIsInZhbHVlIjoiNlNVZDg0Q1lpMkk1SFlkclo4Zjlrc0ZFcXRaREhLdmZmRjdaSGp1dmNnMi9pYzNGanBObU1aeVRXQjlwNTZ6akJaTlZsb0Y4MVJOSExTVXY1WnA5Snc9PSIsIm1hYyI6ImQ3Nzg5MWE3NGNjYmZlODAzMDRjMzUwZDgzNDI5MTA1ZmNlM2VlZmIxNzc3N2FlZTQ2NWU4MTdlNjc5NGExYTYifQ=="
Pengantar_TIK = "http://elearning.bsi.ac.id/absen-mhs/eyJpdiI6InN4c2tNMXkrMmtUMlBLcjJUSEhiWXc9PSIsInZhbHVlIjoiNlNEZkFkclVSdUVyR2RwaXp6N0VUUXR0V09aZmFhTUJPT1lFLzlCUlhYc0ZzZGpITStQY1hJZUprTXZLOWxrd0o4RURTZWEwcjFFVFhNZ0VkQUx2UFVHTiswNVlNYVNtTHozZVBoL2hGVGg2VGFuL3JxT2kyTDdNdzhzTFBXQU0iLCJtYWMiOiI0NmM1OTVlOGQ2YzVmNzdkNjM3MmU1Y2VlZTVmMmY4NDMwMTk1NTYwOTNmNTBiNmU4YTc4NDE2OGM3YmNlNDU5In0="
Bahasa_Inggris = "http://elearning.bsi.ac.id/absen-mhs/eyJpdiI6Imtnazk2eGx2Tkdvc240ZjVDUEtROXc9PSIsInZhbHVlIjoiSXBkKzB5Yk44a1J5bllqaXdaMzlpV1UrMUI1VS9WejV2eWFSYzdYL2FOM0xneDY3bkhtTEE3NG9zVTdQbTNoV3JqYTFIaWpUckFYZ0QyMUU0Z2lsRkE9PSIsIm1hYyI6IjYyZmMwOTcwYzllZTk1NzUzZjUyM2Y0OWYyZjU0YmNjNmZhNjg3Y2JhZmFkMjUwMjE0OTkxNWU1ZTlhM2ZiNDMifQ=="

# Pilih Matkul
pilih = int(input("\nPilih Matkul : "))

if pilih == 1:
    print("Entrepreneurship")
    driver.get(Entrepreneurship)
elif pilih == 2:
    print("Dasar Pemrograman")
    driver.get(Dasar_Pemrograman)
elif pilih == 3:
    print("Logika & Algoritma")
    driver.get(Logika_Algoritma)
elif pilih == 4:
    print("Pengantar TIK")
    driver.get(Pengantar_TIK)
elif pilih == 5:
    print("Bahasa Inggris")
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
print("\n" + "-" * 30)
print("17210757 Absen at", day.strftime("%X"))

# Feedback
feedback = driver.find_element_by_xpath('//*[@class="form-control "]')
feedback.send_keys("Pengajaran Sesuai")

# Kirim Feedback
kirim = driver.find_elements_by_xpath('//*[@class="btn btn-primary btn-rounded left mt-4"]')
kirim.click()

# Timestamp
timestamp = time.time() - start_time
print("Time Execution = %.2f Second" % (timestamp))
print("-" * 30)