"""
Create a simple application that rewrites the JSON data structure from Section A to Section B.
Please note that Section A nodes are sorted in no particular order. The "subordinate" node must 
be removed when no child exists (see "markcorderoi" and "richard").

Section A: login_name works under manager_name
Section B: is sample output

mbarcelona <- nssi <- nishanthi <- markcorderoi
mbarcelona <- richard
letecia <- rudy


"""

Section_A = [
    {
        "manager_name": "nssi",
        "login_name": "nishanthi"
    },
    {
        "manager_name": "mbarcelona",
        "login_name ": "nssi"
    },
    {
        "manager_name": "nishanthi",
        "login_name": "markcorderoi"
    },
    {
        "manager_name": "mbarcelona",
        "login_name ": "richard"
    },
    {
        "manager_name": "letecia",
        "login_name ": "rudy"
    }
]


nodes = {}
parents = {}

for per_section_a in Section_A:
    [manager_name, login_name] = list(per_section_a.values())

    if not manager_name in nodes:
        nodes[manager_name] = []
    if not login_name in nodes:
        nodes[login_name] = []

    parents[login_name] = manager_name


for subbordinate, parent in parents.items():
    nodes[parent].append(subbordinate)


roots : list = [name for name in nodes if name not in parents]

def map(node, name):
    if len(node) <= 0:
        return {"name" : name}
    else:
        return {
            "name" : name,
            "subordinate" : [map(nodes[per], per) for per in node]
        }

Section_B = []

for root_name in roots:
    item = map(nodes[root_name], root_name)
    Section_B.append(item)
    pass


print(Section_B)