import re

from selenium import webdriver

from Database import *
from Grades import Grades

option = webdriver.ChromeOptions()
option.add_argument('headless')
driver = webdriver.Chrome('chromedriver', options=option)


def login(url, name, password):
    driver.get(url)
    driver.find_element_by_id('username').send_keys(name)
    driver.find_element_by_id('password').send_keys(password)
    driver.find_element_by_name('submit').click()


def read_class_names(semester):
    class_table = driver.find_element_by_xpath("//*[@id='layout-c22a']/div[2]/table[2]")
    class_table_source = class_table.get_attribute('outerHTML')
    class_names = re.findall(r';" tabindex="0">(.+)(?<!</span>)</a>', class_table_source)
    for name in class_names:
        insert_class(name, semester)
    return class_names


def save_grades(class_names, names, grades):
    list = []
    pom = ()
    grade = {}
    j = 0
    for i in range(len(names)):
        if names[i] in class_names:
            grade = {}
            if pom:
                list.append(pom)
            pom = (names[i],)
            if (i < len(names) - 1) & (names[i + 1] in class_names):
                grade = {names[i]: grades[j]}
                pom += (grade,)
                j += 1
        else:
            pomka = ()
            if grades[j].startswith("(") & grades[j].endswith(")"):
                pomka += (grades[j],)
                j += 1
            pomka += (grades[j],)
            grade[names[i]] = pomka
            pom += (grade,)
            j += 1
    list.append(pom)
    print(list)
    return list


def save_to_dataset(list_of_grades):
    end_list = []
    for subject in list_of_grades:
        sub = Grades()
        sub.name = subject[0]
        sub_dict = subject[1]
        for key in sub_dict:
            if key == "WYK":
                g = ''
                for grade in sub_dict[key]:
                    g += str(grade)
                sub.WYK = g
            if key == "CW":
                g = ''
                for grade in sub_dict[key]:
                    g += str(grade)
                sub.CW = g
            if key == 'LAB':
                g = ''
                for grade in sub_dict[key]:
                    g += str(grade)
                sub.LAB = g
            if key == 'PP':
                g = ''
                for grade in sub_dict[key]:
                    g += str(grade)
                sub.PP = g
        end_list.append(sub)
        print(sub.name, sub.WYK, sub.CW, sub.LAB, sub.PP)

    for i in end_list:
        insert_grades(i)


def grades():
    driver.find_element_by_xpath("//*[@id='layout-c12-t']/div[2]/div/nav/ul/li[4]/a").click()
    driver.find_element_by_xpath("//*[@id='layout-c22a']/div/table/tbody/tr[3]/td[4]/a").click()
    my_list = driver.find_elements_by_xpath("//*[contains(text(),'szczegóły')]")
    class_names = []
    licznik = 1
    for i in range(len(my_list)):
        list1 = driver.find_elements_by_xpath("//*[contains(text(),'szczegóły')]")
        list1[i].click()
        class_names += read_class_names(licznik)
        licznik += 1
        driver.back()

    driver.back()
    driver.find_element_by_xpath("//*[@id='layout-c22a']/div/table/tbody/tr[2]/td[2]/a").click()
    table = driver.find_elements_by_xpath("//*[@id='layout-c22a']/div/table[3]/tbody")
    names = []
    grades = []
    for i in table:
        table_h = i.get_attribute("outerHTML")
        names += re.findall(r'tabindex="0">(.+)</a>', table_h)
        grades += ["".join(x) for x in re.findall(r'(?:\(brak ocen\)|(?:00;">(.+))|(?: ">(.+)))</span>', table_h)]
    grades = [x if x != '' else 'brak ocen' for x in grades]
    list_of_grades = save_grades(class_names, names, grades)
    save_to_dataset(list_of_grades)

    driver.close()
    driver.quit()


def to_account(url, name, password):
    login(url, name, password)
    grades()



