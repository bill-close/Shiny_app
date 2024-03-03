from shiny import render, ui
from shiny.express import input
from palmerpenguins import load_penguins
import seaborn as sns

ui.panel_title(ui.tags.h1("Penguin data", align = "center"))


ui.panel_sidebar(
    ui.input_select("species", "Select a species", ["Adelie", "Chinstrap", "Gentoo"]),
)

ui.tags.h5("A plot of the flipper length of all penguins", align = "center")
@render.plot(alt="A plot of the penguins")
def plot():
    sns.set_style("white")

    penguins = load_penguins()
    p = penguins[penguins.species == input.species()]

    graph = sns.histplot(
        x="flipper_length_mm",
        hue="species",
        data=p,
        palette=["#FF8C00","#159090","#FF6347"],
        linewidth=0.3,
    )
    return graph

ui.tags.h5("Analysis of a particular species", align = "center")
@render.image
def image():
    from pathlib import Path

    dir = Path(__file__).resolve().parent
    selected_species = input.species()
    img: ImgData = {"src": str(dir / f"{selected_species}.jpeg"), "width": "400px"}
    return img