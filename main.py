
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# --- App Title ---
st.title('Interactive Linear Regression')

# --- Sidebar for Controls ---
st.sidebar.header('Data Controls')

# Add controls to the sidebar
num_points = st.sidebar.slider('Number of points', 50, 1000, 500)
slope_a = st.sidebar.slider('Slope (a) in y = ax + b', 0.0, 10.0, 2.0, 0.1)
noise = st.sidebar.slider('Noise level', 0, 100, 25)

# --- Data Generation ---
# Use a constant seed for reproducibility within a session
np.random.seed(0)
# The 'b' in y = ax + b
intercept_b = 10 

X = np.random.rand(num_points, 1) * 100
# y = a*x + b + noise
y = slope_a * X.squeeze() + np.random.randn(num_points) * noise + intercept_b

# --- Model Training ---
model = LinearRegression()
model.fit(X, y)
y_pred = model.predict(X)

# --- Plotting ---
st.write(f"### Regression Plot")
fig, ax = plt.subplots(figsize=(10, 6))
ax.scatter(X, y, alpha=0.6, label='Data Points')
ax.plot(X, y_pred, color='red', linewidth=2, label='Linear Regression')
ax.set_title(f'Linear Regression with {num_points} Points')
ax.set_xlabel('X')
ax.set_ylabel('y')
ax.legend()
ax.grid(True)

# Display the plot in Streamlit
st.pyplot(fig)

# --- Display Model Coefficients ---
st.write("### Model Information")
st.write(f"**Coefficient (a):** `{model.coef_[0]:.2f}`")
st.write(f"**Intercept (b):** `{model.intercept_:.2f}`")