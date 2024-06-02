from django.shortcuts import render
import requests

def forecast_view(request):
    if request.method == 'POST':
        city = request.POST.get('city')
        APIKey = '271a5d4813583fe9f0cd0948ee304bbb'
        
        current_weather_url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={APIKey}'
        forecast_url = f'https://api.openweathermap.org/data/2.5/forecast?q={city}&units=metric&appid={APIKey}'

        current_weather_response = requests.get(current_weather_url)
        forecast_response = requests.get(forecast_url)
        
        current_weather_data = current_weather_response.json()
        forecast_data = forecast_response.json()
        
        if current_weather_data['cod'] == '404':
            context = {'error': 'City not found'}
        else:
            current_weather = {
                'city': city,
                'temperature': current_weather_data['main']['temp'],
                'description': current_weather_data['weather'][0]['description'],
                'humidity': current_weather_data['main']['humidity'],
                'wind_speed': current_weather_data['wind']['speed'],
                'icon': current_weather_data['weather'][0]['icon'],
            }

            forecast = []
            for i in range(0, 40, 8): # i don't know  loop condition but i got logic from api doccumentaion
                day_data = forecast_data['list'][i]
                day_forecast = {
                    'date': day_data['dt_txt'].split(' ')[0],
                    'temperature': day_data['main']['temp'],
                    'description': day_data['weather'][0]['description'],
                    'icon': day_data['weather'][0]['icon'],
                }
                forecast.append(day_forecast)
            
            context = {'current_weather': current_weather, 'forecast': forecast}

        return render(request, 'weather/index.html', context)

    return render(request, 'weather/index.html')
