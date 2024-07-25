import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load historical data
data = pd.read_csv(r"C:\Users\DELL\Desktop\stock price prediction\stock prices dataset.csv")
data['Date'] = pd.to_datetime(data['Date'], format = 'mixed')
data.set_index('Date', inplace=True)
data.rename(columns={'Price': 'Close', 'Vol.': 'Volume'}, inplace=True)

# Load future predictions
future_df = pd.read_csv(r"C:\Users\DELL\Desktop\stock price prediction\future_predictions.csv")
future_df['Date'] = pd.to_datetime(future_df['Date'], format = 'mixed')
future_df.set_index('Date', inplace=True)

# Streamlit app
st.title('Reliance Industries Limited Stock Price Forecasting')

# Future Predictions Section
st.subheader('Future Predictions (2024-2029)')

# Plot future predictions
st.line_chart(future_df[['Predicted_Close', 'Predicted_Volume']], width=800, height=400)

# User input for date selection
st.subheader('Select Date for Predicted Stock Value')
selected_date = st.date_input("Select a date:", min_value=future_df.index.min().date(), max_value=future_df.index.max().date())

# Display the predicted values for the selected date
if pd.to_datetime(selected_date) in future_df.index:
    predicted_close = future_df.loc[pd.to_datetime(selected_date), 'Predicted_Close']
    predicted_volume = future_df.loc[pd.to_datetime(selected_date), 'Predicted_Volume']
    st.write(f"Predicted Closing Price on {selected_date}  :    {predicted_close}")
    st.write(f"Predicted Volume on {selected_date}  :   {predicted_volume}")
else:
    st.write("Selected date is out of the prediction range.")

# Display the Streamlit app with `streamlit run app.py`
