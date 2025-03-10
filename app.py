import streamlit as st

# 📝 Streamlit To-Do List App
st.title("✅ To-Do List App")

# Initialize session state for tasks
if "tasks" not in st.session_state:
    st.session_state["tasks"] = []

# User input for new task
new_task = st.text_input("Enter a new task:")

# Add task button
if st.button("Add Task"):
    if new_task:
        st.session_state["tasks"].append(new_task)
        st.rerun()  # Refresh the app after adding a task

# Display tasks
st.subheader("Your Tasks:")
for index, task in enumerate(st.session_state["tasks"]):
    col1, col2 = st.columns([0.8, 0.2])
    col1.write(f"📌 {task}")  # Show the task
    if col2.button("❌", key=index):
        st.session_state["tasks"].pop(index)
        st.rerun()  # Refresh the app after deleting a task
