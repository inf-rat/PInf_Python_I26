graph = {
    "BW": ["BY", "HE", "RP"],
    "BY": ["BW", "HE", "SN", "TH"],
    "BE": ["BB"],
    "BB": ["BE", "MV", "NI", "SN", "ST"],
    "HB": ["NI"],
    "HH": ["NI", "SH"],
    "HE": ["BW", "BY", "NI", "NW", "RP", "TH"],
    "MV": ["BB", "NI", "SH"],
    "NI": ["BB", "HB", "HE", "HH", "NW", "SH", "ST"],
    "NW": ["HE", "NI", "RP"],
    "RP": ["BW", "HE", "NW", "SL"],
    "SL": ["RP"],
    "SN": ["BB", "BY", "ST", "TH"],
    "ST": ["BB", "NI", "SN", "TH"],
    "SH": ["HH", "MV", "NI"],
    "TH": ["BY", "HE", "SN", "ST"]
}

def tiefensuche(graph, start, besucht = set()):
    print(start)
    besucht.add(start)
    for n in graph[start]:
        if not n in besucht:
            tiefensuche(graph, n, besucht)

def tiefensuche_wegfindung(graph, start, end, besucht = set()):
    print(start)
    besucht.add(start)
    for n in graph[start]:
        if not n in besucht:
            weg = tiefensuche_wegfindung(graph, n, end, besucht)
            weg.insert(0, start)
            return(weg)

print(tiefensuche_wegfindung(graph, "HB", "BY"))

