import os

def get_files_info(working_directory, directory=None):
    abs_wd = os.path.abspath(working_directory)
    abs_d = os.path.abspath(directory)
    is_directory = os.path.isdir(abs_d)

    print(f"abs_wd: {abs_wd}")
    print(f"abs_d: {abs_d}")
    if abs_d.startswith(abs_wd) is False:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if is_directory is False:
        return f'Error: "{directory}" is not a directory'
    list_directory = os.listdir(abs_d)
    string_builder = []
    for file in list_directory:
        abs_file = os.path.join(abs_d, file)
        file_size = os.path.getsize(abs_file)
        is_file = os.path.isfile(abs_file)
        string_builder.append(f"- {file}: {file_size}, {is_file}")
    print(string_builder)
    return " ".join(string_builder)
