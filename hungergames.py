from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


class SetUpTheGame(object):

    def __init__(self):
        self.path = '/Users/avigranoff/Desktop/chromedriver'
        self.driver = webdriver.Chrome(self.path)
        self.unknown = '//*[@id="gender"]/option[2]'
        self.male = '//*[@id="gender"]/option[3]'
        self.female = '//*[@id="gender"]/option[1]'

    def set_it_up(self):

        self.driver.get('https://brantsteele.net/hungergames/disclaimer.php')
        simulate_button = self.driver.find_element_by_link_text('Simulate')
        simulate_button.click()

        agree_to_the_terms = self.driver.find_element_by_link_text\
            ('I am 13 years or older. I have read and understand these terms.')
        agree_to_the_terms.click()

        self.driver.get('https://brantsteele.net/hungergames/personal.php')

    def name_it(self, season_name):

        title = self.driver.find_element_by_xpath\
            ("//*[@id=\"content\"]/form/table[1]/tbody/tr[1]/td[2]/input")
        title.send_keys(season_name)
        pic = Select(self.driver.find_element_by_xpath("//*[@id=\"logo\"]"))
        pic.select_by_visible_text("Standard")

    def fill_in_names(self, name_and_gender: tuple):

        attempt = 1
        for x in range(len(name_and_gender)):
            if attempt < 10:
                caller = 'cusTribute0' + str(attempt)
                caldsex = 'cusTribute0' + str(attempt) + 'gender'
            elif 10 <= attempt:
                caller = 'cusTribute' + str(attempt)
                caldsex = 'cusTribute' + str(attempt) + 'gender'

            a = name_and_gender[0]
            person, sex = a

            name = self.driver.find_element_by_id(caller)
            name.send_keys(person)
            gender = Select(self.driver.find_element_by_name(caldsex))
            gender.select_by_visible_text(sex)

            name_and_gender = name_and_gender[1:]
            attempt += 1

    def set_the_rest_up(self):
        turn_pic_off = self.driver.find_element_by_xpath\
            ("//*[@id=\"content\"]/form/input[5]")
        turn_pic_off.click()
        turn_nicknames_off = self.driver.find_element_by_xpath\
            ('//*[@id="content"]/form/input[4]')
        turn_nicknames_off.click()

    def start(self):
        start = self.driver.find_element_by_xpath\
            ("//*[@id=\"content\"]/form/input[7]")
        start.click()

    def starter(self):

        try:
            begin = self.driver.find_element_by_xpath\
                ("//*[@id=\"content\"]/a[3]")
            begin.click()
        except:
            self.regular()

    def regular(self):

        try:
            the_use = self.driver.find_element_by_xpath\
                ("/html/body/div/div[5]/div[4]/a")
            if the_use.text == "Proceed.":
                the_use.click()
            else:
                self.tribute()
        except:
            self.tribute()

    def tribute(self):

        try:
            for i in range(2):
                go_there = self.driver.find_element_by_xpath\
                    ("/html/body/div/div[5]/div[4]/a[1]")
                go_there.click()

            self.moveit()

        except:
            pass

    def moveit(self):

        oof = tribt = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            "/html/body/div/div[5]/div[4]/a[2]")))
        tribt.click()


if __name__ == '__main__':

    people = ()
    district = 1
    for i in range(12):
        male = input("Participant A from district {}:   ".format(district))
        sexa = input("Gender of Participant A:   ").upper()
        female = input("Particiapant 2 from district {}:   ".format(district))
        sexb = input("Gender of Participant B:   ").upper()
        add_a = (male, sexa)
        add_b = (female, sexb)
        people += add_a, add_b
        district += 1

    name = input("Enter the name of your game (no symbols and two words):   ")
    game1 = SetUpTheGame()
    game1.set_it_up()
    game1.name_it(name)
    game1.fill_in_names(people)
    game1.set_the_rest_up()
    game1.start()
    for i in range(15):
        game1.starter()

    toit = input("Y to go \n N to stop ").upper()
    while toit != "QUIT":
        if toit == "Y":
            game1.starter()
        else:
            break
        toit = input("Y to go \n N to stop ").upper()
