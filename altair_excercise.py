import altair as alt
import seaborn as sns

source = sns.load_dataset("penguins")

base = alt.Chart(source).mark_point(size=30).encode(
    alt.X('bill_length_mm', scale = alt.Scale(zero=False)),
    alt.Y('flipper_length_mm', scale = alt.Scale(zero=False)),
    color='species',
    tooltip= 'species')

degree_list = [1, 3, 5]

polynomial_fit = [
    base.transform_regression(
        "bill_length_mm", 
        "flipper_length_mm", 
        method="poly", 
        order=order, 
        as_=["bill_length_mm", str(order)]
    )
    .mark_line()
    .transform_fold([str(order)], as_=["degree", "flipper_length_mm"])
    .encode(alt.Color("degree:N"))
    for order in degree_list
]

final = alt.layer(base.interactive(), *polynomial_fit)

#%%
import numpy as np
import pandas as pd
import altair as alt

# Generate some random data
rng = np.random.RandomState(1)
x = rng.rand(40) ** 2
y = 10 - 1.0 / (x + 0.1) + rng.randn(40)
source = pd.DataFrame({"x": x, "y": y})

# Define the degree of the polynomial fits
degree_list = [1, 3, 5]

base = alt.Chart(source).mark_circle(color="black").encode(
        alt.X("x"), alt.Y("y")
)

polynomial_fit = [
    base.transform_regression(
        "x", "y", method="poly", order=order, as_=["x", str(order)]
    )
    .mark_line()
    .transform_fold([str(order)], as_=["degree", "y"])
    .encode(alt.Color("degree:N"), legend=alt.Legend(values=['degree_list']))
    for order in degree_list
]

alt.layer(base, *polynomial_fit)