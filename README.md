# 1CKomunikator 💬
- [Ważne](#ważne-)
- [Instalacja](#instalacja-)
- [Funkcje](#funkcje-)
- [Dokumentacja](#dokumentacja-)
- [Diagram Bazy Danych](https://app.diagrams.net/#HMio-coder%2FKomunikatorC-server%2Fmain%2FDB-model.drawio#%7B%22pageId%22%3A%22IgY-TPN_slxYMBxNZM7g%22%7Dh)
- [Postęp](#postęp): $$0\frac{0}{1}$$%
- [Cele](#cele-)
- [Do Zrobienia](#do-zrobienia-)
- [Znane Błędy](#znane-błędy-)
  <a href="#funkcje">yh</a>
## Ważne ❗
Przed pull-request sparawdź składnie oraz uruchom testy \
Prace nad HTML: dev-html (w trakcie) \
Prace nad Bazą Danych: dev-database (w trakcie) \
Prace nad Serwerem: dev-server (w trakcie)

Po skończeniu pracy pull-request do dev.

## Instalacja 💽

```shell
pip install -r requirements.txt
```

## Testowanie 📋

### testowanie lokalnie

```shell
pip install pytest
pytest
```

### testowanie tak jak na github

wymagany jest [docker](https://www.docker.com/) \
(polecam docker desktop) \
zainstaluj [act](https://nektosact.com/installation/index.html) \
uruchom docker [desktop] oraz wywołaj \
```shell
act
```

### Sprawdzanie składni 📠

```shell
pip install pylint
git ls-files '*.py' | xargs pylint
```


```shell
pip install ruff
ruff . --fix
```

```shell
pip install mypy
mypy --install-types
mypy .
```

## Dokumentacja 🗂️

jak coś się zrobi to dać dokumentację

### db.py 📑

zarządza bazą danych

db.py clear                 - clears the database
db.py add <user> <password> - adds a user
db.py print_table           - prints all users
db.py get <user>            - gets password about

## Postęp

### **Postęp: $$0\frac{0}{1}$$%**

<details>
<summary> Postępy 🏆 </summary>

### Podstawa serwera 🌐

- [ ] Całość gotowa     (100%)
- [ ] Większość gotowa  (~75%)
- [ ] Połowa gotowa     (~50%)
- [ ] Mniejszość gotowa (~25%)
- [x] Nic nie jest gotowe (0%)

### Obsługa bazy danych 📠

- [ ] Całość gotowa     (100%)
- [ ] Większość gotowa  (~75%)
- [ ] Połowa gotowa     (~50%)
- [ ] Mniejszość gotowa (~25%)
- [x] Nic nie jest gotowe (0%)

### Działające API - Weryfikacja danych 🗂️

- [ ] Całość gotowa     (100%)
- [ ] Większość gotowa  (~75%)
- [ ] Połowa gotowa     (~50%)
- [ ] Mniejszość gotowa (~25%)
- [x] Nic nie jest gotowe (0%)

### Działające API - Obsługa wiadomości 💬

- [ ] Całość gotowa     (100%)
- [ ] Większość gotowa  (~75%)
- [ ] Połowa gotowa     (~50%)
- [ ] Mniejszość gotowa (~25%)
- [x] Nic nie jest gotowe (0%)

### Szyfrowanie 📟

- [ ] Całość gotowa     (100%)
- [ ] Większość gotowa  (~75%)
- [ ] Połowa gotowa     (~50%)
- [ ] Mniejszość gotowa (~25%)
- [x] Nic nie jest gotowe (0%)

### Inne g$%&a 🥚

- [ ] Całość gotowa     (100%)
- [ ] Większość gotowa  (~75%)
- [ ] Połowa gotowa     (~50%)
- [ ] Mniejszość gotowa (~25%)
- [x] Nic nie jest gotowe (0%)

</details>

## Cele 🏅

- API po stronie serwera, obłsugujące logowanie i tworzenie kont, czy ktos to wgl czyta, wysyłanie, pobieranie, zarządzanie, odpowiadanie -
  wiadomości
- Szyfrowanie wiadomości, zabezpieczemie przed możliością odczytu po stronie serwera
- Strona aplikacji obsługująca całe API

## Do Zrobienia 🧾

- [ ] Strona (Serwer) 🌐
- [ ] Baza Danych 🗂️
- [ ] Szyfrowanie 🔐
- [ ] API 📟

## Znane Błędy ❗
