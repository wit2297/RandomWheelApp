import streamlit as st
import random
import matplotlib.pyplot as plt
import numpy as np
import time

# Function to create the wheel chart with rotation
def create_wheel(entries, angle=0):
    fig, ax = plt.subplots(figsize=(6, 6))

    # Create the pie chart
    wedges, texts = ax.pie(
        [1] * len(entries),
        labels=entries,
        startangle=angle,
        counterclock=False,
        colors=plt.cm.Paired.colors,
    )

    ax.set_aspect("equal")
    return fig

# App title
st.title("🎡 Realistic Random Wheel Spinner")

# Sidebar: User input for entries
st.sidebar.header("Entries")
entries = st.sidebar.text_area("Add items for the wheel (one per line):").split("\n")
entries = [e.strip() for e in entries if e.strip()]

# Ensure there are entries
if entries:
    st.subheader("Your Wheel")
    placeholder = st.empty()  # Placeholder for the spinning wheel

    # Draw the initial wheel
    initial_wheel = create_wheel(entries)
    placeholder.pyplot(initial_wheel)

    # Button to spin the wheel
    if st.button("Spin the Wheel!"):
        st.subheader("🎰 Spinning the Wheel...")
        total_entries = len(entries)

        # Simulate spinning animation with rotation
        total_rotations = random.randint(5, 10) * 360  # Number of full rotations
        stopping_angle = random.randint(0, 360)  # Final stopping angle
        final_angle = total_rotations + stopping_angle  # Total rotation angle
        spin_steps = 50  # Number of steps in the animation

        for step in range(spin_steps):
            # Calculate the current angle
            current_angle = (final_angle / spin_steps) * step
            fig = create_wheel(entries, angle=current_angle)
            placeholder.pyplot(fig)
            time.sleep(0.05)  # Speed of the animation

        # Calculate the selected entry based on the stopping angle
        slice_angle = 360 / total_entries  # Angle per slice
        selected_index = (total_entries - int(stopping_angle // slice_angle)) % total_entries
        selected_item = entries[selected_index]

        # Show the final result
        st.success(f"🎉 The wheel landed on: **{selected_item}** 🎉")
else:
    st.warning("Please add some entries in the sidebar to create the wheel.")
