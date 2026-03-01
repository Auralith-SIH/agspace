<p align="center">
   <img src="assets/agspace-logo.png" width="180" alt="AGSpace Logo">
</p>

<h1 align="center">AGSpace 🚀</h1>

<p align="center">
  A lightweight, beginner-friendly Python toolkit for space-data analysis, astronomy calculations, and NASA/ISRO API integration.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/python-3.8+-blue.svg" />
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg" />
  <img src="https://img.shields.io/github/stars/Auralith-SIH/agspace?style=social" />
  <img src="https://github.com/Auralith-SIH/agspace/actions/workflows/ci.yml/badge.svg" />
  <img src="https://img.shields.io/badge/Status-Active-success" />
  <img src="https://img.shields.io/badge/Maintained-Yes-green" />
</p>

---

## 🧾 Authorship & Ownership

- **Maintainer / Primary Author:** **ARUSHIGULBHILE** (AURALITH Team)  
- **Repository:** `Auralith-SIH/agspace`  
- **GitHub:** [ARUSHIGULBHILE](https://github.com/ARUSHIGULBHILE)  
- **Status:** Active (student project)

> ✅ This README is authored and maintained by **ARUSHIGULBHILE**.  
> ✅ Claims are traceable via links + repository commit history.

---

## 📌 Overview

**AGSpace** is a modular Python toolkit designed to help beginners explore space-data workflows.  
It provides simple functions for:

- NASA APOD (Astronomy Picture of the Day)
- Space-weather simulation for prototyping
- Satellite position utilities (prototype)

---

## 📑 Table of Contents

- [✨ Features](#-features)
- [📦 Installation](#-installation)
- [⚡ Quick Start](#-quick-start)
- [🧠 Basic Usage](#-basic-usage)
- [📚 API Reference](#-api-reference)
- [📡 Supported APIs](#-supported-apis)
- [📁 Project Structure](#-project-structure)
- [📖 Examples](#-examples)
- [📝 Configuration & API Keys](#-configuration--api-keys)
- [🤝 Contributing](#-contributing)
- [🗂 Changelog](#-changelog)
- [📊 Roadmap](#-roadmap)
- [🏗 Built With](#-built-with)
- [❓ FAQ](#-faq)
- [📄 License](#-license)
- [📬 Contact](#-contact)

---

## ✨ Features

- 🛰️ **NASA APOD Integration** — Fetch Astronomy Picture of the Day
- 🧯 **Safe Fallback Mode** — Returns demo data if NASA API fails
- 🌌 **Space Weather (Prototype)** — Simulated solar activity data
- 📡 **Satellite Tracking (Prototype)** — ISS position utility (simulated for now)
- 🎯 **Beginner Friendly** — Simple functions, clean outputs, easy docs
- 🧩 **Modular** — Easy to extend with new APIs/modules

---

## 📦 Installation

> ⚠️ Note: The name `spacekit` already exists on PyPI (belongs to someone else).  
> Install **AGSpace** from GitHub:

```bash
pip install git+https://github.com/Auralith-SIH/agspace.git
```

### For local development (contributors)

```bash
git clone https://github.com/Auralith-SIH/agspace.git
cd agspace
pip install -e .
```

---

## ⚡ Quick Start

```python
import agspace

apod = agspace.get_apod_safe()
print("APOD Title:", apod["title"])

weather = agspace.get_space_weather()
print("Solar flares:", weather["solar_flares"])

iss = agspace.satellite_position("ISS")
print("ISS Latitude:", iss["latitude"])
```

---

## 🧠 Basic Usage

### 1) Get NASA APOD

```python
from agspace import get_apod

# Uses NASA DEMO_KEY by default (rate limited)
data = get_apod()
print(data["title"])
```

### 2) Get NASA APOD (Safe Mode)

```python
from agspace import get_apod_safe

# Always returns data, even if NASA API fails
data = get_apod_safe()
print(data["title"])
```

### 3) Space Weather (Prototype)

> Status: **Simulated** output for testing/demo purposes.

```python
from agspace import get_space_weather

weather = get_space_weather()
print(weather)
```

### 4) Satellite Position (Prototype)

> Status: **Simulated** output for testing/demo purposes.

```python
from agspace import satellite_position

iss = satellite_position("ISS")
print(iss)
```

---

## 📚 API Reference

### `get_apod(api_key="DEMO_KEY")`
Fetch NASA APOD.

**Parameters**
- `api_key` (string): NASA API key (default `DEMO_KEY`)

**Returns**
- dict: APOD payload

```python
from agspace import get_apod
print(get_apod(api_key="YOUR_NASA_API_KEY")["title"])
```

---

### `get_apod_safe()`
Always returns APOD data; falls back to demo data if NASA API fails.

```python
from agspace import get_apod_safe
print(get_apod_safe()["title"])
```

---

### `get_space_weather()`
Prototype simulated space-weather output.

```python
from agspace import get_space_weather
print(get_space_weather())
```

---

### `satellite_position(satellite_name)`
Prototype satellite position output.

```python
from agspace import satellite_position
print(satellite_position("ISS"))
```

---

## 📡 Supported APIs

| Feature       | Function               | Status          | Description                      |
|---------------|------------------------|-----------------|----------------------------------|
| NASA APOD     | `get_apod()`           | ✅ Working     | Astronomy Picture of the Day     |
| Safe APOD     | `get_apod_safe()`      | ✅ Working     | Demo fallback                    |
| Space Weather | `get_space_weather()`  | 🟡 Prototype   | Simulated demo output            |
| ISS Tracking  | `satellite_position()` | 🟡 Prototype   | Simulated demo output            |

---

## 📁 Project Structure

```text
agspace/
├── agspace/
│   ├── __init__.py
│   ├── nasa.py
│   └── astronomy.py
├── requirements.txt
├── setup.py
├── tests/
└── README.md
```

---

## 📖 Examples

### Full Demo Script

```python
from agspace import get_apod_safe, get_space_weather, satellite_position

print("🚀 AGSpace Demo")
print("APOD:", get_apod_safe()["title"])
print("Weather:", get_space_weather()["solar_flares"])
print("ISS:", satellite_position("ISS")["latitude"])
```

### Real-time ISS Tracker (Prototype Loop)

```python
import time
from agspace import satellite_position

while True:
    pos = satellite_position("ISS")
    print(f"ISS: {pos['latitude']}, {pos['longitude']}")
    time.sleep(10)
```

---

## 📝 Configuration & API Keys

### NASA API Key

Get your free key: https://api.nasa.gov

```python
from agspace import get_apod
print(get_apod(api_key="YOUR_NASA_API_KEY")["title"])
```

---

## 🤝 Contributing

1. Fork the repository  
2. Create a branch:
   ```bash
   git checkout -b feature/my-feature
   ```
3. Commit:
   ```bash
   git commit -m "Add my feature"
   ```
4. Push:
   ```bash
   git push origin feature/my-feature
   ```
5. Open a Pull Request

---

## 🗂 Changelog

### v0.1.0
- NASA APOD integration
- Safe fallback mode
- Prototype space weather + satellite tracking utilities
- CI workflow + smoke tests

---

## 📊 Roadmap

- [x] NASA APOD API integration (live data fetch)
- [x] Safe fallback mode (offline/demo never breaks)
- [x] CI workflow + basic tests (GitHub Actions)

- [ ] NASA endpoints expansion:
  - [ ] NEO (asteroid data)
  - [ ] Mars Rover Photos
  - [ ] EPIC (Earth imagery)

- [ ] Real satellite tracking:
  - [ ] TLE parsing + ISS real coordinates

- [ ] Real space-weather:
  - [ ] Replace simulated outputs with real data sources

- [ ] Visualization tools:
  - [ ] Simple charts / plots for outputs

- [ ] ISRO integration:
  - [ ] Add public ISRO datasets/endpoints where available

---

## 🏗 Built With

- Python 3.8+
- Requests
- Setuptools
- GitHub Actions (CI)

---

## ❓ FAQ

**Do I need a NASA API key?**  
No, but `DEMO_KEY` is rate-limited. Use your own for better access.

**Does it work offline?**  
NASA calls require internet. Prototype utilities may work without internet.

**Is it free?**  
Yes, MIT licensed.

---

## 📄 License

MIT License. See [LICENSE](LICENSE).

---

## 📬 Contact

- Issues: https://github.com/Auralith-SIH/agspace/issues  
- Maintainer: **ARUSHIGULBHILE** — https://github.com/ARUSHIGULBHILE  

---

<p align="center"><b>⭐ If you find this project useful, please star the repository! ⭐</b></p>
<p align="center">Built with ❤️ by students passionate about space technology.</p>
