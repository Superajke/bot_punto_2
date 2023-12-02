import time  # Import the time library
from selenium import webdriver  # Import the webdriver library
from selenium.webdriver.common.by import By  # Import the By library
from selenium.webdriver.common.keys import Keys  # Import the Keys library
from selenium.webdriver.chrome.service import Service  # Import the Service library
from selenium.webdriver.support.ui import WebDriverWait  # Import the WebDriverWait library
from selenium.webdriver.support import expected_conditions as EC  # Import the expected_conditions library

# Set up the Chrome webdriver
service = Service("driver/chromedriver.exe")
bot = webdriver.Chrome(service=service)
bot.maximize_window()
bot.get("https://www.viajesexito.com")

# Navigate to the "Packages" section
packages = bot.find_element(By.XPATH, "/html/body/form/header/div[2]/div/div/nav/div[4]")
packages.click() # Click on the "Packages" section
time.sleep(1)

# Select the flight origin
fligh_origin = bot.find_element(By.XPATH, "/html/body/form/div[3]/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div/div/div[1]/div/div[1]/div/div/input")
fligh_origin.click() # Click on the flight origin
time.sleep(1) 

# Input the flight origin location
fligh_origin_input = bot.find_element(By.XPATH, "/html/body/form/div[3]/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[5]/div[2]/input")
fligh_origin_input.send_keys("Jose María Cordova") # Input the flight origin location
fligh_origin_input.send_keys(Keys.ENTER) # Accept the flight origin location

# Select the flight destination
flight_destination = bot.find_element(By.XPATH, "/html/body/form/div[3]/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div/div/div[1]/div/div[3]/div/div/input")
flight_destination.click() # Click on the flight destination
time.sleep(1)

# Input the flight destination location
flight_destination_input = bot.find_element(By.XPATH, "/html/body/form/div[3]/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[5]/div[2]/input")
flight_destination_input.send_keys("Punta Cana") # Input the flight destination location
flight_destination_input.send_keys(Keys.ENTER) # Accept the flight destination location
time.sleep(1)

# Select the flight date
flight_date = bot.find_element(By.XPATH, "/html/body/form/div[3]/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div/div/div[2]/div/input")
flight_date.click() # Click on the flight date
time.sleep(1)

# Input the flight date range
flight_date_input_start = bot.find_element(By.XPATH, "/html/body/div[11]/div[2]/div[2]/div[1]/div/div[2]/div/div/div/div[2]/div/div[1]/div/div[1]/div/div[2]/div/div[5]/div[2]/div[2]/div[1]")
flight_date_input_start.click() # Click on the start date
flight_date_input_end = bot.find_element(By.XPATH, "/html/body/div[11]/div[2]/div[2]/div[1]/div/div[2]/div/div/div/div[2]/div/div[1]/div/div[1]/div/div[2]/div/div[6]/div[5]/div[2]/div[1]")
flight_date_input_end.click() # Click on the end date
time.sleep(1)

# Accept the selected flight date
flight_date_accept = bot.find_element(By.XPATH, "/html/body/div[11]/div[2]/div[2]/div[2]/button[2]")
flight_date_accept.click() # Click on the accept button
time.sleep(1)

# Select flight information
flight_information = bot.find_element(By.XPATH, "/html/body/form/div[3]/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div/div/div[3]/div/div/div/div/p")
flight_information.click() # Click on the flight information
time.sleep(1)

# Add flight information
flight_information_add = bot.find_element(By.XPATH, "/html/body/form/div[3]/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[4]/div[2]/div[1]/button[1]")
flight_information_add.click() # Click on the add button
time.sleep(1)

# Accept flight information
flight_information_accept = bot.find_element(By.XPATH, "/html/body/form/div[3]/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[4]/div[2]/div[2]/button")
flight_information_accept.click() # Click on the accept button
time.sleep(1)

# Initiate flight search
flight_search = bot.find_element(By.XPATH, "/html/body/form/div[3]/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div/div/div[4]/a")
flight_search.click() # Click on the search button
time.sleep(1)

# Switch to the newly opened window
Emergent = bot.window_handles[1] # Get the new window
bot.switch_to.window(Emergent) # Switch to the new window

# The bot will wait 30 seconds for the page to load (adjust the time if necessary)
WebDriverWait(bot, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[1]/div/div/div[2]/div/div[1]/div/p[1]/span[2]'))) 

# Iterate over the first 10 package prices
for i in range(1, 11):
    xpath = f'/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[{i}]/div/div/div[2]/div/div[1]/div/p[1]/span[2]' # Se crea el XPATH para obtener el precio el cual se iterará en el div de los paquetes
    price = bot.find_element(By.XPATH, xpath) # Get the package price
    print("Packet "+str(i)+" price: "+price.text) # Print the package price
time.sleep(2)

# Access advanced options
advanced_options = bot.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[1]/div[1]/div/div[6]/a")
advanced_options.click() # Click on the advanced options button
time.sleep(1)

# Select airline
select_airline = bot.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[1]/div[1]/div/div[7]/div[2]/input")
select_airline.click() # Click on the airline input
select_airline.send_keys("Avianca") # Input the airline name
time.sleep(1)
select_airline.send_keys(Keys.ENTER) # Accept the airline name
time.sleep(1)

# Accept selected airline
select_airline_accept = bot.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[1]/div[1]/div/div[8]/input")
select_airline_accept.click() # Click on the accept button
time.sleep(1)

# The bot will wait 30 seconds for the page to load (adjust the time if necessary)
WebDriverWait(bot, 25).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[1]/div/div/div[2]/div/div[1]/div/p[1]/span[2]')))

# Access the "Contact Us" section
contact_us = bot.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[2]/div[5]/footer/div[2]/div/div/div[1]/div/p/a")
contact_us.click() # Click on the "Contact Us" section
time.sleep(5)

bot.quit() # the bot will close the browser window and end the program