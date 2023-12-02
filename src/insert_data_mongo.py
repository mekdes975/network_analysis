from src import mongodb_functions as MongoDBHandler
import json
import glob
import os

path_channels = '../Anonymized_B6SlackExport_25Nov23/anonymized/'

with MongoDBHandler('mongodb://localhost:27017/', "Slack") as db_handler:
    
    users_collection = db_handler.create_document('users','../Anonymized_B6SlackExport_25Nov23/anonymized/users.json')
    channels_collection = db_handler.create_document('channels','../Anonymized_B6SlackExport_25Nov23/anonymized/channels.json')
    # specify path to get json files
    combined = []
    
    
    # # loop through all folders and extract json files
    for item_name in os.listdir(path_channels):
        item_path = os.path.join(path_channels, item_name)
        if os.path.isdir(item_path):
            for json_file in glob.glob(f"{item_path}/*.json"):
                with open(json_file, 'r', encoding="utf8") as slack_data:
                    slack_data = json.load(slack_data)
                    combined.append(slack_data)
    
    messages_collection = db_handler.create_document('messages_collection',combined)
