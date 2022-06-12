import pymongo
import pandas as pd

class mongodb:
    def __init__ (self):
        self.client = pymongo.MongoClient(
            "mongodb+srv://mongodb:mongodb@sreeman."
                                     "jzldx.mongodb.net/myFirstDatabase?"
                                     "retryWrites=true&w=majority", tls=True,
                                     tlsAllowInvalidCertificates=True)
        print("Connected to mongodb")

    def get_collection(self):
        db = self.client["Forest_Fire"]
        records = db["Clean_data_forest_fire_trunc"]
        list_records = list(records.find())
        df = pd.DataFrame(list_records)
        df.drop("_id", axis=1, inplace=True)
        return df

class transform:

    def __init__ (self,X_train,trf_model):
        self.X_train = X_train
        self.trf_model = trf_model
        self.X_trf_fit_()

    def X_trf_fit_(self):
        # trf fit the model
        self.trf_model.fit(self.X_train)

    def X_trf_transform(self,X_test):
        return self.trf_model.transform(X_test)


