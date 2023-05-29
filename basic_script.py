# Basic Script for CodeMaster Development AI

import CodeMasterDevelopmentAI

while True:
    user_input = input("User: ")
    response = CodeMasterDevelopmentAI.respond(user_input)
    print("CodeMaster Development AI: " + response)
