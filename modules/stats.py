from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from enums import OPTIONS
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def get_stats(stat, year):

    stats = []

    for stat_name_item, stat_info in OPTIONS:
        if stat_info[0] == stat:
            value = stat_info[2]
            link = stat_info[1]

    # Create a Chromedriver
    options = Options()
    options.add_argument("--headless")
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_argument("--disable-logging")
    options.add_argument("--log-level=3")

    # Initialize the web driver
    driver = webdriver.Chrome(options)

    # Configures the URL with the team and year and adds "#passing::pass_int" to sort by interceptions
    url = f"https://www.pro-football-reference.com/years/{year}/{link}{stat}"
    
    # Loads the url
    driver.get(url)

    # Finds the table and extracts the data
    table = driver.find_element(By.CSS_SELECTOR, 'table')
    
    # Checks if the table exists
    if table:
        # Looks for all table row elements in the table
        rows = table.find_elements(By.TAG_NAME, 'tr')
        # Loop that iterates the first top 10 
        for row in rows[:10]:
            cells = row.find_elements(By.TAG_NAME, 'td')
            if len(cells) >= 3:
                player_name = cells[0].text
                stat_amount = cells[value].text
                
                data = {
                    'name': player_name,
                    'stat_amount': stat_amount,
                }
                stats.append(data)
    
    # Closes the web driver
    driver.quit()

    return stats

def main():
    statistic = input ("Enter Stat: ")
    year = input ("Enter Year: ")
    stats = get_stats(statistic, year)

    num = 1
    for stat in stats:
        name = stat['name']
        stat_amount = stat['stat_amount']
        print(str(num) + ". " + name + " - " + stat_amount)
        num += 1
    print ("\n" + "* - Pro Bowl\n+ - All Pro")

if __name__ == "__main__":
    main()