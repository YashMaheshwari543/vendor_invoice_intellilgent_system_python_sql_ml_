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
    """Load trained freight cost prediction model."""
    with open(model_path, "rb") as f:
        model = joblib.load(f)

    return model


def predict_freight_cost(input_data):
    """Predict freight cost using Invoice Dollars."""

    model = load_model()

    # The trained model uses only the Dollars feature.
    if isinstance(input_data, pd.DataFrame):
        input_df = input_data[["Dollars"]].copy()
    else:
        input_df = pd.DataFrame({
            "Dollars": input_data["Dollars"]
        })

    prediction = model.predict(input_df)[0]

    return {
        "Predicted_Freight": round(float(prediction), 2)
    }
