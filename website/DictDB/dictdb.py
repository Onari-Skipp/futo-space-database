# import json
from .. import encrypt

# with open("instance/_io/database_models.json", "r") as dbFile:
# 	db = json.load(dbFile)


# unused_ids = []
# used_ids = []
# for n in range(10000):
# 	unused_ids.append(n)


# class DictDB:
# 	"""docstring for DictDB"""
# 	def __init__(self):
# 		self.database = db

# 	def get_all(self, model_name):
# 		with open(f"instance/_io/models/{model_name}.json", "r") as model:
# 			database_to_get = json.load(model)

# 		return database_to_get

# 	def find_all(self, model_name, column, value):
# 		with open(f"instance/_io/models/{model_name}.json", "r") as model:
# 			database_to_get = json.load(model)

# 		_ = []
# 		for k, v in database_to_get.items():
# 			for vs in v:
# 				if vs == column:
# 					if (database_to_get[f"{k}"][f"{vs}"]) == str(value):
# 						_.append(database_to_get[f'{k}'])

# 		return _

# 	def update_one(self, model_name, db_id, column, item):
# 		with open(f"instance/_io/models/{model_name}.json", "r") as model:
# 			database_to_update = json.load(model)

# 		database_to_update[f'{db_id}'][f'{column}'] = item
# 		return [model_name, database_to_update]

# 	def find_one(self, model_name, column, item):
# 		with open(f"instance/_io/models/{model_name}.json", "r") as model:
# 			database_to_search = json.load(model)

# 		search_item = f"{column} -> {item}"

# 		def find():
# 			for key, value in database_to_search.items():
# 				for keys, values in value.items():
# 					search_model = f"{keys} -> {values}"
# 					if search_item == search_model:
# 						return key#[key, keys]

# 		if find() == None:
# 			return None
# 		else:
# 			return find()

# 	def add_one(self, model_name, column, item):
# 		with open(f"instance/_io/models/{model_name}.json", "r") as model:
# 			database_to_add = json.load(model)

# 		def get_schema():
# 			with open(f"instance/_io/models/model_settings/{model_name}_settings.modelsettings", "r") as model_settings:
# 				content = model_settings.read()

# 			return eval(content.replace("Schema: ", ""))

# 		for key, value in database_to_add.items():
# 			key_ = int(key)

# 		database_to_add[f'{key_ + 1}'] = {}

# 		for col in get_schema():
# 			database_to_add[f'{key_ + 1}'][f'{col}'] = "NULL"
# 			database_to_add[f'{key_ + 1}'][f'{column}'] = item

# 		database_to_add[f'{key_ + 1}']['id'] = f"{key_ + 1}"
# 		return [model_name, database_to_add]


# 	def add_entry(self, model_name, cvp):#Column-Value Pair
# 		cvp = eval(encrypt.decrypter(cvp))
# 		with open(f"instance/_io/models/{model_name}.json", "r") as model:
# 			database_to_add = json.load(model)

# 		def get_schema():
# 			with open(f"instance/_io/models/model_settings/{model_name}_settings.modelsettings", "r") as model_settings:
# 				content = model_settings.read()

# 			return eval(content.replace("Schema: ", ""))

# 		for key, value in database_to_add.items():
# 			key_ = int(key)

# 		database_to_add[f'{key_ + 1}'] = {}
# 		database_to_add[f'{key_ + 1}']['id'] = f'{key_ + 1}'

# 		# print(len(eval(items)), len(get_schema()))

# 		for k, v in cvp.items():
# 			for col in get_schema():
# 				if k == col:
# 					database_to_add[f'{key_ + 1}'][f'{k}'] = f'{v}'

# 		k_temp = []
# 		for k, v in database_to_add[f'{key_ + 1}'].items():
# 			k_temp.append(k)
		
# 		for col in get_schema():
# 			if col in k_temp:
# 				pass
# 			else:
# 				database_to_add[f'{key_ + 1}'][f'{col}'] = "NULL"

# 		return [model_name, database_to_add]

# 	def update_entry(self, model_name, column, cvp, dnd=False):
# 		if dnd == False:
# 			cvp = eval(encrypt.decrypter(cvp))
# 		else:
# 			cvp = eval(cvp)
# 		with open(f"instance/_io/models/{model_name}.json", "r") as model:
# 			database_to_update = json.load(model)

# 		for k, v in database_to_update.items():
# 			for kn, vn in cvp.items():
# 				database_to_update[column][kn] = vn


# 		return [model_name, database_to_update]

# 	def delete_entry(self, model_name, column):
# 		with open(f"instance/_io/models/{model_name}.json", "r") as model:
# 			database_to_update = json.load(model)
		
# 		for k, v in database_to_update.items():
# 			if k == str(column):
# 				del database_to_update[f'{k}']
# 				break

# 		return [model_name, database_to_update]
	    
# 	def commit(self, db_object):
# 		with open(f"instance/_io/models/{db_object[0]}.json", "w") as dbFile:
# 			dbFile.write(str(db_object[1]).replace("'", '"'))

# 	def create_model(self, name):
# 		with open(f"instance/_io/models/{name}.json", "w") as new_model:
# 			new_model.write("{}")

# 	def set_schema(self, model_name, columns):
# 		with open(f"instance/_io/models/{model_name}.json", "r") as model:
# 			database_to_add_schema = json.load(model)

# 		current_id = []
# 		for x in unused_ids:
# 			if x in used_ids:
# 				pass
# 			else:
# 			    database_to_add_schema[f'{x}'] = {
# 			    	"id": f"{x}"
# 			    }
# 			    current_id.append(x)
# 			    unused_ids.remove(x)
# 			    used_ids.append(x)
# 			    break

# 		for column in columns:
# 			database_to_add_schema[f'{current_id[0]}'][f'{column}'] = "NULL"#["NULL", "NULL"]#here

# 		with open(f"instance/_io/models/{model_name}.json", "w") as model:
# 			model.write(str(database_to_add_schema).replace("'", '"'))

# 		columns_refined = ['id']
# 		for col in columns:
# 			columns_refined.append(col)

# 		with open(f'instance/_io/models/model_settings/{model_name}_settings.modelsettings', "w") as model_settings:
# 			model_settings.write(f"Schema: {columns_refined}")


# 		return f"Added columns {columns} to `{model_name}`"

# 	def add_relationship(self, model_this, model_to, relationship_name):
# 		model_this_name = model_this[0]
# 		model_to_name = model_to[0]
# 		with open(f"instance/_io/models/{model_this_name}.json", "r") as model:
# 			database_to_add_relationship = json.load(model)

# 		with open(f"instance/_io/models/{model_this_name}_settings.modelsettings", "r") as model_settings:
# 			database_settings_to_add_relationship = model_settings.read()





# 	# def function():
# 		# pass
# 		


import json
import os
from functools import lru_cache

class DictDB:
    def __init__(self):
        self.cache = {}
        self.model_schemas = {}

    @lru_cache(maxsize=32)
    def _load_model(self, model_name):
        if model_name not in self.cache:
            with open(f"instance/_io/models/{model_name}.json", "r") as model:
                self.cache[model_name] = json.load(model)
        return self.cache[model_name]

    @lru_cache(maxsize=32)
    def _get_schema(self, model_name):
        if model_name not in self.model_schemas:
            settings_path = f"instance/_io/models/model_settings/{model_name}_settings.modelsettings"
            with open(settings_path, "r") as model_settings:
                content = model_settings.read()
            self.model_schemas[model_name] = eval(content.replace("Schema: ", ""))
        return self.model_schemas[model_name]

    @lru_cache(maxsize=32)
    def _decrypt_and_clean(self, encrypted_text):
        decrypted_text = encrypt.decrypter(encrypted_text)
        cleaned_sarahdb_data = decrypted_text.replace("'", '"')
        return cleaned_sarahdb_data

    def get_all(self, model_name):
        return self._load_model(model_name)

    def find_all(self, model_name, column, value):
        database = self._load_model(model_name)
        return [v for v in database.values() if v.get(column) == str(value)]

    def update_one(self, model_name, db_id, column, item):
        database = self._load_model(model_name)
        database[db_id][column] = item
        self._save_model(model_name, database)
        return [model_name, database]

    def find_one(self, model_name, column, item):
        database = self._load_model(model_name)
        for key, value in database.items():
            if value.get(column) == item:
                return key
        return None

    def add_one(self, model_name, column, item):
        database = self._load_model(model_name)
        new_id = str(max(map(int, database.keys())) + 1)
        schema = self._get_schema(model_name)
        
        new_entry = {col: "NULL" for col in schema}
        new_entry[column] = item
        new_entry['id'] = new_id
        
        database[new_id] = new_entry
        self._save_model(model_name, database)
        return [model_name, database]

    def add_entry(self, model_name, cvp):
        print("asdadd>>>>>>>>asa>>>>>>>>>>>> ", encrypt.decrypter(cvp), " ", type(encrypt.decrypter(cvp)))
        cvp = json.loads(self._decrypt_and_clean(cvp))
        database = self._load_model(model_name)
        schema = self._get_schema(model_name)
        
        new_id = str(max(map(int, database.keys())) + 1)
        new_entry = {col: cvp.get(col, "NULL") for col in schema}
        new_entry['id'] = new_id
        
        database[new_id] = new_entry
        self._save_model(model_name, database)
        return [model_name, database]

    def update_entry(self, model_name, column, cvp, dnd=False):
        cvp = json.loads(self._decrypt_and_clean(cvp)) if not dnd else eval(cvp)
        database = self._load_model(model_name)
        database[column].update(cvp)
        self._save_model(model_name, database)
        return [model_name, database]

    def delete_entry(self, model_name, column):
        database = self._load_model(model_name)
        if column in database:
            del database[column]
            self._save_model(model_name, database)
        return [model_name, database]

    def _save_model(self, model_name, data):
        self.cache[model_name] = data
        with open(f"instance/_io/models/{model_name}.json", "w") as dbFile:
            json.dump(data, dbFile)

    def create_model(self, name):
        with open(f"instance/_io/models/{name}.json", "w") as new_model:
            json.dump({}, new_model)

    def set_schema(self, model_name, columns):
        database = self._load_model(model_name)
        new_id = "0" if not database else str(max(map(int, database.keys())) + 1)
        
        new_entry = {col: "NULL" for col in columns}
        new_entry['id'] = new_id
        database[new_id] = new_entry
        
        self._save_model(model_name, database)
        
        columns_refined = ['id'] + columns
        settings_path = f'instance/_io/models/model_settings/{model_name}_settings.modelsettings'
        with open(settings_path, "w") as model_settings:
            model_settings.write(f"Schema: {columns_refined}")
        
        self.model_schemas[model_name] = columns_refined
        return f"Added columns {columns} to `{model_name}`"

    # The add_relationship method is left as is, as it's not implemented in the original code