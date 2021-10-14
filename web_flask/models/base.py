class BaseModel():
    def to_dict(self, save_sf=None):
        time = "%Y-%m-%dT%H:%M:%S.%f"
        new_dict = self.__dict__.copy()
        if "DateTime" in new_dict:
            new_dict["DateTime"] = new_dict["DateTime"].strftime(time)
        if "UpdateTime" in new_dict:
            new_dict["UpdateTime"] = new_dict["UpdateTime"].strftime(time)
        new_dict["__class__"] = self.__class__.__name__
        if "_sa_instance_state" in new_dict:
            del new_dict["_sa_instance_state"]
        if "Password" in new_dict:
            del new_dict["Password"]
        return new_dict
