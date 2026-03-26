import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Load dataset
df = pd.read_csv("data.csv")

# 🔥 FIX: clean column names
df.columns = df.columns.str.strip()

# Convert dates
df['ScheduledDay'] = pd.to_datetime(df['ScheduledDay'])
df['AppointmentDay'] = pd.to_datetime(df['AppointmentDay'])

# Create NoShow column
df['NoShow'] = df['No-show'].apply(lambda x: 1 if str(x).strip().lower()=="yes" else 0)

st.title("📊 Hospital Appointment QA Dashboard")

# Sidebar filters
st.sidebar.header("Filters")
gender_filter = st.sidebar.multiselect("Select Gender:", df['Gender'].unique())
no_show_filter = st.sidebar.selectbox("Show No-Show Only?", ["All", "Yes", "No"])

filtered = df.copy()
if gender_filter:
    filtered = filtered[filtered['Gender'].isin(gender_filter)]
if no_show_filter=="Yes":
    filtered = filtered[filtered['NoShow']==1]
elif no_show_filter=="No":
    filtered = filtered[filtered['NoShow']==0]

# Display dataset
st.subheader("Filtered Data")
st.dataframe(filtered.head(100))  # limit for performance

# QA metrics
st.markdown("### 📌 QA Summary")
st.write("Total Records (filtered):", len(filtered))
st.write("Total No-Shows:", filtered['NoShow'].sum())
st.write("Duplicate Rows:", filtered.duplicated().sum())
st.write("Missing Values:", filtered.isnull().sum().sum())
st.write("Invalid Ages:", len(filtered[filtered['Age'] < 0]))

# Visualizations
st.markdown("### 📈 Visualizations")

fig1, ax1 = plt.subplots()
sns.histplot(filtered['Age'], bins=30, kde=True, ax=ax1)
ax1.set_title("Age Distribution")
st.pyplot(fig1)

fig2, ax2 = plt.subplots()
sns.countplot(x='Gender', hue='NoShow', data=filtered, ax=ax2)
ax2.set_title("No-Show by Gender")
st.pyplot(fig2)

st.write("Current working directory:", os.getcwd())
st.write("Files in directory:", os.listdir())