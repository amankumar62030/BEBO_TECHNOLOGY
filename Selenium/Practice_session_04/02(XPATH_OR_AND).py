#01.locate an input field with either id="email" or name="userEmail"
driver.find_elements(By.XPATH, "//input[@id='email' or @name='userEmail']")

# 02.Find a button with both types="submit" AND class="btn-primary"
driver.find_elements(By.XPATH, "//button[@types='submit' and @class='btn-primary']")

# 03.Locate the link with href="/home" OR text containing "Home"
driver.find_elements(By.XPATH, "//a[@href='/home' or contains(text(),'Home']")


