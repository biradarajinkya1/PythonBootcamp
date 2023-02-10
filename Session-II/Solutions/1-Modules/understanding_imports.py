
print("\nThis will always run.")

def test():
    print(f"Module's Name: {__name__}, from test function")

if __name__ == "__main__":
    test()
    print(f"Executed File: Module's Name: '{__name__}', Run directly")
else:
    print(f"Module's Name: '{__name__}', Run from an Import")
