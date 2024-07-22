## Die angewandte Breitensuche zur Ermittlung der kürzesten Wege zu einer Abkuehlung

### README


#### Programmablauf


##### Im Programm wird das LED - Panel als Board initialisiert, was wichtig fuer die Ansteuerung der LED Pixels ist. 

Wird das Programm gestartet, gibt der User 2 x eine Zahl zwischen 1 und 16 ein. Das sind die Koordinaten, die als Startpunkt 
festgelegt werden. Die erste Zahl entspricht der X- Achse, die zweite ist fuer die Y- Achse. Da die "goals", in diesem Falle 
Wasserstellen in der Stadt Detmold bereits vordefiniert sind, braucht man nur noch nach der Eingabe der Y- Achse die _<Enter>_ taste 
zu drücken und schon wird der kürzeste Weg bis zur nächstgelegenen Wasserstelle ermittelt. Zusätzlich wird der Weg durch eine 
Pathtracking Funktion aufgezeichnet und auf dem 16 x 16 LED Panel angezeigt.  

Jetzt hat der User noch die Moeglichkeit entweder die Zahl 42 einzugeben oder das Programm zu verlassen, indem eine andere beliebige Taste
gedrueckt wird. Nach Eingabe der Nummer 42, werden auf dem LED Panel die Pfade zu jedem "goal" (Wasserstellte) angezeigt, die von dem Startpunkt aus am kürzesten sind.    

