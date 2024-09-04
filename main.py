from typing import List

def capitalizeTitle(title: str) -> str:
    lst: List[str] = title.split()
    for i in range(len(lst)):
        if len(lst[i]) >= 3:
            lst[i] = lst[i].capitalize()
        else:
            lst[i] = lst[i].lower()
    return " ".join(lst)

def main() -> None:
    print(capitalizeTitle("capiTalIze tHe titLe"))
    print(capitalizeTitle("First leTTeR of EACH Word"))
    print(capitalizeTitle("i lOve leetcode"))
    
if __name__ == "__main__":
    main()