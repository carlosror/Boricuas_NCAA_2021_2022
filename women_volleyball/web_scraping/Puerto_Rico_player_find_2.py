import pandas as pd
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.request import Request

df_dict = {'NCAA DI': 'NCAA_Division_1_volleyball_colleges_2021_2022.csv', 'NCAA DII': 'NCAA_Division_2_volleyball_colleges_2021_2022.csv', 
           'NCAA DIII': 'NCAA_Division_3_volleyball_colleges_2021_2022.csv', 'NAIA': 'NAIA_volleyball_colleges_2021_2022.csv', 
           'NJCAA DI': 'NJCAA_Division_1_volleyball_colleges_2021_2022.csv', 'NJCAA DII': 'NJCAA_Division_2_volleyball_colleges_2021_2022.csv'}
# df_dict = {'NJCAA DI': 'NJCAA_Division_1_volleyball_colleges_2021_2022.csv'}
for division in df_dict.keys():
  df_div = pd.read_csv(df_dict[division])
  roster_links = df_div['Roster'].tolist()
  
  PR_links = [] # list of lists
  Error_links = []
  for link in roster_links:
    try:
      req = Request(link, headers={'User-Agent': 'Mozilla/5.0'})
      # https://stackoverflow.com/questions/2647723/urllib2-to-string
      # second answer
      html = urlopen(req, timeout = 10).read().decode('utf-8')
    except Exception as e:
      print('** Error: ' + division + ': ' + link + '**')
      location = roster_links.index(link)
      institution = df_div.iloc[location]['Institution']
      program_link = df_div.iloc[location]['Link']
      Error_link_list = [division, institution, program_link]
      # print(PR_link_list)
      Error_links.append(Error_link_list)
    except timeout as e2: # The NAIA links keep timing out
      print('** Timed out: ' + division + ': ' + link + '**')
    else:
      if 'Puerto Rico' in html or 'P.R.' in html or ', PR' in html:
        location = roster_links.index(link)
        institution = df_div.iloc[location]['Institution']
        state = df_div.iloc[location]['State']
        program_link = df_div.iloc[location]['Link']
        if 'Conference' in df_div.columns:
          conference = df_div.iloc[location]['Conference']
        else:
          conference = df_div.iloc[location]['Region']
        PR_link_list = [link, institution, state, program_link, conference, division]
        # print(PR_link_list)
        PR_links.append(PR_link_list)
  PR_links_df = pd.DataFrame(PR_links, columns = [ 'Roster', 'Institution', 'State', 'Institution_Link', 'Conference', 'Division'])
  PR_links_df.to_csv(division.replace(' ', '_') + '_players_found_2021_2022.csv', index = False)
  
  Error_links_df = pd.DataFrame(Error_links, columns = [ 'Division', 'Institution', 'Institution_Link'])
  Error_links_df.to_csv(division.replace(' ', '_') + '_program_link_errors.csv', index = False)


