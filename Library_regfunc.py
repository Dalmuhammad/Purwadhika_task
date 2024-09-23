# %%
import datetime
from datetime import date, timedelta

# %%
dict_book = {
    101: {'title': 'Introduction to Python', 'author': 'Alpha', 'qty': 5, 'genre': 'Technology', 'year': 2020},
    102: {'title': 'Basic Principles of Marketing', 'author': 'Beta', 'qty': 6, 'genre': 'Business', 'year': 2018},
    103: {'title': 'Data Science Fundamentals', 'author': 'Alpha', 'qty': 0, 'genre': 'Technology', 'year': 2021},
    104: {'title': 'Understanding Philosophy', 'author': 'Gamma', 'qty': 3, 'genre': 'Philosophy', 'year': 2015},
    105: {'title': 'Python for Data Analysis', 'author': 'Alpha', 'qty': 7, 'genre': 'Technology', 'year': 2019},
    106: {'title': 'Artificial Intelligence Basics', 'author': 'Delta', 'qty': 8, 'genre': 'Technology', 'year': 2021},
    107: {'title': 'Financial Accounting Simplified', 'author': 'Beta', 'qty': 5, 'genre': 'Business', 'year': 2017},
    108: {'title': 'Ethics in Modern Philosophy', 'author': 'Gamma', 'qty': 6, 'genre': 'Philosophy', 'year': 2010},
    109: {'title': 'Exploring Quantum Computing', 'author': 'Epsilon', 'qty': 0, 'genre': 'Science', 'year': 2022},
    110: {'title': 'Marketing Strategies for Startups', 'author': 'Beta', 'qty': 9, 'genre': 'Business', 'year': 2018},
    111: {'title': 'The Future of Robotics', 'author': 'Delta', 'qty': 6, 'genre': 'Technology', 'year': 2020},
    112: {'title': 'Foundations of Sociology', 'author': 'Alpha', 'qty': 0, 'genre': 'Sociology', 'year': 2016},
    113: {'title': 'Philosophical Thoughts in History', 'author': 'Gamma', 'qty': 4, 'genre': 'Philosophy', 'year': 2019},
    114: {'title': 'Basic Concepts in Chemistry', 'author': 'Epsilon', 'qty': 3, 'genre': 'Science', 'year': 2017},
    115: {'title': 'Introduction to Cybersecurity', 'author': 'Alpha', 'qty': 8, 'genre': 'Technology', 'year': 2021},
    116: {'title': 'Urban Planning Essentials', 'author': 'Beta', 'qty': 6, 'genre': 'Urban Studies', 'year': 2019},
    117: {'title': 'History of Modern Art', 'author': 'Delta', 'qty': 10, 'genre': 'Art', 'year': 2018},
    118: {'title': 'Modern Business Leadership', 'author': 'Beta', 'qty': 0, 'genre': 'Business', 'year': 2021},
    119: {'title': 'Introduction to Environmental Studies', 'author': 'Gamma', 'qty': 7, 'genre': 'Environmental', 'year': 2020},
    120: {'title': 'Creative Writing Techniques', 'author': 'Alpha', 'qty': 6, 'genre': 'Literature', 'year': 2015},
}
last_id = 100+len(dict_book)

# %%
def loan_policy():
    print("Book Loan Policy:")
    print("1. The first 7 days of borrowing are free.")
    print("2. A fee of 1000 will be charged per day after the 7th day.")
    print("3. The maximum loan period for a book is 14 days.")
    print("4. A late return penalty of 2000 per day will be applied.")
    print("5. The maximum penalty is 1.000.000.")
#loan_policy()

# %%
def continue_yes_no(statement_):
    while True:
        yes_no = input(statement_)
        if yes_no.lower()=='yes':
            return 1
        elif yes_no.lower()=='no':
            return 0
        else:
            print("Invalid input, please answer with 'yes' or 'no'.")

# %%
def option_number(lower_,upper_,statement_):
    choice = int(input(statement_))
    while choice<lower_ or choice>upper_:
        print('The number is not available, please choose based on the list')
        if continue_yes_no('Would you like to try again? (yes/no)')==0:
            break
        choice= int(input(statement_))
    return choice

# %%
def list_all(dict_):
    keys = list(dict_.keys())
    list_title = list(val['title'].lower() for val in dict_.values())
    list_author = []
    list_genre = []
    for val in dict_.values():
        if val['author'].lower() not in list_author:
            list_author.append(val['author'].lower())
        if val['genre'].lower() not in list_genre:
            list_genre.append(val['genre'].lower())
    return [keys,list_title,list_author, list_genre]

# %%
def display_book(input_dict, max_item=None):
    if max_item is None:
        max_item=20
    number = 0
    print(f"{'No':^4}| {'Book ID':^8} | {'Title':^30} | {'Author':^20} | {'Year':^5} | {'Status':^13} | {'Genre':^15}")
    for key_disp, val_disp in input_dict.items():
        number+=1
        status = 'Available' if val_disp['qty']!=0 else 'Not available'
        print(f"{number:^4}| {key_disp:^8} | {val_disp['title']:<30.30} | {val_disp['author']:<20.20} | {val_disp['year']:^5} | "
        f"{status:<13} | {val_disp['genre']:<15}")
        if number>=max_item:
            break

# %%
def borrowing_details(input_dict):
    number = 0
    print(f"{'No':^4}| {'Book ID':^8} | {'Title':^30} | {'Author':^20} | {'Year':^5} | {'Genre':^15} | {'Borrowing date':^15} | {'Returning date':^15} | {'Status':^10}")
    for key_disp, val_disp in input_dict.items():
        number+=1
        borr_date = val_disp['borr_date'].strftime('%d-%m-%Y')
        return_date = val_disp['return_date'].strftime('%d-%m-%Y')
        print(f"{number:^4}| {key_disp:^8} | {val_disp['title']:<30.30} | {val_disp['author']:<20.20} | {val_disp['year']:^5} | "
        f"{val_disp['genre']:<15} | {borr_date:<15} | {return_date:<15} | {val_disp['status']:<10}")

# %%
def returning_details(input_dict):
    number = 0
    print(f"{'No':^4}| {'Book ID':^8} | {'Title':^30} | {'Borrowing date':^15} | {'Returning date':^15} | {'Borrowing fee':15} | | {'Late fee':15}")
    for key_disp, val_disp in input_dict.items():
        number+=1
        borr_date = val_disp['borr_date'].strftime('%d-%m-%Y')
        return_date = val_disp['return_date'].strftime('%d-%m-%Y')
        print(f"{number:^4}| {key_disp:^8} | {val_disp['title']:<30.30} | {borr_date:<15} | {return_date:<15} | {val_disp['borr_fee']:<15} | {val_disp['late_fee']:<15}")

# %%
def filter_book(dict_, inp_filter, inp_opt=None, display_=None):
    filter_ = []
    for val in dict_.values():
        if val[inp_filter].lower() not in filter_:
            filter_.append(val[inp_filter].lower()) 

    if display_:
        print(f"List of {inp_filter}:")
        print(f"{'No':^4} | {inp_filter.capitalize():<15}")
        for i in range(len(filter_)):
            print(f"{i+1:^4} | {filter_[i]:<15}")
        print("")
    if inp_opt:
        input_opt_ = inp_opt
        filter_option = {key:val for key,val in dict_.items() if val[inp_filter].lower()==filter_[input_opt_-1]}
    else:
        input_opt_ = option_number(1,len(filter_), "Please input the number corresponding to the genre you want from the list: ")
        if 1<=input_opt_<=len(filter_):
            filter_option = {key:val for key,val in dict_.items() if val[inp_filter].lower()==filter_[input_opt_-1]}
        else:
            filter_option={}
    return filter_option

# %%
def sorting_dict(dict_):
    keys_ = list(dict_.keys())
    for i in range(len(keys_)):
        for j in range(i+1, len(keys_)):
            if keys_[i]>keys_[j]:
                keys_[i],keys_[j]=keys_[j],keys_[i]
    
    sort_dict = {keys:dict_[keys] for keys in keys_}
    return sort_dict

# %%
def update_dict(init_dict, dict_input):
    for key_1, val_1 in dict_input.items():
        if key_1 in init_dict:
            if init_dict[key_1] != val_1:
                init_dict[key_1]=[init_dict[key_1],val_1]
        else:
            init_dict[key_1]=val_1
    return init_dict

# %%
def display_by_filter():
    while True:
        filter_ = input("Do you want to show the book by author or genre? (author/genre)").lower()
        if filter_=='author':
            display_book(filter_book(dict_book,'author',display_=True))
            break
        elif filter_=='genre':
            display_book(filter_book(dict_book,'genre',display_=True))
            break
        else:
            print("Invalid input, please answer by 'author' or 'genre'.")

# %%
def borrow_book_filter(filter_, filter_list, optional_filter=None):
    keys=list(dict_book.keys())
    while True:
        input_item = int(input(f"Input {filter_} that you want to borrow: ")) if filter_=='ID'\
            else input(f"Input the {filter_} book that you want to borrow: ").lower()
        if input_item not in filter_list:
            print(f"{filter_} is not available")
            if continue_yes_no(f"Do you still want to borrow the book by {filter_}? (yes/no) ")==0:
                break
        else:
            if filter_=='ID':
                borr_id = input_item
            else:
                index_ = filter_list.index(input_item)
                borr_id = keys[index_]
            
            if optional_filter:
                dict_borr_filter = optional_filter(dict_book,filter_,index_+1)
                keys_borr_filter = list(dict_borr_filter.keys())
                print("\n List of book:")
                display_book(dict_borr_filter)
                borr_number = option_number(1,len(keys_borr_filter),"Input the number corresponding the book that you want to borrow: ")
                if 1<=borr_number<=len(keys_borr_filter):
                    borr_id = keys_borr_filter[borr_number-1]
                        

            print("\n Detail book: ")
            display_book({borr_id: dict_book[borr_id]})

            if dict_book[borr_id]['qty']<=0:
                print("This book is out of stock.")
                break
            
            keys_user = list(user_borrow.keys())
            if borr_id in keys_user:
                print("This book is already in your borrowed list and cannot be added to the cart.")
                break
                        
            if continue_yes_no("Are you sure want to borrow this book? (yes/no)")==0:
                if continue_yes_no(f"Do you still want to borrow the book by the {filter_}? (yes/no) ")==0:
                    break
                else:
                    continue

            total_day = int(input("For how many days would you like to borrow the book? "))
            while total_day < 1 or total_day > 14:
                print("The borrowing period must be between 1 and 14 days.")
                total_day = int(input("Please enter a valid number of days (1-14): "))
            borr_fee = max(0, 1000 * (total_day - 7))

            borr_date = date.today()
            return_date = borr_date +timedelta(days=total_day)

            user_borrow[borr_id] = {'title':dict_book[borr_id]['title'],
                                        'author':dict_book[borr_id]['author'],
                                        'year':dict_book[borr_id]['year'],
                                        'genre':dict_book[borr_id]['genre'],
                                        'borr_date':borr_date,
                                        'return_date':return_date,
                                        'borr_fee':borr_fee,
                                        'status':'Pending'}
            
            break

# %%
def borrowing_book():
    list_=list_all(dict_book)
    while True:
        print("Do you want to borrow the book by: ")
        print("1. ID")
        print("2. Title")
        print("3. Author")
        print("4. Genre")
        print("5. Return to the previous menu")
        book_bb = input("Input the number corresponding from the list: ")
        
        if book_bb == '1':
            borrow_book_filter("ID", list_[0])
        elif book_bb == '2':
            borrow_book_filter("title", list_[1])
        elif book_bb == '3':
            borrow_book_filter("author", list_[2], filter_book)
        elif book_bb == '4':
            borrow_book_filter("genre", list_[3], filter_book)
        elif book_bb == '5':
            break
        else:
            print("Invalid choice. Please try again.")
            continue
        
        if continue_yes_no("Do you want to borrow another book? (yes/no)") == 0:
            break

# %%
def del_book_filter(status, dict_,filter_, filter_list, optional_filter=None):
    if len(dict_)==0:
        print("There are no books available for deletion.")
        return
    disp_function = display_book if status=='admin' else borrowing_details
    if continue_yes_no(f"Do you want to display list of {filter_}? (yes/no)") == 1:
        print(f"List of {filter_}:")
        print(f"{'No':^4} | {filter_.upper():<15}")
        for i in range(len(filter_list)):
            print(f"{i+1:^4} | {filter_list[i]:<15}")
    while True:
        keys = list(dict_.keys())
        input_item = int(input(f"Input {filter_} that you want to delete: ")) if filter_=='ID'\
            else input(f"Input the {filter_} book that you want to delete: ").lower()
        if input_item not in filter_list:
            print(f"{filter_} is not available")
            if continue_yes_no(f"Do you still want to delete the book by {filter_}? (yes/no) ")==0:
                break
        else:
            if filter_=='ID': 
                del_id = input_item
            else:
                index_ = filter_list.index(input_item)
                del_id = keys[index_]
            if optional_filter:
                dict_del_filter = optional_filter(dict_,filter_,index_+1)
                keys_del_filter = list(dict_del_filter.keys())
                if len(dict_del_filter)>1:
                    print("\n List of book:")
                    disp_function(dict_del_filter)
                    del_number = option_number(1,len(keys_del_filter),"Input the number corresponding the book that you want to delete: ")
                    if 1<=del_number<=len(keys_del_filter):
                        del_id = keys_del_filter[del_number-1]

            print("\n Detail book: ")
            disp_function({del_id: dict_[del_id]})

            if continue_yes_no("Are you sure want to delete this book? (yes/no)")==0:
                if continue_yes_no(f"Do you still want to delete the book by the {filter_}? (yes/no) ")==0:
                    break
                else:
                    continue
                        
            del dict_[del_id]

            break

# %%
def deleting_book(status_, dict_):
    while True:
        list_ = list_all(dict_)
        print("Do you want to delete the book by: ")
        print("1. ID")
        print("2. Title")
        print("3. Author")
        print("4. Genre")
        print("5. Return to the previous menu")
        book_bb = input("Input the number corresponding from the list: ")
        
        if book_bb == '1':
            del_book_filter(status_,dict_,"ID", list_[0])
        elif book_bb == '2':
            del_book_filter(status_,dict_,"title", list_[1])
        elif book_bb == '3':
            del_book_filter(status_,dict_,"author", list_[2], filter_book)
        elif book_bb == '4':
            del_book_filter(status_,dict_,"genre", list_[3], filter_book)
        elif book_bb == '5':
            break
        else:
            print("Invalid choice. Please try again.")
            continue
        
        if continue_yes_no("Do you want to delete another book? (yes/no)") == 0:
            break

# %%
def view_item_cart(dict_):
    print("\nList of book(s) in the cart")
    borrowing_details(sorting_dict(dict_))

# %%
def check_status(dict_):
    today = date.today()
    for book_id in dict_.keys():
        if dict_[book_id]['return_date']<today:
            dict_[book_id]['status'] = 'Overdue'

# %%
def add_book():
    title_book = input("What is the title of your book? ")
    author_book = input("Who is the first author's name? ")  
    genre_book = input("What is the genre's book? ")
    year_book = int(input("When is the book published? "))
    qty_book = int(input("How many pcs you want to input? "))
    title_author_year = list((book['title'].lower(), book['author'].lower(), book['year']) for book in dict_book.values())
    tuple_tay = (title_book.lower(),author_book.lower(),year_book)
    keys = list(dict_book.keys())
    global last_id
    last_id +=1
    if tuple_tay in title_author_year:
        index_tuple = title_author_year.index(tuple_tay)
        dict_book[keys[index_tuple]]['qty']+=qty_book
        print("The books have been added")
    else:
        dict_book[last_id]= {'title':title_book.capitalize(), 'author':author_book.capitalize(),'qty':qty_book,'genre':genre_book,'rating':5,'year':year_book}
        print("The books have been added")

# %%
def change_option(book_id):
    while True:
        print("\nAvailable book attributes to modify:")
        print("1. Title")
        print("2. Author")
        print("3. Year")
        print("4. Genre")
        print("5. Quantity\n")
        
        opt_ = input("Which attribute would you like to modify? Please enter the corresponding number: ")
        
        if opt_ == '1':
            new_title = input("Input the new title: ")
            dict_book[book_id]['title'] = new_title
            print(f"Title has been updated to '{new_title}'.")
        
        elif opt_ == '2':
            new_author = input("Input the new author: ")
            dict_book[book_id]['author'] = new_author
            print(f"Author has been updated to '{new_author}'.")
        
        elif opt_ == '3':
            new_year = input("Input the new year: ")
            dict_book[book_id]['year'] = new_year
            print(f"Year has been updated to '{new_year}'.")
        
        elif opt_ == '4':
            new_genre = input("Input the new genre: ")
            dict_book[book_id]['genre'] = new_genre
            print(f"Genre has been updated to '{new_genre}'.")
        
        elif opt_ == '5':
            new_quantity = int(input("Input the new quantity: "))
            dict_book[book_id]['qty'] = new_quantity
            print(f"Quantity has been updated to '{new_quantity}'.")
        
        else:
            print("Invalid option. Please try again.")
            continue
        
        if continue_yes_no("Would you like to modify another attribute? (yes/no) ")==0:
            print("Modification completed.")
            break


# %%
def change_detail():
    keys = list(dict_book.keys())
    print(f"\nList of Book ID : \n{keys}\n")
    while True:
        book_id = int(input("Input Book ID that you want to modify :"))
        while book_id not in keys:
            print("Invalid Book ID!")
            if continue_yes_no("Do you want to input another Book ID ? (yen/no) ")==0:
                break
            book_id = int(input("Input Book ID that you want to modify :"))
        else:
            print("Book's information:")
            display_book({book_id:dict_book[book_id]})
            print("")
            if continue_yes_no("Do you want to modify this book ? (yes/no)")==1:
                change_option(book_id)
            
        if continue_yes_no("Do you want to modify another book? (yes/no) ")==0:
            break

# %%
def view_active_menu():
    check_status(user_borrow2)
    print("\nList of active borrowings\n")
    borrowing_details(sorting_dict(user_borrow2))

# %%
def finalizing_(dict_, dict_2):
    if len(dict_)==0:
        print("There is no item (book) in the cart")
    else:
        view_item_cart(dict_)
        total_borr_fee = sum([value_dict['borr_fee'] for value_dict in dict_.values()])
        print(f"\nTotal borrowing fee = {total_borr_fee}.\nThe borrowing fee can be paid when returning the book")
        if continue_yes_no("Do you want to proceed ? (yes/no)")==0:
            return [dict_, dict_2]
        else:
            id_remove = []
            for book_id in dict_:
                if dict_book[book_id]['qty']<1:
                    borrowing_details({book_id:dict_[book_id]})
                    print("Sorry, this book is out of stock. You can not borrow this book.\nSystem will remove this book from your cart")
                    id_remove.append(book_id)
                    continue
                else:
                    dict_book[book_id]['qty'] -= 1
                    dict_[book_id]['status'] = 'On Loan'

            for book_id in id_remove:
                del dict_[book_id]
            
            dict_2 = update_dict(dict_2,dict_)
            dict_ = {}
        total_borr_fee_2 = sum([value_dict['borr_fee'] for value_dict in dict_2.values()])
        if total_borr_fee!=total_borr_fee_2:
            print(f"\nUpdate!\nTotal borrowing fee = {total_borr_fee_2}.\nThe borrowing fee can be paid when returning the book.")
        print("Successfull!")
    
    return [dict_,dict_2]

# %%
def finalize_borrow(dict_,dict_2):
    dict_, dict_2 = finalizing_(dict_, dict_2)

# %%
def returning_menu():
    dict_=user_borrow2
    today = date.today()
    if len(dict_)==0:
        print("There is no active borrowing.")
    else:
        list_id = list(dict_.keys())
        view_active_menu()
        total_books = int(input("How many book you want to return : "))
        while total_books<1 or total_books>len(dict_):
            print(f"Invalid input!")
            total_books = int(input("How many book you want to return : "))
        
        list_book_id = []
        for i in range(total_books):
            while True:
                book_id = int(input(f"Input ID (Book {i+1}): "))
                if book_id in list_id and book_id not in list_book_id:
                    list_book_id.append(book_id)
                    break
                elif book_id in list_book_id:
                    print("You have entered this ID before")
                else:
                    print("Invalid ID!") 

        dict_del = {id_:dict_[id_] for id_ in list_book_id}
        total_fee = 0
        for id_ in list_book_id:
            diff_day = (today-dict_del[id_]['return_date']).days
            dict_del[id_]['late_fee'] = min(max(0, diff_day*2000),1000000)
            total_f = dict_del[id_]['borr_fee']+dict_del[id_]['late_fee']
            total_fee += total_f

        print("")
        returning_details(dict_del)
        print(f"Total fee = {total_fee}")
        if continue_yes_no("Are you sure want to return this/these book(s)? (yes/no) ")==1:
            money = int(input('Enter the amount of money: '))
            while money<total_fee:
                print(f'Your money is less than {total_fee-money}')
                money = int(input('Enter the amount of money: '))
            print("Payment successful.")
            if money>total_fee:
                print(f'\nYour money back: {money-total_fee}')

            for id_ in list_book_id:
                del dict_[id_]
                dict_book[id_]['qty'] += 1
                dict_del[id_]['status'] = 'Returned'

            update_dict(user_borrow3, dict_del)

# %%
def display_menu():
    while True:
        print("\nDisplay book:")
        print("1. Display all the book")
        print("2. Display the book by filter (genre/author)")
        print("3. Back to main menu")
        choice = input("Please select an option (1-3): ")

        if choice == '1':
            display_book(dict_book, max_item=100)
            if continue_yes_no("Back to main menu? (yes/no)")==1:
                break
        elif choice == '2':
            display_by_filter()
            if continue_yes_no("Back to main menu? (yes/no)")==1:
                break
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

# %%
def borrowing_menu():
    while True:
        print("\nBorrowing Book:")
        print("1. Search and add book(s) to the cart")
        print("2. Delete book(s) from the cart")
        print("3. View book(s) in the cart")
        print("4. Finalize borrowing")
        print("5. Back to main menu")
        choice = input("Please select an option (1-5): ")

        if choice == '1':
            borrowing_book()
            if continue_yes_no("Back to main menu? (yes/no)")==1:
                break
        elif choice == '2':
            deleting_book("user", user_borrow)
            if continue_yes_no("Back to main menu? (yes/no)")==1:
                break
        elif choice == '3':
            view_item_cart(user_borrow)
            if continue_yes_no("Back to main menu? (yes/no)")==1:
                break
        elif choice == '4':
            finalize_borrow(user_borrow,user_borrow2)
            if continue_yes_no("Back to main menu? (yes/no)")==1:
                break
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

# %%
def admin_menu():
    while True:
        print("\nMain Menu:")
        print("1. Display book")
        print("2. Add new book")
        print("3. Delete book")
        print("4. Update book details")
        print("5. Exit")
        choice = input("Please select an option (1-5): ")

        if choice == '1':
            display_menu()
        elif choice == '2':
            add_book()
        elif choice == '3':
            deleting_book("admin", dict_book)
        elif choice == '4':
            change_detail()
        elif choice == '5':
            print("Thank You!")
            break
        else:
            print("Invalid choice. Please try again.")

# %%
def user_menu():
    while True:
        print("\nMain Menu:")
        print("1. Display book")
        print("2. Borrowing book")
        print("3. View active borrowing")
        print("4. Returning book")
        print("5. Exit")
        choice = input("Please select an option (1-5): ")

        if choice == '1':
            display_menu()
        elif choice == '2':
            borrowing_menu()
        elif choice == '3':
            view_active_menu()
        elif choice == '4':
            returning_menu()
        elif choice == '5':
            print("Thank You!")
            break
        else:
            print("Invalid choice. Please try again.")


# %%
#Main Menu
def main_menu():
    print("Welcome to the PWD Library.")
    print("Please log in as either Admin or User.")
    
    while True:
        role = input("Are you admin or user? (admin/user): ").lower()
        
        if role == 'admin':
            print("Welcome, Admin!")
            admin_menu()
            break
        elif role == 'user':
            print("Welcome, User!\n")
            loan_policy()
            user_menu()
            break
        else:
            print("Invalid input. Please enter 'admin' or 'user'.")

# %%
def reset_dict():
    global user_borrow, user_borrow2, user_borrow3
    user_borrow={}
    user_borrow2={}
    user_borrow3={}
reset_dict()

# %%
main_menu()


