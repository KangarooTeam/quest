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


post_api = get_api(result)
def add_api(team_api):
    stack = 0
    cashe = str()
    new_api = {}
    for id, name in enumerate(team_api[0]):
        goal = int(team_api[0][name])
        if id % 2 == 0 or id == 0:
            stack = int(goal)
            cashe = name
        else:
            if stack > goal:
                new_api[name] = [goal, "L", 0]
                new_api[cashe] = [stack, "W", 3]
            elif goal > stack:
                new_api[name] = [goal, "W", 3]
                new_api[cashe] = [stack, "L", 0]
            else:
                new_api[name] = [goal, "D", 1]
                new_api[cashe] = [stack, "D", 1]
        stack = 0
        cashe = str()
    return new_api

print(add_api(post_api))