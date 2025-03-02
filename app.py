import streamlit as st
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans

# Title and Introduction
st.title("Global Connectivity Initiative with ML-Driven Resource Allocation")
st.subheader("Empowering the World Through Internet Connectivity")
st.write("""
This app simulates a system where premium internet fees from users in affluent regions are used to mine cryptocurrency.
The mined cryptocurrency is then allocated to fund internet development projects in underdeveloped regions.
Resource allocation is optimized using a machine learning model.
""")

# User Input: Premium Fee
st.sidebar.header("User Contribution")
premium_fee = st.sidebar.slider("Choose your premium contribution ($)", 5, 50, 10)
crypto_choice = st.sidebar.selectbox("Select Cryptocurrency to Mine", ["Bitcoin (BTC)", "Ethereum (ETH)", "Litecoin (LTC)"])
st.sidebar.write(f"You have chosen to contribute ${premium_fee} monthly.")

# Mining Simulation
st.header("Mining Simulation")
mining_rate = {
    "Bitcoin (BTC)": 0.00001,  # Amount of crypto mined per $1
    "Ethereum (ETH)": 0.0002,
    "Litecoin (LTC)": 0.01
}
crypto_mined = premium_fee * mining_rate[crypto_choice]
st.write(f"Using your contribution, approximately **{crypto_mined:.6f} {crypto_choice}** will be mined each month.")

# Fund Allocation
st.header("Fund Allocation")
development_fund = premium_fee * 0.8  # 80% of the fee goes to the development fund
mining_costs = premium_fee * 0.2  # 20% of the fee goes to mining costs
st.write(f"From your ${premium_fee} contribution:")
st.write(f"- **${development_fund:.2f}** will be allocated to development projects.")
st.write(f"- **${mining_costs:.2f}** will cover mining operation costs.")

# Example Dataset for Resource Allocation
st.header("Resource Allocation with Machine Learning")
st.write("### Dataset: Potential Areas for Internet Development")
data = {
    "Region": ["Region A", "Region B", "Region C", "Region D", "Region E"],
    "Population Density": [500, 1200, 300, 800, 1500],
    "Current Internet Penetration (%)": [20, 50, 10, 30, 70],
    "Funding Required ($)": [5000, 15000, 3000, 8000, 20000]
}
df = pd.DataFrame(data)
st.write(df)

# Machine Learning Model: K-Means Clustering
st.write("### ML Model: Optimizing Resource Allocation")
X = df[["Population Density", "Current Internet Penetration (%)", "Funding Required ($)"]]
kmeans = KMeans(n_clusters=3, random_state=42)
df["Cluster"] = kmeans.fit_predict(X)

# Display Clustering Results
st.write("### Clustering Results")
st.write(df)

# Allocate Resources Based on Clusters
st.write("### Optimized Resource Allocation")
allocated_funds = development_fund / df["Cluster"].nunique()
df["Allocated Funds ($)"] = df["Cluster"].apply(lambda x: allocated_funds)
st.write(df[["Region", "Cluster", "Allocated Funds ($)"]])

# Visualization of Allocation
st.bar_chart(df[["Region", "Allocated Funds ($)"]].set_index("Region"))

# Transparency Dashboard
st.header("Transparency Dashboard")
st.write("### Monthly Contributions and Mining Output")
st.write(f"- **Contribution**: ${premium_fee}")
st.write(f"- **Cryptocurrency Mined**: {crypto_mined:.6f} {crypto_choice}")
st.write(f"- **Allocated for Development Projects**: ${development_fund:.2f}")
st.write(f"- **Mining Costs**: ${mining_costs:.2f}")

st.write("### Cumulative Impact (Example Metrics)")
# Simulate cumulative data for transparency
total_users = np.random.randint(500, 1000)
total_funds = total_users * premium_fee
total_projects = int(total_funds // 1000)
st.write(f"- Total Users Participating: **{total_users}**")
st.write(f"- Total Funds Raised: **${total_funds:,.2f}**")
st.write(f"- Total Projects Supported: **{total_projects}**")

# Footer
st.write("### Together, we can bring the world online!")

