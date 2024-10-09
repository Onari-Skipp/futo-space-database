# import json
from .. import encrypt

import json
import os
from functools import lru_cache

PRODUCTION = True

if PRODUCTION == True:
    data_location_prefix = "SarahDB/"
else:
    data_location_prefix = ""

class DictDB:
    """
    A class to manage a simple dictionary-based database for loading, updating, and saving models.
    """

    def __init__(self):
        """
        Initializes a DictDB instance with cache for loaded models and model schemas.
        """
        self.cache = {}
        self.model_schemas = {}

    @lru_cache(maxsize=32)
    def _load_model(self, model_name):
        """
        Loads the data of the specified model into cache.

        Args:
            model_name (str): The name of the model to load.

        Returns:
            dict: The loaded model data.
        """
        if model_name not in self.cache:
            with open(f"{data_location_prefix}instance/_io/models/{model_name}.json", "r") as model:
                self.cache[model_name] = json.load(model)
        return self.cache[model_name]

    @lru_cache(maxsize=32)
    def _get_schema(self, model_name):
        """
        Retrieves the schema for the specified model.

        Args:
            model_name (str): The name of the model.

        Returns:
            list: The schema of the model.
        """
        if model_name not in self.model_schemas:
            settings_path = f"{data_location_prefix}instance/_io/models/model_settings/{model_name}_settings.modelsettings"
            with open(settings_path, "r") as model_settings:
                content = model_settings.read()
            self.model_schemas[model_name] = eval(content.replace("Schema: ", ""))
        return self.model_schemas[model_name]

    @lru_cache(maxsize=32)
    def _decrypt_and_clean(self, encrypted_text):
        """
        Decrypts and cleans encrypted text.

        Args:
            encrypted_text (str): The encrypted text to decrypt.

        Returns:
            str: The cleaned, decrypted data.
        """
        decrypted_text = encrypt.decrypter(encrypted_text)
        cleaned_sarahdb_data = decrypted_text.replace("'", '"')
        return cleaned_sarahdb_data

    def get_all(self, model_name):
        """
        Retrieves all records from the specified model.

        Args:
            model_name (str): The name of the model.

        Returns:
            dict: All records in the model.
        """
        return self._load_model(model_name)

    def find_all(self, model_name, column, value):
        """
        Finds all entries in a model where a specific column matches a given value.

        Args:
            model_name (str): The name of the model.
            column (str): The column to filter on.
            value (str): The value to match.

        Returns:
            list: A list of matching records.
        """
        database = self._load_model(model_name)
        return [v for v in database.values() if v.get(column) == str(value)]

    def update_one(self, model_name, db_id, column, item):
        """
        Updates a specific entry in the model.

        Args:
            model_name (str): The name of the model.
            db_id (str): The ID of the entry to update.
            column (str): The column to update.
            item (any): The new value for the column.

        Returns:
            list: The updated model name and its data.
        """
        database = self._load_model(model_name)
        database[db_id][column] = item
        self._save_model(model_name, database)
        return [model_name, database]

    def find_one(self, model_name, column, item):
        """
        Finds one entry in the model where the column matches the given value.

        Args:
            model_name (str): The name of the model.
            column (str): The column to search.
            item (any): The value to search for.

        Returns:
            str: The key of the matching entry, or None if not found.
        """
        database = self._load_model(model_name)
        for key, value in database.items():
            if value.get(column) == item:
                return key
        return None

    def add_one(self, model_name, column, item):
        """
        Adds a new entry to the model.

        Args:
            model_name (str): The name of the model.
            column (str): The column to update.
            item (any): The value to add.

        Returns:
            list: The updated model name and its data.
        """
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
        """
        Adds an entry to the model by decrypting and parsing the provided data.

        Args:
            model_name (str): The name of the model.
            cvp (str): The encrypted entry data to add.

        Returns:
            list: The updated model name and its data.
        """
        try:
            cvp = json.loads(self._decrypt_and_clean(cvp))
        except json.JSONDecodeError as e:
            print(f"Error: {e}")
            print("JSON Data")
            print(self._decrypt_and_clean(cvp))

        database = self._load_model(model_name)
        schema = self._get_schema(model_name)
        
        new_id = str(max(map(int, database.keys())) + 1)
        new_entry = {col: cvp.get(col, "NULL") for col in schema}
        new_entry['id'] = new_id
        
        database[new_id] = new_entry
        self._save_model(model_name, database)
        return [model_name, database]

    def update_entry(self, model_name, column, cvp, dnd=False):
        """
        Updates an existing entry in the model.

        Args:
            model_name (str): The name of the model.
            column (str): The column to update.
            cvp (str): The data to update with.
            dnd (bool): Whether to directly evaluate the data (default: False).

        Returns:
            list: The updated model name and its data.
        """
        cvp = json.loads(self._decrypt_and_clean(cvp)) if not dnd else eval(cvp)
        database = self._load_model(model_name)
        database[column].update(cvp)
        self._save_model(model_name, database)
        return [model_name, database]

    def delete_entry(self, model_name, column):
        """
        Deletes an entry from the model.

        Args:
            model_name (str): The name of the model.
            column (str): The column to identify the entry to delete.

        Returns:
            list: The updated model name and its data.
        """
        database = self._load_model(model_name)
        if column in database:
            del database[column]
            self._save_model(model_name, database)
        return [model_name, database]

    def _save_model(self, model_name, data):
        """
        Saves the updated data of a model to the file system.

        Args:
            model_name (str): The name of the model.
            data (dict): The data to save.
        """
        self.cache[model_name] = data
        with open(f"instance/_io/models/{model_name}.json", "w") as dbFile:
            json.dump(data, dbFile)

    def create_model(self, name):
        """
        Creates a new model file.

        Args:
            name (str): The name of the new model.
        """
        with open(f"instance/_io/models/{name}.json", "w") as new_model:
            json.dump({}, new_model)

    def set_schema(self, model_name, columns):
        """
        Sets the schema for a model by defining its columns.

        Args:
            model_name (str): The name of the model.
            columns (list): A list of column names to set for the model.

        Returns:
            str: Confirmation message for schema addition.
        """
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

    def __init__(self):
        self.cache = {}
        self.model_schemas = {}

    @lru_cache(maxsize=32)
    def _load_model(self, model_name):
        if model_name not in self.cache:
            with open(f"{data_location_prefix}instance/_io/models/{model_name}.json", "r") as model:
                self.cache[model_name] = json.load(model)
        return self.cache[model_name]

    @lru_cache(maxsize=32)
    def _get_schema(self, model_name):
        if model_name not in self.model_schemas:
            settings_path = f"{data_location_prefix}instance/_io/models/model_settings/{model_name}_settings.modelsettings"
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
        
        try:
            cvp = json.loads(self._decrypt_and_clean(cvp))
        except json.JSONDecodeError as e:
            print(f"Error: {e}")
            print("JSON Data")
            print(self._decrypt_and_clean(cvp))

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
        with open(f"{data_location_prefix}instance/_io/models/{model_name}.json", "w") as dbFile:
            json.dump(data, dbFile)

    def create_model(self, name):
        with open(f"{data_location_prefix}instance/_io/models/{name}.json", "w") as new_model:
            json.dump({}, new_model)

    def set_schema(self, model_name, columns):
        database = self._load_model(model_name)
        new_id = "0" if not database else str(max(map(int, database.keys())) + 1)
        
        new_entry = {col: "NULL" for col in columns}
        new_entry['id'] = new_id
        database[new_id] = new_entry
        
        self._save_model(model_name, database)
        
        columns_refined = ['id'] + columns
        settings_path = f'{data_location_prefix}instance/_io/models/model_settings/{model_name}_settings.modelsettings'
        with open(settings_path, "w") as model_settings:
            model_settings.write(f"Schema: {columns_refined}")
        
        self.model_schemas[model_name] = columns_refined
        return f"Added columns {columns} to `{model_name}`"

    # The add_relationship method is left as is, as it's not implemented in the original code