def extractLeadIds(data: dict):
    leadIds = []

    for key, value in data.items():
        if ("leads" in key) and ("[id]" in key):
            leadIds.append(int(value))

    return leadIds
