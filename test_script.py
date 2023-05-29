# Test Script for CodeMaster Development AI

import CodeMasterDevelopmentAI

inputs = [
    "What is the weather like today?",
    "Can you recommend a good restaurant in the area?",
    "How do I change my password?",
    "What is the capital of France?",
    "What is the meaning of life?"
]

for input in inputs:
    response = CodeMasterDevelopmentAI.respond(input)
    print("User: " + input)
    print("CodeMaster Development AI: " + response)
