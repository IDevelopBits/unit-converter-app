import streamlit as st
import conversion


def load_length_page():
    col1, col2, col3 = st.columns(3)

    with col1:
        value = st.number_input("Enter length to convert to", value=100.00, step=0.5)
        convert = st.button("Convert", key="convert_length", type="primary", use_container_width=True)
    with col2:
        from_unit = st.selectbox("Unit to convert from", conversion.unit_labels["length"].keys())
    with col3:
        to_unit = st.selectbox("Unit to convert to", conversion.unit_labels["length"].keys())

    if convert:
        length = conversion.convert_length(value, from_unit, to_unit)
        with col2:
            st.metric(label="Old unit", value=f"{value:.2f} {conversion.unit_labels["length"][from_unit]}")
        with col3:
            st.metric(label="New unit", value=f"{length:.2f} {conversion.unit_labels["length"][to_unit]}")
    else:
        with col2:
            st.metric(label="Old unit", value=0)
        with col3:
            st.metric(label="New unit", value=0)

def load_weight_page():
    col1, col2, col3 = st.columns(3)

    with col1:
        value = st.number_input("Enter weight to convert to", value=100.00, step=0.5)
        convert = st.button("Convert", key="convert_weight", type="primary", use_container_width=True)
    with col2:
        from_unit = st.selectbox("Unit to convert from", conversion.unit_labels["weight"].keys())
    with col3:
        to_unit = st.selectbox("Unit to convert to", conversion.unit_labels["weight"].keys())

    if convert:
        weight = conversion.convert_weight(value, from_unit, to_unit)
        with col2:
            st.metric(label="Old unit", value=f"{value:.2f} {conversion.unit_labels["weight"][from_unit]}")
        with col3:
            st.metric(label="New unit", value=f"{weight:.2f} {conversion.unit_labels["weight"][to_unit]}")
    else:
        with col2:
            st.metric(label="Old unit", value=0)
        with col3:
            st.metric(label="New unit", value=0)


def load_temperature_page():
    col1, col2, col3 = st.columns(3)

    with col1:
        value = st.number_input("Enter temperature to convert to", value=100.00, step=0.5)
        convert = st.button("Convert", key="convert_temperature", type="primary", use_container_width=True)
    with col2:
        from_unit = st.selectbox("Unit to convert from", conversion.unit_labels["temperature"].keys())
    with col3:
        to_unit = st.selectbox("Unit to convert to", conversion.unit_labels["temperature"].keys())

    if convert:
        temperature = conversion.convert_temperature(value, from_unit, to_unit)
        with col2:
            st.metric(label="Old unit", value=f"{value:.2f} {conversion.unit_labels["temperature"][from_unit]}")
        with col3:
            st.metric(label="New unit", value=f"{temperature:.2f} {conversion.unit_labels["temperature"][to_unit]}")
    else:
        with col2:
            st.metric(label="Old unit", value=0)
        with col3:
            st.metric(label="New unit", value=0)

st.title("Unit Converter")
tabs = st.tabs(["Length", "Width", "Temperature"])

with tabs[0]:
    load_length_page()

with tabs[1]:
    load_weight_page()

with tabs[2]:
    load_temperature_page()

