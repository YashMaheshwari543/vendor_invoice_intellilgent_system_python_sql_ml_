import joblib
import pandas as pd

from pathlib import Path

MODEL_PATH = (
    Path(__file__).resolve().parent.parent
    / "Freight_csot_prediction"
    / "models"
    / "predict_freight_model.pkl"
)


def load_model(model_path=MODEL_PATH):
    """
    Load trained freight cost prediction model.
    """
    with open(model_path, "rb") as f:
        model = joblib.load(f)

    return model


def predict_freight_cost(input_data):
    """
    Predict freight cost for a new vendor invoice.

    Accepts either:
    - pandas DataFrame
    - dictionary
    """

    model = load_model()

    # If app.py sends a DataFrame
    if isinstance(input_data, pd.DataFrame):
        input_df = input_data[["Dollars"]].copy()

    # If called with a dictionary
    else:
        input_df = pd.DataFrame({
            "Dollars": input_data["Dollars"]
        })

    # Generate prediction
    prediction = model.predict(input_df)[0].round()

    return {
        "Predicted_Freight": prediction
    }


if __name__ == "__main__":

    # Example local testing
    sample_data = {
        "Dollars": [18500]
    }

    prediction = predict_freight_cost(sample_data)

    print(prediction)
