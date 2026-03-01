from spacekit import get_apod_safe, get_space_weather, satellite_position

def test_apod_safe():
    d = get_apod_safe()
    assert isinstance(d, dict)
    assert "title" in d

def test_space_weather():
    d = get_space_weather()
    assert isinstance(d, dict)
    assert "solar_flares" in d

def test_satellite_position():
    d = satellite_position("ISS")
    assert isinstance(d, dict)
    assert "latitude" in d and "longitude" in d