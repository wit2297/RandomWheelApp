import streamlit as st
import random
import matplotlib.pyplot as plt

# Function to create the wheel chart
def create_wheel(entries):
    fig, ax = plt.subplots(figsize=(6, 6))
    wedges, _ = ax.pie([1] * len(entries), labels=entries, startangle=90, colors=plt.cm.Paired.colors)
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
        selected_item = random.choice(entries)
        st.success(f"🎉 The wheel landed on: **{selected_item}** 🎉")
else:
    st.warning("Please add some entries in the sidebar to create the wheel.")
