from data.body import body1, body2, body3
from data.files import file1
from data.headers import headers1, headers2, headers3
from helpers.base_service import BaseServices


class PetServices(BaseServices):

    def get_pet_json(self):
        path = "v2/pet/10"
        response = self.get(path, headers=headers1)
        return response

    def post_new_pet(self):
        path = "v2/pet"
        response = self.post(path, headers=headers2, body=body1, code=400)
        return response

    def upload_image(self):
        path = "v2/pet/10/uploadImage"
        response = self.upload(path, headers=headers3, file=file1, code=400)
        return response

    def delete_oder(self):
        path = "v2/store/order/10"
        response = self.delete(path, headers=headers1)
        return response

    def post_list(self):
        path = "v2/user/createWithList"
        response = self.post(path, headers=headers2, body=body2, code=400)
        return response

    def put_user(self):
        path = "v2/user/izzy"
        response = self.put(path, headers=headers2, body=body3, code=400)
        return response
