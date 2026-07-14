import streamlit as st
from graph.travel_graph import build_graph

graph = build_graph()

st.title("AI Travel Planner")

query = st.text_input("Describe your trip")

if st.button("Generate Trip") and query:

    result = graph.invoke({"query": query})

    # ✅ Itinerary at the top
    st.subheader("Travel Itinerary")
    st.write(result["itinerary"])

    # ✅ Weather
    st.subheader("Current Weather")

    weather = result.get("weather", {})

    if weather:
        st.write(f"🌡 Temperature: {weather.get('temperature')}°C")
        st.write(f"💨 Wind Speed: {weather.get('windspeed')} km/h")
    else:
        st.write("Weather information not available")

    # ✅ Places
    st.subheader("Places to Visit")

    places = result.get("places", [])

    if places:
        for place in places:
            st.write(f"📍 {place}")
    else:
        st.write("No places found.")

    # ✅ Flights
    st.subheader("Recommended Flights")
    st.write(result.get("flights", "No flights available"))

    # ✅ Hotels
    st.subheader("Hotels")
    st.write(result.get("hotels", "No hotels available"))

    # ✅ Restaurants
    st.subheader("Restaurants")
    st.write(result.get("restaurants", "No restaurants available"))

    # ✅ Cost
    st.subheader("Estimated Cost")
    st.json(result.get("cost", {}))