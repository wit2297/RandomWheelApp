import streamlit as st
import random
import matplotlib.pyplot as plt
import time

# Function to create the wheel chart
def create_wheel(entries, highlight=None):
    fig, ax = plt.subplots(figsize=(6, 6))
    wedges, texts = ax.pie(
        [1] * len(entries), labels=entries, startangle=90, colors=plt.cm.Paired.colors
    )

    # Highlight the selected item
    if highlight is not None:
        for i, wedge in enumerate(wedges):
            if i == highlight:
                wedge.set_edgecolor("black")
                wedge.set_linewidth(3)

    ax.set_aspect("equal")
    return fig

# App title
st.title("🎡 Random Wheel Spinner")

# User input for entries
st.sidebar.header("Entries")
entries = st.sidebar.text_area("Add items for the wheel (one per line):").split("\n")
entries = [e.strip() for e in entries if e.strip()]

# Show the wheel
if entries:
    st.subheader("Your Wheel")
    st.pyplot(create_wheel(entries))

    # Spin the wheel button
    if st.button("Spin the Wheel!"):
        st.subheader("🎰 Spinning the Wheel...")
        spin_index = random.randint(0, len(entries) - 1)

        # Simulate spinning animation
        for i in range(20):  # Number of "spins"
            current_index = (spin_index + i) % len(entries)
            fig = create_wheel(entries, highlight=current_index)
            st.pyplot(fig)
            time.sleep(0.1)  # Delay between spins

        # Show the result
        selected_item = entries[spin_index]
        st.success(f"🎉 The wheel landed on: **{selected_item}** 🎉")
else:
    st.warning("Please add some entries in the sidebar to create the wheel.")
