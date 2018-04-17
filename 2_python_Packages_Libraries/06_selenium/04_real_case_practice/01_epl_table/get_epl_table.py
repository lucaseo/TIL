from selenium import webdriver
import pandas as pd

def epl_table():
    driver = webdriver.Chrome()
    driver.get('https://www.premierleague.com/tables')
    driver.find_element_by_css_selector("#advertClose").click()

    table = driver.find_elements_by_css_selector("#mainContent .tableBodyContainer")[0]

    groups = []
    group_1 = table.find_elements_by_css_selector(".tableDark")[0]
    groups.append(group_1)

    for num in range(3, 41, 2):
        group_2 = table.find_elements_by_css_selector("tr:nth-child("+str(num)+")")[0]
        groups.append(group_2)

    epl_table = pd.DataFrame(columns=['Ranking', 'Club', 'Pl', 'W', 'D', 'L', 'GD', 'Pts'])

    for team in groups:
        ranking = team.find_element_by_css_selector(".value").text
        club = team.find_element_by_css_selector(".team > a").text
        play = team.find_element_by_css_selector("td:nth-child(4)").text
        win = team.find_element_by_css_selector("td:nth-child(5)").text
        draw = team.find_element_by_css_selector("td:nth-child(6)").text
        lose = team.find_element_by_css_selector("td:nth-child(7)").text
        goal = team.find_element_by_css_selector("td:nth-child(10)").text
        pts = team.find_element_by_css_selector(".points").text

        data = {"Ranking" : ranking,
                "Club" : club,
                "Pl" : play,
                "W" : win,
                "D" : draw,
                "L" : lose,
                "GD": goal,
                "Pts": pts}

        epl_table.loc[len(epl_table)] = data

    driver.close()

    epl_table.set_index('Ranking', inplace=True)
    epl_table.to_csv('epl_table')

    return "File generated !"

epl_table()

data = pd.read_csv("epl_table", index_col = 0)

print(data)
