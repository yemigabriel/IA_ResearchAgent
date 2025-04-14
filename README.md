# Development Individual Project: Research Agent

Agent built with Streamlit, designed to assist academic researchers by autonomously retrieving relevant research papers from online sources.

---

## Features
- Query academic papers using Google Scholar via SerpApi
- Automatically falls back to scraping ArXiv if SerpApi fails
- Maintains internal state and adapts actions (model-based reflex agent)
- Save paper metadata locally with SQLite
- Export saved papers as CSV

---

## Agent Architecture (Hybrid Design)

This system uses a **hybrid intelligent agent approach**:

- **Model-Based Reflex Logic:**
  - Reacts to user input with conditional actions
  - Maintains internal state with Streamlit's session state

- **Deliberative Reasoning:**
  - Makes autonomous decisions between structured API vs fallback scraping
  - Demonstrates awareness of environment state (API limits, failures)

Though no ML model is used, the agent exhibits adaptive, autonomous behavior.

---

## Tech Stack
- [Python 3.10+](https://www.python.org)
- [Streamlit](https://streamlit.io)
- [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/)
- [Pandas](https://pandas.pydata.org/)
- [SQLite](https://www.sqlite.org/index.html)
- [SerpApi](https://serpapi.com/) (Google Scholar engine)

---

## Demo

https://github.com/user-attachments/assets/beec6eb6-7784-4dc4-b0a4-90d8e3cb1d2a


---

## Setup Instructions

1. **Clone this repo**
```bash
git clone <repo-url>
cd IA_ResearchAgent
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
IA_ResearchAgent/
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
└──  README.md
```

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
