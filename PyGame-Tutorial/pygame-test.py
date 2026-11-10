# WICHTIG: Importieren von pygame als "spiel"
import pygame as spiel

# Initialisiert das Spiel
spiel.init()

# Fenstergröße bestimmen
bildschirm = spiel.display.set_mode((1280, 720))

# Variable setzen für den "Schläfer"
schlaefer = spiel.time.Clock()

# Variablensetzung von "spiel_leauft"
spiel_leauft = True

# Errechnung der Bewegungsgeschwindigkeit
vergangene_zeit = 0

# Die Spielerposition wird mittels der Mittelpunkte des Bildschirms definiert
spieler_position = spiel.Vector2(bildschirm.get_width() / 2, bildschirm.get_height() / 2)

# Die Magie sowie das Hauptgeschehen hinter einem Spiel:
# Begrenzt ist das ganze in 60 FPS schritten - alle 16,6 Millisekunden wiederholt sich diese "while"-Schleife
while spiel_leauft: # spiel_leauft ist unser oben definierter Wahrheitswert (sogenannter Boolean)

    # Check, ob ein "Event" (also ein sogenanntes Ereignis) aufgetreten ist
    for event in spiel.event.get():
        # Wenn das Spiel beendet werden soll, wird das Spiel_leauft auf False gesetzt
        if event.type == spiel.QUIT:
            spiel_leauft = False


    # Füllt den Hintergrund mti der Farbe Lila
    bildschirm.fill("purple")

    # Erstellt bei jeder Wiederholung an der Spielerposition einen Kreis als Spielerfigur
    spiel.draw.circle(bildschirm, "red", spieler_position, 40)


    # Hier wird geschaut, welche Tasten aktuell gedrückt werden
    testen_gedrueckt = spiel.key.get_pressed()

    # Geschwindigkeitszuordnung je nach Koordinatensystem x | y
    if testen_gedrueckt[spiel.K_w]:
        spieler_position.y -= 300 * vergangene_zeit # 300 Pixel mal die Sekunde fortbewegung
    if testen_gedrueckt[spiel.K_s]:
        spieler_position.y += 300 * vergangene_zeit # 300 Pixel mal die Sekunde fortbewegung
    if testen_gedrueckt[spiel.K_a]:
        spieler_position.x -= 300 * vergangene_zeit # 300 Pixel mal die Sekunde fortbewegung
    if testen_gedrueckt[spiel.K_d]:
        spieler_position.x += 300 * vergangene_zeit # 300 Pixel mal die Sekunde fortbewegung

    # Gibt die Änderungen, die wir übergeben haben, an den Bildschirm für den Spieler weiter
    spiel.display.flip()

    # Definiert die Bildwiederholrate.
    vergangene_zeit = schlaefer.tick(60) / 1000
    # Sie enthält die vergangene Zeit seit dem letzten Aufruf in Sekunden.
    # tick(60) begrenzt dabei auf maximal 60 Bilder pro Sekunde; / 1000 wandelt Millisekunden in Sekunden um.

    # Zum verdeutlichen, warum vergangene_zeit = schlaefer.tick(60) / 1000 verwendet wird:
    # 60 FPS	ca. 0,0167 Sekunden -> 5 Pixel
    # 30 FPS	ca. 0,0333 Sekunden	-> 10 Pixel
    # 10 FPS	0,1 Sekunden > 30 Pixel
    #
    # Je "mehr laggs" der Spieler hat, desto größer muss seine Bewegung sein.

# Wird erst dann ausgeführt, wenn die While-Schleife beendet wird
spiel.quit()