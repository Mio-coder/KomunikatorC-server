# List of Fractions with LaTeX and Handwritten-Style Fractions

Here is a list of fractions representing percentages of some random data.

<style>
  .latex-fraction {
    display: inline;
  }

  .handwritten-fraction {
    display: none;
  }

  /* CSS media query for smaller screens */
  @media (max-width: 768px) {
    .latex-fraction {
      display: none;
    }
    .handwritten-fraction {
      display: inline;
    }
  }
</style>

1. <span class="latex-fraction">\(\frac{1}{2}\)</span><span class="handwritten-fraction">0 1/2</span> = 50%
2. <span class="latex-fraction">\(\frac{3}{4}\)</span><span class="handwritten-fraction">0 3/4</span> = 75%
3. <span class="latex-fraction">\(\frac{2}{5}\)</span><span class="handwritten-fraction">0 2/5</span> = 40%
4. <span class="latex-fraction">\(\frac{5}{6}\)</span><span class="handwritten-fraction">0 5/6</span> = 83.33%
5. <span class="latex-fraction">\(\frac{7}{8}\)</span><span class="handwritten-fraction">0 7/8</span> = 87.5%


# 1CKomunikator 💬
- [Ważne](#ważne-)
- [Instalacja](#instalacja-)
- [Dokumentacja](#dokumentacja-)
- [Diagram Bazy Danych](https://app.diagrams.net/#HMio-coder%2FKomunikatorC-server%2Fmain%2FDB-model.drawio#%7B%22pageId%22%3A%22IgY-TPN_slxYMBxNZM7g%22%7Dh)
- [Postęp: <img src="https://latex.codecogs.com/svg.image?\tiny&space;&space;0\frac{0}{1}\%" alt="0 0/1%">](#postęp)
- [Cele](#cele-)
- [Do Zrobienia](#do-zrobienia-)
- [Znane Błędy](#znane-błędy-)

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

## Postęp: $$0\frac{0}{1}$$%

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
