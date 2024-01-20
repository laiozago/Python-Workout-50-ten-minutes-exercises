"""
Function to extract user and domain from email address
"""


def user_domain(st):
    at_position = st.find("@")
    result = [st[:at_position], st[at_position + 1:]]
    return result


print(user_domain("alberto@gmail.com"))
