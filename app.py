import streamlit as st
import pandas as pd
from PIL import Image
import pickle
from sklearn.cluster import KMeans

# Loading the model
filename = "dietrec.sav"
loaded_model = pickle.load(open(filename, 'rb'))

# Reading Food.csv for diet recommendation
data = pd.read_csv("food.csv")
diet = data.drop("Food_items", axis=1)

# Applying k-means and defining the number of clusters
km = KMeans(n_clusters=4)
y_predicted = km.fit_predict(diet)

# Adding a new column containing the cluster a food item is part of
data['cluster'] = y_predicted

# Streamlit app
st.set_page_config(page_title="DIET RECOMMENDATION SYSTEM", page_icon="diet.ico")

st.title("DIET RECOMMENDATION SYSTEM")

# User input
weight = st.number_input("Enter your weight in kg", min_value=0.0, step=0.1, format="%.1f")
height = st.number_input("Enter your height in m", min_value=0.01, step=0.01, format="%.2f")  # Set a minimum height value

# Check for zero height
if height == 0:
    st.error("Error: Height should be a non-zero value.")
else:
    # Calculate BMI
    bmi = weight / (height ** 2)

    # Predict using the model
    Xdata = {'Height': [height], 'Weight': [weight], 'BMI': [bmi]}
    df = pd.DataFrame(Xdata, columns=['Height', 'Weight', 'BMI'])
    predicted = loaded_model.predict(df)
    predicted_cluster = predicted[0]

    # Display BMI and diet recommendation with styling
    st.markdown(f"### Your BMI is **{bmi:.2f}**", unsafe_allow_html=True)

    st.markdown("### Diet Recommendation:")
    recommended_food = data[data['cluster'] == predicted_cluster].Food_items.sample(5).values
    for i, food in enumerate(recommended_food, 1):
        st.markdown(f"{i}. {food}", unsafe_allow_html=True)

    # Additional Streamlit settings
    st.set_option('deprecation.showfileUploaderEncoding', False)
