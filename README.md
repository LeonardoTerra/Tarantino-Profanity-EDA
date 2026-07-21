# Summary

A collection of EDAs with descriptive statistics and Machine Learning wrapped in interactive Streamlit apps.
Each project lives in its own subfolder and can be explored locally or deployed independently to Streamlit Cloud.

## Projects

| Project | Description | Streamlit App |
|---------|-------------|---------------|
| [tarantino-profanity](./tarantino-profanity/) | EDA of F-words and on-screen deaths across 7 Quentin Tarantino films | [tarantino-f-words.streamlit.app](https://tarantino-f-words.streamlit.app/) |

## Structure

```
tarantino-profanity/              # Tarantino profanity & deaths EDA
├── tarantino_f_words_overview_app.py
├── app.py                        # Backward-compatible alias
├── eda.ipynb                     # Exploratory analysis notebook
├── requirements.txt              # Project dependencies
├── tarantino_analysis/           # App modules (charts, data, i18n, etc.)
└── README.md
```
