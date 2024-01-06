import streamlit as st
import random

def get_mental_health_recommendation():
    tips_and_tricks = [
        "Practice mindfulness meditation for 10 minutes daily.",
        "Take a break and go for a short walk outside.",
        "Connect with a friend or loved one for emotional support.",
        "Write down three things you're grateful for each day.",
        "Engage in a hobby or activity you enjoy.",
        "Limit screen time before bedtime for better sleep.",
        "Establish a daily routine to add structure to your day.",
        "Try deep breathing exercises to reduce stress.",
        "Set realistic goals and celebrate small achievements.",
        "Consider seeking professional help if needed."
        "Practice mindfulness meditation for 10 minutes daily.",
        "Take a break and go for a short walk outside.",
        "Connect with a friend or loved one for emotional support.",
        "Write down three things you're grateful for each day.",
        "Engage in a hobby or activity you enjoy.",
        "Limit screen time before bedtime for better sleep.",
        "Establish a daily routine to add structure to your day.",
        "Try deep breathing exercises to reduce stress.",
        "Set realistic goals and celebrate small achievements.",
        "Consider seeking professional help if needed.",
        "Engage in regular physical exercise to boost mood and energy.",
        "Practice positive self-talk and challenge negative thoughts.",
        "Listen to calming music or nature sounds.",
        "Prioritize self-care activities, such as taking a warm bath or reading a book.",
        "Learn and practice time management techniques.",
        "Attend a support group or talk to someone who understands your experiences.",
        "Create a gratitude journal and write in it daily.",
        "Limit exposure to negative news and social media.",
        "Explore relaxation techniques like progressive muscle relaxation.",
        "Volunteer for a cause that is meaningful to you.",
        "Practice a creative outlet, such as drawing, writing, or playing a musical instrument."
         "Practice mindfulness meditation for 10 minutes daily.",
        "Take a break and go for a short walk outside.",
        "Connect with a friend or loved one for emotional support.",
        "Write down three things you're grateful for each day.",
        "Engage in a hobby or activity you enjoy.",
        "Limit screen time before bedtime for better sleep.",
        "Establish a daily routine to add structure to your day.",
        "Try deep breathing exercises to reduce stress.",
        "Set realistic goals and celebrate small achievements.",
        "Consider seeking professional help if needed.",
        "Engage in regular physical exercise to boost mood and energy.",
        "Practice positive self-talk and challenge negative thoughts.",
        "Listen to calming music or nature sounds.",
        "Prioritize self-care activities, such as taking a warm bath or reading a book.",
        "Learn and practice time management techniques.",
        "Attend a support group or talk to someone who understands your experiences.",
        "Create a gratitude journal and write in it daily.",
        "Limit exposure to negative news and social media.",
        "Explore relaxation techniques like progressive muscle relaxation.",
        "Volunteer for a cause that is meaningful to you.",
        "Practice a creative outlet, such as drawing, writing, or playing a musical instrument.",
        "Believe you can and you're halfway there. -Theodore Roosevelt",
        "Your time is limited, don't waste it living someone else's life. -Steve Jobs",
        "The only way to do great work is to love what you do. -Steve Jobs",
        "Don't watch the clock; do what it does. Keep going. -Sam Levenson",
        "Believe in yourself and all that you are. Know that there is something inside you that is greater than any obstacle. -Christian D. Larson",
        "The only place where success comes before work is in the dictionary. -Vidal Sassoon",
        "You are never too old to set another goal or to dream a new dream. -C.S. Lewis",
        "Success is not final, failure is not fatal: It is the courage to continue that counts. -Winston Churchill",
        "The only limit to our realization of tomorrow will be our doubts of today. -Franklin D. Roosevelt",
        "The best way to predict the future is to create it. -Peter Drucker"

    ]

    motivational_quotes = [
        "Believe you can and you're halfway there. -Theodore Roosevelt",
        "Your time is limited, don't waste it living someone else's life. -Steve Jobs",
        "The only way to do great work is to love what you do. -Steve Jobs",
        "Don't watch the clock; do what it does. Keep going. -Sam Levenson",
        "Believe in yourself and all that you are. Know that there is something inside you that is greater than any obstacle. -Christian D. Larson",
        "The only place where success comes before work is in the dictionary. -Vidal Sassoon",
        "You are never too old to set another goal or to dream a new dream. -C.S. Lewis",
        "Success is not final, failure is not fatal: It is the courage to continue that counts. -Winston Churchill",
        "The only limit to our realization of tomorrow will be our doubts of today. -Franklin D. Roosevelt",
        "The best way to predict the future is to create it. -Peter Drucker",
    ]

    mental_health_recommendation = random.choice(tips_and_tricks)
    motivational_quote = random.choice(motivational_quotes)

    return f"{mental_health_recommendation}\n\n{motivational_quote}"

def main():
    st.title("Mental Health Recommendation System")
    st.subheader("Feeling stressed or anxious? Get a mental health tip and a motivational quote!")

    if st.button("Get Recommendation"):
        recommendation = get_mental_health_recommendation()
        st.success(recommendation)

if __name__ == "__main__":
    main()
