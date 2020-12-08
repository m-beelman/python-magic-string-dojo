import pytest

# Das ist die Methode die Du entwickeln sollst. Aufgabe für Aufgabe wir die Funktion mächtiger.
def magic_string_function(numbers_as_string):
    # some magic will hapen here
    return None

# 1. Schreibe die Function magic_string_function() so, das ich einen String mit einer variablen Anazahl von Zahlen als Parameter eingebe und eine Summe herausbekomme.
# Beispiel:
# magic_string_function("1,2,4") liefert mir das Ergebnis von 1 + 2 + 4 zurück, also 7
# magic_string_function("1.2,7.6,4") liefert mir das Ergebnis von 1.2 + 7.6 + 4 zurück, also 12.8
# magic_string_function("") liefert mir 0 zurück

def test_task_1():
    assert magic_string_function("1,2,4") == 7
    assert round(magic_string_function("1.2,7.6,4"),1) == 12.8
    assert magic_string_function("") == 0

# 2. Erweitere die Funktion so, das ich eine variable Anzahl von string übergeben kann
# magic_string_function("1","2","4") liefert mir das Ergebnis von 1 + 2 + 4 zurück, also 7
# magic_string_function("1.2,7.6","4") liefert mir das Ergebnis von 1.2 + 7.6 + 4 zurück, also 12.8
# magic_string_function("") liefert mir 0 zurück

# def test_task_2():
#     assert magic_string_function("1","2","4") == 7
#     assert round(magic_string_function("1.2,7.6", "4"),1) == 12.8

# 3. Erweitere die Funktion so, das neben dem Komma das ';' auch als Seperator dienen kann
# magic_string_function("1;2,4") liefert mir das Ergebnis von 1 + 2 + 4 zurück, also 7
# magic_string_function("1.2;7.6","4") liefert mir das Ergebnis von 1.2 + 7.6 + 4 zurück, also 12.8
# magic_string_function("") liefert mir 0 zurück

# def test_task_3():
#     assert magic_string_function("1;2,4") == 7
#     assert round(magic_string_function("1.2;7.6", "4"),1) == 12.8

# 4. Erweitere die Funktion so, das niemals der Seperator als letztes Zeichen String vorkommt
# magic_string_function("1;2,4,") liefert None und gibt auf der Konsole die Ausgabe "The string should not end with a seperator character."
# magic_string_function("1.2;7.6","4") liefert mir das Ergebnis von 1.2 + 7.6 + 4 zurück, also 12.8

# def test_task_4():
#     assert magic_string_function("1;2,4,") == None
#     assert round(magic_string_function("1.2;7.6", "4"),1) == 12.8


# 5. Erweitere die Funktion so, das ich der Methode als optionale Parameter einen weiteren Seperator übergeben kann
# magic_string_function("1;2:4",opt_sep=":") liefert mir das Ergebnis von 1 + 2 + 4 zurück, also 7
# magic_string_function("1.2|7.6","4", opt_sep="|") liefert mir das Ergebnis von 1.2 + 7.6 + 4 zurück, also 12.8

# def test_task_5():
#     assert magic_string_function("1;2:4", opt_sep=":") == 7
#     assert round(magic_string_function("1.2|7.6", "4", opt_sep="|"),1) == 12.8
