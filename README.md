# Heart Disease Prediction System

This project is a comprehensive heart disease prediction system that incorporates a machine learning model to predict heart disease based on user input. The system is built using Python and integrates with MongoDB for data storage and retrieval.

## Features

1. **MongoDB Integration**: The system establishes a connection with a MongoDB database to store user inputs and prediction results.

2. **User Interface**: A user interface is implemented using FastAPI, allowing users to submit their data for prediction. The interface is designed for versatility and performance.

3. **Model Prediction and Data Handling**: After storing the user input data in the MongoDB database, the system retrieves this data to perform the prediction using the machine learning model. The prediction outcome is then saved back into the database.

## Requirements

- Python 3.x
- FastAPI
- MongoDB
- Scikit-learn
- Pandas
- NumPy
- Joblib

## Installation

1. Clone the repository:

2. Navigate to the project directory:

3. Install the required dependencies:
pip install -r requirements.txt

## Usage

1. Start the MongoDB server.

2. Run the FastAPI application:

   uvicorn main:app --reload

3. Access the user interface by navigating to `http://localhost:8000` in your web browser.

4. Submit your data through the user interface.

5. The system will store your input data in the MongoDB database, perform the prediction using the machine learning model, and save the prediction result back into the database.

## Screenshots
![Screenshot 2024-04-03 at 5 58 30 PM](https://github.com/shivayapandey/heart_disease_prediction/assets/143429039/43be65d8-8f55-490e-8fb4-b4d442c8d1ae)



## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
