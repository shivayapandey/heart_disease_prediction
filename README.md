# 📈 Heart Disease Prediction System 🩺

This project is a comprehensive heart disease prediction system that incorporates a machine learning model to predict heart disease based on user input. The system is built using Python and integrates with MongoDB for data storage and retrieval.

## 🚀 Features

1. **MongoDB Integration**: The system establishes a connection with a MongoDB database to store user inputs and prediction results. 📂
2. **User Interface**: A user interface is implemented using FastAPI, allowing users to submit their data for prediction. The interface is designed for versatility and performance. 🌐
3. **Model Prediction and Data Handling**: After storing the user input data in the MongoDB database, the system retrieves this data to perform the prediction using the machine learning model. The prediction outcome is then saved back into the database. 🔮

## 📋 Requirements

- Python 3.x 🐍
- FastAPI 🚀
- MongoDB 📂
- Scikit-learn 🧠
- Pandas 📊
- NumPy 🔢
- Joblib 📦

## 🚀 Installation

1. Clone the repository:

git clone https://github.com/shivayapandey/heart-disease-prediction.git

css
Copy code

2. Navigate to the project directory:

cd heart-disease-prediction-system

markdown
Copy code

3. Install the required dependencies:

pip install -r requirements.txt

markdown
Copy code

## 🏃‍♂️ Usage

1. Start the MongoDB server. 🚀

2. Run the FastAPI application:

uvicorn main:app --reload

markdown
Copy code

3. Access the user interface by navigating to `http://localhost:8000` in your web browser. 🌐

4. Submit your data through the user interface. 📝

5. The system will store your input data in the MongoDB database, perform the prediction using the machine learning model, and save the prediction result back into the database. 💾

## 📸 Screenshots
### MongoDB Input Files Saved
![Screenshot 2024-04-03 at 5 58 30 PM](https://github.com/shivayapandey/heart_disease_prediction/assets/143429039/9f0156e0-baea-4652-884e-8981d3326742)

### Model Graphs

*Model achieved 83% accuracy*
<img width="1470" alt="Screenshot 2024-04-05 at 4 37 19 AM" src="https://github.com/shivayapandey/heart_disease_prediction/assets/143429039/5e427f85-73d0-4b74-9ff9-b377e60a7f5d">
<img width="1470" alt="Screenshot 2024-04-05 at 4 37 24 AM" src="https://github.com/shivayapandey/heart_disease_prediction/assets/143429039/514594ea-e577-4d26-8893-43c4efe93a8a">
<img width="1470" alt="Screenshot 2024-04-05 at 4 37 38 AM" src="https://github.com/shivayapandey/heart_disease_prediction/assets/143429039/011b7fb5-e338-4c03-b75e-3adffceecd92">
<img width="1470" alt="Screenshot 2024-04-05 at 4 37 40 AM" src="https://github.com/shivayapandey/heart_disease_prediction/assets/143429039/4ad76be3-8620-4639-bf78-62f17d30d6de">
<img width="1470" alt="Screenshot 2024-04-05 at 4 37 43 AM" src="https://github.com/shivayapandey/heart_disease_prediction/assets/143429039/0f4e184b-e6a0-4238-a619-bda89245bf44">





## 🤝 Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request. 🙌

## 📄 License

This project is licensed under the [MIT License](LICENSE). 📜
