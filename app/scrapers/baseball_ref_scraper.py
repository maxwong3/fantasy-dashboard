import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import requests

url = "https://www.baseball-reference.com/leagues/majors/2025-standard-batting.shtml"
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(url)

wait = WebDriverWait(driver, 15)
wait.until(EC.presence_of_element_located((By.ID, "players_standard_batting")))

html = driver.page_source

soup = BeautifulSoup(html, "html.parser")
table = soup.find('table', id='players_standard_batting')
tbody = table.find('tbody')

class Player:
    def __init__(self, name, age, team, league, war, games_played, pa, ab, r, h, doubles, triples, hr, rbi, sb, cs, bb, so, ba, obp, slg, ops, ops_plus, roba, rbat_plus, tb, gidp, hbp, sh, sf, ibb, pos, awards):
        self.name = name
        self.age = age
        self.team = team
        self.league = league
        self.war = war
        self.games_played = games_played
        self.pa = pa
        self.ab = ab
        self.r = r
        self.h = h
        self.doubles = doubles
        self.triples = triples
        self.hr = hr
        self.rbi = rbi
        self.sb = sb
        self.cs = cs
        self.bb = bb
        self.so = so
        self.ba = ba
        self.obp = obp
        self.slg = slg
        self.ops = ops
        self.ops_plus = ops_plus
        self.roba = roba
        self.rbat_plus = rbat_plus
        self.tb = tb
        self.gidp = gidp
        self.hbp = hbp
        self.sh = sh
        self.sf = sf
        self.ibb = ibb
        self.pos = pos
        self.awards = awards

def castint(string):
    try:
        return int(string)
    except:
        return 0
    
def castfloat(string):
    try:
        return float(string)
    except:
        return 0.0
    
players_df = pd.DataFrame(data=None, index=None, columns=['name','age','team','league','war','games_played','pa','ab','r','h','doubles','triples','hr','rbi','sb','cs','bb','so','ba','obp','slg','ops','ops_plus','roba','rbat_plus','tb','gidp','hbp','sh','sf','ibb','pos','awards'])

index = 0
for p in tbody.find_all('tr'):
    if p.get('class') == None or 'thead' not in p.get('class'):
        player_th = p.find('th')
        name_td = p.find('td', attrs={'data-stat':'name_display'})
        age_td = p.find('td', attrs={'data-stat':'age'})        
        team_td = p.find('td', attrs={'data-stat':'team_name_abbr'})
        league_td = p.find('td', attrs={'data-stat': 'comp_name_abbr'})
        war_td = p.find('td', attrs={'data-stat': 'b_war'})
        games_played_td = p.find('td', attrs={'data-stat': 'b_games'})
        pa_td = p.find('td', attrs={'data-stat': 'b_pa'})
        ab_td = p.find('td', attrs={'data-stat': 'b_ab'})
        r_td = p.find('td', attrs={'data-stat': 'b_r'})
        h_td = p.find('td', attrs={'data-stat': 'b_h'})
        doubles_td = p.find('td', attrs={'data-stat': 'b_doubles'})
        triples_td = p.find('td', attrs={'data-stat': 'b_triples'})
        hr_td = p.find('td', attrs={'data-stat': 'b_hr'})
        rbi_td = p.find('td', attrs={'data-stat': 'b_rbi'})
        sb_td = p.find('td', attrs={'data-stat': 'b_sb'})
        cs_td = p.find('td', attrs={'data-stat': 'b_cs'})
        bb_td = p.find('td', attrs={'data-stat': 'b_bb'})
        so_td = p.find('td', attrs={'data-stat': 'b_so'})
        ba_td = p.find('td', attrs={'data-stat': 'b_batting_avg'})
        obp_td = p.find('td', attrs={'data-stat': 'b_onbase_perc'})
        slg_td = p.find('td', attrs={'data-stat': 'b_slugging_perc'})
        ops_td = p.find('td', attrs={'data-stat': 'b_onbase_plus_slugging'})
        ops_plus_td = p.find('td', attrs={'data-stat': 'b_onbase_plus_slugging_plus'})
        roba_td = p.find('td', attrs={'data-stat': 'b_roba'})
        rbat_plus_td = p.find('td', attrs={'data-stat': 'b_rbat_plus'})
        tb_td = p.find('td', attrs={'data-stat': 'b_tb'})
        gidp_td = p.find('td', attrs={'data-stat': 'b_gidp'})
        hbp_td = p.find('td', attrs={'data-stat': 'b_hbp'})
        sh_td = p.find('td', attrs={'data-stat': 'b_sh'})
        sf_td = p.find('td', attrs={'data-stat': 'b_sf'})
        ibb_td = p.find('td', attrs={'data-stat': 'b_ibb'})
        pos_td = p.find('td', attrs={'data-stat': 'pos'})
        awards_td = p.find('td', attrs={'data-stat': 'awards'})

        # If there's no content for name, means the row doesn't contain player information so we will skip it
        if name_td.a is None:
            continue
        # rank information, same player may appear in multiple rows with same rank so we will avoid duplicates
        if int(player_th.get_text(strip=True)) == index:
            continue
            
        name = name_td.a.get_text(strip=True)
        age = castint(age_td.get_text(strip=True))
        team = team_td.get_text(strip=True)
        league = league_td.get_text(strip=True)
        war = castfloat(war_td.get_text(strip=True))
        games_played = castint(games_played_td.get_text(strip=True))
        pa = castint(pa_td.get_text(strip=True))
        ab = castint(ab_td.get_text(strip=True))
        r = castint(r_td.get_text(strip=True))
        h = castint(h_td.get_text(strip=True))
        doubles = castint(doubles_td.get_text(strip=True))
        triples = castint(triples_td.get_text(strip=True))
        hr = castint(hr_td.get_text(strip=True))
        rbi = castint(rbi_td.get_text(strip=True))
        sb = castint(sb_td.get_text(strip=True))
        cs = castint(cs_td.get_text(strip=True))
        bb = castint(bb_td.get_text(strip=True))
        so = castint(so_td.get_text(strip=True))
        ba = castfloat(ba_td.get_text(strip=True))
        obp = castfloat(obp_td.get_text(strip=True))
        slg = castfloat(slg_td.get_text(strip=True))
        ops = castfloat(ops_td.get_text(strip=True))
        ops_plus = castint(ops_plus_td.get_text(strip=True))
        roba = castfloat(roba_td.get_text(strip=True))
        rbat_plus = castint(rbat_plus_td.get_text(strip=True))
        tb = castint(tb_td.get_text(strip=True))
        gidp = castint(gidp_td.get_text(strip=True))
        hbp = castint(hbp_td.get_text(strip=True))
        sh = castint(sh_td.get_text(strip=True))
        sf = castint(sf_td.get_text(strip=True))
        ibb = castint(ibb_td.get_text(strip=True))
        pos = pos_td.get_text(strip=True)
        awards = awards_td.get_text(strip=True)
        
        players_df.loc[len(players_df)] = [name, age, team, league, war, games_played, pa, ab, r, h, doubles, triples, hr, rbi, sb, cs, bb, so, ba, obp, slg, ops, ops_plus, roba, rbat_plus, tb, gidp, hbp, sh, sf, ibb, pos, awards]
        index+=1
    else:
        continue
driver.quit()

players_table = players_df.to_html(index=False)