Zadanie: biblioteka filmów
A teraz coś z zupełnie innej beczki. Wyobraź sobie, że tworzysz system obsługujący bibliotekę filmów i seriali.
Wykorzystaj wiedzę na temat programowania obiektowego i napisz program, który spełnia następujące założenia:

Jest w stanie przechowywać informacje na temat filmów,
które znajdują się w systemie. Każdy film powinien mieć następujące atrybuty:

- Tytuł
- Rok wydania
- Gatunek
- Liczba odtworzeń


Umożliwia przechowywanie informacji na temat seriali.
Każdy serial powinien mieć następujące atrybuty:

- Tytuł
- Rok wydania
- Gatunek
- Numer odcinka
- Numer sezonu
- Liczba odtworzeń


Filmy i seriale mają metodę play, która zwiększa liczbę odtworzeń danego tytułu o 1.
Po wyświetleniu serialu jako string pokazują się informacje o konkretnym odcinku, np.:
“The Simpsons S01E05” (gdzie po S pokazany jest numer sezonu w notacji dwucyfrowej,
natomiast po E - numer odcinka, również w zapisie dwucyfrowym).

Po wyświetleniu filmu jako string widoczne są tytuł i rok wydania np. “Pulp Fiction (1994)”.
Przechowuje filmy i seriale w jednej liście.


Dodatkowo:

- Napisz funkcje get_movies oraz get_series, które będą filtrować listę i zwracać odpowiednio
  tylko filmy oraz tylko seriale. Posortuj listę wynikową alfabetycznie.
- Napisz funkcję search, która wyszukuje film lub serial po jego tytule.
- Napisz funkcję generate_views, która losowo wybiera element z biblioteki,
  a następnie dodaje mu losową (z zakresu od 1 do 100) ilość odtworzeń.
- Napisz funkcję, która uruchomi generate_views 10 razy.
- Napisz funkcję top_titles(), która zwróci wybraną ilość najpopularniejszych tytułów z biblioteki.
  Dla chętnych: dodaj do funkcji parametr content_type,
  którym wybierzesz czy mają zostać pokazane filmy, czy seriale.

Zadania dla chętnych:
- Napisz funkcję, która za pomocą pętli dodaje pełne sezony seriali do biblioteki.
  Funkcja powinna przyjmować parametry takie jak: tytuł serialu, rok wydania, gatunek,
  numer sezonu, liczba odcinków do dodania.
- Do klasy reprezentującej serial, dopisz funkcję zewnętrzną,
  która wyświetla liczbę odcinków danego serialu dostępnych w bibliotece.


Niech program po uruchomieniu działa w następujący sposób:

- Wyświetli na konsoli komunikat Biblioteka filmów.
- Wypełni bibliotekę treścią.
- Wygeneruje odtworzenia treści za pomocą funkcji generate_views.
- Wyświetli na konsoli komunikat Najpopularniejsze filmy i seriale dnia <data>,
  gdzie <data> to bieżąca data w formacie DD.MM.RRRR.
- Wyświetli listę top 3 najpopularniejszych tytułów.
- Kod udostępnij na Githubie i wyślij link do Mentora.