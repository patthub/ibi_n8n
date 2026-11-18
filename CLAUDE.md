# Instrukcje dla Claude Code

Ten folder to statyczna strona kursu (bez builda, bez zależności) plus materiały dla prowadzącego.

Zadanie: opublikować folder w repozytorium https://github.com/patthub/ibi_n8n i włączyć GitHub Pages.

1. `git init -b main` (jeśli to jeszcze nie repozytorium), dodaj wszystkie pliki, commit.
2. `git remote add origin https://github.com/patthub/ibi_n8n.git` i `git push -u origin main`. Jeśli repozytorium ma już commity, najpierw `git pull --rebase origin main`; nie nadpisuj cudzej historii force-pushem bez pytania.
3. Włącz Pages z gałęzi `main`, folder `/ (root)`:
   `gh api -X POST repos/patthub/ibi_n8n/pages -f "source[branch]=main" -f "source[path]=/"`
   (jeśli Pages już istnieje, użyj `-X PUT`).
4. Sprawdź `https://patthub.github.io/ibi_n8n/` po 1–2 minutach: czy ładują się obrazki z `img/` i plik `agent-arxiv-n8n.json`.

Uwagi:
- `index.html` to jeden plik: HTML + CSS + JS inline. Treść po polsku.
- Zrzuty ekranu pochodzą z lokalnego n8n 2.48; skrypty do ich odtworzenia są w `materialy/zrzuty-skrypty/` (patrz README tam).
- Nie ma w repozytorium żadnych kluczy API. `stages.json` odwołuje się do przykładowego credentiala bez prawdziwego klucza.
