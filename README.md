# Weather App

This Weather App provides current weather information and a five-day forecast for various locations. It offers an intuitive and user-friendly interface for weather updates.

## Features

- **Current Weather**: Real-time weather data including temperature, humidity, wind speed, and a brief description.
- **Five-Day Forecast**: Expected weather conditions and temperatures for the next five days.
- **Search Functionality**: Search for weather information by city name.

## Technologies Used

- **Frontend**: HTML, CSS
- **Backend**: Django
- **API**: OpenWeatherMap API
- ***Database***: postgresql

## Setup and Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/weather-app.git
2. Navigate to the project directory:
   ```bash
   cd weather-app
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
4. Apply migrations:
   ```bash
   python manage.py migrate
5. Start the server:
   ```bash
   python manage.py runserver
## Usage

- **Open your browser and navigate to** [localhost](http://localhost:8000)
- **Enter a city name in the search bar to get the current weather and forecast.**

## Contributing
**Contributions are welcome! Please fork the repository and submit a pull request for review.**

## Acknowledgements
- [OpenWeatherMap](https://openweathermap.org/) **for providing the weather data API.**

## Test Run

To test the functionality using the provided API endpoint, follow these steps:

### Using cURL

```bash
curl -X GET https://weather-app-vbta.onrender.com/


