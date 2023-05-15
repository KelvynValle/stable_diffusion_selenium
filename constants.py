from enum import Enum
#URLs
URL = "https://stablediffusionweb.com/"
#PATHS
GECKO_PATH = r"C:\Users\kelvy\Desktop\bot_youtube\gecko\geckodriver.exe"
FIREFOX_LOCATION = r"C:\Program Files\Mozilla Firefox\firefox.exe"
#XPATHS
PROMPT = "//input[@placeholder='Enter your prompt']"
BUTTON_INPUT = "/html/body/gradio-app/div/div[2]/div/div/div[2]/div[1]/div/button"                    
FIRST_IMG = "//*[@id='gallery']/div[2]/div/button[1]/img"
IFRAME = "//iframe[@id='inneriframe']"
TRY = "/html/body/div/main/div[1]/div[1]/a[1]"
#ENUM
drivers = Enum("drivers", ["FIREFOX"])