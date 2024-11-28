import nltk
from nltk.corpus import words

# Ensure the word list is available
nltk.download("words")

# Load English words into a set for fast lookups (case-insensitive)
english_words = set(word.lower() for word in words.words())

def find_words(grid):
    def is_valid_word(word):
        return word in english_words

    def dfs(x, y, node, path, visited):
        char = grid[x][y]
        if not node + char in english_words or (x, y) in visited:
            return

        visited.add((x, y))
        node += char
        path.append((x, y))

        if len(node) > 1 and is_valid_word(node):  # Valid word (longer than 1 char)
            words_found.append((path[:], node))

        # Explore all 8 directions
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                dfs(nx, ny, node, path, visited)

        path.pop()
        visited.remove((x, y))

    words_found = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            dfs(i, j, "", [], set())
    
    # Sort words by length (largest to smallest)
    words_found.sort(key=lambda x: len(x[1]), reverse=True)
    return words_found

def visualize_path(grid, path):
    visual_grid = [["⬜"] * len(grid[0]) for _ in range(len(grid))]
    for idx, (x, y) in enumerate(path):
        visual_grid[x][y] = f"{idx + 1}\u20e3"  # Add numbers with a square indicator
    return "\n".join("".join(row) for row in visual_grid)

def main():
    # Input grid from the user
    size = int(input("Enter grid size (4 or 5): "))
    print("Enter the grid, one row at a time (letters only):")
    grid = [list(input().strip().lower()) for _ in range(size)]

    words_found = find_words(grid)

    if not words_found:
        print("No words found.")
    else:
        print("\nWords found (from largest to smallest):")
        for path, word in words_found:
            print(f"Word: {word}")
            print(visualize_path(grid, path))
            print()

if __name__ == "__main__":
    main()
