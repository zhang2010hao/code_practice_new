
def findItinerary(tickets):

    def dfs(from_loc):
        if len(flag) > 0:
            return

        if len(tic_tuples) == 0:
            flag.append(1)
            return

        if from_loc not in ticket_dict:
            return


        for to_loc in ticket_dict[from_loc]:
            if (from_loc, to_loc) not in tic_tuples:
                continue
            else:
                tic_tuples.remove((from_loc, to_loc))
                rst.append(to_loc)
                dfs(to_loc)
                if len(flag) > 0:
                    return
                rst.pop(-1)
                tic_tuples.append((from_loc, to_loc))




    n = len(tickets)
    tic_tuples = [(ticket[0], ticket[1]) for ticket in tickets]

    flag = []

    ticket_dict = {}
    for ticket in tickets:
        tmp = ticket_dict.get(ticket[0], [])
        tmp.append(ticket[1])
        ticket_dict[ticket[0]] = tmp

    for k, v in ticket_dict.items():
        v_sorted = sorted(v)
        ticket_dict[k] = v_sorted

    rst = ['JFK']
    dfs('JFK')

    return rst

tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
rest = findItinerary(tickets)
print(rest)


