# 가챠 아이템 교환 프로그램
# 사용자는 자신의 보유 아이템과 원하는 아이템을 관리하고,
# 다른 사용자의 교환 글 중 조건이 맞는 글을 찾을 수 있다.


my_items = ["에렌", "피카츄", "코난"]
wanted_items = []

exchange_posts = [
    {
        "user": "푸앙",
        "have": "리바이",
        "want": "에렌"
    },
    {
        "user": "앙푸",
        "have": "님피아",
        "want": "피카츄"
    },
    {
        "user": "푸푸",
        "have": "괴도키드",
        "want": "코난"
    }
]


def show_my_items():
    print("\n[내 보유 아이템]")

    if len(my_items) == 0:
        print("보유한 아이템이 없습니다.")
    else:
        for number, item in enumerate(my_items, start=1):
            print(f"{number}. {item}")


def add_my_item():
    item = input("추가할 보유 아이템을 입력하세요: ").strip()

    if item == "":
        print("아이템 이름을 입력하지 않았습니다.")
    else:
        my_items.append(item)
        print(f"'{item}'이(가) 보유 아이템에 추가되었습니다.")


def show_wanted_items():
    print("\n[내가 원하는 아이템]")

    if len(wanted_items) == 0:
        print("원하는 아이템이 등록되지 않았습니다.")
    else:
        for number, item in enumerate(wanted_items, start=1):
            print(f"{number}. {item}")


def add_wanted_item():
    item = input("원하는 아이템을 입력하세요: ").strip()

    if item == "":
        print("아이템 이름을 입력하지 않았습니다.")
    else:
        wanted_items.append(item)
        print(f"'{item}'이(가) 원하는 아이템에 추가되었습니다.")


def show_exchange_posts():
    print("\n[전체 교환 글]")

    if len(exchange_posts) == 0:
        print("등록된 교환 글이 없습니다.")
    else:
        for number, post in enumerate(exchange_posts, start=1):
            print(f"{number}. 작성자: {post['user']}")
            print(f"   보유 아이템: {post['have']}")
            print(f"   원하는 아이템: {post['want']}")


def find_matching_posts():
    print("\n[교환 가능한 사용자 찾기]")

    match_count = 0

    for post in exchange_posts:
        # 상대방이 가진 아이템이 내가 원하는 아이템에 있고,
        # 상대방이 원하는 아이템이 내 보유 아이템에 있으면 교환 가능
        if post["have"] in wanted_items and post["want"] in my_items:
            print(f"작성자: {post['user']}")
            print(f"받을 수 있는 아이템: {post['have']}")
            print(f"내가 제공할 아이템: {post['want']}")
            print("-" * 30)
            match_count += 1

    if match_count == 0:
        print("현재 조건에 맞는 교환 글이 없습니다.")
        print("원하는 아이템을 등록하거나 보유 아이템을 추가해 보세요.")


def add_exchange_post():
    user_name = input("작성자 이름을 입력하세요: ").strip()
    have_item = input("교환 가능한 보유 아이템을 입력하세요: ").strip()
    want_item = input("원하는 아이템을 입력하세요: ").strip()

    if user_name == "" or have_item == "" or want_item == "":
        print("모든 항목을 입력해야 합니다.")
    else:
        new_post = {
            "user": user_name,
            "have": have_item,
            "want": want_item
        }

        exchange_posts.append(new_post)
        print("교환 글이 등록되었습니다.")


def print_menu():
    """메뉴를 출력하는 함수"""
    print("\n" + "=" * 35)
    print("        가챠 아이템 교환 프로그램")
    print("=" * 35)
    print("1. 내 보유 아이템 보기")
    print("2. 내 보유 아이템 추가")
    print("3. 원하는 아이템 보기")
    print("4. 원하는 아이템 추가")
    print("5. 전체 교환 글 보기")
    print("6. 교환 가능한 사용자 찾기")
    print("7. 교환 글 등록")
    print("0. 프로그램 종료")


while True:
    print_menu()
    choice = input("메뉴 번호를 선택하세요: ").strip()

    if choice == "1":
        show_my_items()

    elif choice == "2":
        add_my_item()

    elif choice == "3":
        show_wanted_items()

    elif choice == "4":
        add_wanted_item()

    elif choice == "5":
        show_exchange_posts()

    elif choice == "6":
        find_matching_posts()

    elif choice == "7":
        add_exchange_post()

    elif choice == "0":
        print("가챠 아이템 교환 프로그램을 종료합니다.")
        break

    else:
        print("올바른 메뉴 번호를 입력하세요.")



