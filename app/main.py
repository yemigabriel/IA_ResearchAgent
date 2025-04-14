import streamlit as st
from app.data_handler import search_papers
from app.db import init_db, save_paper, get_saved_papers
import os
import pandas as pd

# ---------- STREAMLIT UI ---------- #
def main():
    st.set_page_config(page_title="Research Agent", layout="centered")
    st.title("Development Individual Project: Academic Research Online")

    st.sidebar.header("Search Papers")
    query = st.sidebar.text_input("Enter search term")
    do_search = st.sidebar.button("Search")

    search_error = None

    if do_search and query:
        with st.spinner("Searching papers via SerpApi or fallback (ArXiv)..."):
            try:
                papers = search_papers(query)
                if isinstance(papers, str):
                    search_error = papers
                    st.session_state["papers"] = []
                else:
                    st.session_state["papers"] = papers
            except Exception as e:
                search_error = str(e)
                st.session_state["papers"] = []

    papers = st.session_state.get("papers", [])

    if search_error:
        st.error(f"Search failed: {search_error}")

    if papers:
        st.subheader("Search Results")
        for i, p in enumerate(papers):
            with st.expander(p['title']):
                st.write(p['snippet'])
                st.markdown(f"[Read full paper]({p['link']})")
                if st.button("Save this paper", key=f"save_{i}"):
                    save_paper(p)
                    st.success("Paper saved to database!")

    st.divider()
    st.subheader("Saved Papers")
    saved = get_saved_papers()
    st.dataframe(saved[['title', 'link', 'saved_at']])

    if not saved.empty:
        if st.button("Export as CSV"):
            saved.to_csv("saved_papers.csv", index=False)
            st.success("Exported to saved_papers.csv")

if __name__ == '__main__':
    init_db()
    main()
