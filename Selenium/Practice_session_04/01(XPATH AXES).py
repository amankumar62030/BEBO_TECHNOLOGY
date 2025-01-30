# 01.XPATH AXES
# 1.Locate the parent of an input field with id="username"
driver.find_elements(By.XPATH,"//input[@id='username']/parent::*")

# 2.Identify all childs elements of a div with class container.
driver.find_elements(By.XPATH,"//div[@class='container']/child::*")

# 3.Find all descendants of a section with id="main-content"
driver.find_elements(By.XPATH,"//section[@id='main-content']/descendant::*")

# 4.Locate the following sibiling of a button with id="submit"
driver.find_elements(By.XPATH,"//button[@id='submit']/following-sibling::*")

# 5.Find the preceding sibling of a label with for="email"
driver.find_elements(By.XPATH,"//label[@id='email']/following-sibling::*")

