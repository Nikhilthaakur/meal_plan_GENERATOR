import streamlit as st
from googleapiclient.discovery import build

# Set up your YouTube API key
API_KEY = 'AIzaSyCvRe0S4mNSu__uduUN-x2bkngwsEu6Wq4'
youtube = build('youtube', 'v3', developerKey=API_KEY)

# Initialize session state
if 'recommendations' not in st.session_state:
    st.session_state.recommendations = None

# Function to recommend exercise videos based on user input
@st.cache_data()
def recommend_videos(height, weight, meal, body_part, carbs):
    # Map body parts to relevant YouTube search queries
    body_part_queries = {
        "Upper Body": "upper body workout",
        "Lower Body": "lower body workout",
        "Full Body": "full body workout",
    }

    # Use the YouTube API to search for videos based on the user's body part preference
    search_query = body_part_queries.get(body_part, "exercise workout")
    search_response = youtube.search().list(q=search_query, part='id', type='video', maxResults=6).execute()

    # Extract video IDs from the search results
    video_ids = [item['id']['videoId'] for item in search_response.get('items', [])]

    # Construct video URLs
    video_urls = [f"https://www.youtube.com/watch?v={video_id}" for video_id in video_ids]

    return video_urls

# Streamlit app
def main():
    st.title("🏋️‍♂️ Personalized Exercise Video Recommender 🏋️‍♀️")

    # Create a search bar in the sidebar
    search_query = st.sidebar.text_input("Search for Videos", "")

    # User input
    height = st.slider("Height (cm)", 100, 250, 170)
    weight = st.slider("Weight (kg)", 40, 200, 70)
    meal = st.selectbox("Meal Preference", ["Low Carb", "Balanced", "High Carb"])
    body_part = st.selectbox("Target Body Part", ["Upper Body", "Lower Body", "Full Body"])
    carbs = st.slider("Carbs Intake (g)", 0, 300, 150)

    # Recommendation button
    if st.button("Get Recommendations"):
        # Get recommendations based on user input
        recommendations = recommend_videos(height, weight, meal, body_part, carbs)

        # Update the session state to store recommendations
        st.session_state.recommendations = recommendations

    # Display recommendations in a styled grid
    st.subheader("Recommended Exercise Videos:")
    cols = st.columns(3)  # 3 columns in each row

    for i, video_url in enumerate(st.session_state.recommendations or (), start=1):
        with cols[i % 3]:
            # Use st.video to directly embed YouTube videos
            st.video(video_url)

if __name__ == "__main__":
    main()
