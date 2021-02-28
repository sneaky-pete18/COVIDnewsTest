from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
#working now - need to find out what to do about iterating numbers
driver = webdriver.Chrome(ChromeDriverManager().install()) 


#working but something is up with the If statement. Not returning correct results. 
i = 1
test = 0
checkStr= ["COVID", "COVID-19", "coronavirus"]
noResults= ["0"]
while i<1985:
    url = "https://duckduckgo.com/?q=" + str(i) +"+new+cases&t=h_&ia=web"
    print(url)
    
    driver.get("https://duckduckgo.com/?q=" + str(i) +"+new+cases&t=h_&ia=web")
    results=driver.find_element_by_id("links")
    searchresults = results.text
    print(searchresults)
    
    if any(x in searchresults for x in checkStr):
        #print("Found results in" +" " + str(i))
        test = test +1
        print("Total numbers with results=" + " " + str(test))
    else:
        noResults.append(str(i))
    
    i = i +1

    
print("Found no covid mentions in the following " + str(noResults))
##results=driver.find_element_by_id("links")
###print(results)
##description=[]
##
###for result in results:
##description.append(results.text)
##
##print(description)
##print(' ')


driver.quit()
