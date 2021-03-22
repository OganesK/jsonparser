import ast
from faker_schema.faker_schema import FakerSchema
import json
import json_schema_generator as jsg
from PyQt5.QtWidgets import QTreeWidgetItem

def generate_json_from_schema(schema):
    ss = ast.literal_eval(schema)
    faker = FakerSchema(locale='it_IT')
    data = faker.generate_fake(ss)
    return data

def validator(json_str, schema):
    json_message = json.loads(json_str)
    try:
        s = ast.literal_eval(schema)
        status = validate(json_message, s)
        if (status == None):
            return "True"
        else:
            return "False"
    except:
        return "Schema Error"


def validator_for_vizual_app(json_str):
    json_message = json.loads(json_str)
    schema = jsg.SchemaGenerator(json_message)
    sch = schema.to_dict()
    return True, sch


def fill_item(item, value):
    item.setExpanded(True)
    if type(value) is dict:
        for key, val in sorted(value.items()):
            child = QTreeWidgetItem()
            child.setText(0, str(key))
            item.addChild(child)
            fill_item(child, val)
    elif type(value) is list:
        for val in value:
            child = QTreeWidgetItem()
            item.addChild(child)
            if type(val) is dict:
                child.setText(0, '[dict]')
                fill_item(child, val)
            elif type(val) is list:
                child.setText(0, '[list]')
                fill_item(child, val)
            else:
                child.setText(0, str(val))
            child.setExpanded(True)
    else:
        child = QTreeWidgetItem()
        child.setText(0, str(value))
        item.addChild(child)


def fill_widget(widget, value):
    widget.clear()
    fill_item(widget.invisibleRootItem(), value)
