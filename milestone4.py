import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Road Accident Analysis Dashboard")

# Load data
df = pd.read_csv("US_Accidents_March23.csv")

df["Start_Time"] = pd.to_datetime(df["Start_Time"], errors="coerce")
df["Hour"] = df["Start_Time"].dt.hour

# 1. Severity Distribution

st.subheader("Accident Severity Distribution")

severity_counts = df["Severity"].value_counts().sort_index()

fig, ax = plt.subplots()
ax.bar(
    severity_counts.index,
    severity_counts.values,
    color="skyblue"   # ✅ colour added
)

ax.set_xlabel("Severity")
ax.set_ylabel("Number of Accidents")

st.pyplot(fig)

st.write("Most accidents belong to medium severity levels.")

# 2. Accidents by Hour

st.subheader("Accidents by Time of Day")

hourly = df["Hour"].value_counts().sort_index()

fig, ax = plt.subplots()
ax.plot(
    hourly.index,
    hourly.values,
    color="green",    # ✅ colour added
    marker="o"
)

ax.set_xlabel("Hour of Day")
ax.set_ylabel("Number of Accidents")

st.pyplot(fig)

st.write("Accidents increase during morning and evening peak hours.")


# 3. Top 10 States

st.subheader("Top 10 Accident-Prone States")

top_states = df["State"].value_counts().head(10)

fig, ax = plt.subplots()
ax.barh(
    top_states.index,
    top_states.values,
    color="orange"    # ✅ colour added
)

ax.set_xlabel("Number of Accidents")

st.pyplot(fig)

st.write("A few states contribute to a high number of accidents.")


# Conclusion

st.subheader("Key Takeaways")

st.markdown("""
- Peak accidents occur during rush hours  
- Majority accidents are of moderate severity  
- Certain states need focused safety measures  
""")
