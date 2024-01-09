LAB202-MM-Zaliczenie 3
Termin: 19 stycznia 2022 12:03Kończy się 21 stycznia 2022 23:59
Instrukcje

## Przypomnienia

Proszę stworzyć program do zarządzania listą przypomnień ("todo list"). Program
obsługuje wielu użytkowników, z których każdy może mieć wiele przypomnień,
które mogą być wykonane lub nie. Program przechowuje listę przypomnień w
postaci pliku .json.

Domyślnie wczytywanym plikiem powinien być `todos.json`
znajdujący się w tym samym katalogu co program, natomiast można też podać nazwę innego pliku jako argument wywołania.  

Wywołanie programu
bez dodatkowych argumentów powinno wypisać wszystkie przypomnienia w sposób
czytelny dla użytkownika.

Proszę dostarczyć też wywołań z następującymi argumentami (podane identyfikatory są przykładowe):

* `--reset` - pobiera z [**API**](https://jsonplaceholder.typicode.com/todos) listę przypomnień i zapisuje ją do pliku `todos.json`,
* `--user 1` - wyświetla wszystkie przypomnienia dla użytkownika o identyfikatorze 1,
* `--list-not-completed 5` - wyświetla niewykonane przypomnienia dla użytkownika o identyfikatorze 5,
* `--toggle-todo 31` - zmienia stan przypomnienia o id 31 (jeśli było wykonane, to zmienia na niewykonane, i odwrotnie). Edycja przypomnienia powinna być odzwierciedlona w pliku .json.
* `--bar-plot` - rysuje wykres słupkowy przedstawiający sumaryczną ilość wykonanych i niewykonanych przypomnień
* `--pie-plot` - rysuje wykres kołowy przedstawiający sumaryczną ilość wykonanych i niewykonanych przypomnień

API: [https://jsonplaceholder.typicode.com/todos](https://jsonplaceholder.typicode.com/todos)