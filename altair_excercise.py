import altair as alt
import seaborn as sns
from os import chdir

path = (
    r"C:\Users\krzys\Desktop\data science\IV semestr\machine_learning\altair_excercise"
)

chdir(path)

source = sns.load_dataset("penguins")

base = (
    alt.Chart(source)
    .mark_point(size=30)
    .encode(
        alt.X("bill_length_mm", scale=alt.Scale(zero=False)),
        alt.Y("flipper_length_mm", scale=alt.Scale(zero=False)),
        color="species",
        tooltip="species",
    )
)

degree_list = [1, 3, 5]

polynomial_fit = [
    base.transform_regression(
        "bill_length_mm",
        "flipper_length_mm",
        method="poly",
        order=order,
        as_=["bill_length_mm", str(order)],
    )
    .mark_line()
    .transform_fold([str(order)], as_=["degree", "flipper_length_mm"])
    .encode(alt.Color("degree:N"))
    for order in degree_list
]

final = alt.layer(base.interactive(), *polynomial_fit)
final.save("Chojnacki_Krzysztof_altair.html")
