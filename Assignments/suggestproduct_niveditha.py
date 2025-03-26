data = {
    "red tshirt": ["trending tshirt", "branded tshirt", "cotton tshirt"],
    "chair": ["table", "sofa"],
    "blue jeans": ["black jeans", "ripped jeans", "denim jacket"]
}
def suggestions(search):
    if search in data:
        print(f"Item name: {search}")
        print("Suggested items for you:")
        for suggestion in data[search]:
            print(suggestion)
    else:
        print("No matching item found.")
search_term = input("Search: ")
suggestions(search_term)


