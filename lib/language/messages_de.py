#!/usr/bin/env python
# -*- coding: utf-8 -*-


def all_messages():
    return \
        {
            "0": "Nettacker Programm gestartet ...\n\n",
            "1": "python nettacker.py [Optionen]",
            "2": "Nettacker Hilfe-Menü anzeigen",
            "3": "Bitte lesen Sie die Lizenz und Vereinbarungen https://github.com/viraintel/OWASP-Nettacker\n",
            "4": "Programm",
            "5": "Optionen für das Programm",
            "6": "Bitte eine Sprache {0} auswählen.",
            "7": "Alle IPs im Bereich scannen",
            "8": "Subdomains suchen und scannen",
            "9": "Thread-Nummern für Verbindungen zu einem Host",
            "10": "Thread-Nummern für Scan-Hosts",
            "11": "Alle Protokolle der Datei (results.txt, results.html, results.json) speichern",
            "12": "Ziel",
            "13": "Optionen für das Ziel",
            "14": "Liste der Ziele mit \",\" getrennt",
            "15": "Ziele aus Datei lesen",
            "16": "Optionen für Scan-Methoden",
            "17": "Scan-Methode {0} wählen",
            "18": "Scan-Methode auswählen, um {0} auszuschließen",
            "19": "Benutzernamen-Liste mit \",\" getrennt",
            "20": "Benutzernamen aus Datei lesen",
            "21": "Passwörter-Liste mit \",\" getrennt",
            "22": "Passwörter aus Datei lesen",
            "23": "Port-Liste mit \",\" getrennt",
            "24": "Passwörter aus Datei lesen",
            "25": "Wartezeit (sleep) zwischen jeder Anfrage",
            "26": "Das Ziel kann nicht angegeben werden",
            "27": "Das Ziel kann nicht angegeben werden. Die Datei kann nicht geöffnet werden: {0}",
            "28": "Die Thread-Nummer sollte kleiner als 100 sein, es wird trotzdem weitergemacht ...",
            "29": "Zeitlimit auf {0} Sekunden setzen, es ist zu groß, oder?  es wird trotzdem weitergemacht ...",
            "30": "Dieses Scan-Modul [{0}] wurde nicht gefunden!",
            "31": "Dieses Scan-Modul [{0}] wurde nicht gefunden!",
            "32": "Es können nicht alle Scan-Methoden ausgeschlosen werden",
            "33": "Es können nicht alle Scan-Methoden ausgeschlosen werden",
            "34": "Das Modul {0}, das zum Ausschließen ausgewählt wurde, wurde nicht gefunden!",
            "35": "Bitte Eingabe für Methode angeben, Beispiel: \"ftp_brute_users =test,admin&ftp_brute_passwds="
                  "read_from_file:/tmp/pass.txt&ftp_brute_port=21\"",
            "36": "Datei {0} kann nicht gelesen werden",
            "37": "Der Benutzername kann nicht angegeben werden. Die Datei kann nicht geöffnet werden: {0}",
            "38": "",
            "39": "Das Passwort kann nicht angegeben werden. Die Datei kann nicht geöffnet werden: {0}",
            "40": "Datei \"{0}\" ist nicht schreibbar!",
            "41": "Bitte Scan-Methode wählen!",
            "42": "Temporäre Dateien entfernen!",
            "43": "Ergebnisse sortieren!",
            "44": "fertig!",
            "45": "beginne {0}, {1} von {2} anzugreifen",
            "46": "Das Modul \"{0}\" ist nicht verfügbar",
            "47": "Leider kann diese Version der Software nur unter Linux/OSX/Windows laufen.",
            "48": "Die Python-Version wird nicht unterstützt!",
            "49": "Überspringe ein doppeltes Ziel (einige Subdomains / Domains können dieselbe IP und Ranges haben)",
            "50": "unbekannter Zieltyp [{0}]",
            "51": "{0} Bereich prüfen ...",
            "52": "Überprüfung {0} ...",
            "53": "GASTGEBER",
            "54": "USERNAME",
            "55": "PASSWORT",
            "56": "PORT",
            "57": "TYP",
            "58": "BESCHREIBUNG",
            "59": "ausführliche Meldungen (0-5) (Standardeinstellung 0)",
            "60": "Softwareversion anzeigen",
            "61": "auf Update überprüfen",
            "62": "",
            "63": "",
            "64": "Wiederholungen beim Verbindungs-Timeout (Standard 3)",
            "65": "ftp-Verbindung zu {0}: {1} Zeitüberschreitung, überspringen {2}: {3}",
            "66": "ERFOLGREICH EINGELOGGT!",
            "67": "ERFOLGREICH ABGESCHLOSSEN, KEINE BERECHTIGUNG FÜR LISTE-BEFEHL!",
            "68": "ftp-Verbindung zu {0}: {1} ist fehlgeschlagen, gesamter Schritt wirdübersprungen"
                  " [process {2} von {3}]! weiter mit nächstem Schritt",
            "69": "Das Ziel für das {0} -Modul muss DOMAIN, HTTP oder SINGLE_IPv4 sein, wobei {1}",
            "70": "Benutzer: {0} übergeben: {1} Host: {2} Port: {3} gefunden!",
            "71": "(KEINE BERECHTIGUNG FÜR LISTEN-DATEIEN)",
            "72": "versuche {0} von {1} im Prozess {2} von {3} {4}: {5}",
            "73": "SMTP-Verbindung zu {0}: {1} Zeitüberschreitung, überspringe {2}: {3}",
            "74": "smtp-Verbindung zu {0}: {1} ist fehlgeschlagen, gesamter Schritt wird übersprungen "
                  "[process {2} von {3}]! weiter mit nächstem Schritt",
            "75": "Ziel für {0} -Modul muss HTTP sein, {1} wird übersprungen",
            "76": "ssh-Verbindung zu {0}: {1} Zeitüberschreitung, überspringe {2}: {3}",
            "77": "ssh-Verbindung zu {0}: {1} ist fehlgeschlagen, gesamter Schritt wird übersprungen "
                  "[process {2} von {3}]! weiter mit nächstem Schritt",
            "78": "ssh-Verbindung zu% s:% s ist fehlgeschlagen, gesamter Schritt [Prozess% s von% s]"
                  " wird übersprungen! weiter mit nächstem Schritt",
            "79": "OFFENER PORT",
            "80": "Host: {0} Port: {1} gefunden!",
            "81": "Ziel {0} eingereicht!",
            "82": "Kann keine Proxy-Listendatei öffnen: {0}",
            "83": "Proxy-Listendatei kann nicht gefunden werden: {0}",
            "84": "OWASP-Nettacker-Version {0} {1} {2} {6} mit dem Codenamen {3} {4} {5} wird ausgeführt",
            "85": "Diese Funktion ist noch nicht verfügbar! Bitte \"git clone https://github.com/viraintel/"
                  "OWASP-Nettacker.git\" oder \"pip install -U OWASP-Nettacker\" ausführen, um die letzte"
                  " Version zu erhalten.",
            "86": "Erstellen Sie ein Diagramm aller Aktivitäten und Informationen erstellen, HTML-Ausgabe"
                  " muss verwendet werden. Verfügbare Diagramme: {0}",
            "87": "Um den Graphen verwenden zu können, muss der Ausgabedateiname mit \".html\" oder \".htm\" enden!",
            "88": "Diagramm erstellen ...",
            "89": "Diagramm fertig bauen!",
            "90": "Penetrationstests",
            "91": "Diese Grafik wurde von OWASP Nettacker erstellt. Diagramm enthält alle Module Aktivitäten"
                  ", Netzwerkkarte und vertrauliche Informationen, Bitte teilen Sie diese Datei nicht mit"
                  " jemandem, wenn es nicht zuverlässig ist.",
            "92": "OWASP Nettacker Bericht",
            "93": "Softwaredetails: OWASP-Nettacker-Version {0} [{1}] in {2}",
            "94": "Keine offenen Ports gefunden!",
            "95": "Kein Benutzer / Passwort gefunden!",
            "96": "{0} Module geladen ...",
            "97": "Dieses Grafikmodul wurde nicht gefunden: {0}",
            "98": "Dieses Grafikmodul \"{0}\" ist nicht verfügbar",
            "99": "ping vor dem Scan des Host",
            "100": "Überspringe gesamtes Ziel und Scanmethode {1}, weil --ping-before-scan benutzt wurde und"
                   " keine Antwort erhalten hat!",
            "101": "Es wird nicht die aktuelle Version von OWASP Nettacker verwendet, bitte aktualisieren.",
            "102": "Kann nicht nach Update suchen, bitte Internetverbindung überprüfen.",
            "103": "Es wird nicht die aktuelle Version von OWASP Nettacker verwendet ...",
            "104": "Verzeichniseintrag in {0} gefunden",
            "105": "Bitte den Port über die Option -g oder --methods-args anstelle von URL einfügen",
            "106": "HTTP-Verbindung {0} Timeout!",
            "107": "",
            "108": "Kein Verzeichnis oder keine Datei für {0} in Port {1} gefunden",
            "109": "Kann {0} nicht öffnen",
            "110": "Die Methode für dir_scan_http_method muss GET oder HEAD sein, Standard wird auf GET gesetzt.",
            "111": "Zeige alle Methodenargumente an",
            "112": "Kann {0} Modulargumente nicht abrufen",
            "113": "",
            "114": "",
            "115": "",
            "116": "",
            "117": ""
        }
