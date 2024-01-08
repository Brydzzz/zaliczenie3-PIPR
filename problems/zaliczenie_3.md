# Zaliczenie 3 - Wyszukiwarka filmów

Celem zadania jest napisanie prostej wyszukiwarki filmów.

Wyszukiwarka powinna mieć postać aplikacji konsolowej. Powinna umożliwić wyszukanie filmu po tytule oraz wyświetlenie następujących informacji o nim:

- Tytuł

- Czas trwania w minutach

- Rok produkcji

- Gatunek

- Opis

Dane filmów są przekazywane w pliku csv, którego ścieżka jest podawana jako argument wywołania programu. Plik csv posiada następujące kolumny:

- `title` - tytuł

- `year` - rok

- `genre` - gatunek

- `duration` - czas trwania

- `description` - opis

Jeżeli przekazana zostanie flaga `-r`, argumentem nie jest pojedynczy plik .csv tylko katalog - wówczas dane filmów powinny być brane ze wszystkich plików zawartych w tym katalogu oraz jego podkatalogach.

Jeżeli zostanie przekazana flaga `-d`, program zaraz po uruchomieniu powinien poinformować użytkownika o ewentualnych duplikatach tytułów.

Przy wyszukiwaniu nie powinien być brany pod uwagę rozmiar liter. Powinna zostać uwzględniona sytuacja, że filmu o podanym tytule może nie być w bazie.

Przykładowe wywołania programu:

    `{nazwa_programu}.py data/datadir -r -d` 

Przykładowa zawartość pliku csv:

```
title,year,genre,duration,description
The Phantom of the Opera,1925,horror,93,"A mad, disfigured composer seeks love with a lovely young opera singer."
The Three Musketeers,1921,adventure,120,"The young Gascon D'Artagnan arrives in Paris, his heart set on joining the king's Musketeers. He is taken under the wings of three of the most respected and feared Musketeers, Porthos, Aramis, and Athos. Together they fight to save France and the honor of a lady from the machinations of the powerful Cardinal Richelieu."
Night of the Living Dead,1968,horror,96,"A ragtag group of Pennsylvanians barricade themselves in an old farmhouse to remain safe from a bloodthirsty, flesh-eating breed of monsters who are ravaging the East Coast of the United States."
```