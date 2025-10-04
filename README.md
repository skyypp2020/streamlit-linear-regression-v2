Demosite: https://app-linear-regression-v2-asiv4zjvi39tta3jqnrd8j.streamlit.app/

---

# Project: Interactive Linear Regression Analysis

This project demonstrates a simple linear regression model within an interactive web application built with Streamlit. The process follows the CRISP-DM methodology.

---

## 1. Business Understanding

The primary goal is to visualize and understand the effect of different parameters on a linear regression model. By creating an interactive application, users can dynamically change variables such as the number of data points, the underlying slope of the data, and the level of random noise to immediately see their impact on the regression line.

## 2. Data Understanding

The data for this project is not from an external source but is synthetically generated using the NumPy library. This allows for a controlled environment to study the model's behavior.

- **Generation Formula:** The data is created based on the linear equation `y = ax + b` with added randomness.
- **X-values:** A set of uniformly distributed random numbers.
- **y-values:** Calculated by applying the formula to the X-values, then introducing Gaussian noise.
- **Interactivity:** The application allows the user to control the slope (`a`), the amount of noise, and the total number of data points.

## 3. Data Preparation

The generated data is prepared for the model as follows:

1.  **Generation:** NumPy is used to create the `X` and `y` arrays based on the user's input from the Streamlit sidebar.
2.  **Reshaping:** The `X` data, which is initially a 1D array, is reshaped into a 2D array. This is a requirement for the `scikit-learn` `LinearRegression` model, which expects input features in a `(n_samples, n_features)` format.

## 4. Modeling

A simple linear regression model was chosen for this analysis.

- **Library:** `scikit-learn`
- **Model:** `LinearRegression`
- **Process:** For each change in the input data (triggered by the user), a new `LinearRegression` model is instantiated and fitted to the newly generated data points. The model then makes predictions on the same `X` values to generate the regression line.

## 5. Evaluation

Evaluation is performed visually and quantitatively within the application:

- **Visual Plot:** The core of the evaluation is a `matplotlib` scatter plot showing the original data points overlaid with the red regression line. This provides an immediate, intuitive understanding of how well the model fits the data.
- **Model Coefficients:** The calculated slope (`a`) and intercept (`b`) of the regression line are displayed in the app, allowing for a quantitative comparison with the input parameters.

## 6. Deployment

The model is deployed as an interactive web application using **Streamlit**.

- **Interface:** The app features a main area to display the plot and a sidebar containing sliders for user input.
- **Execution:** The application is self-contained within the `main.py` script and can be run with a single command.

### How to Run the Application

1.  **Install dependencies:**
    ```bash
    pip install streamlit numpy scikit-learn matplotlib
    ```
2.  **Run the app:**
    ```bash
    streamlit run main.py
    ```