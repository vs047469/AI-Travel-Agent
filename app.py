import streamlit as st
from graph.travel_graph import build_graph


# -----------------------------------------
# Page Configuration
# -----------------------------------------

st.set_page_config(
    page_title="Travel AI",
    page_icon="✈️",
    layout="wide"
)


# -----------------------------------------
# Build Graph
# -----------------------------------------

@st.cache_resource
def get_graph():
    return build_graph()


graph = get_graph()


# -----------------------------------------
# Header
# -----------------------------------------

st.title("✈️ AI Travel Planner")

st.write(
    "Describe your trip and let the AI agents "
    "plan your journey."
)


# -----------------------------------------
# User Query
# -----------------------------------------

query = st.text_area(
    "Describe your trip",
    placeholder=(
        "Example: Plan a 5 day trip to Kashmir "
        "with hotels, restaurants, places to visit "
        "and flights."
    ),
    height=100
)


# -----------------------------------------
# Generate Trip
# -----------------------------------------

if st.button("🚀 Generate Trip", type="primary") and query:

    st.divider()

    # -------------------------------------
    # Progress Status
    # -------------------------------------

    status = st.status(
        "🚀 Starting AI Travel Planner...",
        expanded=True
    )

    # -------------------------------------
    # Create containers
    # -------------------------------------

    itinerary_container = st.container()

    weather_container = st.container()

    places_container = st.container()

    flights_container = st.container()

    hotels_container = st.container()

    restaurants_container = st.container()

    cost_container = st.container()

    city_images_container = st.container()

    # Store final state
    result = {}

    try:

        # ---------------------------------
        # Stream LangGraph
        # ---------------------------------

        for event in graph.stream(
            {"query": query},
            stream_mode="updates"
        ):

            for node_name, node_output in event.items():

                # ---------------------------------
                # Agent Progress
                # ---------------------------------

                display_name = (
                    node_name
                    .replace("_", " ")
                    .title()
                )

                status.write(
                    f"✅ {display_name} completed"
                )

                # ---------------------------------
                # Update final result
                # ---------------------------------

                result.update(node_output)


                # =================================
                # ITINERARY
                # =================================

                if "itinerary" in node_output:

                    with itinerary_container:

                        st.subheader(
                            "🗺️ Travel Itinerary"
                        )

                        st.write(
                            node_output["itinerary"]
                        )


                # =================================
                # WEATHER
                # =================================

                if "weather" in node_output:

                    weather = node_output["weather"]

                    with weather_container:

                        st.subheader(
                            "🌤️ Current Weather"
                        )

                        if weather:

                            col1, col2 = st.columns(2)

                            with col1:

                                st.metric(
                                    "Temperature",
                                    f"{weather.get('temperature', 'N/A')} °C"
                                )

                            with col2:

                                st.metric(
                                    "Wind Speed",
                                    f"{weather.get('windspeed', 'N/A')} km/h"
                                )

                        else:

                            st.write(
                                "Weather information not available."
                            )


                # =================================
                # PLACES
                # =================================

                if "places" in node_output:

                    places = node_output["places"]

                    with places_container:

                        st.subheader(
                            "📍 Places to Visit"
                        )

                        if places:

                            if isinstance(
                                places,
                                list
                            ):

                                for place in places:

                                    st.write(
                                        f"📍 {place}"
                                    )

                            else:

                                st.write(places)

                        else:

                            st.write(
                                "No places found."
                            )


                # =================================
                # FLIGHTS
                # =================================

                if "flights" in node_output:

                    flights = node_output["flights"]

                    with flights_container:

                        st.subheader(
                            "✈️ Recommended Flights"
                        )

                        if flights:

                            if isinstance(
                                flights,
                                list
                            ):

                                for flight in flights:

                                    st.write(
                                        f"✈️ {flight}"
                                    )

                            else:

                                st.write(flights)

                        else:

                            st.write(
                                "No flights available."
                            )


                # =================================
                # HOTELS
                # =================================

                if "hotels" in node_output:

                    hotels = node_output["hotels"]

                    with hotels_container:

                        st.subheader(
                            "🏨 Hotels"
                        )

                        if hotels:

                            if isinstance(
                                hotels,
                                list
                            ):

                                for hotel in hotels:

                                    st.write(
                                        f"🏨 {hotel}"
                                    )

                            else:

                                st.write(hotels)

                        else:

                            st.write(
                                "No hotels available."
                            )


                # =================================
                # RESTAURANTS
                # =================================

                if "restaurants" in node_output:

                    restaurants = node_output[
                        "restaurants"
                    ]

                    with restaurants_container:

                        st.subheader(
                            "🍽️ Restaurants"
                        )

                        if restaurants:

                            if isinstance(
                                restaurants,
                                list
                            ):

                                for restaurant in restaurants:

                                    st.write(
                                        f"🍽️ {restaurant}"
                                    )

                            else:

                                st.write(restaurants)

                        else:

                            st.write(
                                "No restaurants available."
                            )


                # =================================
                # CITY IMAGES
                # =================================

                if "city_images" in node_output:

                    city_images = node_output[
                        "city_images"
                    ]

                    with city_images_container:

                        if city_images:

                            st.subheader(
                                "🌆 Destination"
                            )

                            if isinstance(
                                city_images,
                                list
                            ):

                                cols = st.columns(
                                    min(
                                        len(city_images),
                                        3
                                    )
                                )

                                for index, image in enumerate(
                                    city_images
                                ):

                                    with cols[
                                        index % len(cols)
                                    ]:

                                        st.image(
                                            image,
                                            use_container_width=True
                                        )

                            else:

                                st.image(
                                    city_images,
                                    use_container_width=True
                                )


                # =================================
                # COST
                # =================================

                if "cost" in node_output:

                    cost = node_output["cost"]

                    with cost_container:

                        st.subheader(
                            "💰 Estimated Cost"
                        )

                        if cost:

                            if isinstance(
                                cost,
                                dict
                            ):

                                st.json(cost)

                            else:

                                st.write(cost)

                        else:

                            st.write(
                                "Cost information not available."
                            )


        # -------------------------------------
        # Finished
        # -------------------------------------

        status.update(
            label="✅ Trip planning completed!",
            state="complete",
            expanded=False
        )

        st.success(
            "Your travel plan has been generated successfully!"
        )


    except Exception as e:

        status.update(
            label="❌ Trip planning failed",
            state="error"
        )

        st.error(
            f"An error occurred: {str(e)}"
        )