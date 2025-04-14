import streamlit as st
import pandas as pd
from cost_calculator import calculate_costs

st.title("☁️ Cloud Cost Optimizer Dashboard")

df = pd.read_csv("data/usage_data.csv")
st.subheader("Cloud Usage Data")
st.dataframe(df)

costs = calculate_costs(df)

st.subheader("💰 Cost Breakdown")
total_cost = sum(costs.values())
for service, cost in costs.items():
    st.write(f"**{service}**: ${cost}")

st.markdown(f"### 🔻 Total Monthly Cost: **${round(total_cost, 2)}**")

# Suggestions
st.subheader("🧠 Optimization Suggestions")
if df[df['service'] == 'EC2']['usage_hours'].values[0] > 100:
    st.write("🔹 Consider using EC2 Spot Instances or Auto Scaling to reduce EC2 cost.")
if df[df['service'] == 'Lambda']['invocations'].values[0] > 100000:
    st.write("🔹 Optimize your Lambda functions or reduce invocation frequency.")
if df[df['service'] == 'S3']['storage_gb'].values[0] > 40:
    st.write("🔹 Use S3 Infrequent Access or Glacier for older files.")
