
# Item Data Explorer 📊

An interactive data exploration app built with **Preswald**, **Plotly**, and **Pandas** to explore item data. It includes dynamic filtering, visualizations, and a table to analyze the relationship between quantity and value.

## Output :
<img width="1428" alt="Screenshot 2025-04-26 at 4 32 45 PM" src="https://github.com/user-attachments/assets/51bd27f0-9ee4-4b96-bb47-99494cb07789" />
<img width="1429" alt="Screenshot 2025-04-26 at 4 33 01 PM" src="https://github.com/user-attachments/assets/c74d957d-fdbd-42b4-a127-079ef39ec3a4" />
<img width="1436" alt="Screenshot 2025-04-26 at 4 33 21 PM" src="https://github.com/user-attachments/assets/e2435045-8b78-40a6-8f7a-37512dc8cd5b" />
<img width="1434" alt="Screenshot 2025-04-26 at 4 33 34 PM" src="https://github.com/user-attachments/assets/465194e5-c2e8-4d99-a4c4-114690b6ff20" />

## Features

- **Filter by Quantity**: Slider to filter items by quantity.
- **Visualize Data**: Scatter plot and bar chart to visualize item data.
- **Full Dataset**: Display the complete dataset.

## Technologies Used

- **Preswald**: Framework for interactive apps.
- **Plotly**: Used for interactive visualizations.
- **Pandas**: Data manipulation and processing.
- **Python 3.x**: Programming language.

## Prerequisites

Install the required Python packages:

```bash
pip install preswald pandas plotly
```

## How to Run

1. **Clone or download** the script.
2. **Prepare the dataset**: Use the following format for `sample_data.csv`:

   ```csv
   item,quantity,value
   Item A,10,100
   Item B,5,60
   Item C,8,80
   Item D,12,150
   Item E,7,90
   Item F,9,110
   Item G,4,50
   Item H,11,130
   Item I,6,70
   Item J,3,40
   ```

3. **Run the script**:

   ```bash
   preswald run      
```


