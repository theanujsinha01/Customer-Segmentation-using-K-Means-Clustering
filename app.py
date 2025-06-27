import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans

# Streamlit setup
st.set_page_config(page_title="Customer Segmentation", layout="wide")
st.title("🛍️ Customer Segmentation using K-Means")

# Upload CSV file
uploaded_file = st.file_uploader("📤 Upload Customer Dataset (CSV)", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.subheader("📄 Dataset Preview")
    st.dataframe(df.head())

    # Feature selection
    st.subheader("🔧 Select Features for Clustering")
    features = st.multiselect(
        "Choose exactly 2 numeric features:",
        df.select_dtypes(include='number').columns,
        default=["Annual Income (k$)", "Spending Score (1-100)"]
    )

    if len(features) != 2:
        st.warning("Please select exactly 2 numeric features.")
    else:
        X = df[features]

        # Elbow Method to find best K
        st.subheader("📈 Elbow Method (to choose best number of clusters)")
        wcss = []
        for i in range(1, 11):
            kmeans = KMeans(n_clusters=i, init='k-means++', random_state=0)
            kmeans.fit(X)
            wcss.append(kmeans.inertia_)

        fig1, ax1 = plt.subplots()
        sns.lineplot(x=range(1, 11), y=wcss, marker='o', ax=ax1)
        ax1.set_xlabel("Number of Clusters (K)")
        ax1.set_ylabel("WCSS")
        ax1.set_title("Elbow Method")
        st.pyplot(fig1)

        # Choose number of clusters
        k = st.slider("Select number of clusters (K)", min_value=2, max_value=10, value=5)

        # KMeans model
        model = KMeans(n_clusters=k, init='k-means++', random_state=0)
        df['Cluster'] = model.fit_predict(X)

        # Clustered Data
        st.subheader("🧠 Clustered Data (sample)")
        st.dataframe(df[[features[0], features[1], 'Cluster']].head())

        # Visualize Clusters
        st.subheader("🎨 Cluster Visualization")
        fig2, ax2 = plt.subplots()
        sns.scatterplot(data=df, x=features[0], y=features[1], hue='Cluster', palette='Set2', s=100, ax=ax2)
        ax2.set_title("Customer Clusters")
        st.pyplot(fig2)

        # Cluster Report
        st.subheader("📋 Cluster Report (Business Insights)")
        cluster_summary = df.groupby('Cluster')[[features[0], features[1]]].mean().reset_index()
        st.dataframe(cluster_summary)

        # Dynamic cluster descriptions
        st.markdown("### 💡 Cluster Descriptions (Auto Generated)")
        feature1 = features[0]
        feature2 = features[1]
        mean1 = df[feature1].mean()
        mean2 = df[feature2].mean()

        for idx, row in cluster_summary.iterrows():
            val1 = row[feature1]
            val2 = row[feature2]
            st.markdown(f"**Cluster {int(row['Cluster'])}:**")

            level1 = "Low" if val1 < mean1 else "High"
            level2 = "Low" if val2 < mean2 else "High"

            st.write(f"- {level1} **{feature1}**, {level2} **{feature2}** → Use custom marketing for this group.")

        st.success("✅ Use this dynamic report to understand and target customer groups smartly!")
