from io import BytesIO

import pandas as pd
import streamlit as st

from tarantino_analysis.charts import configure_paper_plot_style
from tarantino_analysis.config import CSV_NAME, LOCAL_CSV_PATH
from tarantino_analysis.data import dataset_source_label, load_dataset, prepare_dataframe
from tarantino_analysis.i18n import t
from tarantino_analysis.report import render_eda, render_insights, render_statistical_analysis, render_summary
from tarantino_analysis.ui import apply_paper_style, render_sidebar


def resolve_dataset() -> pd.DataFrame | None:
    local_df = load_dataset()
    if local_df is not None:
        return local_df

    uploaded = st.session_state.get("uploaded_csv")
    if uploaded is None:
        return None

    if isinstance(uploaded, bytes):
        return pd.read_csv(BytesIO(uploaded))

    uploaded.seek(0)
    return pd.read_csv(uploaded)


def main() -> None:
    st.set_page_config(
        page_title="Tarantino F-words Overview",
        page_icon="🎬",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    if "language" not in st.session_state:
        st.session_state.language = "en"

    apply_paper_style()
    configure_paper_plot_style()

    source_file = dataset_source_label()
    render_sidebar(source_file)

    raw_df = resolve_dataset()
    if raw_df is None:
        st.error(t("error.missing_dataset", path=str(LOCAL_CSV_PATH), filename=CSV_NAME))
        return

    df = prepare_dataframe(raw_df)

    render_summary()
    render_eda(df)
    render_statistical_analysis(df)
    render_insights()
    apply_paper_style()


if __name__ == "__main__":
    main()
