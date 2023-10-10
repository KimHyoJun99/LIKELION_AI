

from Day2_fn import *

def main():
    menu_exec= {1:menu_input, 2:menu_output, 3:menu_search, 4:menu_exit}
    
    while True:
        menu()
        input_menu = int(input("번호를 입력하세요:"))
        if input_menu == 4:
            menu_exit()
            break;
        else:
            if 0< input_menu < 4:
                menu_exec[input_menu]()
            else:
                print("1,2,3,4중에 입력하세요")
if __name__ == '__main__':
    main()
    