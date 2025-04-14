# Research Agent

A hybrid intelligent agent built with Streamlit, designed to assist academic researchers by autonomously retrieving relevant research papers from online sources.

---

## Features
- Query academic papers using Google Scholar via SerpApi
- Automatically falls back to scraping ArXiv if SerpApi fails
- Maintains internal state and adapts actions (model-based reflex agent)
- Save paper metadata locally with SQLite
- Export saved papers as CSV
- Clean and modular Python codebase

---

## Agent Architecture (Hybrid Design)

This system uses a **hybrid intelligent agent approach**:

- **Model-Based Reflex Logic:**
  - Reacts to user input with conditional actions
  - Maintains internal state with Streamlit's session state

- **Deliberative Reasoning:**
  - Makes autonomous decisions between structured API vs fallback scraping
  - Demonstrates awareness of environment state (API limits, failures)

This aligns with **Russell & Norvig's model-based reflex agent** definition while incorporating basic decision-making logic. Though no ML model is used, the agent exhibits adaptive, autonomous behavior.

---

## Tech Stack
- [Python 3.10+](https://www.python.org)
- [Streamlit](https://streamlit.io)
- [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/)
- [Pandas](https://pandas.pydata.org/)
- [SQLite](https://www.sqlite.org/index.html)
- [SerpApi](https://serpapi.com/) (Google Scholar engine)

---

## Setup Instructions

1. **Clone this repo**
```bash
git clone <repo-url>
cd ai-research-agent
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Add your SerpApi key** to a `.env` file:
```
SERPAPI_KEY=your_key_here
```

4. **Run the app**
```bash
PYTHONPATH=. streamlit run app/main.py
```

5. **Run tests**
```bash
PYTHONPATH=. pytest
```

---

## Ethical Considerations
- The agent defaults to using **Google Scholar via API**
- If that fails, it **only scrapes ArXiv**, a public open-access research archive
- This design avoids violating any terms of service

---

## Folder Structure
```
ai-research-agent/
├── app/
│   ├── main.py
│   ├── data_handler.py
│   └── db.py
├── tests/
│   ├── test_data_handler.py
│   └── test_db.py
├── papers.db
├── requirements.txt
├── .env
├── README.md
└── saved_papers.csv (optional)
```

---

## Screenshot Evidence
| Step | Screenshot |
|------|------------|
| App launched successfully | `01_home_screen.png` |
| SerpApi search results shown | `02_serpapi_success.png` |
| Paper saved to database | `03_save_paper_success.png` |
| Saved papers displayed | `04_saved_papers_list.png` |
| Exported to CSV | `05_export_success.png` |
| SerpApi failure triggers ArXiv fallback | `06_arxiv_fallback.png` |
| Error handling works (invalid input / network) | `07_error_handling.png` |
| Unit tests executed successfully | `08_pytest_output.png` |

---

## References
- Russell, S., & Norvig, P. (2021). *Artificial Intelligence: A Modern Approach* (4th ed.). Pearson.
- SerpApi Documentation. https://serpapi.com/
- ArXiv. https://arxiv.org/help/api/index
- Streamlit Documentation. https://docs.streamlit.io/
- BeautifulSoup Documentation. https://www.crummy.com/software/BeautifulSoup/

---

## License
MIT License
