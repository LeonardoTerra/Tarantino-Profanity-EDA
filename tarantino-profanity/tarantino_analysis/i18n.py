from __future__ import annotations

import streamlit as st

TRANSLATIONS: dict[str, dict[str, str]] = {
    "en": {
        "language.label": "Language",
        "language.switch_to": "Português",
        "language.current": "English",
        "sidebar.contents": "Contents",
        "sidebar.data": "Data",
        "sidebar.local_file": "Local file",
        "sidebar.expected_file": "Expected file",
        "sidebar.upload_hint": "Place the CSV next to the app script, or upload it below.",
        "sidebar.upload_label": "Upload dataset",
        "error.missing_dataset": (
            "Could not load the dataset. Expected file:\n\n`{path}`\n\n"
            "Save `{filename}` in the same folder as this app, or upload it in the sidebar."
        ),
        "page.title": "Tarantino F-words Overview",
        "page.subtitle": "Exploratory analysis of profanity and death events across seven Quentin Tarantino films",
        "section.summary.title": "Summary",
        "section.summary.description": "Dataset overview, feature definitions, and analysis goals.",
        "section.summary.body": (
            "This dataset contains records of profanity and death events across **7 Quentin Tarantino films**. "
            "The dataset covers **60 unique profane words** and death events across films spanning multiple "
            "genres like Crime, Action, War, and Western. This analysis aims to explore the level of "
            "profanity in Tarantino films."
        ),
        "section.features.title": "Features",
        "section.features.body": (
            "- **Movie** — Title of the Tarantino film in which the event occurred (7 unique films)\n"
            "- **Type** — Category of the event: `word` (profane word spoken) or `death` (character died)\n"
            "- **Word** — The specific profane word spoken; only populated when type == `word`\n"
            "- **Minutes_in** — Timestamp (in minutes) within the film when the event occurred"
        ),
        "section.eda.title": "EDA",
        "section.eda.description": "Shape, schema, data quality checks, and sample records.",
        "section.eda.subtitle": "Data Exploration",
        "section.eda.body": (
            "During this step we explore the shape of the data we are working with. It is usual to check "
            "and deal with the number of columns and rows, missing values, outliers, and other "
            "inconsistencies that might appear."
        ),
        "section.analysis.title": "Statistical Analysis",
        "section.analysis.description": "Movie and genre metrics with comparative bar charts.",
        "section.analysis.body": (
            "This step seeks to understand the relationships among the features through summary "
            "metrics, grouped comparisons, and visualizations."
        ),
        "section.analysis.sub.movies": "Movie overview",
        "section.analysis.sub.death_movie": "Death vs F-word per movie",
        "section.analysis.sub.rates_movies": "Rates per minute (movies)",
        "section.analysis.sub.genre": "Genre overview",
        "section.analysis.sub.death_genre": "Death vs F-word per genre",
        "section.analysis.sub.rates_genres": "Rates per minute (genres)",
        "section.analysis.movie_overview": "Movie Overview",
        "section.analysis.genre_overview": "Genre Overview",
        "section.analysis.death_movie": "Death vs F-word per Movie",
        "section.analysis.rates_movie": "Deaths per minute vs F-word per minute",
        "section.analysis.death_genre": "Death vs F-word per Genre",
        "section.insights.title": "Insights",
        "section.insights.description": "Key findings on profanity rates, deaths, and genre patterns.",
        "section.insights.subtitle": "Statistics",
        "section.insights.body": (
            "- **Pulp Fiction**, **Reservoir Dogs**, and **Jackie Brown** are the movies with the most "
            "F-words per minute. They are also among the movies with the lowest number of deaths.\n"
            "- While **Pulp Fiction** has the most F-words overall, **Reservoir Dogs** shows a rate of "
            "almost 5 F-words per minute, followed by Pulp Fiction with almost 3 and Jackie Brown with "
            "around 2.\n"
            "- **Crime** is by far the most profane genre among Tarantino movies with +1,200 F-words and "
            "a rate of around 3 words per minute, followed by **Western**, with +200 words and a rate "
            "of almost 2.\n\n"
            "---\n\n"
            "*Thank you for taking the time to view this analysis. If you found it useful and have any "
            "feedback or suggestions, don't hesitate to reach out — we are here to learn!*"
        ),
        "output.label": "Output",
        "output.death_sample": "Output — death events sample",
        "chart.death_fword_movie": "Death vs F words per Movie",
        "chart.rates_movie": "Death vs F-words Rate per minute",
        "chart.death_fword_genre": "Death vs F-words per Genre",
        "chart.rates_genre": "Death vs F-words per minute",
        "label.f_words": "F-words",
        "label.deaths": "Deaths",
        "label.f_words_per_minute": "F-words per minute",
        "label.deaths_per_minute": "Deaths per minute",
        "table.column": "Column",
        "table.description": "Description",
        "table.data_type": "Data Type",
        "table.missing_values": "Missing Values",
        "table.unique_values": "Unique Values",
        "table.example_value": "Example Value",
        "dict.movie": "Title of the Tarantino film in which the event occurred (7 unique films).",
        "dict.type": "Category of the event — either 'word' (a profane word was spoken) or 'death' (a character died).",
        "dict.word": "The specific profane word spoken. Only populated when type == 'word'; None for death events.",
        "dict.minutes_in": "Timestamp (in minutes) within the film when the event occurred.",
    },
    "pt": {
        "language.label": "Idioma",
        "language.switch_to": "English",
        "language.current": "Português",
        "sidebar.contents": "Conteúdo",
        "sidebar.data": "Dados",
        "sidebar.local_file": "Arquivo local",
        "sidebar.expected_file": "Arquivo esperado",
        "sidebar.upload_hint": "Coloque o CSV na pasta do app ou faça upload abaixo.",
        "sidebar.upload_label": "Enviar dataset",
        "error.missing_dataset": (
            "Não foi possível carregar o dataset. Arquivo esperado:\n\n`{path}`\n\n"
            "Salve `{filename}` na mesma pasta do app ou faça upload na barra lateral."
        ),
        "page.title": "Visão Geral de F-words de Tarantino",
        "page.subtitle": "Análise exploratória de palavrões e mortes em sete filmes de Quentin Tarantino",
        "section.summary.title": "Resumo",
        "section.summary.description": "Visão geral do dataset, definições de variáveis e objetivos da análise.",
        "section.summary.body": (
            "Este dataset registra eventos de palavrão e morte em **7 filmes de Quentin Tarantino**. "
            "Ele cobre **60 palavrões únicos** e mortes em gêneros como Crime, Ação, Guerra e Faroeste. "
            "Esta análise explora o nível de profanação nos filmes de Tarantino."
        ),
        "section.features.title": "Variáveis",
        "section.features.body": (
            "- **Movie** — Título do filme de Tarantino em que o evento ocorreu (7 filmes únicos)\n"
            "- **Type** — Categoria do evento: `word` (palavrão falado) ou `death` (morte de personagem)\n"
            "- **Word** — Palavrão específico; preenchido apenas quando type == `word`\n"
            "- **Minutes_in** — Momento (em minutos) do filme em que o evento ocorreu"
        ),
        "section.eda.title": "AED",
        "section.eda.description": "Dimensões, esquema, qualidade dos dados e amostras.",
        "section.eda.subtitle": "Exploração dos Dados",
        "section.eda.body": (
            "Nesta etapa exploramos a forma dos dados com os quais trabalhamos. É comum verificar "
            "número de colunas e linhas, valores ausentes, outliers e outras inconsistências."
        ),
        "section.analysis.title": "Análise Estatística",
        "section.analysis.description": "Métricas por filme e gênero com gráficos comparativos.",
        "section.analysis.body": (
            "Esta etapa busca entender as relações entre as variáveis por meio de métricas "
            "resumidas, comparações agrupadas e visualizações."
        ),
        "section.analysis.sub.movies": "Visão por filme",
        "section.analysis.sub.death_movie": "Mortes vs F-word por filme",
        "section.analysis.sub.rates_movies": "Taxas por minuto (filmes)",
        "section.analysis.sub.genre": "Visão por gênero",
        "section.analysis.sub.death_genre": "Mortes vs F-word por gênero",
        "section.analysis.sub.rates_genres": "Taxas por minuto (gêneros)",
        "section.analysis.movie_overview": "Visão por Filme",
        "section.analysis.genre_overview": "Visão por Gênero",
        "section.analysis.death_movie": "Mortes vs F-word por Filme",
        "section.analysis.rates_movie": "Mortes por minuto vs F-word por minuto",
        "section.analysis.death_genre": "Mortes vs F-word por Gênero",
        "section.insights.title": "Insights",
        "section.insights.description": "Principais achados sobre palavrões, mortes e padrões por gênero.",
        "section.insights.subtitle": "Estatísticas",
        "section.insights.body": (
            "- **Pulp Fiction**, **Reservoir Dogs** e **Jackie Brown** são os filmes com mais "
            "F-words por minuto. Também estão entre os com menor número de mortes.\n"
            "- Embora **Pulp Fiction** tenha o maior total de F-words, **Reservoir Dogs** apresenta "
            "quase 5 F-words por minuto, seguido por Pulp Fiction com quase 3 e Jackie Brown com cerca de 2.\n"
            "- **Crime** é de longe o gênero mais profano entre os filmes de Tarantino, com +1.200 F-words "
            "e taxa de cerca de 3 palavras por minuto, seguido por **Faroeste**, com +200 palavras "
            "e taxa de quase 2.\n\n"
            "---\n\n"
            "*Obrigado por acompanhar esta análise. Se foi útil e você tiver feedback ou sugestões, "
            "entre em contato — estamos aqui para aprender!*"
        ),
        "output.label": "Saída",
        "output.death_sample": "Saída — amostra de eventos de morte",
        "chart.death_fword_movie": "Mortes vs F-words por Filme",
        "chart.rates_movie": "Taxa de Mortes vs F-words por minuto",
        "chart.death_fword_genre": "Mortes vs F-words por Gênero",
        "chart.rates_genre": "Mortes vs F-words por minuto",
        "label.f_words": "F-words",
        "label.deaths": "Mortes",
        "label.f_words_per_minute": "F-words por minuto",
        "label.deaths_per_minute": "Mortes por minuto",
        "table.column": "Coluna",
        "table.description": "Descrição",
        "table.data_type": "Tipo de Dado",
        "table.missing_values": "Valores Ausentes",
        "table.unique_values": "Valores Únicos",
        "table.example_value": "Valor de Exemplo",
        "dict.movie": "Título do filme de Tarantino em que o evento ocorreu (7 filmes únicos).",
        "dict.type": "Categoria do evento — 'word' (palavrão falado) ou 'death' (morte de personagem).",
        "dict.word": "Palavrão específico. Preenchido apenas quando type == 'word'; None para mortes.",
        "dict.minutes_in": "Momento (em minutos) do filme em que o evento ocorreu.",
    },
}


def get_language() -> str:
    return st.session_state.get("language", "en")


def t(key: str, **kwargs: str) -> str:
    language = get_language()
    text = TRANSLATIONS.get(language, TRANSLATIONS["en"]).get(key, TRANSLATIONS["en"].get(key, key))
    return text.format(**kwargs) if kwargs else text


def get_sections() -> list[dict]:
    return [
        {
            "id": "summary",
            "title": t("section.summary.title"),
            "description": t("section.summary.description"),
        },
        {
            "id": "eda",
            "title": t("section.eda.title"),
            "description": t("section.eda.description"),
        },
        {
            "id": "statistical-analysis",
            "title": t("section.analysis.title"),
            "description": t("section.analysis.description"),
            "subsections": [
                t("section.analysis.sub.movies"),
                t("section.analysis.sub.death_movie"),
                t("section.analysis.sub.rates_movies"),
                t("section.analysis.sub.genre"),
                t("section.analysis.sub.death_genre"),
                t("section.analysis.sub.rates_genres"),
            ],
        },
        {
            "id": "insights",
            "title": t("section.insights.title"),
            "description": t("section.insights.description"),
        },
    ]


def get_data_dictionary() -> dict[str, str]:
    return {
        "movie": t("dict.movie"),
        "type": t("dict.type"),
        "word": t("dict.word"),
        "minutes_in": t("dict.minutes_in"),
    }


def render_language_toggle() -> None:
    if st.button(t("language.switch_to"), key="language_toggle"):
        st.session_state.language = "pt" if get_language() == "en" else "en"
        st.rerun()
