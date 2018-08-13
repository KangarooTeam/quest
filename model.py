from settings import Parameter

match = Parameter()
result = match.get_parameter()

def get_api(teams):
    stack = []
    cashe = {}
    result = []
    for team, goals in teams.items():
        stack.append(team.split("-"))
        stack.append(goals.split(":"))
        cashe[stack[0][0]] = stack[1][0]
        cashe[stack[0][1]] = stack[1][1]
        result.append(cashe)
        stack = []
        cashe = {}

    return result


team_api = get_api(result)