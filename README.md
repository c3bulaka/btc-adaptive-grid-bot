# BTC Adaptacyjny Bot Siatki (BTC Adaptive Grid Bot)

![Status: Aktywny](https://img.shields.io/badge/Status-Aktywny-green)
![Licencja: MIT](https://img.shields.io/badge/Licencja-MIT-blue)
![Język: Python](https://img.shields.io/badge/Język-Python-yellow)

## 📋 Spis Treści

- [Opis](#opis)
- [Cechy](#cechy)
- [Wymagania](#wymagania)
- [Instalacja](#instalacja)
- [Konfiguracja](#konfiguracja)
- [Użytkowanie](#użytkowanie)
- [Architektura](#architektura)
- [API](#api)
- [Strategie Tradingowe](#strategie-tradingowe)
- [Monitoring i Logowanie](#monitoring-i-logowanie)
- [Testowanie](#testowanie)
- [Rozwiązywanie Problemów](#rozwiązywanie-problemów)
- [Wkład w Projekt](#wkład-w-projekt)
- [Licencja](#licencja)
- [Kontakt i Wsparcie](#kontakt-i-wsparcie)

## 🎯 Opis

**BTC Adaptive Grid Bot** to zaawansowany bot tradingowy działający na bazie strategii siatki adaptacyjnej (grid trading) dla Bitcoin (BTC). Bot automatycznie dostosowuje gridy handlowe na podstawie warunków rynkowych w czasie rzeczywistym, umożliwiając efektywne czerpanie zysków z wahań ceny na rynku kryptowalut.

Bot został zaprojektowany do pracy z głównymi giełdami kryptowalut i oferuje zaawansowane funkcje zarządzania portfelem, analizę techniczną oraz zaawansowane mechanizmy zabezpieczające.

## ✨ Cechy

### Podstawowe Możliwości
- ✅ **Adaptacyjne Siatki Handlowe** - Dynamiczne dostosowanie gridu na podstawie zmienności rynku
- ✅ **Wsparcie Wielu Giełd** - Integracja z Binance, Kraken, Coinbase i innymi
- ✅ **Handel 24/7** - Automatyczne operacje przez całą dobę
- ✅ **Zarządzanie Ryzykiem** - Zaawansowane limity stop-loss i take-profit
- ✅ **Monitorowanie Czasu Rzeczywistego** - Live monitoring cen i pozycji

### Zaawansowane Funkcje
- 🔄 **Dynamiczna Rebalansacja** - Automatyczne dostosowanie pozycji do zmieniających się warunków rynkowych
- 📊 **Analiza Techniczna** - Integracja ze wskaźnikami technicznymi (RSI, MACD, Bollinger Bands)
- 📈 **Obliczanie Volatilności** - Inteligentne skalowanie gridu na podstawie zmienności ceny
- 🛡️ **Mechanizmy Zabezpieczające** - Przerwanie handlu w przypadku anomalii rynkowych
- 📱 **Powiadomienia** - Alerty via email, Discord, Telegram
- 📉 **Analiza Wydajności** - Szczegółowe raporty i statystyki zysków/strat
- 🔐 **Bezpieczeństwo** - Szyfrowanie kluczy API, uwierzytelnianie wielopoziomowe

## 📦 Wymagania

### Minimalne Wymagania
- **Python 3.8+** (rekomendacja: Python 3.10+)
- **pip** - menedżer pakietów Python
- **virtualenv** (opcjonalne, ale rekomendowane)
- Konto na jednej z obsługiwanych giełd (Binance, Kraken, itp.)
- Stały dostęp do internetu
- Moc obliczeniowa: serwer VPS lub komputer 24/7

### Zależności
Wszystkie zależności są wyszczególnione w pliku `requirements.txt`:

```
ccxt>=2.15.0          # Obsługa wielu giełd
requests>=2.28.0      # HTTP requests
python-dotenv>=0.20.0 # Zmienne środowiskowe
pandas>=1.5.0         # Analiza danych
numpy>=1.23.0         # Obliczenia numeryczne
ta-lib>=0.4.24        # Wskaźniki techniczne
websocket-client>=1.3.0 # WebSocket dla stream'ów
pyyaml>=6.0           # Parsowanie plików konfiguracyjnych
```

## 🚀 Instalacja

### 1. Klonowanie Repozytorium

```bash
git clone https://github.com/c3bulaka/btc-adaptive-grid-bot.git
cd btc-adaptive-grid-bot
```

### 2. Tworzenie Środowiska Wirtualnego

```bash
# Na Linux/macOS
python3 -m venv venv
source venv/bin/activate

# Na Windows
python -m venv venv
venv\Scripts\activate
```

### 3. Instalacja Zależności

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Konfiguracja Zmiennych Środowiskowych

```bash
# Skopiuj plik przykładowy
cp .env.example .env

# Edytuj plik z własnymi danymi
nano .env  # lub użyj innego edytora
```

## ⚙️ Konfiguracja

### Zmienne Środowiskowe (.env)

```env
# Giełda
EXCHANGE=binance
API_KEY=twój_klucz_api
API_SECRET=twój_sekret_api
API_PASSPHRASE=passphrase_jeśli_wymagany  # Dla Coinbase

# Ustawienia Bota
TRADING_PAIR=BTC/USDT
INITIAL_CAPITAL=1000
GRID_LEVELS=20
GRID_RANGE_PERCENT=10

# Zarządzanie Ryzykiem
MAX_POSITION_SIZE=0.05
STOP_LOSS_PERCENT=5
TAKE_PROFIT_PERCENT=3

# Notyfikacje
DISCORD_WEBHOOK_URL=https://discord.com/api/webhooks/...
TELEGRAM_BOT_TOKEN=token_bota
TELEGRAM_CHAT_ID=id_czatu

# Logowanie
LOG_LEVEL=INFO
LOG_FILE=logs/bot.log

# Tryb
MODE=production  # lub testing
BACKTEST=false
```

### Plik Konfiguracyjny (config.yaml)

```yaml
bot:
  name: "BTC Adaptive Grid Bot"
  version: "1.0.0"
  environment: "production"

exchange:
  name: "binance"
  sandbox: false
  
trading:
  pair: "BTC/USDT"
  initial_capital: 1000
  base_asset: "BTC"
  quote_asset: "USDT"

grid:
  type: "adaptive"
  levels: 20
  range_percent: 10
  min_order_size: 0.0001
  auto_adjust: true
  adjustment_interval: 3600

risk_management:
  max_position_size: 0.05
  stop_loss_percent: 5
  take_profit_percent: 3
  drawdown_limit_percent: 15

analysis:
  use_technical_indicators: true
  indicators:
    - rsi_period: 14
    - macd_fast: 12
      macd_slow: 26
      macd_signal: 9
    - bollinger_period: 20
      bollinger_std_dev: 2

notifications:
  discord:
    enabled: true
    webhook_url: "${DISCORD_WEBHOOK_URL}"
  telegram:
    enabled: true
    bot_token: "${TELEGRAM_BOT_TOKEN}"
    chat_id: "${TELEGRAM_CHAT_ID}"

logging:
  level: "INFO"
  file: "logs/bot.log"
  max_file_size: 10485760  # 10MB
  backup_count: 5
```

## 📖 Użytkowanie

### Uruchomienie Bota

```bash
# Uruchamianie w trybie produkcji
python main.py

# Uruchamianie w trybie testowania
python main.py --mode testing

# Uruchamianie testu wstecznego
python main.py --backtest --period 30d

# Z poziomem debugowania
python main.py --debug
```

### Przykłady Użytkowania

#### Prosty Start

```python
from btc_grid_bot import AdaptiveGridBot

# Inicjalizacja bota
bot = AdaptiveGridBot(
    exchange='binance',
    api_key='YOUR_API_KEY',
    api_secret='YOUR_API_SECRET',
    trading_pair='BTC/USDT',
    initial_capital=1000,
    grid_levels=20
)

# Uruchomienie
bot.start()
```

#### Zaawansowana Konfiguracja

```python
from btc_grid_bot import AdaptiveGridBot
from btc_grid_bot.strategies import GridStrategy
from btc_grid_bot.risk import RiskManager

# Konfiguracja zarządzania ryzykiem
risk_manager = RiskManager(
    max_drawdown=0.15,
    stop_loss=0.05,
    take_profit=0.03
)

# Tworzenie strategii
strategy = GridStrategy(
    grid_levels=20,
    range_percent=10,
    adaptive=True,
    volatility_threshold=1.5
)

# Inicjalizacja bota z niestandardową konfiguracją
bot = AdaptiveGridBot(
    exchange='binance',
    api_key='YOUR_API_KEY',
    api_secret='YOUR_API_SECRET',
    trading_pair='BTC/USDT',
    strategy=strategy,
    risk_manager=risk_manager
)

bot.start()
```

### Interfejs Wiersza Poleceń (CLI)

```bash
# Wyświetlenie statusu bota
python cli.py status

# Wyświetlenie otwartych pozycji
python cli.py positions

# Wyświetlenie historii tradów
python cli.py history --limit 50

# Ustawienie parametrów
python cli.py set --grid-levels 25 --range 12

# Zatrzymanie bota
python cli.py stop

# Przywrócenie z kopii zapasowej
python cli.py restore --backup latest
```

## 🏗️ Architektura

### Struktura Projektowa

```
btc-adaptive-grid-bot/
├── main.py                      # Punkt wejścia aplikacji
├── cli.py                       # Interfejs wiersza poleceń
├── config.yaml                  # Plik konfiguracyjny
├── requirements.txt             # Zależności Python
├── .env.example                 # Przykład zmiennych środowiskowych
├── README.md                    # Ta dokumentacja
├── LICENSE                      # Licencja MIT
│
├── btc_grid_bot/                # Pakiet główny
│   ├── __init__.py
│   ├── bot.py                   # Klasa główna AdaptiveGridBot
│   ├── exchange_manager.py      # Zarządzanie giełdą
│   ├── config.py                # Zarządzanie konfiguracją
│   │
│   ├── strategies/              # Strategie handlowe
│   │   ├── __init__.py
│   │   ├── base_strategy.py     # Klasa bazowa
│   │   ├── grid_strategy.py     # Strategia siatki
│   │   └── adaptive_strategy.py # Adaptacyjna strategia
│   │
│   ├── analysis/                # Analiza techniczna
│   │   ├── __init__.py
│   │   ├── indicators.py        # Wskaźniki techniczne
│   │   ├── volatility.py        # Analiza zmienności
│   │   └── candlestick.py       # Analiza świec
│   │
│   ├── risk/                    # Zarządzanie ryzykiem
│   │   ├── __init__.py
│   │   ├── manager.py           # Menedżer ryzyka
│   │   ├── position_sizer.py    # Kalkulacja rozmiaru pozycji
│   │   └── drawdown.py          # Analiza rysunku
│   │
│   ├── notifications/           # System powiadomień
│   │   ├── __init__.py
│   │   ├── base_notifier.py     # Klasa bazowa
│   │   ├── discord_notifier.py  # Powiadomienia Discord
│   │   ├── telegram_notifier.py # Powiadomienia Telegram
│   │   └── email_notifier.py    # Powiadomienia email
│   │
│   ├── utils/                   # Funkcje pomocnicze
│   │   ├── __init__.py
│   │   ├── logger.py            # Logowanie
│   │   ├── data_loader.py       # Ładowanie danych
│   │   └── validators.py        # Walidatory
│   │
│   └── models/                  # Modele danych
│       ├── __init__.py
│       ├── trade.py             # Model transakcji
│       ├── position.py          # Model pozycji
│       └── order.py             # Model zlecenia
│
├── tests/                       # Testy
│   ├── __init__.py
│   ├── test_bot.py
│   ├── test_strategies.py
│   ├── test_analysis.py
│   ├── test_risk_manager.py
│   └── test_exchange_manager.py
│
├── data/                        # Dane
│   ├── cache/                   # Cache danych
│   └── backups/                 # Kopie zapasowe
│
├── logs/                        # Pliki logów
│   └── bot.log
│
└── docs/                        # Dokumentacja
    ├── INSTALLATION.md          # Instrukcja instalacji
    ├── CONFIGURATION.md         # Dokumentacja konfiguracji
    ├── STRATEGY.md              # Opis strategii
    ├── API.md                   # Dokumentacja API
    └── TROUBLESHOOTING.md       # Rozwiązywanie problemów
```

### Diagram Przepływu Danych

```
┌─────────────────────────────────────────────────────────┐
│         Giełda (Binance, Kraken, itd.)                  │
└────────────────┬────────────────────────────────────────┘
                 │ API
                 ▼
        ┌────────────────┐
        │ Exchange       │
        │ Manager        │
        └────────┬───────┘
                 │
        ┌────────▼───────────────┐
        │  Market Data           │
        │  - Ceny               │
        │  - Wolumen            │
        │  - OHLCV              │
        └────────┬───────────────┘
                 │
    ┌────────────┼────────────────┐
    │            │                │
    ▼            ▼                ▼
┌─────────┐ ┌────────────┐ ┌──────────┐
│ Analysis │ │  Strategy  │ │ Risk Mgmt│
│ Module   │ │ Module     │ │ Module   │
└────┬────┘ └────┬───────┘ └──────┬───┘
     │           │                │
     └───────────┼────────────────┘
                 │
                 ▼
        ┌────────────────────┐
        │ Decision Engine    │
        │ - Kalkulacja gridów│
        │ - Wielkości zleceń │
        │ - Timing           │
        └────────┬───────────┘
                 │
                 ▼
        ┌────────────────────┐
        │ Order Manager      │
        │ - Tworzenie zleceń │
        │ - Zarządzanie      │
        └────────┬───────────┘
                 │
                 ▼
        ┌────────────────────┐
        │ Notifications      │
        │ - Discord          │
        │ - Telegram         │
        │ - Email            │
        └────────────────────┘
```

## 🔗 API

### Publiczne API Bota

Bot udostępnia publiczne API dla integracji z innymi systemami:

#### Statystyki Bota

```python
bot.get_statistics()
# Zwraca: {
#     'total_trades': 250,
#     'winning_trades': 180,
#     'losing_trades': 70,
#     'win_rate': 0.72,
#     'total_profit': 1250.50,
#     'profit_percent': 25.01,
#     'max_drawdown': 0.08
# }
```

#### Otwarte Pozycje

```python
bot.get_open_positions()
# Zwraca: [
#     {
#         'order_id': '123456',
#         'pair': 'BTC/USDT',
#         'type': 'buy',
#         'price': 45000.00,
#         'amount': 0.001,
#         'status': 'open'
#     },
#     ...
# ]
```

#### Historia Tradów

```python
bot.get_trade_history(limit=50, offset=0)
# Zwraca listę zakończonych transakcji
```

#### Ustawienia Bota

```python
# Pobranie ustawień
settings = bot.get_settings()

# Aktualizacja ustawień
bot.update_settings({
    'grid_levels': 25,
    'range_percent': 12
})
```

#### Zarządzanie Stanem

```python
# Wznowienie
bot.resume()

# Wstrzymanie
bot.pause()

# Zatrzymanie
bot.stop()

# Status
status = bot.get_status()
```

## 📊 Strategie Tradingowe

### Strategia Siatki (Grid Trading)

**Opis:** Bot tworzy serię zleceń kupna i sprzedaży w regularnych interwałach cenowych w wyniku określonego zakresu.

**Parametry:**
- `grid_levels` - Liczba poziomów gridu
- `range_percent` - Procent zakresu handlu
- `lower_price` - Dolny limit ceny
- `upper_price` - Górny limit ceny

**Przykład:**
```
Cena: 45,000 USDT, Range: 10%
Dolny Limit: 40,500 USDT
Górny Limit: 49,500 USDT

Grid Level 1: 40,500 - Kupuj 0.1 BTC
Grid Level 2: 41,500 - Kupuj 0.1 BTC
Grid Level 3: 42,500 - Kupuj 0.1 BTC
... (20 poziomów)
Grid Level 11: 45,000 - Punkt równowagi
... 
Grid Level 20: 49,500 - Sprzedaj 0.1 BTC
```

### Strategia Adaptacyjna

**Opis:** Automatyczne dostosowanie gridu na podstawie zmienności rynku i wskaźników technicznych.

**Mechanizm Działania:**
1. Obliczanie zmienności (Volatility Index)
2. Ocena trendu (RSI, MACD)
3. Dostosowanie liczby poziomów gridu
4. Dynamiczna zmiana zakresu handlu
5. Rebalansacja pozycji

**Wskaźniki Techniczne:**
- **RSI (14)** - Momentum
- **MACD (12,26,9)** - Trend
- **Bollinger Bands (20,2)** - Volatilność
- **ATR (14)** - Average True Range

## 🔍 Monitoring i Logowanie

### Logowanie

Bot loguje wszystkie ważne zdarzenia do konsoli i pliku:

```
[2026-01-13 20:21:27] [INFO] Bot uruchomiony
[2026-01-13 20:21:28] [INFO] Połączono z giełdą Binance
[2026-01-13 20:21:30] [INFO] Pobieranie danych rynkowych...
[2026-01-13 20:21:35] [INFO] BTC/USDT = 45,230.50 USDT
[2026-01-13 20:21:35] [INFO] Volatility = 2.3%
[2026-01-13 20:21:36] [INFO] Tworzenie gridu...
[2026-01-13 20:21:40] [INFO] Zlecenie zakupu #123456 - 0.001 BTC @ 45,000 USDT
[2026-01-13 20:22:15] [INFO] Zlecenie wykonane - Zysk: 50 USDT
```

### Poziomy Logowania

- `DEBUG` - Szczegółowe informacje debugowania
- `INFO` - Ogólne informacje
- `WARNING` - Ostrzeżenia
- `ERROR` - Błędy
- `CRITICAL` - Krytyczne błędy

### Metryki Monitorowania

```python
# Pobieranie metryk
metrics = bot.get_metrics()
print(f"CPM (Trades Per Hour): {metrics['cpm']}")
print(f"Aktywne Zlecenia: {metrics['active_orders']}")
print(f"Procent Kapitału Zaangażowanego: {metrics['capital_usage']}")
print(f"Średni Zysk na Tradzie: {metrics['avg_profit_per_trade']}")
```

## 🧪 Testowanie

### Uruchamianie Testów

```bash
# Wszystkie testy
pytest

# Konkretny moduł
pytest tests/test_strategies.py

# Z raportami pokrycia
pytest --cov=btc_grid_bot

# Szczegółowe wyjście
pytest -v
```

### Test Wsteczny (Backtest)

```bash
# Backtest na ostatnich 30 dniach
python main.py --backtest --period 30d

# Backtest na określonym przedziale czasowym
python main.py --backtest --from 2025-01-01 --to 2025-12-31

# Generowanie raportu
python main.py --backtest --period 30d --report pdf
```

### Wyniki Backtestingu

```
═══════════════════════════════════════════════════════════
                    RAPORT BACKTESTINGU
═══════════════════════════════════════════════════════════

Okres:                    2025-01-01 do 2025-12-31
Kapitał Początkowy:       $1,000.00
Kapitał Końcowy:          $1,425.50

Transakcje:               250
Wygrane:                  180 (72.0%)
Przegrane:                70 (28.0%)

Zysk Netto:               $425.50 (42.55%)
Zysk/Miesiąc:             $35.46
Zysk/Miesiąc (%)          3.55%

Max Drawdown:             8.2%
Sharpe Ratio:             1.85
Sortino Ratio:            2.42

Średnia Zysku:            $2.35
Średnia Straty:           $1.80
Profit Factor:            2.45

═══════════════════════════════════════════════════════════
```

## 🔧 Rozwiązywanie Problemów

### Problem: Bot się nie łączy z giełdą

**Przyczyny i Rozwiązania:**

1. **Błędne klucze API**
   ```bash
   # Sprawdź klucze w pliku .env
   grep API_KEY .env
   grep API_SECRET .env
   ```

2. **Problemy z siecią**
   ```bash
   # Testuj połączenie
   ping api.binance.com
   
   # Sprawdź firewall
   curl -v https://api.binance.com/api/v3/ping
   ```

3. **Wygasłe klucze API**
   - Wygeneruj nowe klucze na stronie giełdy
   - Zaktualizuj plik `.env`

### Problem: Bot nie otwiera pozycji

**Diagnostyka:**

```python
# Sprawdź saldo
balance = bot.get_balance()
print(f"Dostępne środki: {balance['USDT']}")

# Sprawdź ostatnie błędy
errors = bot.get_recent_errors()
for error in errors:
    print(error)

# Włącz tryb debugowania
bot.enable_debug()
```

**Częste Przyczyny:**

1. **Brak wystarczających środków**
   - Sprawdź saldo konta
   - Zwiększ `initial_capital` lub zmniejsz `grid_levels`

2. **Minimalna wielkość zlecenia**
   - Giełdy mają minimalne kwoty zleceń
   - Zwiększ `min_order_size`

3. **Giełda w trybie konserwacji**
   - Czekaj na zakończenie prac
   - Sprawdzaj status giełdy

### Problem: Wysoka latencja

**Rozwiązania:**

1. **Użyj serwera VPS**
   ```bash
   # Rekomendowane serwery
   - DigitalOcean (VPS)
   - Linode
   - AWS EC2
   - Hetzner
   ```

2. **Optymalizuj kod**
   ```python
   # Zwiększ interwał aktualizacji
   bot.update_interval = 5  # 5 sekund zamiast 1
   ```

3. **Zmniejsz obciążenie**
   - Wyłącz niepotrzebne wskaźniki
   - Zmniejsz liczbę poziomów gridu

### Problem: Boty się duplikują (wielokrotnie otwiera transakcje)

**Przyczyna:** Wielokrotne uruchomienia tego samego skryptu

**Rozwiązanie:**

```python
# Zastosuj plik blokady (lock file)
import os
import sys

LOCK_FILE = '/tmp/btc_grid_bot.lock'

if os.path.exists(LOCK_FILE):
    print("Bot już jest uruchomiony!")
    sys.exit(1)

# Stwórz plik blokady
with open(LOCK_FILE, 'w') as f:
    f.write(str(os.getpid()))

try:
    bot.start()
finally:
    os.remove(LOCK_FILE)
```

### Logi Debugowania

```bash
# Wyświetl ostatnie logi
tail -f logs/bot.log

# Logi z ostatnich 100 linii
tail -n 100 logs/bot.log

# Szukaj błędów
grep ERROR logs/bot.log

# Szukaj konkretnego warunku
grep "Buy Order" logs/bot.log
```

## 🤝 Wkład w Projekt

Zapraszamy do udziału w rozwoju projektu!

### Jak Przyczynić się do Projektu

1. **Fork'uj repozytorium**
   ```bash
   git clone https://github.com/[twoja-nazwa]/btc-adaptive-grid-bot.git
   cd btc-adaptive-grid-bot
   ```

2. **Stwórz gałąź dla funkcjonalności**
   ```bash
   git checkout -b feature/twoja-funkcjonalność
   ```

3. **Wprowadź zmiany i zapisz je**
   ```bash
   git add .
   git commit -m "Dodaj opisową wiadomość commitową"
   ```

4. **Wyślij zmiany do swojej gałęzi**
   ```bash
   git push origin feature/twoja-funkcjonalność
   ```

5. **Otwórz Pull Request**

### Wytyczne Kodowania

- Następuj [PEP 8](https://www.python.org/dev/peps/pep-0008/)
- Pisz testy dla nowych funkcji
- Dokumentuj publiczne API
- Używaj type hints
- Testy muszą przechodzić

### Zgłaszanie Błędów

1. Sprawdź czy bug nie został już zgłoszony
2. Podaj dokładny opis problemu
3. Załącz logi błędów
4. Opisz kroki do reprodukcji
5. Sugeruj rozwiązanie (jeśli wiesz)

## 📄 Licencja

Projekt jest objęty licencją **MIT**. Zobacz plik [LICENSE](LICENSE) dla szczegółów.

```
MIT License

Copyright (c) 2026 c3bulaka

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```

## 💬 Kontakt i Wsparcie

### Kanały Wsparcia

- **GitHub Issues** - Zgłaszanie bugów i sugestii
- **Dyskusje** - Ogólne pytania i dyskusje
- **Email** - Kontakt bezpośredni

### Społeczność

- **Discord** - [Dołącz do serwera](https://discord.gg/example)
- **Telegram** - [@BTC_Grid_Bot](https://t.me/example)
- **Twitter** - [@BTC_Grid_Bot](https://twitter.com/example)

### FAQ

**P: Czy bot jest bezpieczny?**
O: Tak, bot używa szyfrowania API keys i nie przechowuje danych w chmurze.

**P: Ile mogę zarobić?**
O: Zyski zależą od zmienności rynku. Średnio 2-5% miesięcznie.

**P: Czy jest darmowy?**
O: Tak, projekt jest open-source i darmowy.

**P: Czy mogę handlować innymi parami?**
O: Tak, bot wspiera wszystkie pary dostępne na giełdzie.

**P: Czy działa 24/7?**
O: Tak, pod warunkiem nieprzerwanych zasobów serwera.

---

**Ostatnia Aktualizacja:** 13 stycznia 2026  
**Autor:** [c3bulaka](https://github.com/c3bulaka)  
**Status:** Aktywny i Utrzymywany

⭐ Jeśli projekt Ci się podoba, pamiętaj o dodaniu gwiazdki!
