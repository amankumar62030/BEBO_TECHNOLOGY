# A.contains().................................................

# 1.find element whose id contains the word "user"
driver.find_element(By.XPATH, "//*[contains(@id,'user']")

# 02.Locate the button whose class contains "submit-bin"
driver.find_element(By.XPATH, "//button[contains(@class,'submit-bin']")

# 03.Find a paragraph(<p>) with text containing "Welcome"
driver.find_element(By.XPATH, "//p[contains(text(),'Welcome']")


# B.text()-------------------------------------------------------------
# 01.locate th elink with exact text "About Us"
driver.find_element(By.XPATH, "//a[text(),'About Us']")

# 02.Find a span with text with exactly "Submit-form
driver.find_element(By.XPATH,"//span[text(),'Submit-Form']")




#C.starts-with()------------------------------------------------------------
# 01.Locate an input field whose name starts with "user"
driver.find_elements(By.XPATH,"//input[starts-with(@name,'User')]")