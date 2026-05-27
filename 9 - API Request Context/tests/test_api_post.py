

def test_api_get(playwright):
    request = playwright.request.new_context(
        extra_http_headers={
            "Accept": "application/json",
            "Authorization": "Bearer YOUR_ACCESS_TOKEN",
            "x-api-key": "free_user_3EGf7x8buQsQHIY1HCeX3xYmJed"
        }
    )
    data = {
        "name": "Jacob",
        "job": "none"
    }
    response = request.post(
        "https://reqres.in/api/users",
        data=data
    )
    
    assert response.ok
    print(response.json())
    request.dispose()
    