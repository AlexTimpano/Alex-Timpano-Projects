Updated version of Quickcalc with a new and improved graphing calculator. V1 had a broken graphing calculator due to a poor choice in windows forms control
V2.0 uses oxyplot to accurately graph algebraic equations. It even supports discontinuous functions! The oxyplot chart also supports scrolling and zooming for a better
viewing experience!

How to use graphing calculator
___________________________________
1: Input algebraic equation into the top text box

2: Input leftmost interval to display the graph on

3: Input rightmost interval to display the graph on

4: Input steps. The steps determine how many data points within the interval will be calculated and used when making the graph.
e.g: 

equation=x^2

left = 0 

right = 5

With step 2

data points [X,Y] will be [0,0], [1,1], [2,4], [3,9], [4,16], [5,25]

VS

With step 2

data points [X,Y] will be [0,0], [2,2], [4,16]


Why does this matter?: A lower step value will result in a more accurate graph at the cost of longer time to display. This can become significant when graphing over larger intervals. A higher step value will result in a less accurate graph but with a quicker time to display. The inaccuracy becomes significant over short intervals. Step values below 0.01 are not recommended.

___________________________________

The chart may not always update correctly by itself. Simply zoom in or out a little and it will update right away.
