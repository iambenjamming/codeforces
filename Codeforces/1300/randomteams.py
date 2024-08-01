players, teams = map(int, input().split())

if teams == 1:
    kmin = kmax = (players - 1) * players // 2
else:

    cluster = players - (teams - 1)
                        
    kmax = (cluster - 1) * cluster // 2

    #kmin
    base_size = players // teams

    extra_teams = players % teams
    
    extra_team_pairs = extra_teams * (base_size + 1) * base_size // 2

    base_team_pairs = (teams - extra_teams) * base_size * (base_size - 1) // 2
    
    kmin = extra_team_pairs + base_team_pairs

print(kmin, kmax)
