import pandas as pd
import itertools

mono_chart = pd.read_csv("data/mono-chart.csv")
mono_chart.set_index("Attacking", inplace = True)

types = mono_chart.index.tolist()

dual_types = list(itertools.combinations(types, 2))

mono_vs_dual = pd.DataFrame(
    index = types,
    columns = [f"{t1}/{t2}" for t1, t2 in dual_types],
    dtype = float
)

for attacker in types:

    for t1, t2 in dual_types:

        mono_vs_dual.loc[attacker, f"{t1}/{t2}"] = (mono_chart.loc[attacker, t1] * mono_chart.loc[attacker, t2])

# Saving the mono-dual chart.

mono_vs_dual.index.name = "Attacking"
# mono_vs_dual.to_csv("data/mono-dual-chart.csv")

dual_vs_dual = pd.DataFrame(

    index = [f"{t1}/{t2}" for t1, t2 in dual_types],
    columns = [f"{t1}/{t2}" for t1, t2 in dual_types],
    dtype = float

)

for a1, a2 in dual_types:

    attacker = f"{a1}/{a2}"

    for b1, b2 in dual_types:

        defender = f"{b1}/{b2}"

        dual_vs_dual.loc[attacker, defender] = (mono_vs_dual.loc[a1, defender] + mono_vs_dual.loc[a2, defender])/2

dual_vs_dual.index.name = "Attacking"
dual_vs_dual.to_csv("data/dual-chart.csv")