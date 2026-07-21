import html

import pandas as pd
import streamlit as st

from tarantino_analysis.config import CURSOR_LIGHT, LOCAL_CSV_PATH
from tarantino_analysis.i18n import get_sections, render_language_toggle, t


def build_paper_css() -> str:
    c = CURSOR_LIGHT
    return f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Source+Serif+4:ital,wght@0,400;0,600;0,700;1,400&family=IBM+Plex+Mono:wght@400;500&display=swap');

    :root {{
        color-scheme: light;
        --background-color: {c["page"]} !important;
        --secondary-background-color: {c["page"]} !important;
        --st-background-color: {c["page"]} !important;
        --st-secondary-background-color: {c["page"]} !important;
    }}

    .stApp,
    [data-testid="stApp"],
    html,
    body,
    #root,
    [data-testid="stAppViewContainer"],
    [data-testid="stAppViewContainer"] > section,
    [data-testid="stMain"],
    [data-testid="stMain"] > div,
    [data-testid="stHeader"],
    section[data-testid="stSidebar"],
    section[data-testid="stSidebar"] > div,
    [data-testid="stSidebarContent"],
    [data-testid="stSidebarUserContent"],
    [data-testid="stMainBlockContainer"],
    [data-testid="stVerticalBlock"],
    [data-testid="stVerticalBlockBorderWrapper"],
    [data-testid="stElementContainer"],
    .appview-container,
    .withScreencast,
    .main .block-container,
    .block-container,
    .stMainBlockContainer {{
        background-color: {c["page"]} !important;
        background: {c["page"]} !important;
        color: {c["text"]} !important;
    }}

    [data-testid="stMain"] .block-container,
    [data-testid="stMainBlockContainer"],
    .stMainBlockContainer,
    .block-container {{
        max-width: 920px;
        padding: 2.5rem 3rem 3rem 3rem;
        border: none !important;
        box-shadow: none !important;
        border-radius: 0 !important;
    }}

    [data-testid="stMain"] [data-testid="stMarkdownContainer"],
    [data-testid="stMain"] [data-testid="stMarkdownContainer"] p,
    [data-testid="stMain"] [data-testid="stMarkdownContainer"] li,
    [data-testid="stMain"] [data-testid="stMarkdownContainer"] ol,
    [data-testid="stMain"] [data-testid="stMarkdownContainer"] ul,
    [data-testid="stMain"] [data-testid="stMarkdownContainer"] span,
    [data-testid="stMain"] [data-testid="stMarkdownContainer"] em,
    [data-testid="stMain"] [data-testid="stMarkdownContainer"] strong,
    [data-testid="stMain"] [data-testid="stMarkdownContainer"] h1,
    [data-testid="stMain"] [data-testid="stMarkdownContainer"] h2,
    [data-testid="stMain"] [data-testid="stMarkdownContainer"] h3,
    [data-testid="stMain"] [data-testid="stMarkdownContainer"] h4,
    [data-testid="stMain"] [data-testid="stMarkdownContainer"] h5,
    [data-testid="stMain"] [data-testid="stMarkdownContainer"] h6,
    [data-testid="stMain"] .stMarkdown,
    [data-testid="stMain"] .stMarkdown p,
    [data-testid="stMain"] .stMarkdown li,
    [data-testid="stMain"] .stMarkdown h1,
    [data-testid="stMain"] .stMarkdown h2,
    [data-testid="stMain"] .stMarkdown h3,
    [data-testid="stMain"] .stMarkdown h4 {{
        color: {c["text"]} !important;
        font-family: 'Source Serif 4', Georgia, serif;
    }}

    [data-testid="stMain"] [data-testid="stMarkdownContainer"] h1,
    [data-testid="stMain"] .stMarkdown h1,
    [data-testid="stMain"] .page-title {{
        font-size: 1.85rem;
        font-weight: 700;
        letter-spacing: -0.02em;
        margin-bottom: 0.25rem;
        color: {c["text"]} !important;
    }}

    [data-testid="stMain"] [data-testid="stMarkdownContainer"] h2,
    [data-testid="stMain"] .stMarkdown h2,
    [data-testid="stMain"] .section-title {{
        font-size: 1.5rem;
        font-weight: 700;
        margin-top: 2.25rem;
        margin-bottom: 0.75rem;
        padding-bottom: 0.35rem;
        border-bottom: 1px solid {c["border"]};
        color: {c["text"]} !important;
    }}

    [data-testid="stMain"] [data-testid="stMarkdownContainer"] h3,
    [data-testid="stMain"] .stMarkdown h3,
    [data-testid="stMain"] .subsection-title-3 {{
        font-size: 1.1rem;
        font-weight: 600;
        margin-top: 1.35rem;
        margin-bottom: 0.55rem;
        color: {c["text_muted"]} !important;
    }}

    [data-testid="stMain"] [data-testid="stMarkdownContainer"] h4,
    [data-testid="stMain"] .stMarkdown h4,
    [data-testid="stMain"] .subsection-title-4 {{
        font-size: 1rem;
        font-weight: 600;
        margin-top: 1.15rem;
        margin-bottom: 0.45rem;
        color: {c["text_muted"]} !important;
    }}

    [data-testid="stMain"] [data-testid="stMarkdownContainer"] h5,
    [data-testid="stMain"] [data-testid="stMarkdownContainer"] h6,
    [data-testid="stMain"] .stMarkdown h5,
    [data-testid="stMain"] .subsection-title-5 {{
        font-size: 0.92rem;
        font-weight: 600;
        margin-top: 1rem;
        margin-bottom: 0.4rem;
        color: {c["text_muted"]} !important;
    }}

    [data-testid="stMain"] [data-testid="stMarkdownContainer"] p,
    [data-testid="stMain"] [data-testid="stMarkdownContainer"] li,
    [data-testid="stMain"] .stMarkdown p,
    [data-testid="stMain"] .stMarkdown li {{
        font-size: 0.95rem;
        line-height: 1.65;
        color: {c["text"]} !important;
    }}

    [data-testid="stMain"] pre,
    [data-testid="stMain"] code,
    [data-testid="stMain"] [data-testid="stCode"],
    [data-testid="stMain"] [data-testid="stCode"] pre {{
        color: {c["text"]} !important;
        background-color: {c["code_bg"]} !important;
        font-family: 'IBM Plex Mono', monospace !important;
        font-size: 0.85rem !important;
    }}

    [data-testid="stMain"] [data-testid="stAlert"] {{
        background-color: {c["header"]} !important;
        color: {c["text"]} !important;
        border: 1px solid {c["border"]};
    }}

    [data-testid="stMain"] [data-testid="stAlert"] p,
    [data-testid="stMain"] [data-testid="stAlert"] code {{
        color: {c["text"]} !important;
    }}

    .subtitle {{
        font-family: 'Source Serif 4', Georgia, serif;
        font-style: italic;
        color: {c["text_muted"]} !important;
        font-size: 0.95rem;
        margin-bottom: 1.25rem;
    }}

    .section-rule {{
        border: none;
        border-top: 1px solid {c["border"]};
        margin: 2rem 0;
    }}

    .notebook-cell {{
        background: {c["code_bg"]};
        border-left: 3px solid {c["border"]};
        padding: 0.65rem 0.9rem;
        margin: 0.85rem 0;
        font-family: 'IBM Plex Mono', monospace;
        font-size: 0.8rem;
        color: {c["text_muted"]} !important;
        overflow-x: auto;
    }}

    .output-label {{
        font-family: 'IBM Plex Mono', monospace;
        font-size: 0.68rem;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        color: {c["text_muted"]} !important;
        margin: 1rem 0 0.3rem 0;
    }}

    .paper-table {{
        width: 100%;
        border-collapse: collapse;
        margin: 0.25rem 0 1rem 0;
        font-family: 'Source Serif 4', Georgia, serif;
        font-size: 0.8125rem;
        color: {c["text"]};
        border: 1px solid {c["border"]};
        border-radius: 4px;
        overflow: hidden;
    }}

    .paper-table thead th {{
        background-color: {c["header"]};
        color: {c["text"]};
        font-weight: 600;
        border-bottom: 1px solid {c["border"]};
        padding: 8px 12px;
        text-align: left;
    }}

    .paper-table tbody td {{
        color: {c["text"]};
        border-top: 1px solid {c["border"]};
        padding: 8px 12px;
        vertical-align: top;
    }}

    .paper-table tbody tr:nth-child(even) td {{
        background-color: {c["row_alt"]};
    }}

    .paper-table tbody tr:nth-child(odd) td {{
        background-color: {c["surface"]};
    }}

    section[data-testid="stSidebar"] {{
        background-color: {c["page"]} !important;
        border-right: 1px solid {c["border"]};
    }}

    section[data-testid="stSidebar"] > div {{
        background-color: {c["page"]} !important;
    }}

    section[data-testid="stSidebar"] .stMarkdown,
    section[data-testid="stSidebar"] p,
    section[data-testid="stSidebar"] li,
    section[data-testid="stSidebar"] span,
    section[data-testid="stSidebar"] label,
    section[data-testid="stSidebar"] h1,
    section[data-testid="stSidebar"] h2,
    section[data-testid="stSidebar"] h3,
    section[data-testid="stSidebar"] [data-testid="stWidgetLabel"],
    section[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] {{
        color: {c["text"]} !important;
    }}

    section[data-testid="stSidebar"] h2 {{
        font-size: 1.05rem !important;
    }}

    section[data-testid="stSidebar"] h3 {{
        font-size: 0.9rem !important;
    }}

    section[data-testid="stSidebar"] p,
    section[data-testid="stSidebar"] li,
    section[data-testid="stSidebar"] [data-testid="stCaptionContainer"] {{
        font-size: 0.85rem !important;
        line-height: 1.5;
    }}

    section[data-testid="stSidebar"] code {{
        color: {c["text"]} !important;
        background-color: {c["code_bg"]} !important;
    }}

    section[data-testid="stSidebar"] a {{
        color: {c["text"]} !important;
        text-decoration: none;
    }}

    section[data-testid="stSidebar"] a:hover {{
        text-decoration: underline;
    }}
</style>
"""


def apply_paper_style() -> None:
    st.markdown(build_paper_css(), unsafe_allow_html=True)


def section_title(title: str) -> None:
    st.markdown(
        f'<h2 class="section-title">{html.escape(title)}</h2>',
        unsafe_allow_html=True,
    )


def subsection_title(title: str, *, level: int = 3) -> None:
    tag = f"h{level}"
    st.markdown(
        f'<{tag} class="subsection-title subsection-title-{level}">{html.escape(title)}</{tag}>',
        unsafe_allow_html=True,
    )


def section_anchor(section_id: str) -> None:
    st.markdown(f'<span id="{section_id}"></span>', unsafe_allow_html=True)


def notebook_cell(code: str) -> None:
    st.markdown(f'<div class="notebook-cell">{html.escape(code)}</div>', unsafe_allow_html=True)


def output_label(text: str | None = None) -> None:
    label = t("output.label") if text is None else text
    st.markdown(f'<p class="output-label">{html.escape(label)}</p>', unsafe_allow_html=True)


def format_cell(value: object) -> str:
    if value is None or (isinstance(value, float) and pd.isna(value)):
        return ""
    return html.escape(str(value))


def show_table(df: pd.DataFrame) -> None:
    headers = "".join(f"<th>{html.escape(str(col))}</th>" for col in df.columns)
    rows: list[str] = []

    for _, row in df.iterrows():
        cells = "".join(f"<td>{format_cell(value)}</td>" for value in row)
        rows.append(f"<tr>{cells}</tr>")

    st.markdown(
        f"""
        <table class="paper-table">
            <thead><tr>{headers}</tr></thead>
            <tbody>{''.join(rows)}</tbody>
        </table>
        """,
        unsafe_allow_html=True,
    )


def render_sidebar(source_file: str | None) -> None:
    with st.sidebar:
        st.markdown(f"### {t('language.label')}")
        render_language_toggle()

        st.divider()
        st.markdown(f"## {t('sidebar.contents')}")

        for index, section in enumerate(get_sections(), start=1):
            st.markdown(f"**[{index}. {section['title']}](#{section['id']})**")
            st.markdown(
                f'<p style="font-size:0.85rem;line-height:1.5;color:{CURSOR_LIGHT["text_muted"]};margin:0.2rem 0 0.65rem 0;">{section["description"]}</p>',
                unsafe_allow_html=True,
            )
            for subsection in section.get("subsections", []):
                st.markdown(
                    f'<p style="font-size:0.78rem;color:{CURSOR_LIGHT["text_muted"]};margin:0 0 0.15rem 0.75rem;">• {subsection}</p>',
                    unsafe_allow_html=True,
                )

        st.divider()
        st.markdown(f"### {t('sidebar.data')}")

        if source_file:
            st.markdown(f"{t('sidebar.local_file')}: `{source_file}`")
        else:
            st.markdown(f"{t('sidebar.expected_file')}: `{LOCAL_CSV_PATH.name}`")
            st.caption(t("sidebar.upload_hint"))
            uploaded = st.file_uploader(t("sidebar.upload_label"), type=["csv"], label_visibility="collapsed")
            if uploaded is not None:
                st.session_state["uploaded_csv"] = uploaded.getvalue()
