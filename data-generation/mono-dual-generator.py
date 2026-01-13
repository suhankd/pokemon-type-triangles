import pandas as pd
import itertools

mono_chart = pd.read_csv(f"./data/mono_chart.csv")
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

mono_vs_dual.to_csv("./data/mono-vs-dual-chart.csv")