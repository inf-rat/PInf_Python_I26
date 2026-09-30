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

def breitensuche(graph, start) :
    besucht = set()
    warteschlange= [start]
    while warteschlange :
        knoten = warteschlange.pop(0)
        if not knoten in besucht :
            print(knoten)
            besucht.add(knoten)
            for n in graph[knoten] :
                warteschlange.append(n)

breitensuche(graph, "HB")