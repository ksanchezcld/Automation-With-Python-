from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')
messageField = driver.find_element_by_xpath('//*[@id="user-message"]')
messageField.send_keys('<script>alert(1)</script')
showMessageButton = driver.find_element_by_xpath('//*[@id="get-input"]/button')
showMessageButton.click()
additionField1 = driver.find_element_by_xpath('//*[@id="sum1"]')
additionField1.send_keys('10\'1 or 1=1 --+')
additionField2 = driver.find_element_by_xpath('//*[@id="sum2"]')
additionField2.send_keys("10'order+by+10--+")
getTotalButton = driver.find_element_by_xpath('//*[@id="gettotal"]/button')
getTotalButton.click()



#EXECUTE :: python2.7 webBrowse.py 

#Version #2 :: Que cargue un diccionario de Payloads