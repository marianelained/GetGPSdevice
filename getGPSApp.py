import streamlit as st
import geocoder
import pandas as pd

def main():
    st.title("Device GPS Location")

    if st.button("Get GPS Location"):
        # Get the current GPS location
        location = geocoder.ip('me').latlng

        # Print the location
        st.write("Latitude:", location[0])
        st.write("Longitude:", location[1])

        # Create DataFrame
        df = pd.DataFrame({'Latitude': [location[0]],
                           'Longitude': [location[1]]
                           })

        # Save GPS data to CSV
        save_gps_data(df)

        # Display saved GPS data
        display_saved_gps_data()

def save_gps_data(df):
    df.to_csv("gps.csv", mode='a', index=False, header=False)

def display_saved_gps_data():
    df = pd.read_csv("gps.csv")
    st.dataframe(df)

if __name__ == '__main__':
    main()
