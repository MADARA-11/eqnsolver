import streamlit as st
from scipy.optimize import fsolve
from scipy.linalg import solve
import numpy as np

st.set_page_config(page_title="equation solver",layout="wide")

st.title("equation solver")
st.subheader("This app solves linear,quadratic,cubic,system of equations: ")

linear = "linear (ax + b = 0)"
quadratic = "quadratic(ax² + bx + c = 0))"
cubic = "cubic(ax³ + bx² + cx + d = 0)"

opt = st.sidebar.radio("pls choose type of equation to solve",(linear,quadratic,cubic,"system of two equation","system of three equation"))
st.divider()

if opt == linear:
    st.subheader("linear equation")
    num1 = st.number_input("Enter a coefficient value",value=1)
    num2 = st.number_input("Enter a constant value",value=1)
    st.latex(fr"{num1}x+{num2}")
    if st.button("display"):

        if num1 != 0:
            res = -num2/num1
            st.success(f"the value of the x is : {res}")
        else:
            st.warning("this is  not a valid equation ")


elif opt == quadratic:
    st.subheader("quadratic")
    num1 = st.number_input("Enter a coefficient value a",value=1)
    num2 = st.number_input("Enter a coefficient value b",value=1)
    num3 = st.number_input("Enter a constant value",value=1)

    st.latex(fr"{num1}x^2+{num2}x+{num3}")
    if st.button("display"):
        coef =[num1,num2,num3]
        root =np.roots(coef)

        st.success(f"the roots are {root[0]} and {root[1]}")




elif opt == cubic:
    st.subheader("cubic")
    num1 = st.number_input("Enter a coefficient value a ",value=1)
    num2 = st.number_input("Enter a coefficient value b ", value=1)
    num3 = st.number_input("Enter a coefficient value c ", value=1)
    num4 = st.number_input("Enter a constant value", value=1)

    st.latex(fr"{num1}x^3 +{num2}x^2+{num3}x+{num4}")
    if st.button("Display"):
        coef =[num1,num2,num3,num4]
        root = np.roots(coef)

        st.success(f"the roots are {root[0]} and {root[1]} and {root[2]}")


elif opt == "system of two equation":
    st.subheader("system of two equation")
    x1 = st.number_input("Enter a coefficient of x(eqn1)",value=1)
    y1 = st.number_input("Enter a coefficient of y(eqn1)", value=1)
    con1 = st.number_input("Enter a constant (enq1)", value=1)

    x2 = st.number_input("Enter a coefficient of x(eqn2)", value=1)
    y2 = st.number_input("Enter a coefficient of y(eqn2)", value=1)
    con2 = st.number_input("Enter a constant (enq2)", value=1)

    st.latex(fr"{x1}x + {y1}y = {con1}")
    st.latex(fr"{x2}x + {y2}y = {con2}")
    if st.button("Display"):
        coef =[[x1,y1],
               [x2,y2]]
        con =[con1,con2]

        result =solve(coef,con)

        st.success(f"the result of x and y is : {result[0]} and {result[1]}")

elif opt == "system of three equation":
    st.subheader("system of three equation")
    x1 = st.number_input("Enter a coefficient of x(eqn1)", value=1)
    y1 = st.number_input("Enter a coefficient of y(eqn1)", value=1)
    z1 = st.number_input("Enter a coefficient of z(eqn1)", value=1)
    con1 = st.number_input("Enter a constant (enq1)", value=1)

    x2 = st.number_input("Enter a coefficient of x(eqn2)", value=1)
    y2 = st.number_input("Enter a coefficient of y(eqn2)", value=1)
    z2 = st.number_input("Enter a coefficient of z(eqn2)", value=1)
    con2 = st.number_input("Enter a constant (enq2)", value=1)

    x3 = st.number_input("Enter a coefficient of x(eqn3)", value=1)
    y3 = st.number_input("Enter a coefficient of y(eqn3)", value=1)
    z3 = st.number_input("Enter a coefficient of z(eqn3)", value=1)
    con3 = st.number_input("Enter a constant (enq3)", value=1)

    st.latex(fr"{x1}x + {y1}y + {z1}z = {con1} ")
    st.latex(fr"{x2}x + {y2}y + {z2}z = {con2} ")
    st.latex(fr"{x3}x + {y3}y + {z3}z = {con3} ")

    if st.button("Display"):
        coef =[[x1,y1,z1],
               [x2,y2,z2],
               [x3,y3,z3]]
        con =[con1,con2,con3]

        result =solve(coef,con)

        st.success(f"the result of x , y and z is : {result[0]} and {result[1]} and {result[2]}")
