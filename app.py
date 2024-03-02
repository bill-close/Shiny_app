from shiny import render, ui
from shiny.express import input
from palmerpenguins import load_penguins
import seaborn as sns

ui.panel_title("A plot of the flipper length of penguins from various species")
# ui.input_slider("n", "N", 0, 100, 20)

# @render.text
# def txt():
#     return f"n*2 is {input.n() * 2}"


@render.plot(alt="A plot of the penguins")
def plot():
    sns.set_style("whitegrid")

    penguins = load_penguins()

    g = sns.histplot(
        x="flipper_length_mm",
        hue="species",
        data=penguins,
        palette=["#FF8C00","#159090","#FF6347"],
        linewidth=0.3,
    )
    return g
