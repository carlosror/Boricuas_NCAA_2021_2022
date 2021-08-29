import pandas as pd
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.request import Request


ncaa_d1_colleges = pd.read_csv("NCAA_Division_1_volleyball_colleges_2021_2022.csv")
roster_links = ncaa_d1_colleges['Roster'].tolist()

# print(roster_links)

req = Request(roster_links[0], headers={'User-Agent': 'Mozilla/5.0'})    

html = urlopen(req).read().decode('utf-8')

PR_links = [] # list of lists
for link in roster_links:
  try:
    req = Request(link, headers={'User-Agent': 'Mozilla/5.0'})
    # https://stackoverflow.com/questions/2647723/urllib2-to-string
    # second answer
    html = urlopen(req).read().decode('utf-8')
  except Exception as e:
    print(link)
  else:
    if 'Puerto Rico' in html or 'P.R.' in html:
      location = roster_links.index(link)
      institution = ncaa_d1_colleges.iloc[location]['Institution']
      state = ncaa_d1_colleges.iloc[location]['State']
      program_link = ncaa_d1_colleges.iloc[location]['Link']
      conference = ncaa_d1_colleges.iloc[location]['Conference']
      division = 'NCAA DI'
      PR_link_list = [link, institution, state, program_link, conference, division]
      print(PR_link_list)
      PR_links.append(PR_link_list)

# print(PR_links)
# print(len(PR_links))

PR_links_df = pd.DataFrame(PR_links, columns = [ 'Roster', 'Institution', 'State', 'Institution_Link', 'Conference', 'Division'])
PR_links_df.to_csv('PR_links.csv', index = False)