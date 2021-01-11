# Function that parses the Money value to an float

def format_money(value_to_parse: str) -> str:
    """
    Format money is a function that formats the string to a string with numeric separators
    i.e. 10000.00 to 10,000.00
    i.e 12345678.00 to 1,234,456.00
    """
    try:
        rounded = round(float(value_to_parse),2)
        # split to get decimal + integer
        parsed_value = '{:,}'.format(rounded).replace(',', ' ')
        # decide if need to add extra 0
        if len(parsed_value.split('.')[1]) == 1:
            return f"{parsed_value}0"
        return parsed_value
    except ValueError:
        print(f"could not convert to float: '{value_to_parse}'")
        return ""
    except:
        print(f"unexpected error: '{value_to_parse}'")
        return ""
