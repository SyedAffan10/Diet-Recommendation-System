# Diet Recommendation System

This project implements a Diet Recommendation System using machine learning and Streamlit.

## Overview

The Diet Recommendation System uses a pre-trained machine learning model to recommend a diet based on user input such as weight, height, and gender. It utilizes k-means clustering for grouping food items into clusters and recommends a diet from the cluster predicted by the model.

## Prerequisites

- Python >= 3.8
- Streamlit
- pandas
- PIL (Pillow)
- scikit-learn
- Your pre-trained model file (e.g., `dietrec.sav`)
- Food data file (e.g., `food.csv`)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/SyedAffan10/Diet-Recommendation-System.git
   cd Diet-Recommendation-System

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the Streamlit app:

   ```bash
   streamlit run app.py
   ```

## Usage

1. Enter your weight and height.
2. Receive BMI calculation and diet recommendation.

## Project Structure

- `app.py`: Streamlit application script.
- `dietrec.sav`: Pre-trained machine learning model file.
- `food.csv`: Data file containing food items for clustering.

## Acknowledgments

- [Streamlit](https://streamlit.io/)
- [scikit-learn](https://scikit-learn.org/)
- [Pandas](https://pandas.pydata.org/)
- [Pillow](https://pillow.readthedocs.io/)

## Author

Syed Affan Hussain
