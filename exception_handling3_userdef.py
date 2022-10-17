###
id_list = [1,2,3,4,5,6]
class UserDefinedException(Exception):
    pass

class InvalidIdError(Exception):
    def __init__(self,id) -> None:
        super().__init__(id)


try:
    p = int(input("Enter id: "))
    if type(p) != int:
        raise ValueError("Invalid type")
       
    else:
        if p not in id_list:
            raise InvalidIdError("Please Enter valid id")
        else:
            print(p)
except InvalidIdError as i:
    print(i)
except ValueError as t:
    print(t)


