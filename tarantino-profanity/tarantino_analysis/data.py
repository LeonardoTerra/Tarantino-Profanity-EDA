from pathlib import Path

import pandas as pd
import streamlit as st

from tarantino_analysis.config import CSV_NAME, LOCAL_CSV_PATH, MOVIE_GENRE


def resolve_local_csv_path() -> Path | None:
    if LOCAL_CSV_PATH.is_file():
        return LOCAL_CSV_PATH

    matches = sorted(LOCAL_CSV_PATH.parent.glob("*Tarantino*.csv"))
    return matches[0] if matches else None


@st.cache_data(show_spinner="Loading local dataset…")
def load_data_from_local(csv_path: str) -> pd.DataFrame:
    return pd.read_csv(csv_path)


def load_dataset() -> pd.DataFrame | None:
    local_csv = resolve_local_csv_path()
    if local_csv is not None:
        return load_data_from_local(str(local_csv))
    return None


def prepare_dataframe(raw_df: pd.DataFrame) -> pd.DataFrame:
    df = raw_df.copy()
    df["word"] = df["word"].fillna("None")
    df["genre"] = df["movie"].map(lambda movie: MOVIE_GENRE.get(movie, "Unknown"))
    return df


def build_data_check(df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame(
        {
            "Column": [str(col) for col in df.columns],
            "Data Type": [str(df[col].dtype) for col in df.columns],
            "Missing Values": [f"{df[col].isna().mean() * 100:.1f}%" for col in df.columns],
            "Unique Values": [str(df[col].nunique()) for col in df.columns],
            "Example Value": [
                str(df[col].dropna().iloc[0]) if df[col].notna().any() else ""
                for col in df.columns
            ],
        }
    )


def build_movies_overview(df: pd.DataFrame) -> pd.DataFrame:
    overview = (
        df.groupby(["movie", "genre"])
        .agg(
            f_word_count=("type", lambda values: (values == "word").sum()),
            duration_min=("minutes_in", "max"),
            death_count=("type", lambda values: (values == "death").sum()),
        )
        .reset_index()
    )
    overview["wpm"] = (overview["f_word_count"] / overview["duration_min"]).round(2)
    overview["dpm"] = (overview["death_count"] / overview["duration_min"]).round(2)
    return overview


def build_genre_overview(movies_overview: pd.DataFrame) -> pd.DataFrame:
    overview = (
        movies_overview.groupby("genre")
        .agg(
            f_word_count=("f_word_count", "sum"),
            duration_min=("duration_min", "sum"),
            death_count=("death_count", "sum"),
        )
        .reset_index()
    )
    overview["wpm"] = (overview["f_word_count"] / overview["duration_min"]).round(2)
    overview["dpm"] = (overview["death_count"] / overview["duration_min"]).round(2)
    return overview


def dataset_source_label() -> str | None:
    local_csv = resolve_local_csv_path()
    if local_csv is None:
        return None
    return local_csv.name
