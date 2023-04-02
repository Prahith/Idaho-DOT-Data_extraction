from selenium import webdriver
import time
import pandas as pd
driver=webdriver.Chrome()
ans=[]
driver.get('https://qcpi.questcdn.com/cdn/posting/?group=1950787&provider=1950787')
time.sleep(2)

ans=[]

clic=driver.find_element('xpath','//*[@id="table_id"]/tbody/tr[1]/td[2]/a').click()
time.sleep(1)
close_date=driver.find_element('xpath','//*[@id="current_project"]/div/div[2]/div/table/tbody/tr[1]/td[2]').text
est_value_notes=driver.find_element('xpath','//*[@id="current_project"]/div/div[2]/div/table/tbody/tr[3]/td[2]').text
description=driver.find_element('xpath','//*[@id="current_project"]/div/div[3]/div/table/tbody/tr[3]/td[2]').text
ans.append([close_date,est_value_notes,description])
i=1
while i<=9:
    clic=driver.find_element('xpath','//*[@id="id_prevnext_next"]/b').click()
    time.sleep(0.5)
    close_date=driver.find_element('xpath','//*[@id="current_project"]/div/div[2]/div/table/tbody/tr[1]/td[2]').text
    est_value_notes=driver.find_element('xpath','//*[@id="current_project"]/div/div[2]/div/table/tbody/tr[3]/td[2]').text
    description=driver.find_element('xpath','//*[@id="current_project"]/div/div[3]/div/table/tbody/tr[3]/td[2]').text
    ans.append([close_date,est_value_notes,description])
    i+=1

attributes=['Closing Date','Estimated Value Notes','Description']
df = pd.DataFrame(ans, columns =attributes)
df.to_csv('Idaho projects.csv',index=False)
new_df = pd.read_csv('Idaho projects.csv')
print(new_df)