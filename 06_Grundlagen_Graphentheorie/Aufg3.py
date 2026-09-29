adj = {
    "BE": ["BB"],
    "BB": ["BE", "MV", "NI", "SN", "ST"],
    "BW": ["BY", "HE", "RP"],
    "BY": ["BW", "HE", "SN", "TH"],
    "HB": ["NI"],
    "HE": ["BW", "BY", "NI", "NW", "RP", "TH"],
    "HH": ["NI", "SH"],
    "MV": ["BB", "NI", "SH"],
    "NI": ["BB", "HB", "HE", "HH", "MV", "NW", "SH", "ST", "TH"],
    "NW": ["HE", "NI", "RP"],
    "RP": ["BW", "HE", "NW", "SL"],
    "SH": ["HH", "MV", "NI"],
    "SL": ["RP"],
    "SN": ["BB", "BY", "ST", "TH"],
    "ST": ["BB", "NI", "SN", "TH"],
    "TH": ["BY", "HE", "NI", "SN", "ST"]
}

def are_neighbors(adj, land1, land2):
    if land1 not in adj or land2 not in adj:
        print("Fehler: Eins der Länder ist nicht im Graphen!")
    else:
        return land2 in adj.get(land1)

print(are_neighbors(adj, "BW", "BY"))
print(are_neighbors(adj, "SN", "HB"))
print(are_neighbors(adj, "HB", "x"))
print(are_neighbors(adj, "Sachsen", "HB"))

