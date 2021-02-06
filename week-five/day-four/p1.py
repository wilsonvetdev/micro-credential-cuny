# s. trowbridge 2020
import functions as fn
import plotly.express as px
import plotly.graph_objects as go

n = 10
nums = [i for i in range(1, n+1)]
sums = []
products = []

for i in range(1, n+1):
    sums.append(fn.summation(i))

for i in range(1, n+1):
    products.append(fn.factorial(i))

print(sums)
print(products)
print("")

# instantiate a plotly express line chart from list comprehensions
fig = go.Figure(
    data = [
        go.Scatter( x=nums,
                    y=sums,
                    mode='markers+lines',
                    marker_color=sums,
                    marker_size=5,
                    name='final_exam_grade'
        ),
        go.Scatter( x=nums,
                    y=products,
                    mode='markers+lines',
                    marker_color='green',
                    marker_size=5,
                    name='gpa'
        )
    ]
)

# render an html file of the chart and open in default browser
fig.show()
