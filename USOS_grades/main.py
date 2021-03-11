import os

from selenium import webdriver
from Database import *
import re
option = webdriver.ChromeOptions()
option.add_argument('headless')
driver = webdriver.Chrome('chromedriver', options=option)

class Class_info():

    def __init__(self, info = null, gardes = null):
        self.info = info
        self.gardes = grades


def login():
    driver.get('https://logowanie.wat.edu.pl/cas/login?service=https%3A%2F%2Fusos.wat.edu.pl%2Fkontroler.php%3F_action%3Dlogowaniecas%2Findex&locale=pl')
    driver.find_element_by_id('username').send_keys('')
    driver.find_element_by_id('password').send_keys('')
    driver.find_element_by_name('submit').click()



def read_class_names(semester):
    class_table = driver.find_element_by_xpath("//*[@id='layout-c22a']/div[2]/table[2]")
    class_table_source = class_table.get_attribute('outerHTML')
    class_names = re.findall(r';" tabindex="0">(.+)(?<!</span>)</a>', class_table_source)
    for name in class_names:
        insert_class(name, semester)
    return class_names


def save_to_data(class_names, names, grades):
    list = []
    pom = ()
    j = 0
    for i in range(len(names)):
        if names[i] in class_names:
            if pom:
                list.append(pom)
            pom = (names[i], )
            if (i<len(names)-1) & (names[i+1] in class_names):
                grade = {names[i]: grades[j]}
                pom += (grade,)
                j += 1
        else:
            pomka = ()
            if grades[j].startswith("(") & grades[j].endswith(")"):
                pomka += (grades[j],)
                j+=1
            pomka+=(grades[j], )
            grade = {names[i]: pomka}
            pom+= (grade,)
            j+=1
    list.append(pom)
    print(list)


def grades():
    driver.find_element_by_xpath("//*[@id='layout-c12-t']/div[2]/div/nav/ul/li[4]/a").click()
    driver.find_element_by_xpath("//*[@id='layout-c22a']/div/table/tbody/tr[3]/td[4]/a").click()
    list = driver.find_elements_by_xpath("//*[contains(text(),'szczegóły')]")
    class_names = []
    licznik = 1
    for i in range(len(list)):
        list1 = driver.find_elements_by_xpath("//*[contains(text(),'szczegóły')]")
        list1[i].click()
        class_names += read_class_names(licznik)
        licznik+=1
        driver.back()

    driver.back()
    driver.find_element_by_xpath("//*[@id='layout-c22a']/div/table/tbody/tr[2]/td[2]/a").click()
    table = driver.find_elements_by_xpath("//*[@id='layout-c22a']/div/table[3]/tbody")
    names = []
    grades = []
    for i in table:
        table_h = i.get_attribute("outerHTML")
        names += re.findall(r'tabindex="0">(.+)</a>', table_h )
        grades += ["".join(x) for x in re.findall(r'(?:\(brak ocen\)|(?:00;">(.+))|(?: ">(.+)))</span>', table_h )]
    grades = [x if x !='' else 'brak ocen' for x in grades ]
    print(names)
    print(grades)
    print(class_names)
    save_to_data(class_names, names, grades)
    driver.close()
    driver.quit()


login()
grades()


