import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

from tarantino_analysis.charts import styled_barplot
from tarantino_analysis.config import DATA_DICTIONARY
from tarantino_analysis.data import build_data_check, build_genre_overview, build_movies_overview
from tarantino_analysis.ui import (
    notebook_cell,
    output_label,
    section_anchor,
    section_title,
    show_table,
    subsection_title,
)


def render_summary() -> None:
    section_anchor("summary")
    st.markdown('<h1 class="page-title">Tarantino F-words Overview</h1>', unsafe_allow_html=True)
    st.markdown(
        '<p class="subtitle">Exploratory analysis of profanity and death events across seven Quentin Tarantino films</p>',
        unsafe_allow_html=True,
    )

    section_title("Summary")
    st.markdown(
        """
This dataset contains records of profanity and death events across **7 Quentin Tarantino films**.
The dataset covers **60 unique profane words** and death events across films spanning multiple
genres like Crime, Action, War, and Western. This analysis aims to explore the level of
profanity in Tarantino films.
        """
    )

    subsection_title("Features", level=4)
    st.markdown(
        """
- **Movie** — Title of the Tarantino film in which the event occurred (7 unique films)
- **Type** — Category of the event: `word` (profane word spoken) or `death` (character died)
- **Word** — The specific profane word spoken; only populated when type == `word`
- **Minutes_in** — Timestamp (in minutes) within the film when the event occurred
        """
    )
    st.markdown('<hr class="section-rule">', unsafe_allow_html=True)


def render_eda(df: pd.DataFrame) -> None:
    section_anchor("eda")
    section_title("EDA")
    subsection_title("Data Exploration")
    st.markdown(
        """
During this step we explore the shape of the data we are working with. It is usual to check
and deal with the number of columns and rows, missing values, outliers, and other
inconsistencies that might appear.
        """
    )

    notebook_cell("df.shape")
    output_label()
    st.code(f"{df.shape}", language=None)

    notebook_cell("data_dictionary")
    output_label()
    show_table(
        pd.DataFrame({"Column": DATA_DICTIONARY.keys(), "Description": DATA_DICTIONARY.values()}),
    )

    notebook_cell("data_check")
    output_label()
    show_table(build_data_check(df))

    notebook_cell("df[death_mask]")
    output_label("Output — death events sample")
    show_table(df[df["type"] == "death"].head(10))

    notebook_cell("movie_list")
    output_label()
    st.write(list(df["movie"].unique()))

    st.markdown('<hr class="section-rule">', unsafe_allow_html=True)


def render_statistical_analysis(df: pd.DataFrame) -> None:
    section_anchor("statistical-analysis")
    section_title("Statistical Analysis")
    st.markdown(
        """
This step seeks to understand the relationships among the features through summary
metrics, grouped comparisons, and visualizations.
        """
    )

    movies_overview = build_movies_overview(df)
    genre_overview = build_genre_overview(movies_overview)

    subsection_title("Movie Overview", level=4)
    notebook_cell("movies_overview")
    output_label()
    show_table(movies_overview)

    subsection_title("Death vs F-word per Movie", level=5)
    plot_df = (
        movies_overview[["movie", "f_word_count", "death_count"]]
        .rename(columns={"f_word_count": "F-words", "death_count": "Deaths"})
        .melt(id_vars="movie", var_name="type", value_name="count")
    )
    _show_figure(
        styled_barplot(plot_df, "movie", "count", "type", "Death vs F words per Movie", (10, 6), "upper left")
    )

    subsection_title("Deaths per minute vs F-word per minute", level=5)
    plot_df_metrics = (
        movies_overview[["movie", "wpm", "dpm"]]
        .rename(columns={"wpm": "F-words per minute", "dpm": "Deaths per minute"})
        .melt(id_vars="movie", var_name="type", value_name="value")
    )
    _show_figure(
        styled_barplot(
            plot_df_metrics,
            "movie",
            "value",
            "type",
            "Death vs F-words Rate per minute",
            (10, 6),
            "upper left",
        )
    )

    subsection_title("Genre Overview", level=4)
    notebook_cell("genre_overview")
    output_label()
    show_table(genre_overview)

    subsection_title("Death vs F-word per Genre", level=5)
    plot_df_genre = (
        genre_overview[["genre", "f_word_count", "death_count"]]
        .rename(columns={"f_word_count": "F-words", "death_count": "Deaths"})
        .melt(id_vars="genre", var_name="type", value_name="count")
    )
    _show_figure(
        styled_barplot(plot_df_genre, "genre", "count", "type", "Death vs F-words per Genre", (10, 4), "upper right")
    )

    subsection_title("Deaths per minute vs F-word per minute", level=5)
    plot_df_rates = (
        genre_overview[["genre", "wpm", "dpm"]]
        .rename(columns={"wpm": "F-words per minute", "dpm": "Deaths per minute"})
        .melt(id_vars="genre", var_name="type", value_name="value")
    )
    _show_figure(
        styled_barplot(
            plot_df_rates,
            "genre",
            "value",
            "type",
            "Death vs F-words per minute",
            (10, 4),
            "upper right",
        )
    )

    st.markdown('<hr class="section-rule">', unsafe_allow_html=True)


def render_insights() -> None:
    section_anchor("insights")
    section_title("Insights")
    subsection_title("Statistics")
    st.markdown(
        """
- **Pulp Fiction**, **Reservoir Dogs**, and **Jackie Brown** are the movies with the most
  F-words per minute. They are also among the movies with the lowest number of deaths.
- While **Pulp Fiction** has the most F-words overall, **Reservoir Dogs** shows a rate of
  almost 5 F-words per minute, followed by Pulp Fiction with almost 3 and Jackie Brown with
  around 2.
- **Crime** is by far the most profane genre among Tarantino movies with +1,200 F-words and
  a rate of around 3 words per minute, followed by **Western**, with +200 words and a rate
  of almost 2.

---

*Thank you for taking the time to view this analysis. If you found it useful and have any
feedback or suggestions, don't hesitate to reach out — we are here to learn!*
        """
    )


def _show_figure(fig: plt.Figure) -> None:
    st.pyplot(fig)
    plt.close(fig)
