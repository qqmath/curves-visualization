# Introduction and description of the interactive article
st.write("""
# Spiral Visualization with Streamlit

This interactive article demonstrates different types of spirals using Streamlit.

**Cardioid Spiral**

The Cardioid spiral resembles a heart shape, and you can adjust the number of points and turns to explore it.
""")

# Interactive widget for adjusting the parameters of the Cardioid spiral
with st.echo(code_location='below'):
    # Slider to control the number of points in the Cardioid spiral
    total_points = st.slider("Number of points in Cardioid spiral", 1, 5000, 2000)
    # Slider to control the number of turns in the Cardioid spiral
    num_turns = st.slider("Number of turns in Cardioid spiral", 1, 100, 9)

    # Define a namedtuple to store the (x, y) coordinates of the spiral points
    Point = namedtuple('Point', 'x y')
    data = []

    # Calculate the number of points per turn based on the total points and turns
    points_per_turn = total_points / num_turns

    # Generate the points for the Cardioid spiral
    for curr_point_num in range(total_points):
        curr_turn, i = divmod(curr_point_num, points_per_turn)
        angle = (curr_turn + 1) * 2 * math.pi * i / points_per_turn
        radius = (5 - 5 * math.sin(angle)) * curr_point_num / total_points
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        data.append(Point(x, y))

    # Display the Cardioid spiral using Altair chart
    st.altair_chart(alt.Chart(pd.DataFrame(data), height=500, width=500)
        .mark_circle(color='#0068c9', opacity=0.5)
        .encode(x='x:Q', y='y:Q'))

# Description of the Astroid spiral
st.write("""
**Astroid Spiral**

The Astroid spiral resembles a star shape, and you can customize its appearance by adjusting the number of points and turns.
""")

# Interactive widget for adjusting the parameters of the Astroid spiral
with st.echo(code_location='below'):
    # Slider to control the number of points in the Astroid spiral
    total_points2 = st.slider("Number of points in Astroid spiral", 1, 10000, 2000, key=2)
    # Slider to control the number of turns in the Astroid spiral
    num_turns2 = st.slider("Number of turns in Astroid spiral", 1, 100, 11, key=3)

    Point = namedtuple('Point', 'x y')
    data = []

    # Calculate the number of points per turn based on the total points and turns
    points_per_turn2 = total_points2 / num_turns2

    # Generate the points for the Astroid spiral
    for curr_point_num2 in range(total_points2):
        curr_turn2, i = divmod(curr_point_num2, points_per_turn2)
        angle2 = (curr_turn2 + 1) * 2 * math.pi * i / points_per_turn2
        radius2 = curr_point_num2 / total_points2
        x = radius2 * math.cos(angle2) ** 3
        y = radius2 * math.sin(angle2) ** 3
        data.append(Point(x, y))

    # Display the Astroid spiral using Altair chart
    st.altair_chart(alt.Chart(pd.DataFrame(data), height=500, width=500)
        .mark_circle(color='#0068c9', opacity=0.5)
        .encode(x='x:Q', y='y:Q'))

# Description of the Trochoid spiral
st.write("""
**Trochoid Spiral**

The Trochoid spiral consists of two circles, and you can experiment with different angle and radius multipliers to observe the spiral's behavior.
""")

# Interactive widget for adjusting the parameters of the Trochoid spiral
with st.echo(code_location='below'):
    # Slider to control the number of points in the Trochoid spiral
    total_points3 = st.slider("Number of points in Trochoid spiral", 1, 10000, 2000, key=4)
    # Slider to control the number of turns of the first circle in the Trochoid spiral
    num_turns3 = st.slider("Number of turns of the first circle", 1, 100, 11, key=5)
    # Number input to control the second angle multiplier in the Trochoid spiral
    angle321 = st.number_input("Second angle multiplier in Trochoid spiral", value=0.05, step=0.01, key=6)
    # Number input to control the second radius multiplier in the Trochoid spiral
    radius321 = st.number_input("Second radius multiplier in Trochoid spiral", value=11.00, step=0.01, key=7)

    Point = namedtuple('Point', 'x y')
    data = []

    # Calculate the number of points per turn based on the total points and turns
    points_per_turn3 = total_points3 / num_turns3

    # Generate the points for the Trochoid spiral
    for curr_point_num3 in range(total_points3):
        curr_turn3, i = divmod(curr_point_num3, points_per_turn3)
        angle31 = (curr_turn3 + 1) * 2 * math.pi * i / points_per_turn3
        angle32 = angle321 * angle31
        radius31 = curr_point_num3 / total_points3
        radius32 = radius321 * radius31
        x = radius31 * math.cos(angle31) + radius32 * math.cos(angle32)
        y = radius31 * math.sin(angle31) + radius32 * math.sin(angle32)
        data.append(Point(x, y))

    # Display the Trochoid spiral using Altair chart
    st.altair_chart(alt.Chart(pd.DataFrame(data), height=500, width=500)
        .mark_circle(color='#0068c9', opacity=0.5)
        .encode(x='x:Q', y='y:Q'))

# Description of the Archimedean spiral
st.write("""
**Archimedean Spiral**

The Archimedean spiral is another interesting type of spiral that can be adjusted using different parameters.
""")

# Interactive widget for adjusting the parameters of the Archimedean spiral
with st.echo(code_location='below'):
    # Slider to control the number of points in the Archimedean spiral
    total_points4 = st.slider("Number of points in Archimedean spiral", 1, 10000, 2000, key=8)
    # Slider to control the number of turns in the Archimedean spiral
    num_turns4 = st.slider("Number of turns in Archimedean spiral", 1, 100, 15, key=9)
    # Number input to control the radius increment in the Archimedean spiral
    radius_increment = st.number_input("Radius increment in Archimedean spiral", value=0.1, step=0.01, key=10)

    Point = namedtuple('Point', 'x y')
    data = []

    # Calculate the number of points per turn based on the total points and turns
    points_per_turn4 = total_points4 / num_turns4

    # Generate the points for the Archimedean spiral
    for curr_point_num4 in range(total_points4):
        curr_turn4, i = divmod(curr_point_num4, points_per_turn4)
        angle4 = (curr_turn4 + 1) * 2 * math.pi * i / points_per_turn4
        radius4 = curr_point_num4 * radius_increment
        x = radius4 * math.cos(angle4)
        y = radius4 * math.sin(angle4)
        data.append(Point(x, y))

    # Display the Archimedean spiral using Altair chart
    st.altair_chart(alt.Chart(pd.DataFrame(data), height=500, width=500)
        .mark_circle(color='#0068c9', opacity=0.5)
        .encode(x='x:Q', y='y:Q'))

# Description of Fermat's spiral
st.write("""
**Fermat's Spiral**

Fermat's spiral is a beautiful spiral with unique characteristics, and you can explore it by adjusting the number of points and turns.
""")

# Interactive widget for adjusting the parameters of Fermat's spiral
with st.echo(code_location='below'):
    # Slider to control the number of points in Fermat's spiral
    total_points5 = st.slider("Number of points in Fermat's spiral", 1, 10000, 2000, key=11)
    # Slider to control the number of turns in Fermat's spiral
    num_turns5 = st.slider("Number of turns in Fermat's spiral", 1, 100, 10, key=12)
    # Number input to control the spiral constant in Fermat's spiral
    spiral_constant = st.number_input("Spiral constant in Fermat's spiral", value=0.1, step=0.01, key=13)

    Point = namedtuple('Point', 'x y')
    data = []

    # Calculate the number of points per turn based on the total points and turns
    points_per_turn5 = total_points5 / num_turns5

    # Generate the points for Fermat's spiral
    for curr_point_num5 in range(total_points5):
        curr_turn5, i = divmod(curr_point_num5, points_per_turn5)
        angle5 = (curr_turn5 + 1) * 2 * math.pi * i / points_per_turn5
        radius5 = spiral_constant * math.sqrt(curr_point_num5)
        x = radius5 * math.cos(angle5)
        y = radius5 * math.sin(angle5)
        data.append(Point(x, y))

    # Display Fermat's spiral using Altair chart
    st.altair_chart(alt.Chart(pd.DataFrame(data), height=500, width=500)
        .mark_circle(color='#0068c9', opacity=0.5)
        .encode(x='x:Q', y='y:Q'))
