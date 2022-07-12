import http.client
import json
import yaml
import pandas as pd
connection = http.client.HTTPConnection('api.football-data.org')
headers = { 'X-Auth-Token': 'e0fb20bd96704f6ab405956361bed1ae' }
leagues = {1: 'PL', 2: 'SA', 3: 'BL1',4:'CL',5:'FL1',6:'PD'} 

def teams_info(league):

    connection.request('GET', '/v4/competitions/'+league+'/teams', None, headers )
    response1 = json.loads(connection.getresponse().read().decode()) 
    teams_names=dict()
    teams_address=dict()
    teams_ids=dict()
    for i in response1['teams']:
        teams_names[i['id']]=i['name']
        teams_address[i['id']]=i['address']
        teams_ids[i['name']]=i['id']
    return teams_names ,teams_address ,teams_ids
def result(team_id,datefrom,dateto):
    connection.request('GET', '/v4/teams/'+str(team_id)+'/matches?dateFrom='+datefrom+'&dateTo='+dateto, None, headers )
    team_results = json.loads(connection.getresponse().read().decode())
    return(team_results['resultSet'])
def MoneyLine(league,matchday):
    count=0
    HeadToHead=dict()
    odds=dict()
    connection.request('GET', '/v4/competitions/'+league+'/matches?matchday='+str(matchday), None, headers )
    response1 = json.loads(connection.getresponse().read().decode())
    for i in response1['matches']:
        count+=1
        #print(i['awayTeam']['name']+' away team'+' VS '+i['homeTeam']['name']+' home team')
        #print(yaml.dump(i['odds'], default_flow_style=False))
        HeadToHead[count]= [{'awayteam':i['awayTeam']['name']}, {'hometeam': i['homeTeam']['name']}]
        odds[count]=i['odds']
    return HeadToHead,odds  
#print(yaml.dump(leagues, default_flow_style=False))
#league_num=int(input('please select the number of the league = '))
#teams_names ,teams_address ,teams_ids=teams_info(leagues[league_num])
#command_num=int(input('for team info press 1 for matches in specific match day press 2 = '))
#if command_num==1:
#    print(yaml.dump(teams_names, default_flow_style=False))
#    team_num=int(input('please select the num of ur team = '))
#    datefrom='2022-01-01'
#    dateto='2022-06-06'
#    results=result(team_num,datefrom,dateto)
#    print(yaml.dump(results, default_flow_style=False))
#elif command_num==2:
#    MatchDay=int(input('Enter the match day = '))
#    HeadToHead,odds = MoneyLine(leagues[league_num],MatchDay) 
#else: print('please choose wisely')    
