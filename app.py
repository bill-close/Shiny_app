from shiny import render, ui
from shiny.express import input
from palmerpenguins import load_penguins
import seaborn as sns

ui.panel_title("A plot of the flipper length of penguins from various species")

ui.panel_sidebar(
    ui.input_select("species", "Select a species", ["Adelie", "Chinstrap", "Gentoo"]),
)

# What does this do??
# app_ui = ui.page_fluid(ui.output_image("image"))


# ui.input_slider("n", "N", 0, 100, 20)

# @render.text
# def txt():
#     return f"n*2 is {input.n() * 2}"


@render.plot(alt="A plot of the penguins")
def plot():
    sns.set_style("whitegrid")

    penguins = load_penguins()
    p = penguins[penguins.species == input.species()]

    g = sns.histplot(
        x="flipper_length_mm",
        hue="species",
        data=p,
        palette=["#FF8C00","#159090","#FF6347"],
        linewidth=0.3,
    )
    return g


@render.image
def image():
    from pathlib import Path

    dir = Path(__file__).resolve().parent
    img: ImgData = {"src": str(dir / "Adelie.jpeg"), "width": "400px"}
    return img