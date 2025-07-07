# Singapore HDB Resale Flat Price Prediction

This project predicts the resale price of HDB flats in Singapore using machine learning and provides an interactive web app built with Streamlit.

---

## Features

- Predicts resale prices for HDB flats based on user input
- User-friendly Streamlit interface
- Uses a trained Decision Tree model (`Decisiontree.pkl`)
- Handles categorical encoding and feature engineering
- Visualizes data preprocessing and modeling steps in Jupyter Notebook

---

## Dataset

- Historical HDB resale flat data (1990–2024) from official sources
- Data files are located in the `data/` directory

---

## Project Structure

```
.
├── singapore_main.py           # Streamlit app source code
├── pre_processing.ipynb        # Data cleaning, feature engineering, and modeling notebook
├── Decisiontree.pkl            # Trained Decision Tree model
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation
└── data/
    ├── Resale Flat Prices (Based on Approval Date), 1990 - 1999.csv
    ├── Resale Flat Prices (Based on Approval Date), 2000 - Feb 2012.csv
    ├── Resale Flat Prices (Based on Registration Date), From Jan 2015 to Dec 2016.csv
    ├── Resale Flat Prices (Based on Registration Date), From Mar 2012 to Dec 2014.csv
    └── Resale flat prices based on registration date from Jan-2017 onwards.csv
```

---

## Setup Instructions

1. **Clone the repository:**
    ```sh
    git clone https://github.com/yourusername/guvi_singapore_resale_flat.git
    cd guvi_singapore_resale_flat
    ```

2. **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

3. **Run the Streamlit app:**
    ```sh
    streamlit run singapore_main.py
    ```

---

## Usage

- Go to the "Get Prediction" section in the sidebar.
- Enter the required flat details (month, town, flat type, model, area, etc.).
- Click **PREDICT** to get the estimated resale price.

---

## Project Objective

To develop a machine learning model that accurately predicts the resale price of HDB flats in Singapore, helping buyers and sellers make informed decisions.

---


