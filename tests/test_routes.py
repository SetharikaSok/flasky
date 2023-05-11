def test_read_all_crystals_return_empty_list(client):
    #arrange

    #act
    response = client.get("/crystals")
    response_body = response.get_json()

    #assert
    assert response_body == []
    assert response.status_code == 200

    
def test_read_crystal_by_id(client):
    response = client.get("/crystals/2")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == {
            "id": 2,
            "name": "garnet",
            "color": "red",
            "powers": "awesom+protection againt disaster, evil spirit, and mental illness",
        }
def test_create_crystal(client):
    response = client.post("/crystals", json={
        "name":"tiger",
        "color":"gold",
        "powers":"Focus"})
    
    response_body = response.get_json()

    assert response.status_code == 201
    assert response_body == (f"Yayyy Crystal tiger succesfully created")
    
