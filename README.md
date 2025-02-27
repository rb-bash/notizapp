Voraussetzungen!!!

Bevor du beginnst, stelle sicher, dass du Folgendes installiert hast:

pip: Normalerweise wird pip mit Python installiert. Überprüfe dies, indem du den Befehl `pip --version` in der Konsole eingibst.

Schritt 1: Installiere die benötigten Pakete

Installiere Flask und Flask-SocketIO, indem du diesen Befehl in der Konsole ausführst:

      

    pip install Flask Flask-SocketIO

    

Schritt 2: Bestimme deine lokale IP-Adresse

Um den Server für andere Benutzer im lokalen Netzwerk zugänglich zu machen, bestimme zuerst die lokale IP-Adresse deines Computers:

Windows:
Öffne die Eingabeaufforderung (Cmd).
Gib ipconfig ein und drücke Enter.
Suche die IPv4-Adresse deines Netzwerkadapters.

macOS und Linux:
Öffne ein Terminal.
Gib ifconfig für macOS oder ip addr für Linux ein.
Finde die inet-Adresse, die der IPv4-Adresse entspricht.

Schritt 3: Ändere die Bind-Adresse des Flask-Servers


In der Datei app.py musst du den Server so konfigurieren, dass er auf deiner lokalen IP-Adresse hört. Ändere den Aufruf von socketio.run(app, debug=True) wie folgt:

      

    if __name__ == '__main__':
        socketio.run(app, host='0.0.0.0', port=5000, debug=True)

    

host='0.0.0.0' bewirkt, dass der Server auf allen Netzwerk-Schnittstellen hört.


Schritt 4: Starte den Flask-Server

Starte deinen Flask-Server mit folgendem Befehl:

      

    python app.py

    

Alternativ kannst du ihn auch so im Hintergrund laufen lassen:

      

    nohup flask run --host=0.0.0.0 --port=5000 &

    

Schritt 5: Zugriff auf den Webserver von anderen Geräten

Benutzer im selben lokalen Netzwerk können nun auf deinen Server zugreifen, indem sie die IP-Adresse deines Computers in ihren Webbrowser eingeben:

      

    http://192.168.1.xxx:5000

    

Wichtige Hinweise:

    Firewall-Einstellungen: Überprüfe, ob deine Firewall eingehenden Verkehr auf Port 5000 zulässt. Möglicherweise musst du eine Regel erstellen, um den Verkehr zu ermöglichen.

    Netzwerksicherheit: Achte darauf, dass du diese Konfiguration nur in einem sicheren Netzwerk verwendest, da 0.0.0.0 den Server für alle Geräte im lokalen Netzwerk zugänglich macht.

