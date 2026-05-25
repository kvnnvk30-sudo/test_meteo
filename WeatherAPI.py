import pytest

class TestWeatherAPI:

    @pytest.fixture
    def data_weath(self, client):
        params = {
            "latitude": 50.45,
            "longitude": 30.52,
            "current_weather": "true"
        }
        response = client.get(f"{client.base_url}/v1/forecast", params=params)
        assert response.status_code == 200
        return response.json()


    def test_session(self,data_weath):
        assert "current_weather" in data_weath
        weather = data_weath["current_weather"]
        assert "temperature" in weather
        assert "windspeed" in weather

    def test_temperature_is_number(self,data_weath):
        temperature = data_weath["current_weather"]["temperature"]
        assert isinstance(temperature, (int, float))
        assert -60 <= temperature <= 60

    def test_coordinates(client,data_weath):
        expected_lat = 50.45
        expected_lon = 30.52
        for key in ["latitude","longitude"]:
            assert key in ["latitude", "longitude"]

        assert data_weath["latitude"] == pytest.approx(expected_lat, abs=1)
        assert data_weath["longitude"] == pytest.approx(expected_lon, abs=1)



