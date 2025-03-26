<p>Heard of korean talking about their personality like INTP, ENTP, ENFJ etc?</p>
<p>Know your personality by giving answers to 5 simple questions</p>


# Korean MBTI Personality Predictor
Discover your Korean MBTI personality type with this fun and easy web application!  Inspired by the popularity of MBTI in Korean culture, this predictor uses a Gen AI model to analyze your responses to five simple questions and determine your likely personality type.

## Features
*   **Quick Personality Assessment:** Answer just five questions about your preferences and tendencies.
*   **Gen AI Powered Prediction:**  Utilizes the Google Gemini AI model for personality analysis.
*   **Korean MBTI Focus:**  Specifically designed to predict personality types as understood in Korean culture.
*   **User-Friendly Web Interface:**  Built with Flask for a simple and intuitive experience.
*   **Dockerized:** Easy to set up and run in any environment with Docker.

## Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/RaWseekQWERTY/Personality-Predictor
    cd rawseekqwerty-personality-predictor
    ```

2.  **Install Python dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3.  **Set up your Gemini API Key:**

    *   You need a Google Gemini API key to use this application.  You can obtain one by following the [Gemini API documentation](https://ai.google.dev/gemini-api/docs).
    *   Create a `.env` file in the root directory of the project.
    *   Add the following line to your `.env` file, replacing `YOUR_API_KEY` with your actual Gemini API key:

    ```
    GOOGLE_API=YOUR_API_KEY
    ```
    **Important:**  Do not commit your `.env` file to your repository if it contains sensitive information like API keys. Consider adding `.env` to your `.gitignore` file.

## Usage

1.  **Build and run the Docker container (Recommended):**

    ```bash
    docker build -t korean-mbti-predictor .
    docker run -d -p 5000:5000 korean-mbti-predictor
    ```

2.  **Alternatively, run directly with Flask (for development):**

    ```bash
    cd src/web
    flask --app run run
    ```

3.  **Access the application:**

    Open your web browser and go to `http://localhost:5000`.

4.  **Take the Personality Quiz:**

    *   Navigate to the "Explore" page.
    *   Answer the five questions by selecting the options that best describe you.
    *   Click "Submit" to get your personality prediction.

5.  **View your Personality Results:**

    The "Personality Analysis" page will display your likely MBTI type, a description of your personality, and insights into how you might handle different situations, based on the Gemini AI analysis.

## Technology Stack

*   **Backend:** Python 3.8, Flask
*   **AI Model:** Google Gemini Pro (via `google-generativeai` Python library)
*   **Frontend:** HTML, CSS, JavaScript
*   **Containerization:** Docker

## Future Improvements (Possible Enhancements)

*   **Enhanced UI/UX:** Improve the visual design and user experience of the web application.
*   **More Robust Response Parsing:** Make the Gemini response parsing more reliable and less dependent on specific text patterns.
*   **Error Handling:** Implement comprehensive error handling for API calls and other potential issues.
*   **Input Validation:** Add client-side and server-side validation to ensure correct user input.
*   **Internationalization:** Support multiple languages.
*   **More Detailed Personality Reports:**  Expand the personality analysis to include more traits and insights.
*   **Database Integration:** Store user responses and potentially track prediction accuracy over time (for research or improvement).
*   **Social Sharing:**  Allow users to easily share their personality results on social media.

## Author

[Rasik Kayastha / RaWseekQWERTY] - [https://github.com/RaWseekQWERTY]
