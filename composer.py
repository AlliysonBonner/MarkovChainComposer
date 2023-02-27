import os
import string
import random
from graph import Graph, Vertex


def get_words_from_text(text_path: str) -> list:
    """Extracts words from text file and returns as a list of lowercase words
    with no punctuation.

    Args:
        text_path (str): Path to the text file.

    Returns:
        list: List of lowercase words with no punctuation.
    """
    with open(text_path, 'rb') as file:
        text = file.read().decode("utf-8")

        # Remove extra whitespace and punctuation
        text = ' '.join(text.split())
        text = text.lower()
        text = text.translate(str.maketrans('', '', string.punctuation))

    words = text.split()
    if len(words) < 3000:
        return words
    else:
        return words[:3000]


def make_graph(words: list) -> Graph:
    """Creates a graph from a list of words.

    Args:
        words (list): List of words to create a graph from.

    Returns:
        Graph: Graph object containing the words and their connections.
    """
    g = Graph()
    prev_word = None
    for word in words:
        # Get or create the vertex for the current word
        word_vertex = g.get_vertex(word)

        # If there was a previous word, add an edge from the previous word to the current word
        if prev_word:
            prev_word.increment_edge(word_vertex)

        prev_word = word_vertex

    g.generate_probability_mappings()

    return g


def compose(g: Graph, words: list, length: int = 50) -> str:
    """Generates a composition of words using a given graph.

    Args:
        g (Graph): Graph to generate words from.
        words (list): List of words to use for starting the composition.
        length (int, optional): Length of the composition in words. Defaults to 50.

    Returns:
        str: String of composed words formatted into stanzas.
    """
    composition = []
    word = g.get_vertex(random.choice(words))
    for _ in range(length):
        composition.append(word.value)
        word = g.get_next_word(word)

    # Group words into stanzas
    stanzas = []
    stanza = []
    for word in composition:
        stanza.append(word.capitalize())
        if len(stanza) == 9:
            # Add extra empty element to separate stanzas
            stanzas.append(stanza + [''])
            stanza = []

    # Add extra empty element to last stanza if needed
    if stanza:
        stanzas.append(stanza + [''])

    # Convert stanzas to strings and join with line breaks
    stanza_strings = [' '.join(stanza) for stanza in stanzas]

    # Add extra line break after every four stanzas
    for i in range(2, len(stanza_strings), 4):
        stanza_strings[i] += '\n'

    output = '\n\n'.join(stanza_strings)

    return output


def main() -> None:
    """Main function to run the program."""
    words = []
    for song in os.listdir('songs'):
        if song == '.DS_Store':
            continue
        words.extend(get_words_from_text("songs/" + song))

    g = make_graph(words)
    composition = compose(g, words, 300)
    print(composition)


if __name__ == '__main__':
    main()
