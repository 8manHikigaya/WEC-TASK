import supabase

url = "SUPABASE URL"
key = "API KEY"
supabase_client = supabase.create_client(url,key)


def handle_response(message: str) -> str:
    p_message = message.lower()

    if p_message == 'hello':
        return 'Hii'
    if 'convenor' in p_message and 'wec club' in p_message:
        return 'The convenor of WEC club is Pranav R S.'

    # Get distinct roles from the database
    roles = get_distinct_roles()

    # Check if the message contains any role keyword
    for role in roles:
        if role.lower() in p_message:
            keyword_name = role
            name = get_name_by_keyword('Role', keyword_name)

            if name:
                return f"The role '{keyword_name}' is {name}."
            else:
                return f"No role found with the name '{keyword_name}'."

    return 'I do not understand your request.'

def get_distinct_roles():
    response = supabase_client.query("SELECT DISTINCT Role FROM 'Wec members'")
    roles = [entry['Role'] for entry in response['data']]
    return roles

def get_name_by_keyword(keyword, keyword_name):
    response = supabase_client.table('Wec members').select('Role', 'Member').eq(keyword, keyword_name).execute()
    data = response['data']

    if data:
        return data[0]['Member']
    else:
        return None
