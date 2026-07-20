import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from tarantino_analysis.config import PAPER_CHART


def configure_paper_plot_style() -> None:
    sns.set_theme(
        style="white",
        palette=[PAPER_CHART["bar_primary"], PAPER_CHART["bar_secondary"]],
        rc={
            "figure.facecolor": PAPER_CHART["background"],
            "axes.facecolor": PAPER_CHART["background"],
            "axes.edgecolor": PAPER_CHART["spine"],
            "axes.labelcolor": PAPER_CHART["text"],
            "text.color": PAPER_CHART["text"],
            "xtick.color": PAPER_CHART["tick"],
            "ytick.color": PAPER_CHART["tick"],
            "grid.color": PAPER_CHART["grid"],
            "font.family": "serif",
            "font.size": 10,
        },
    )


def apply_paper_chart_style(fig: plt.Figure, ax: plt.Axes) -> None:
    fig.patch.set_facecolor(PAPER_CHART["background"])
    ax.set_facecolor(PAPER_CHART["background"])
    ax.title.set_color(PAPER_CHART["text"])
    ax.tick_params(colors=PAPER_CHART["tick"], labelcolor=PAPER_CHART["tick"])
    ax.grid(axis="y", color=PAPER_CHART["grid"], linewidth=0.8, alpha=0.75)
    ax.set_axisbelow(True)

    for spine in ax.spines.values():
        spine.set_color(PAPER_CHART["spine"])

    legend = ax.get_legend()
    if legend is not None:
        legend.get_frame().set_facecolor(PAPER_CHART["background"])
        legend.get_frame().set_edgecolor(PAPER_CHART["spine"])
        for text in legend.get_texts():
            text.set_color(PAPER_CHART["text"])


def styled_barplot(
    data: pd.DataFrame,
    x: str,
    y: str,
    hue: str,
    title: str,
    figsize: tuple[float, float],
    legend_loc: str,
) -> plt.Figure:
    fig, ax = plt.subplots(figsize=figsize, facecolor=PAPER_CHART["background"])
    sns.barplot(
        data=data,
        x=x,
        y=y,
        hue=hue,
        ax=ax,
        palette=[PAPER_CHART["bar_primary"], PAPER_CHART["bar_secondary"]],
    )

    for container in ax.containers:
        ax.bar_label(container, fontsize=8, padding=3, color=PAPER_CHART["text"])

    tick_labels = [label.get_text() for label in ax.get_xticklabels()]
    ax.set_xticks(range(len(tick_labels)))
    ax.set_xticklabels(tick_labels, rotation=30, ha="right", fontsize=9)
    ax.tick_params(axis="y", labelsize=9)
    ax.set_title(title, fontsize=11, color=PAPER_CHART["text"])
    ax.set_xlabel("")
    ax.set_ylabel("")
    ax.legend(loc=legend_loc, frameon=False)
    sns.despine(left=False, right=True, top=True, bottom=False, ax=ax)
    apply_paper_chart_style(fig, ax)
    fig.tight_layout()
    return fig
