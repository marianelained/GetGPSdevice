import streamlit as st
import geocoder
import pandas as pd

def main():
    st.title("Geocoder Example")
    
    # Get user input for address
    address = st.text_input("Enter an address:")
    
    # Perform geocoding
    if address:
        g = geocoder.osm(address)
        if g.ok:
            st.write("Latitude:", g.lat)
            st.write("Longitude:", g.lng)
        else:
            st.write("Geocoding failed. Please enter a valid address.")

    # Create DataFrame
    df = pd.DataFrame({'Latitude': [g.lat],
                       'Longitude': [g.lng]
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

#this code obtains the device's GPS location and displays ot on the webapp in dataframe