import json_schema_generator as jsg
import json

class JSONSchema:
    def __init__(self, json_input):
        self.json_code = json_input
        self.serialized = json.loads(json_input)
        sg = jsg.SchemaGenerator(self.serialized)
        self.schema = sg.to_dict()

def insert(table, type, name, value):
    text = ""
    text += " INSERT INTO "
    text += table
    text += " VALUES('" + type + "','" + name + "','" + value + "')\n "
    return text

def create(table):
    text = ""
    text += " CREATE TABLE "
    text += table
    text += " (Type VARCHAR(10), Name VARCHAR(100), Value NVARCHAR(250))\n "
    return text
