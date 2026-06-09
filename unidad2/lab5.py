def show_menu():
    print("=== SPOTIFY ===")
    print("Select a genre:")
    print("1. Alternative Rock")
    print("2. Pop")
    print("3. Indie")
    print("4. Reggaeton")


def get_genre():
    option = input("Option: ")
    return option


def recommend_content(genre):
    if genre == "1":
        return ["Do I Wanna Know? - Arctic Monkeys", "Mr. Brightside - The Killers"]
    elif genre == "2":
        return ["Flowers - Miley Cyrus", "Style - Taylor Swift"]
    elif genre == "3":
        return ["505 - Arctic Monkeys", "Sweater Weather - The Neighbourhood"]
    elif genre == "4":
        return ["Provenza - Karol G", "Tití Me Preguntó - Bad Bunny"]
    else:
        return []


def show_recommendations(recommendations):
    if len(recommendations) == 0:
        print("Invalid option. No recommendations found.")
    else:
        print("\nRecommendations:")
        for content in recommendations:
            print("- " + content)


def rate_content():
    rating = int(input("\nRate the content from 1 to 5: "))

    while rating < 1 or rating > 5:
        print("Invalid rating. Please enter a number from 1 to 5.")
        rating = int(input("Rate the content from 1 to 5: "))

    return rating


def main():
    repeat = "Y"

    while repeat.upper() == "Y":
        show_menu()
        genre = get_genre()
        recommendations = recommend_content(genre)
        show_recommendations(recommendations)

        if len(recommendations) > 0:
            rating = rate_content()
            print("Thank you! Your rating was:", rating)

        repeat = input("\nWould you like to perform another search? (Y/N): ")

    print("Thank you for using Spotify recommendations!")


main()