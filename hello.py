from preswald import text, plotly, connect, get_df, table, slider
import pandas as pd
import plotly.express as px

# Step 1: Connect and load the dataset
connect()
df = get_df("sample_csv")  # Load your dataset

# Convert to pandas DataFrame for easier handling
df = pd.DataFrame(df)

# Print out the columns to check the dataset
print(df.columns)  # This will show all column names, ensure 'quantity' and 'value' exist

# Step 2: Add Title and Description
text("# 📊 Item Data Explorer")
text("Explore the item dataset with interactive filters and visualizations.")

# Step 3: Show Full Dataset
text("## 📋 Full Dataset")
table(df, title="Complete Item Dataset")

# Step 4: Check if the expected columns exist
if "quantity" in df.columns and "value" in df.columns:
    # Slider to Filter by Quantity
    text("## 🔍 Filter by Quantity")
    quantity_threshold = slider("Minimum Quantity", min_val=0, max_val=20, default=5)

    # 🛠 Use Pandas for filtering based on quantity
    filtered_df = df[df["quantity"] >= quantity_threshold]

    # Step 5: Show Filtered Table
    if not filtered_df.empty:
        table(filtered_df, title=f"Items with Quantity ≥ {quantity_threshold}")
    else:
        text("⚠️ No items match the filter criteria.")

    # Step 6: Create a Scatter Plot Visualization
    text("## 📈 Quantity vs. Value Scatter Plot")
    fig = px.scatter(
        filtered_df,
        x="quantity",
        y="value",
        color="item",
        title="Relationship between Quantity and Value",
        labels={"quantity": "Quantity", "value": "Value"},
        template="plotly_white"
    )
    plotly(fig)

    # Step 7: Create a Bar Chart to Compare Value by Item
    text("## 📊 Bar Chart - Total Value by Item")
    fig_bar = px.bar(
        df.groupby("item").agg({"value": "sum"}).reset_index(),
        x="item",
        y="value",
        title="Total Value by Item",
        labels={"item": "Item", "value": "Total Value"},
        template="plotly_white"
    )
    plotly(fig_bar)
else:
    text("⚠️ The dataset does not contain the required columns 'quantity' and 'value'.")
