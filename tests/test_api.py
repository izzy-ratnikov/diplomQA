import allure
from services.api_pet_service import PetServices


@allure.title("Test get pet")
def test_get_pet():
    pet_services = PetServices()
    assert pet_services.get_pet_json().get("id") == 10
    assert pet_services.get_pet_json().get("category").get("id")
    assert pet_services.get_pet_json().get("category").get("name")


@allure.title("Test post pet")
def test_post_add_new_pet():
    pet_services = PetServices()
    assert pet_services.post_new_pet()


@allure.title("Test upload image")
def test_pet_upload_image():
    pet_services = PetServices()
    assert pet_services.upload_image()


@allure.title("Test delete order")
def test_delete_purchase_order():
    pet_services = PetServices()
    assert pet_services.delete_oder()


@allure.title("Test post list of users")
def test_post_list_of_users():
    pet_services = PetServices()
    assert pet_services.post_list()


@allure.title("Test put updates user")
def test_put_updated_user():
    pet_services = PetServices()
    assert pet_services.put_user()
