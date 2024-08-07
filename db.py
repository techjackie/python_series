import pymongo as mongo

class DataBase:
    def __init__(self, connect_uri, db_name, col_name):
        # conn = mongo.MongoClient(host='localhost',port=27017, username='root', password='example')
        conn = mongo.MongoClient(connect_uri)

        try:
            conn.list_database_names()
            print('Database is successfully connected :)')

        except Exception as e:
            print('Database is not connected :<')
            exit() 

        # connection['db_name']
        self.db = conn[db_name]
        self.col = self.db[col_name]

    def insert_data(self, data: dict):
        """
        1. checking data already exists or not
        2. if not exists, insert the data and return success
        3. else return already exists

        --- Return Codes ---
        200 --> Success
        500 --> Error
        404 --> data not found
        403 --> already exists
        """

        try:
            result = self.col.find_one(data)

            if result == None:
                self.col.insert_one(data)
                return 200

            else:
                return 403   

        except Exception as e:
            return 500
        
    def update_data(self, old_data: dict, new_data: dict):
        """
        1. checking data already exists or not
        2. if not exists, return data not found
        3. else update the data and return success
        """
        
        try:
            result = self.col.find_one(old_data)

            if result == None:
                return 404

            else:
                self.col.update_many(old_data, {"$set":new_data})
                return 200
            
        except Exception as e:
            return 500   

    def delete_data(self, data: dict):
        """
        1. checking data already exists or not
        2. if not exists, return data not found
        3. else delete the data and return success
        """
        try:
            result = self.col.find_one(data)

            if result == None:
                return 404

            else:
                self.col.delete_many(data)
                return 200
            
        except Exception as e:
            return 500  

    def find_data(self, query):
        """
        1. checking data exists or not 
        2. if exists return the data else return 404
        """

        result = list(self.col.find(query))

        # True Block if condition else False Block
        return 404 if result == [] else result




# creation of object
db = DataBase('mongodb://root:example@localhost:27017/','books','fiction_books')

result = db.find_data({})
print(result)
