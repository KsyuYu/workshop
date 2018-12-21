import plotly
import plotly.graph_objs as go
from plotly import tools


bar = go.Bar(
    x=["Київ","Вінниця","Волинь", "Луганськ", "Дніпро", "Донецьк", "Житомир", "Закарпаття"],
    y=[22,19,17,20,13, 31, 12, 22],
            )
pie1 = go.Pie(
    labels = ["Київ","Вінниця","Волинь", "Луганськ", "Дніпро", "Донецьк", "Житомир", "Закарпаття"],
    values = [22,19,17,20,13, 31, 12, 22],
)



fig = tools.make_subplots(rows=1, cols=2)

fig.append_trace(bar, 1, 1)

fig.append_trace(pie1, 1, 2)

plotly.offline.plot(fig, filename='plotly.html')

