import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

from tarantino_analysis.charts import styled_barplot
from tarantino_analysis.data import build_data_check, build_genre_overview, build_movies_overview
from tarantino_analysis.i18n import get_data_dictionary, t
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
    st.markdown(f'<h1 class="page-title">{t("page.title")}</h1>', unsafe_allow_html=True)
    st.markdown(f'<p class="subtitle">{t("page.subtitle")}</p>', unsafe_allow_html=True)

    section_title(t("section.summary.title"))
    st.markdown(t("section.summary.body"))

    subsection_title(t("section.features.title"), level=4)
    st.markdown(t("section.features.body"))
    st.markdown('<hr class="section-rule">', unsafe_allow_html=True)


def render_eda(df: pd.DataFrame) -> None:
    section_anchor("eda")
    section_title(t("section.eda.title"))
    subsection_title(t("section.eda.subtitle"))
    st.markdown(t("section.eda.body"))

    notebook_cell("df.shape")
    output_label()
    st.code(f"{df.shape}", language=None)

    notebook_cell("data_dictionary")
    output_label()
    data_dictionary = get_data_dictionary()
    show_table(
        pd.DataFrame({"Column": data_dictionary.keys(), "Description": data_dictionary.values()}).rename(
            columns={"Column": t("table.column"), "Description": t("table.description")}
        ),
    )

    notebook_cell("data_check")
    output_label()
    data_check = build_data_check(df)
    data_check.columns = [
        t("table.column"),
        t("table.data_type"),
        t("table.missing_values"),
        t("table.unique_values"),
        t("table.example_value"),
    ]
    show_table(data_check)

    notebook_cell("df[death_mask]")
    output_label(t("output.death_sample"))
    show_table(df[df["type"] == "death"].head(10))

    notebook_cell("movie_list")
    output_label()
    st.write(list(df["movie"].unique()))

    st.markdown('<hr class="section-rule">', unsafe_allow_html=True)


def render_statistical_analysis(df: pd.DataFrame) -> None:
    section_anchor("statistical-analysis")
    section_title(t("section.analysis.title"))
    st.markdown(t("section.analysis.body"))

    movies_overview = build_movies_overview(df)
    genre_overview = build_genre_overview(movies_overview)

    subsection_title(t("section.analysis.movie_overview"), level=4)
    notebook_cell("movies_overview")
    output_label()
    show_table(movies_overview)

    subsection_title(t("section.analysis.death_movie"), level=5)
    plot_df = (
        movies_overview[["movie", "f_word_count", "death_count"]]
        .rename(columns={"f_word_count": t("label.f_words"), "death_count": t("label.deaths")})
        .melt(id_vars="movie", var_name="type", value_name="count")
    )
    _show_figure(
        styled_barplot(
            plot_df,
            "movie",
            "count",
            "type",
            t("chart.death_fword_movie"),
            (10, 6),
            "upper left",
        )
    )

    subsection_title(t("section.analysis.rates_movie"), level=5)
    plot_df_metrics = (
        movies_overview[["movie", "wpm", "dpm"]]
        .rename(columns={"wpm": t("label.f_words_per_minute"), "dpm": t("label.deaths_per_minute")})
        .melt(id_vars="movie", var_name="type", value_name="value")
    )
    _show_figure(
        styled_barplot(
            plot_df_metrics,
            "movie",
            "value",
            "type",
            t("chart.rates_movie"),
            (10, 6),
            "upper left",
        )
    )

    subsection_title(t("section.analysis.genre_overview"), level=4)
    notebook_cell("genre_overview")
    output_label()
    show_table(genre_overview)

    subsection_title(t("section.analysis.death_genre"), level=5)
    plot_df_genre = (
        genre_overview[["genre", "f_word_count", "death_count"]]
        .rename(columns={"f_word_count": t("label.f_words"), "death_count": t("label.deaths")})
        .melt(id_vars="genre", var_name="type", value_name="count")
    )
    _show_figure(
        styled_barplot(
            plot_df_genre,
            "genre",
            "count",
            "type",
            t("chart.death_fword_genre"),
            (10, 4),
            "upper right",
        )
    )

    subsection_title(t("section.analysis.rates_movie"), level=5)
    plot_df_rates = (
        genre_overview[["genre", "wpm", "dpm"]]
        .rename(columns={"wpm": t("label.f_words_per_minute"), "dpm": t("label.deaths_per_minute")})
        .melt(id_vars="genre", var_name="type", value_name="value")
    )
    _show_figure(
        styled_barplot(
            plot_df_rates,
            "genre",
            "value",
            "type",
            t("chart.rates_genre"),
            (10, 4),
            "upper right",
        )
    )

    st.markdown('<hr class="section-rule">', unsafe_allow_html=True)


def render_insights() -> None:
    section_anchor("insights")
    section_title(t("section.insights.title"))
    subsection_title(t("section.insights.subtitle"))
    st.markdown(t("section.insights.body"))


def _show_figure(fig: plt.Figure) -> None:
    st.pyplot(fig)
    plt.close(fig)
