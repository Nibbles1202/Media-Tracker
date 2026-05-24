import streamlit as st
from storage import load_items, save_items

items = load_items()

st.title("🎬 Media Tracker")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Items", len(items))

with col2:
    st.metric("In Progress", len([i for i in items if i["status"] == "In Progress"]))

with col3:
    st.metric("Completed", len([i for i in items if i["status"] == "Completed"]))

st.header("Add New Item")

title = st.text_input("Title")
category = st.selectbox("Category", ["Game", "Movie", "Show"])
rating = st.slider("Rating (1-10)", 1, 10, 5)

if st.button("Add Item"):
    if title:
        items.append({
            "title": title,
            "category": category,
            "status": "Not Started",
            "rating": rating
        })
        save_items(items)
        st.success("Item added!")
    else:
        st.error("Please enter a title")

st.header("Filters")

search = st.text_input("Search by title")

filter_status = st.selectbox(
    "Filter by status",
    ["All", "Not Started", "In Progress", "Completed"]
)

filtered_items = items

if search:
    filtered_items = [
        item for item in filtered_items
        if search.lower() in item["title"].lower()
    ]

if filter_status != "All":
    filtered_items = [
        item for item in filtered_items
        if item["status"] == filter_status
    ]

st.header("Your List")

if not items:
    st.info("No items yet.")
else:
    for i, item in enumerate(filtered_items):
        col1, col2, col3 = st.columns([3, 2, 1])

        with col1:
            st.write(
                f"{i+1}. {item['title']} ({item['category']})")
        with col2:
            status_options = ["Not Started", "In Progress", "Completed"]

            current_status = item.get("status", "Not Started")

            if current_status not in status_options:
                current_status = "Not Started"

            new_status = st.selectbox(
                "Status",
                status_options,
                index=status_options.index(current_status),
                key=f"status_{i}"
            )
                 

            item["status"] = new_status
            save_items(items)

        with col3:
            if st.button("Delete", key=f"delete_{i}"):
                items.pop(i)
                save_items(items)
                st.rerun()

        st.write(f" Rating: {item['rating']}")
        st.divider()