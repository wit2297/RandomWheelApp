import streamlit as st
import random
import matplotlib.pyplot as plt
import numpy as np
import time

# Function to create the wheel chart
def create_wheel(entries, highlight_index=None):
    fig, ax = plt.subplots(figsize=(6, 6))
    wedges, texts = ax.pie(
        [1] * len(entries), labels=entries, startangle=90, colors=plt.cm.Paired.colors
    )

    # Highlight the selected wedge if provided
    if highlight_index is not None:
        wedges[highlight_index].set_edgecolor("black")
        wedges[highlight_index].set_linewidth(3)

    ax.set_aspect("equal")
    return fig

# App title
st.title("🎡 Random Wheel Spinner")

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

        # Simulate the spinning animation
        total_spins = 50  # Total frames in the spin
        slowing_factor = 1.05  # Slow down gradually

        spin_index = random.randint(0, len(entries) - 1)  # Random final position
        for i in range(total_spins):
            current_index = (spin_index + i) % len(entries)  # Simulate spinning
            fig = create_wheel(entries, highlight_index=current_index)
            placeholder.pyplot(fig)  # Update the wheel in the same placeholder

            # Adjust sleep time for slowing down effect
            time.sleep(max(0.01, (i / total_spins) ** 2))

        # Show the final result
        selected_item = entries[spin_index]
        st.success(f"🎉 The wheel landed on: **{selected_item}** 🎉")
else:
    st.warning("Please add some entries in the sidebar to create the wheel.")
