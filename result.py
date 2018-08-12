#output pk, name, result, points, top
"""
def get_result(teams, points):

    result = {
        'pk': [],
        'name': [],
        'points': [],
        'top': [],
    }
    stack = []
    for index, team in enumerate(teams):
        stack = result['pk']
        stack.append(index)
        result['pk'] = stack
        stack = result['name']
        stack.append(team)
        result['name'] = stack
        stack = []

    return result"""