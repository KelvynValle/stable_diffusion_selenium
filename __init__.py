"""A module destinated to get images from stable diffusion using selenium"""
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import time
import base64
import constants

class stable_diffusion_downloader:
    def __init__(self, driver):
        self.browser = self.__get_driver(driver)
        self.__load_page(constants.URL)

    #get the driver of browser
    def __get_driver(self, driver):
        if driver == constants.drivers.FIREFOX:
            options = Options()
            options.binary_location = constants.FIREFOX_LOCATION
            return webdriver.Firefox(options=options, executable_path=constants.GECKO_PATH)
    #load the stable diffusion page    
    def __load_page(self, url):
        self.browser.get(constants.URL)
        ended = False
        self.browser.execute_script("window.scrollTo(0, 100)") 
        while not ended:
            try:
                self.browser.find_element_by_xpath(constants.TRY).click()#self.browser.find_element_by_xpath(constants.PROMPT_INPUT_ONE) if switcher else self.browser.find_element_by_xpath(constants.PROMPT_INPUT_TWO)#.send_keys(prompt)
                ended = True
            except Exception as ex:
                time.sleep(0.5)
    #write request in the prompt
    def __prompt(self, prompt):
        ended = False
        self.browser.switch_to.frame(frame_reference = self.browser.find_element_by_xpath(constants.IFRAME))
        while not ended:
            try:
                prompt_field = self.browser.find_element_by_xpath(constants.PROMPT)#self.browser.find_element_by_xpath(constants.PROMPT_INPUT_ONE) if switcher else self.browser.find_element_by_xpath(constants.PROMPT_INPUT_TWO)#.send_keys(prompt)
                ended = True
            except Exception as ex:
                time.sleep(0.5)

        prompt_field.send_keys(prompt)
        ended = False
        current_component = False
        while not ended:
            try:
                current_component = not current_component
                self.browser.find_element_by_id("component-9" if current_component else "component-6").click()
                ended = True
                
            except Exception as ex:
                time.sleep(0.5)
    #extract result images
    def __extract_images(self, path):
        ended = False
        while not ended:
            try:
                self.browser.find_element_by_xpath(constants.FIRST_IMG).click()#self.browser.find_element_by_xpath(constants.PROMPT_INPUT_ONE) if switcher else self.browser.find_element_by_xpath(constants.PROMPT_INPUT_TWO)#.send_keys(prompt)
                ended = True
            except Exception as ex:
                time.sleep(0.5)
        img = self.browser.find_element_by_xpath(constants.FIRST_IMG)
        src = img.get_attribute('src')
        imgdata = base64.b64decode(src.replace("data:image/jpeg;base64,", ""), validate=True)
        with open(path, "wb") as fh:
           fh.write(imgdata)
    #get images from input and save in the path
    def get_images(self, prompt, path):
        self.__prompt(prompt)
        self.__extract_images(path)

std = stable_diffusion_downloader(constants.drivers.FIREFOX)
std.get_images("zabumbas from black sea", r"C:\Users\kelvy\Desktop\stable diffusion selenium\stable_diffusion_selenium\img.jpg")