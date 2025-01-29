# 🎨 Color Detection with Trackbars

## 📌 Overview
This project implements color detection using OpenCV in Python. It allows users to adjust HSV color ranges dynamically using trackbars and detect specific colors in an image.

## 🛠️ Features
- Uses OpenCV to process images in HSV color space.
- Adjustable trackbars for selecting lower and upper HSV values.
- Real-time color filtering and masking.
- Displays the original image, mask, and filtered result.

## 📸 Output Preview
![image](https://github.com/user-attachments/assets/b54777a1-dec2-4ca0-bb04-22a4a834975a)


## 🚀 Installation & Usage

### Prerequisites
Make sure you have Python and the following libraries installed:
```sh
pip install opencv-python numpy
```

### Run the Script
1. Place an image named `color_balls.jpg` in the same directory as the script.
2. Run the script using:
   ```sh
   python color_detection.py
   ```
3. Adjust the trackbars to filter specific colors.
4. Press `v` to exit the program.

## 📝 Code Explanation
1. **Read & Resize Image**: Loads the input image and resizes it.
2. **Create Trackbars**: Provides user control over HSV values.
3. **Convert to HSV**: Converts the image from BGR to HSV.
4. **Apply Mask**: Filters the image based on selected HSV values.
5. **Display Results**: Shows the original image, mask, and filtered output.

## 📂 File Structure
```
📁 Color-Detection
│── color_detection.py   # Main script
│── color_balls.jpg      # Input image
│── output.png           # Example output image
│── README.md            # Project documentation
```

## ✨ Example Output Screens
- **Original Image**
- **Mask**
- **Filtered Output**

## 📜 License
This project is open-source under the MIT License.

## 🤝 Contributing
Feel free to fork this repository, open issues, or submit pull requests. 🚀

## 📬 Contact
If you have any questions, reach out via [GitHub](https://github.com/Vaishnavit08).

