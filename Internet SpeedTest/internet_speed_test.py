from tkinter import *
import speedtest
import threading

root = Tk()
root.title("Internet Speed Test")
root.geometry("560x600")
root.resizable(False, False)
root.configure(bg="#1a212d")

# Function to animate a number from 0 to the final result
def animate_number(label, target, unit, current=0):

     # Keep increasing the number until it reaches the target
    if current < target:

        # Calculate how much the number should increase each time
        step = max(target / 40, 1)

         # Increase the current number without going past the target
        current = min(current + step, target)

        # Update the label with the current animated number
        label.config(text=f"{current:.1f} {unit}")

        # Run this function again after 25 milliseconds
        root.after(
            25,
            animate_number,
            label,
            target,
            unit,
            current
        )
    else:
        # Display the final result
        label.config(text=f"{target:.1f} {unit}")

# Function that describes the quality of the internet connection
def connection_quality(speed):
          # If the speed is below 10 Mbps, the connection is slow
        if speed < 10:
            return "Slow Connection"
        
         # If the speed is between 10 and 49 Mbps, the connection is good
        elif speed < 50:
            return "Good Connection"

         # If the speed is between 50 and 99 Mbps, the connection is very good
        elif speed < 100: 
            return "Very Good Connection"

         # If the speed is 100 Mbps or higher, the connection is very fast
        else: 
            return "Very fast Connection"

# Function that performs the internet speed test
def Check():

     # Create a Speedtest object
    test = speedtest.Speedtest()

    # Test the download speed and convert it to Mbps
    downloading = round(test.download() / (1024 * 1024), 2)

    # Animate the download speed
    root.after(0, animate_number, download_label, downloading, "Mbps")

     # Test the upload speed and convert it to Mbps
    uploading = round(test.upload() / (1024 * 1024), 2)

    # Display the upload speed
    root.after(0, animate_number, upload_label, uploading, "Mbps")

    # Get the ping result and round it to 2 decimal places
    ping = round(test.results.ping, 2)

    # Animate the upload speed
    root.after(0, animate_number, ping_label, ping, "ms")

    # Work out the connection quality using the download speed
    quality = connection_quality(downloading)

    # Display the connection quality
    connection_label.config(text=quality)

# Title
Label(
    root,
    text="Internet Speed Test",
    font=("Arial", 28, "bold"),
    fg="white",
    bg="#1a212d"
).pack(pady=40)

# Ping
Label(
    root,
    text="PING",
    font=("Arial", 15, "bold"),
    fg="white",
    bg="#1a212d"
).pack()

ping_label = Label(
    root,
    text="0 ms",
    font=("Arial", 25, "bold"),
    fg="#00d9ff",
    bg="#1a212d"
)
ping_label.pack(pady=(5, 20))

# Download
Label(
    root,
    text="DOWNLOAD",
    font=("Arial", 15, "bold"),
    fg="white",
    bg="#1a212d"
).pack()

download_label = Label(
    root,
    text="0 Mbps",
    font=("Arial", 25, "bold"),
    fg="#00d9ff",
    bg="#1a212d"
)
download_label.pack(pady=(5, 20))

# Upload
Label(
    root,
    text="UPLOAD",
    font=("Arial", 15, "bold"),
    fg="white",
    bg="#1a212d"
).pack()

upload_label = Label(
    root,
    text="0 Mbps",
    font=("Arial", 25, "bold"),
    fg="#00d9ff",
    bg="#1a212d"
)
upload_label.pack(pady=(5, 30))

connection_label = Label(
    root,
    text="Connection: Not Tested",
    font=("Arial", 14, "bold"),
    fg="#00d9ff",
    bg="#1a212d"
)
connection_label.pack(pady=10)

# Start button
start_button = Button(
    root,
    text="START",
    font=("Arial", 18, "bold"),
    width=15,
    height=2,
    command=lambda: threading.Thread(
    target=Check,
    daemon=True
    ).start()
)

# Display the START button in the window
start_button.pack() 

# Keep the application running and listen for user actions
root.mainloop()