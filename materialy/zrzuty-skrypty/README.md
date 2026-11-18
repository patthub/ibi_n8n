# Jak powstały zrzuty ekranu

Zrzuty zrobiono w lokalnym n8n 2.48.5 (Node 24), sterowanym przez Playwright (Python) w Chrome bez okna.

1. Instalacja: `npm install n8n` (wymaga Node ≥ 24).
2. Start: `start.sh` (ustaw ścieżkę `N8N_USER_FOLDER` u siebie). n8n działa na `http://127.0.0.1:5678`.
3. `pw_setup.py` zakłada lokalne konto właściciela (dane testowe, tylko dla lokalnej instancji) i zapisuje sesję do `state.json`.
4. `stages.json` to trzy etapy budowy agenta (import: `npx n8n import:workflow --input=stages.json`). Etap 2 i 3 odwołują się do credentiala Gemini z przykładowym kluczem; zaimportuj go osobno albo podłącz własny.
5. `build.py` buduje agenta od zera w interfejsie i robi zrzuty `shots/b_*.png`. Zrzuty paneli z wypełnionymi polami (`p_*.png`, `etap3*.png`) powstały przez dwuklik w węzły zaimportowanego etapu 3.
6. `mkimg.py` dodaje czerwone ramki, przycina i zmniejsza zrzuty do `site/img/`.

Ścieżki w skryptach wskazują na `/home/claude/...`; zmień je u siebie. Współrzędne kliknięć i ramek są dopasowane do okna 1440×860 przy skali 1,5 i po zmianie wersji n8n mogą wymagać poprawek.

Nie powstał zrzut z prawdziwego przebiegu agenta (panel Logs), bo środowisko nie miało dostępu do Gemini ani arXiv.
