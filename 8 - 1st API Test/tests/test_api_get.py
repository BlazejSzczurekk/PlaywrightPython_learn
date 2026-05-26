

def test_api_get(playwright):
    request = playwright.request.new_context(
        extra_http_headers={
            "Accept": "application/json",
            "Authorization": "Bearer YOUR_ACCESS_TOKEN",
            "x-api-key": "free_user_3EGf7x8buQsQHIY1HCeX3xYmJed"
        }
    )
    response = request.get("https://reqres.in/api/users?page=2")
    
    assert response.status == 200
    json_data = response.json()
    print(json_data)
    #assert json_data["id"] == 1
    assert json_data["data"][3]["first_name"] == "Byron"
    request.dispose()
    