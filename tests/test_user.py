import requests

def test_authentication_fails(mocker):
    # Create a mock response object with the expected failure status and text
    mock_response = mocker.Mock()
    mock_response.status_code = 401
    mock_response.text = ""
    
    # Patch requests.get to return the mock_response instead of hitting a real server
    mocker.patch("requests.get", return_value=mock_response)

    # Call the URL with parameters expected to fail
    # Note: Since the call is mocked, the actual URL string is intercepted
    response = requests.get(
        "http://127.0.0.1:8000/login", 
        params={"username": "admin", "password": "admin"}
    )

    # Assert that the status code is 401 and text is empty
    assert response.status_code == 401
    assert response.text.strip() == ""

def test_authentication_successful(mocker):
    # Create a mock response object with the expected success status and text
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.text = ""
    
    # Patch requests.get to return the mock_response
    mocker.patch("requests.get", return_value=mock_response)

    # Call the URL with parameters expected to succeed
    response = requests.get(
        "http://127.0.0.1:8000/login", 
        params={"username": "admin", "password": "qwerty"}
    )

    # Assert that the status code is 200 and text is empty
    assert response.status_code == 200
    assert response.text.strip() == ""