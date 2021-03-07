from selenium import webdriver
import re
option = webdriver.ChromeOptions()
#option.add_argument('headless')
driver = webdriver.Chrome('chromedriver', options=option)
def login():
    driver.get('https://logowanie.wat.edu.pl/cas/login?service=https%3A%2F%2Fusos.wat.edu.pl%2Fkontroler.php%3F_action%3Dlogowaniecas%2Findex&locale=pl')
    driver.find_element_by_id('username').send_keys('mail')
    driver.find_element_by_id('password').send_keys('haslo')
    driver.find_element_by_name('submit').click()



def read_class_names():
    class_table = driver.find_element_by_xpath("//*[@id='layout-c22a']/div[2]/table[2]")
    class_table_source = class_table.get_attribute('outerHTML')
    class_names = re.findall(r'tabindex="0"><span>(.+)</span></a>', class_table_source)
    print(class_names)



def grades():
    driver.find_element_by_xpath("//*[@id='layout-c12-t']/div[2]/div/nav/ul/li[4]/a").click()
    driver.find_element_by_xpath("//*[@id='layout-c22a']/div/table/tbody/tr[3]/td[4]/a").click()
    list = driver.find_elements_by_xpath("//*[contains(text(),'szczegóły')]")
    print(len(list))
    for i in range(len(list)):
        list1 = driver.find_elements_by_xpath("//*[contains(text(),'szczegóły')]")
        list1[i].click()
        read_class_names()
        driver.back()



    #do ocen
    # driver.find_element_by_xpath("//*[@id='layout-c22a']/div/table/tbody/tr[2]/td[2]/a").click()
    # grade_table = driver.find_element_by_xpath("//*[@id='layout-c22a']/div/table[3]")
    # grade_table_source = grade_table.get_attribute('outerHTML')

    #driver.close()
    # s = "abc123AUG|GAC|UGAasdfg789"
    # substring = re.findall("AUG(.*?)UGA", s)

login()
grades()


# class UsosBot:
#
#     def __init__(self, username, password):
#         self.driver = webdriver.Chrome()  #path to chromedriver
#         self.driver.get('https://usos.wat.edu.pl/kontroler.php?_action=home/index')
#         self.driver.find_element_by_xpath("//a[contains(text(), 'zaloguj się')]").click()
#         self.driver.find_element_by_xpath("//input[@name='username']").send_keys(username)
#         self.driver.find_element_by_xpath("//input[@name='password']").send_keys(password)
#         self.driver.find_element_by_xpath("//*[@id='fm1']/section[5]/input[4]").click()
#
#     def get_classes(self):
#         self.driver.find_element_by_xpath("//*[@id='layout-c12-t']/div[2]/div/nav/ul/li[4]/a").click() #'dla studentow' tab
#         self.driver.find_element_by_xpath("//*[@id='layout-c22a']/div/table/tbody/tr[2]/td[2]/a").click() #'oceny' tab
#         grades_box = self.driver.find_element_by_xpath("//*[@id='layout-c22a']/div/table[3]")
#         grades_box_source = grades_box.get_attribute("outerHTML")
#         class_names = re.findall(r'tabindex="0">(.+)</a>', grades_box_source)
#         grades = re.findall(r'(\(brak ocen\)|\d,\d|ZAL)</span>', grades_box_source)
#         return {class_name: grade for class_name, grade in zip(class_names, grades)}
#
#     def log_out(self):
#         self.driver.find_element_by_xpath("//a[contains(text(), 'wyloguj się')]").click()
#         self.driver.close()
#
#
# def average_grade(classes):
#     grades = [float(grade.replace(',', '.')) for grade in classes.values() if bool(re.fullmatch(r'\d,\d', grade))]
#     return sum(grades)/len(grades)
#
#
# index_number = 'weronika.gramacka@student.wat.edu.pl'
# password = 'Awima454545'
#
# my_bot = UsosBot(index_number, password)
# classes = my_bot.get_classes()
# my_bot.log_out()
# avg_grade = average_grade(classes)
#
# for class_name, grade in classes.items():
#     print(f'{class_name} : {grade}')
# print(f'average grade: {avg_grade}')
