# Exercise 2: String Utilities


from os import O_TEMPORARY


def reverse_string(s: str) -> str:
    """
    Return the input string in reverse order.

    Args:
        s: Input string

    Returns:
        The reversed string
    """
    # TODO: Implement this function
    return s[::-1] 


def count_vowels(s: str) -> int:
    """
    Return the number of vowels (a, e, i, o, u) in the input string.
    Case-insensitive: both uppercase and lowercase vowels should be counted.

    Args:
        s: Input string

    Returns:
        The number of vowels in the string
    """
    # TODO: Implement this function
    vowels = {'a', 'e', 'i', 'o', 'u'}  # Utilisation d'un set pour une recherche rapide
    return sum(1 for char in s.lower() if char in vowels)


def is_palindrome(s: str) -> bool:
    """
    Check if the input string is a palindrome.
    A palindrome reads the same backward as forward.
    Spaces and case should be ignored.

    Args:
        s: Input string

    Returns:
        True if the string is a palindrome, False otherwise
    """
    # TODO: Implement this function
    cleaned_s = "".join(char.lower() for char in s if char.isalnum())  # Suppression des espaces et caractères non alphanumériques
    return cleaned_s == cleaned_s[::-1]  # Comparaison avec la version inversée


def capitalize_words(s: str) -> str:
    """
    Capitalize the first letter of each word in the input string.

    Args:
        s: Input string

    Returns:
        The input string with the first letter of each word capitalized
    """
    # TODO: Implement this function
    return s.title()  # Utilisation de la méthode title() pour capitaliser chaque mot
print(reverse_string(3456))