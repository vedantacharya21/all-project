import streamlit as st

# ---------------------------
# Page Configuration
# ---------------------------
st.set_page_config(
    page_title="To-Do List",
    page_icon="📝",
    layout="centered"
)

st.title("📝 To-Do List App")
st.write("Manage your daily tasks easily.")

# ---------------------------
# Session State
# ---------------------------
if "tasks" not in st.session_state:
    st.session_state.tasks = []

# ---------------------------
# Sidebar Menu
# ---------------------------
menu = st.sidebar.selectbox(
    "Choose an Option",
    (
        "Add Task",
        "Remove Task",
        "View Tasks",
        "Print Every Task"
    )
)

# ---------------------------
# Add Task
# ---------------------------
if menu == "Add Task":

    st.subheader("➕ Add New Task")

    task = st.text_input("Enter Task")

    if st.button("Add Task"):

        if task.strip() == "":
            st.warning("Task cannot be empty.")
        else:
            st.session_state.tasks.append(task)
            st.success("Task Added Successfully!")

# ---------------------------
# Remove Task
# ---------------------------
elif menu == "Remove Task":

    st.subheader("❌ Remove Task")

    if len(st.session_state.tasks) == 0:
        st.info("No Tasks Available.")
    else:

        selected_task = st.selectbox(
            "Select Task",
            st.session_state.tasks
        )

        if st.button("Remove Task"):

            st.session_state.tasks.remove(selected_task)

            st.success("Task Removed Successfully!")

# ---------------------------
# View Tasks
# ---------------------------
elif menu == "View Tasks":

    st.subheader("📋 Your Tasks")

    if len(st.session_state.tasks) == 0:
        st.info("No Tasks Found.")
    else:

        for i, task in enumerate(st.session_state.tasks, start=1):
            st.write(f"**{i}.** {task}")

# ---------------------------
# Print Every Task
# ---------------------------
elif menu == "Print Every Task":

    st.subheader("🖨️ Print Every Task")

    if len(st.session_state.tasks) == 0:
        st.info("No Tasks Found.")
    else:

        for i, task in enumerate(st.session_state.tasks, start=1):

            st.markdown(f"""
### Task {i}

{task}

---
""")