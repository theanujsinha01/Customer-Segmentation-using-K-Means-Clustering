
# 🛍️ Customer Segmentation using K-Means (Streamlit App)

This project performs **customer segmentation** using **K-Means Clustering**, and builds an interactive **Streamlit web app** for visual analysis and business insights.

It helps businesses understand different types of customers like:
- 🟥 High-income, high-spending customers
- 🟦 Low-income, low-spending customers
- 🟪 Impulsive buyers
- 🟩 Cautious but wealthy customers

---

## 📌 Objective

🎯 To segment customers into useful clusters using machine learning and visualize results dynamically.  
The tool allows:
- Marketing teams to design **targeted strategies**
- Businesses to **personalize offers**
- Analysts to **explore patterns** in customer behavior

---

## 🚀 Features

✅ Upload your own dataset  
✅ Select any 2 numeric features (Age, Income, Spending Score, etc.)  
✅ Elbow Method to choose the best number of clusters  
✅ K-Means clustering  
✅ Dynamic scatter plot with cluster colors  
✅ Smart report with cluster-wise insights  
✅ Styled table showing cluster means  
✅ Business-friendly auto descriptions

---

## 🧪 Technologies Used

| Tool / Library     | Purpose                             |
|--------------------|--------------------------------------|
| Python             | Main programming language            |
| Pandas             | Data analysis & cleaning             |
| Matplotlib         | Elbow graph                          |
| Seaborn            | Cluster visualization                |
| Scikit-learn       | K-Means clustering                   |
| Streamlit          | UI for interactive web app           |

---

## 📊 Dataset Overview

We used `Mall_Customers.csv`, containing:

| Column                | Description                         |
|------------------------|-------------------------------------|
| CustomerID            | Unique customer ID                  |
| Gender                | Male / Female                       |
| Age                   | Age of customer                     |
| Annual Income (k$)    | Income in thousands of dollars      |
| Spending Score (1–100)| Score assigned by the shopping mall |

---

## 🖼️ How It Works

1. Upload the CSV file (or use the default one)
2. Select 2 numeric features for clustering
3. See the Elbow Method graph to pick the best number of clusters (K)
4. Visualize customers in color-coded clusters
5. Read auto-generated cluster descriptions
6. View a styled summary table for insights

---

