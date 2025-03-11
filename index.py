from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

def google_search():
    # Définir les options du navigateur avec un User-Agent
    options = Options()
    # options.add_argument("--headless")  # Exécuter en mode sans tête (optionnel)
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
    
    # Initialiser le navigateur avec les options
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.lagastronomiepizza.com/menu.html")
    
    # Trouver la barre de recherche et entrer la requête
    menu = driver.find_element(By.CSS_SELECTOR,'body > section > div > div.row.justify-content-center.mb-5.pb-3.mt-5.pt-5 > div > h2').text
    description = driver.find_element(By.CSS_SELECTOR,"body > section > div > div.row.justify-content-center.mb-5.pb-3.mt-5.pt-5 > div > p.mt-5").text
    # print('menu gastro',menu,'description',description)

    carte = driver.find_elements(By.CSS_SELECTOR,'div.col-md-6 > div.pricing-entry.d-flex.ftco-animate.fadeInUp.ftco-animated')

    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "example-id"))
    )   
    
    for item in carte:
        h3 =item.find_element(By.CSS_SELECTOR,'h3').text
        span=item.find_element(By.CSS_SELECTOR,'span.price').text
        print(h3,".....",span,"")
   
    # search_box = driver.find_element(By.NAME, "q")
    # search_box.send_keys(' jesosy ')
    # search_box.send_keys(Keys.RETURN)
    
    # # Attendre que les résultats chargent
    # time.sleep(2)
    
    # # Récupérer les titres des premiers résultats de recherche
    # results = driver.find_elements(By.CSS_SELECTOR, "h1")
    # for index, result in enumerate(results[:10]):
    #     print(f"{index + 1}. {result.text}")
    
    
    time.sleep(1000)

    # Fermer le navigateur
    driver.quit()

if __name__ == "__main__":
    google_search()