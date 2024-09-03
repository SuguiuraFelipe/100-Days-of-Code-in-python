def format_name(f_name, l_name):
    name = f_name.title() + " " + l_name.title()
    return name


print(format_name("fElipe", "meLO"))

def function_1(text):
    return text + text

def function_2(text):
    return text.title()

print(function_2(function_1("hello")))
