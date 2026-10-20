
import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

st.set_page_config(
    page_title="ML-Enhanced CFD Heat Exchanger",
    page_icon="🌡️",
    layout="wide"
)

st.title("ML-Enhanced CFD Heat Exchanger Optimization")
st.write("Predict heat exchanger performance using trained ML surrogate models.")

MODEL_PATH = (
    Path(__file__).parent
    / "models"
    / "best_surrogate_models.joblib"
)

@st.cache_resource
def load_saved_model():
    return joblib.load(MODEL_PATH)

if not MODEL_PATH.exists():
    st.error(
        f"Model file not found: {MODEL_PATH}. "
        "Upload best_surrogate_models.joblib into the models folder."
    )
    st.stop()

try:
    saved = load_saved_model()
except Exception as exc:
    st.error(f"Could not load the saved model: {exc}")
    st.stop()

models = saved["models"]
features = saved["features"]
targets = saved["targets"]

st.caption(f"Dataset type: {saved.get('dataset_type', 'Not specified')}")

if not saved.get("genuine_cfd_validated", False):
    st.warning(
        "This model has not been validated against genuine CFD simulation results."
    )

st.subheader("Operating conditions")

defaults = {
    "mass_flow_kg_s": 0.10,
    "inlet_temp_C": 25.0,
    "wall_heat_flux_W_m2": 2000.0,
    "tube_diameter_m": 0.02,
    "tube_length_m": 2.0,
}

values = {}

for feature in features:
    values[feature] = st.number_input(
        feature,
        value=float(defaults.get(feature, 1.0)),
        format="%.6f"
    )

if st.button("Predict performance", type="primary"):
    input_data = pd.DataFrame(
        [[values[f] for f in features]],
        columns=features
    )

    results = {}

    for target in targets:
        if target not in models:
            st.error(f"No trained model found for target: {target}")
            st.stop()

        results[target] = float(models[target].predict(input_data)[0])

    output = pd.DataFrame(
        [{"Output": key, "Prediction": value}
         for key, value in results.items()]
    )

    st.dataframe(output, use_container_width=True, hide_index=True)

    st.download_button(
        "Download predictions",
        output.to_csv(index=False),
        file_name="heat_exchanger_predictions.csv",
        mime="text/csv"
    )

