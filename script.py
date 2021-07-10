from selenium import webdriver
from read_excel import read_excel, write_excel
import pandas as pd
# from selenium.webdriver.common.keys import Keys

values = read_excel()
driver = webdriver.Chrome('C:\webdrivers\chromedriver.exe')
url = 'https://buofc.inhawk.com/examresults/'
driver.get(url)

def send_data():
    for regno in values:
        input = driver.find_element_by_xpath('//*[@id="ContentPlaceHolder1_txtSearch"]')
        checkResultBtn = driver.find_element_by_xpath('//*[@id="ContentPlaceHolder1_btnSearch"]')
        input.send_keys(regno)
        checkResultBtn.click()
        std_marks = []

        for i in range(2, 18):
            std_marks.append(driver.find_element_by_xpath(f'//*[@id="ContentPlaceHolder1_grdexamresults"]/tbody/tr[{i}]/td[5]').text)

        dict1 = {
            'regno': regno,
            'std_marks': std_marks,
        }
        marks_list.append(dict1)
        clearResultBtn = driver.find_element_by_xpath('//*[@id="ContentPlaceHolder1_btnclear"]')
        
        clearResultBtn.click()

# df = pd.DataFrame(marks_list)

if __name__ == '__main__':   
    marks_list = []
    send_data()
    write_excel(marks_list)
    pass 
