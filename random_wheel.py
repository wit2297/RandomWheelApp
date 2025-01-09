import streamlit as st
import random
import matplotlib.pyplot as plt
import time

# Function to create the wheel chart
def create_wheel(entries, highlight=None):
    fig, ax = plt.subplots(figsize=(6, 6))
    wedges, _ = ax.pie(
        [1] * len(entries), labels=entries, startangle=90, colors=plt.cm.Paired.colors
    )
    if highlight is not None:
        # Highlight the selected wedge
        wedges[highlight].set_edgecolor("black")
        wedges[highlight].set_linewidth(3)
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
    placeholder = st.empty()  # Placeholder for the spinning animation
    st.pyplot(create_wheel(entries))

    # Spin the wheel button
    if st.button("Spin the Wheel!"):
        st.subheader("🎰 Spinning the Wheel...")
        spin_index = random.randint(0, len(entries) - 1)

        # Simulate spinning animation
        for i in range(30):  # Number of "spins"
            current_index = (spin_index + i) % len(entries)
            fig = create_wheel(entries, highlight=current_index)
            placeholder.pyplot(fig)  # Update the placeholder with the new frame
            time.sleep(0.1)  # Delay between frames

        # Show the final result
        selected_item = entries[spin_index]
        st.success(f"🎉 The wheel landed on: **{selected_item}** 🎉")
else:
    st.warning("Please add some entries in the sidebar to create the wheel.")
