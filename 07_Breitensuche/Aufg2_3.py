from collections import deque

graph_DE = {
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

graph_EU = {
    "AL": ["ME", "XK", "MK", "GR"],
    "AD": ["FR", "ES"],
    "AT": ["DE", "CZ", "SK", "HU", "SI", "IT", "CH", "LI"],
    "BY": ["LV", "LT", "PL", "RU", "UA"],
    "BE": ["FR", "LU", "DE", "NL"],
    "BA": ["HR", "RS", "ME"],
    "BG": ["RO", "RS", "MK", "GR", "TR"],
    "HR": ["SI", "HU", "RS", "BA", "ME"],
    "CY": [],  # keine Landgrenzen
    "CZ": ["DE", "PL", "SK", "AT"],
    "DK": ["DE"],
    "EE": ["LV", "RU"],
    "FI": ["SE", "NO", "RU"],
    "FR": ["BE", "LU", "DE", "CH", "IT", "MC", "ES", "AD"],
    "DE": ["DK", "PL", "CZ", "AT", "CH", "FR", "LU", "BE", "NL"],
    "GR": ["AL", "MK", "BG", "TR"],
    "HU": ["AT", "SK", "UA", "RO", "RS", "HR", "SI"],
    "IS": [],  # keine Landgrenzen
    "IE": ["GB"],
    "IT": ["FR", "CH", "AT", "SI", "SM", "VA"],
    "XK": ["RS", "ME", "AL", "MK"],
    "LV": ["EE", "RU", "BY", "LT"],
    "LI": ["CH", "AT"],
    "LT": ["LV", "BY", "PL", "RU"],
    "LU": ["BE", "DE", "FR"],
    "MT": [],  # keine Landgrenzen
    "MD": ["RO", "UA"],
    "MC": ["FR"],
    "ME": ["HR", "BA", "RS", "XK", "AL"],
    "NL": ["BE", "DE"],
    "MK": ["AL", "XK", "RS", "BG", "GR"],
    "NO": ["SE", "FI", "RU"],
    "PL": ["DE", "CZ", "SK", "UA", "BY", "LT", "RU"],
    "PT": ["ES"],
    "RO": ["HU", "UA", "MD", "BG", "RS"],
    "RU": ["NO", "FI", "EE", "LV", "LT", "PL", "BY", "UA"],
    "SM": ["IT"],
    "RS": ["HU", "RO", "BG", "MK", "XK", "ME", "BA", "HR"],
    "SK": ["CZ", "AT", "PL", "UA", "HU"],
    "SI": ["IT", "AT", "HU", "HR"],
    "ES": ["PT", "FR", "AD"],
    "SE": ["NO", "FI"],
    "CH": ["DE", "FR", "IT", "AT", "LI"],
    "TR": ["GR", "BG"],
    "UA": ["PL", "SK", "HU", "RO", "MD", "BY", "RU"],
    "GB": ["IE"],
    "VA": ["IT"],
}


def breiten_suche_weg(graph, start, ende):
    besucht = {}
    warteschlange = deque([(start, None)])
    pfad = deque([])
    while warteschlange:
        (knoten, vorgaenger) = warteschlange.popleft()
        if not knoten in besucht:
            besucht[knoten] = vorgaenger
            if knoten == ende:
                pfad.appendleft(knoten)
                wegpunkt = vorgaenger
                while wegpunkt is not None:
                    pfad.appendleft(wegpunkt)
                    wegpunkt = besucht[wegpunkt]
                return list(pfad)
            for n in graph[knoten]:
                if not n in besucht:
                    warteschlange.append((n, knoten))
    return pfad

print(breiten_suche_weg(graph_DE, "HB", "BY"))
print(breiten_suche_weg(graph_EU, "DE", "TR"))