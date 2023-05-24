import streamlit as st
import geocoder
import pandas as pd
import pywebview as pw
import base64

def main():
    st.title("Device GPS Location and Camera")

    # Get the current GPS location
    location = get_gps_location()

    # Print the location
    st.write("Latitude:", location[0])
    st.write("Longitude:", location[1])

    # Capture photo with camera
    capture_photo()

def get_gps_location():
    # Use geocoder to get the current GPS location
    g = geocoder.ip('me')
    return g.latlng

def capture_photo():
    # Create a WebView to handle camera capture
    pw.create_window("Camera Capture", html="""
        <html>
        <head>
        <script type="text/javascript">
        function capturePhoto() {
            navigator.mediaDevices.getUserMedia({ video: true, audio: false })
                .then(function(stream) {
                    var video = document.getElementById('video');
                    video.srcObject = stream;
                    video.play();

                    var canvas = document.createElement('canvas');
                    var context = canvas.getContext('2d');
                    video.addEventListener('canplay', function() {
                        canvas.width = video.videoWidth;
                        canvas.height = video.videoHeight;
                        context.drawImage(video, 0, 0, video.videoWidth, video.videoHeight);
                        var imgData = canvas.toDataURL('image/jpeg');
                        window.pywebview.api.handlePhotoCapture(imgData);
                        stream.getTracks().forEach(function(track) {
                            track.stop();
                        });
                    });
                })
                .catch(function(error) {
                    console.error('Error accessing camera:', error);
                });
        }
        </script>
        </head>
        <body>
        <video id="video" autoplay></video>
        <button onclick="capturePhoto()">Capture Photo</button>
        </body>
        </html>
    """)

    # Register a WebView API handler to receive captured photo
    pw.api.handlePhotoCapture = handle_photo_capture

    # Open the WebView window
    pw.start()

def handle_photo_capture(img_data):
    # Decode the base64 image data
    img_bytes = base64.b64decode(img_data.split(',')[1])

    # Save the photo with GPS location
    save_photo_with_gps(img_bytes)

def save_photo_with_gps(img_bytes):
    # Get the current GPS location
    location = get_gps_location()

    # Save the photo with GPS location
    # Modify this code to suit your specific needs
    # For example, you can save the photo to a file, database, or perform any other processing
    # Here, we'll just print the GPS location and display the photo in Streamlit
    st.write("Photo Captured with GPS Location:")
    st.write("Latitude:", location[0])
    st.write("Longitude:", location[1])
    st.image(img_bytes, use_column_width=True)

if __name__ == '__main__':
    main()
