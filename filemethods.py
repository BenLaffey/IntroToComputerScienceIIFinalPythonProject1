def normalOutput(filecopy: list) -> str:
    """
    Function to return the normal contents of a read file as a string.
    :param filecopy: The copy of the read text file as a list.
    :return: A string representing the normal contents of the read text file.
    """
    return "".join(filecopy)


def replaceOutput(filecopy: list, replacing: str, replacement: str) -> str:
    """
    Function to replace strings within a file and return a new file output as a string where the 'replacing' parameter strings are replaced with the 'replacment' parameter strings.
    :param filecopy: The copy of the read text file as a list.
    :param replacing: The old strings in the file as a string that will be replaced by the 'replacement' parameter's string.
    :param replacement: The new strings in the file as a string that will replace the 'replacing' parameter's string.
    :return: A string representing the replaced contents of the read text file.
    """
    return ("".join(filecopy)).replace(replacing, replacement)


def reverseOutput(filecopy: list) -> str:
    """
    Function to return the reversed contents of a read file as a string.
    :param filecopy: The copy of the read text file as a list.
    :return: A string representing the reversed contents of the read text file.
    """
    text: str = "".join(filecopy)
    output: str = ""
    for i in range(len(text)):
        output: str = output + text[(len(text) - 1) - i]
    return output
