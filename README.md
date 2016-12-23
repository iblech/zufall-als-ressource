# Wenn die Sonne über Monte-Carlo scheint
## wie mathematische Zufallsmethoden Simulationen physikalischer Naturphänomene ermöglichen (notes for a German math course)

![Auf Graphen tanzen – mit Zufallsmethoden kann man vom Mikroskopischen auf das
Makroskopische schließen. (Bearbeitung eines Fotos von Crevisio, verwendet mit
Erlaubnis.)](monte-carlo.jpeg)

*Hier entstehen Unterlagen zu einem Kurs auf der JGW-Schülerakademie in
Papenburg vom 23. Juli bis 3. August 2017, gehalten von Ingo Blechschmidt und
Maximilian Schlögel. Die Illustration hat das Motto "Auf Graphen tanzen", denn
mit Zufallsmethoden kann man vom Mikroskopischen auf das Makroskopische
schließen. (Bearbeitung eines Fotos von Crevisio, verwendet mit Erlaubnis.).*

Ein grundlegendes Ansinnen des Menschen ist es, seine Umgebung zu verstehen.
Die Physik leistet dazu wichtige Beiträge: Viele Naturphänomene sind
quantitativ mittels Gleichungen beschreibbar. Zu einem vollen Verständnis
gehört allerdings auch, Vorhersagen treffen zu können, und dazu muss man in der
Lage sein, diese Gleichungen auch zu lösen. Das ist zwar bei den in der
Schulphysik behandelten Phänomenen meistens der Fall, aber die Ausnahme bei den
Modellen, die auf universitärem Niveau Verwendung finden. Dafür ist man auf
computergestützte Näherungsmethoden angewiesen, aber wegen des Fluchs der
Dimensionalität steigt der Rechenaufwand bei klassischen Verfahren exponentiell
mit der Systemgröße an und macht praktische Anwendungen unmöglich.

Dies änderte sich mit einem mathematischen Durchbruch, der zu den modernen
Markov-Chain-Monte-Carlo-Methoden führte: Paradoxerweise kann man
unvorhersehbare Zufallsziehungen auf emergente Art und Weise so kombinieren,
dass sie zur Simulation physikalischer Systeme ausgenutzt werden können. Ein
Ziel des Kurses besteht darin, Zufall als wertvolle Ressource zu begreifen,
diese Einsicht von vielen Seiten aus anschaulich zu beleuchten und in
praktischer Programmierarbeit zu nutzen.

Dazu werden wir im Kurs zunächst die nötigen mathematischen Grundlagen
behandeln, wie etwa das Vektorkalkül und Differential- und Integralrechnung im
Mehrdimensionalen, welche auch in vielen weiteren Teilgebieten der Mathematik
und Physik eine wichtige Rolle spielen. Parallel steigen wir in Python ein,
einer Programmiersprache, die sich in Wirtschaft und Wissenschaft großer
Beliebtheit erfreut.

Mit diesem Handwerkszeug ausgerüstet gehen wir dann diverse Projekte an:
thermodynamische Bewegung von Gasteilchen simulieren, Hysterese bei
Magnetisierung beobachten, Chaostheorie am Doppelpendel erforschen und
kritische Stellen physikalischer Systeme finden. Wir werden uns aber auch mit
Beispielen beschäftigen, die auf den ersten Blick weniger mit Physik zu tun
haben: Wir werden die Macht der zwei Wahlmöglichkeiten in der
Warteschlangentheorie untersuchen, optimale Strategien bei Gesellschaftsspielen
finden, Chatroboter programmieren, die Entropie menschlicher Sprachen
analysieren und lernen, wie man ganz allgemein seine Vermutungen über die reale
Welt im Lichte neuer Beobachtungen am effizientesten anpasst.

Einen Höhepunkt wird ein Ausflug in die Quantenchemie darstellen: Wir werden
über die wundersamen Besonderheiten der Quantenmechanik sprechen und verstehen,
was es mit der gefeierten Schrödingergleichung auf sich hat und wie man mit
Zufallsmethoden die Form der Orbitale und grundlegende atomare Kenngrößen
bestimmen kann.
