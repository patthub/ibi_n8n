# Historia rozmowy z Claude: ostatnie zajęcia z „Ilościowych badań informacji”

18 listopada 2026. Wypowiedzi prowadzącego zachowano dosłownie. Odpowiedzi Claude są streszczone, z najważniejszymi propozycjami i decyzjami.

---

## 1. Punkt wyjścia

**Prowadzący:**
> prowadzę zajecia z ilosciowych badan informacji. Wklejam syllabus: Przedmiot poświęcony jest zastosowaniu metod ilościowych do analizy różnych zasobów informacyjnych, w tym zasobów informacji o piśmiennictwie naukowym i obserwacji na jej podstawie zjawisk związanych z wykorzystywaniem informacji, w tym komunikacją naukową. […] Studenci poznają założenia, metody i zastosowanie ilościowych badań informacji, w szczególności w zakresie bibliometrii, naukometrii, informetrii, altmetrii i webometrii. Omawiane są ilościowe prawa informacyjne i ich zastosowanie. -- prowadzilem konkretnie zajecia z excela (przetwarzanie danych o publikacjach naukowych), uzycie LLMow do analizy literatury (promptowanie) oraz male modele jezykowe (nery, sentyment itp w przetwarzaniu artykulow). Jutro mam ostatnie zajecia, potrzebuje czegos fajnego dla studentow jakiegos tematu cyfrowego, co proponujesz?

**Claude** zaproponował pięć tematów:
1. „Czy LLM zmyśla bibliografię?”: ilościowy eksperyment z weryfikacją cytowań w OpenAlex/Crossref (polecany).
2. Mapa dziedziny: OpenAlex + VOSviewer.
3. Prawa Lotki, Bradforda i Zipfa na żywych danych.
4. „Detektyw naukometryczny”: paper mills, kartele cytowań, tortured phrases, retrakcje.
5. Embeddingi i mapy tematyczne (BERTopic w Colabie).

## 2. Bardziej technologicznie, bez programowania

**Prowadzący:**
> wole cos bardziej technologicznego ale dla osob ktore nie potrafia programowac. cos co im tez sie przyda ale na przykladach artykulow naukowych jednak

**Claude:** vibe coding. Studenci budują własny dashboard bibliometryczny z CSV z OpenAlex, opisując aplikację modelowi AI. Alternatywy: automatyzacja no-code (n8n/Make), lokalny model na własnych PDF-ach (LM Studio/AnythingLLM).

## 3. Coś pod pracę licencjacką

**Prowadzący:**
> zaproponuj jednak cos innego. Moze cos co przyda sie podczas pisania pracy licencjackiej?

**Claude:** warsztat „od tematu do bibliografii”: wyszukiwanie semantyczne (Semantic Scholar, Elicit, Consensus), sieci cytowań (Connected Papers, ResearchRabbit, Litmaps), Zotero, NotebookLM, weryfikacja i zasady korzystania z AI.

**Prowadzący:**
> tylko nie mamy dostepow premium do llmow

**Claude:** scenariusz działa na darmowych wersjach (Zotero, Semantic Scholar, NotebookLM z kontem Google, darmowe plany Connected Papers/ResearchRabbit/Litmaps). Elicit i Consensus tylko jako pokaz.

**Prowadzący:**
> nie wiem, wolalbym jedno narzedzie chyba

**Claude:** NotebookLM jako jedno narzędzie: źródła, tabela przeglądowa, mapa myśli, weryfikacja odpowiedzi z liczeniem trafności, podcast lub fiszki.

**Prowadzący:**
> troche to malo na zajecia plus jednak juz wspominalismy o notebook lm

**Claude:** VOSviewer z pobieraniem danych z OpenAlex przez API: mapy słów kluczowych, overlay w czasie, współcytowania, współautorstwo, opis metody do pracy. Alternatywa: Zotero.

## 4. Analiza danych

**Prowadzący:**
> troche nudne, zaproponuj mi jednak cos innego. Nie musi byc pod ten licencjat koniecznie, mozemy skupic sie na anaizie danych

**Claude:** Orange Data Mining: wizualne uczenie maszynowe na abstraktach („Czy maszyna rozpozna dyscyplinę z abstraktu?”), modelowanie tematów, embeddingi, klasyfikator i konkurs na trafność.

**Prowadzący:**
> bez instalowania i nie takie infantylne

**Claude** sprawdził w sieci, że od 13 lutego 2026 OpenAlex wymaga darmowego klucza API (1 USD darmowego limitu dziennie). Zaproponował mini-hackathon naukometryczny na API OpenAlex wpisywanym w przeglądarkę (filtry, `group_by`), z projektami zespołowymi: retrakcje, nierówność cytowań, open access, umiędzynarodowienie polskiej nauki, boom na AI, prawa Lotki i Bradforda.

## 5. Decyzja: własny agent

**Prowadzący:**
> nie podoba mi sie. Moze jednak dalej cos o nlp. Moze zrobmy swojego agenta?

**Claude** sprawdził aktualne warunki:
- n8n Cloud ma 14-dniowy okres próbny bez karty,
- darmowe limity Gemini API mocno obcięto pod koniec 2025 roku, liczą się per projekt i Google nie publikuje już dziennych limitów darmowego planu.

Zaproponował agenta-asystenta przeglądu literatury w n8n: model Gemini (darmowy klucz z AI Studio) + narzędzie HTTP do API arXiv (bez klucza) + pamięć. Przebieg: model bez narzędzi (halucynacje) → narzędzie arXiv i log wykonania → instrukcja systemowa → ekstrakcja NLP z abstraktów do tabeli → testy „łamania” agenta. Główne ryzyko: limity Gemini, do sprawdzenia przed zajęciami.

**Prowadzący:**
> podoba mi sie. naucz mnie tego

**Claude** przygotował dokument „Własny agent AI w n8n — przewodnik do zajęć” (plik `przewodnik-prowadzacego.md`) i gotowy przepływ `agent-arxiv-n8n.json`. Import przepływu sprawdził w lokalnie zainstalowanym n8n 2.48.5.

## 6. Interaktywny kurs na GitHub Pages

**Prowadzący:**
> proponuje zebys zrobil mi interaktywny kurs ze screenshotami z n8n. wrzucimy ten kurs na github pages

**Claude** uruchomił lokalnie n8n, zbudował agenta od zera w interfejsie (sterowanym skryptem Playwright) i zrobił 21 zrzutów ekranu z zaznaczonymi miejscami do kliknięcia. Złożył z nich statyczną stronę `index.html`: 12 rozdziałów, pasek postępu, quizy, przyciski kopiowania promptów, powiększanie zrzutów, plan B z importem przepływu i tabela problemów.

Ustalenia z budowy w n8n 2.48 wpisane do kursu:
- wyzwalacz to **Chat → On new Chat event**,
- przy szukaniu „agent” pierwszy na liście jest „Message an Agent”; trzeba wybrać **AI Agent**,
- import przepływu: **… → Import → From File**,
- pole parametru wypełniane przez model: ikona gwiazdek albo `{{ $fromAI(...) }}`.

Ograniczenia: brak zrzutu z prawdziwego przebiegu agenta w panelu Logs (środowisko bez dostępu do Gemini i arXiv); na zrzucie wyboru modelu pole jest czerwone, bo użyto przykładowego klucza.

**Prowadzący:**
> wrzuc tu jak skonczysz: https://github.com/patthub/ibi_n8n.git

**Claude:** nie mógł wypchnąć zmian, bo sesja nie miała połączenia z kontem GitHub. Przekazał paczkę ZIP z kursem i instrukcję ręcznego wgrania oraz włączenia Pages.

**Prowadzący:**
> daj mi historie tego czatu i wszystkie pliki wrzuce to przez claude code

**Claude:** przygotował tę paczkę: kurs, przewodnik prowadzącego, tę historię, skrypty do zrzutów i plik `CLAUDE.md` z instrukcją publikacji dla Claude Code.

---

## Źródła sprawdzane w trakcie rozmowy

- OpenAlex: klucze API wymagane od lutego 2026, https://developers.openalex.org/api-reference/authentication.md
- n8n: okres próbny Cloud i węzeł AI Agent, https://aiagentsquare.pages.dev/agents/n8n oraz https://fieldtested.pages.dev/agents/tools/n8n/
- Gemini API: zmiany darmowych limitów, https://agentdeals.dev/gemini-api-pricing-2026 oraz https://benchlm.ai/md/free-tier/google-ai-studio.md
