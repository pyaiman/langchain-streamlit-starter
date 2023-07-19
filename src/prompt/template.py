def example_visual_chat_prompt(query):
    return f"For the following query {query}, Determine the type of graph(bar,line,map,area) which is requested in the query, If query contains any of these type then respond as below example format .\n\n"\
    f"For example: {{'bar': {{'columns': ['title', 'ratings_count'], 'data': [['Gilead', 361], ['Spider Web', 5164]]}}}}\n\n"\
    f"if {query} is asking data in table format then only respond in {{'table': {{'columns': ['column1', 'column2', ...], 'data': [[value1, value2, ...], [value1, value2, ...], ...]}}}} this format .\n\n"\
    f"if it hasn't specify any format respond in plaintext format\n"\
    f"If you do not know the answer, reply as follows:\n"\
    f"Answer: 'I do not know.'\n\n"\
    f"Lets think step by step.\n\n"

