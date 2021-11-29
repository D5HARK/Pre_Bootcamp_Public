x = [[5, 2, 3], [10, 8, 9]]
students = [
    {'first_name': 'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'}
]
sports_directory = {
    'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer': ['Messi', 'Ronaldo', 'Rooney']
}
z = [{'x': 10, 'y': 20}]


def value_change(primary_l_pos, secondary_l_pos, new_val):
    print("value update function")
    print("original list", x)
    x[primary_l_pos][secondary_l_pos] = new_val
    print("new list", x, "\n")


def dictionary_iterate(parent_list):
    print("dictionary iterate function one")
    for i in range(len(parent_list)):
        print(''.join("{}: {} ".format(k, v) for k, v in parent_list[i].items()))
    print("\n")


def dictionary_iterate_two(key, parent_list):
    print("dictionary iterate two")
    for i in range(len(parent_list)):
        print(parent_list[i][key])
    print("\n")

def print_info(parent_dictionary):
    for j in parent_dictionary:
        print(len(parent_dictionary[j]), j, "players")
        for i in parent_dictionary[j]:
            print(i)
        print("\n")








def main():
    value_change(1, 0, 15)
    dictionary_iterate(students)
    dictionary_iterate_two("last_name", students)
    print_info(sports_directory)

if __name__ == "__main__":
    main()
