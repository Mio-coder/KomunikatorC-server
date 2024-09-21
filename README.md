# 1CKomunikator 💬
- [Ważne](#ważne-)
- [Instalacja](#instalacja-)
- [Dokumentacja](#dokumentacja-)
- [Diagram Bazy Danych](https://app.diagrams.net/#HMio-coder%2FKomunikatorC-server%2Fmain%2FDB-model.drawio#%7B%22pageId%22%3A%22IgY-TPN_slxYMBxNZM7g%22%7Dh)
- [Postęp: <picture> <source media="(prefers-color-scheme: dark)" srcset="https://latex.codecogs.com/svg.image?\inline&space;\tiny&space;\color{white}25\frac{0}{1}\%"> <img alt="25 0\1%" src="https://latex.codecogs.com/svg.image?\inline&space;\tiny&space;&space;25\frac{0}{1}\%"> </picture>](#postęp-0frac01)
- [Cele](#cele-)
- [Do Zrobienia](#do-zrobienia-)
- [Znane Błędy](#znane-błędy-)
- [README na Github Mobile](/README_github_mobile.md)

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

### UWAGA! OBECNIE NIE DZIAŁA

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

## Postęp: $` $25\frac{0}{1}\%$ `$

<details>
<summary> Postępy 🏆 </summary>

### Podstawa serwera 🌐

- [ ] $` $\color{green} Całość \space gotowa \space (100\%)$ `$
- [ ] $` $\color{yellow} Większość \space gotowa \space (~75\%)$ `$
- [ ] $` $\color{orange} Połowa \space gotowa \space (~50\%)$ `$
- [ ] $` $\color{red} Mniejszość \space gotowa \space (~25\%)$ `$
- [x] $` $\color{purple} Nic \space nie \space jest \space gotowe \space (0\%)$ `$

### Obsługa bazy danych 📠

- [ ] $` $\color{green} Całość \space gotowa \space (100\%)$ `$
- [ ] $` $\color{yellow} Większość \space gotowa \space (~75\%)$ `$
- [ ] $` $\color{orange} Połowa \space gotowa \space (~50\%)$ `$
- [ ] $` $\color{red} Mniejszość \space gotowa \space (~25\%)$ `$
- [x] $` $\color{purple} Nic \space nie \space jest \space gotowe \space (0\%)$ `$

### Działające API - Weryfikacja danych 🗂️

- [ ] $` $\color{green} Całość \space gotowa \space (100\%)$ `$
- [ ] $` $\color{yellow} Większość \space gotowa \space (~75\%)$ `$
- [ ] $` $\color{orange} Połowa \space gotowa \space (~50\%)$ `$
- [ ] $` $\color{red} Mniejszość \space gotowa \space (~25\%)$ `$
- [x] $` $\color{purple} Nic \space nie \space jest \space gotowe \space (0\%)$ `$

### Działające API - Obsługa wiadomości 💬

- [ ] $` $\color{green} Całość \space gotowa \space (100\%)$ `$
- [ ] $` $\color{yellow} Większość \space gotowa \space (~75\%)$ `$
- [ ] $` $\color{orange} Połowa \space gotowa \space (~50\%)$ `$
- [ ] $` $\color{red} Mniejszość \space gotowa \space (~25\%)$ `$
- [x] $` $\color{purple} Nic \space nie \space jest \space gotowe \space (0\%)$ `$

### Szyfrowanie 📟

- [ ] $` $\color{green} Całość \space gotowa \space (100\%)$ `$
- [ ] $` $\color{yellow} Większość \space gotowa \space (~75\%)$ `$
- [ ] $` $\color{orange} Połowa \space gotowa \space (~50\%)$ `$
- [ ] $` $\color{red} Mniejszość \space gotowa \space (~25\%)$ `$
- [x] $` $\color{purple} Nic \space nie \space jest \space gotowe \space (0\%)$ `$

### Inne g$%&a 🥚

- [ ] $` $\color{green} Całość \space gotowa \space (100\%)$ `$
- [ ] $` $\color{yellow} Większość \space gotowa \space (~75\%)$ `$
- [ ] $` $\color{orange} Połowa \space gotowa \space (~50\%)$ `$
- [ ] $` $\color{red} Mniejszość \space gotowa \space (~25\%)$ `$
- [x] $` $\color{purple} Nic \space nie \space jest \space gotowe \space (0\%)$ `$

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

[//]: # (TODO: @Wojciech napraw, potrafisz to pisć)
## Docker generated readme
### Building and running your application

When you're ready, start your application by running:
`docker compose up --build`.

Your application will be available at http://localhost:8000.

### Deploying your application to the cloud

First, build your image, e.g.: `docker build -t myapp .`.
If your cloud uses a different CPU architecture than your development
machine (e.g., you are on a Mac M1 and your cloud provider is amd64),
you'll want to build the image for that platform, e.g.:
`docker build --platform=linux/amd64 -t myapp .`.

Then, push it to your registry, e.g. `docker push myregistry.com/myapp`.

Consult Docker's [getting started](https://docs.docker.com/go/get-started-sharing/)
docs for more detail on building and pushing.

### References
* [Docker's Python guide](https://docs.docker.com/language/python/)