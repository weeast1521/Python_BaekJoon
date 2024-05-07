import tkinter as tk
import csv

def search_word():
    word = entry_word.get().lower()  # 입력된 단어를 소문자로 변환하여 저장
    if word in word_dict:
        meaning = word_dict[word]
        label_meaning.config(text=meaning)
    else:
        label_meaning.config(text="단어를 찾을 수 없습니다.")

def login():
    username = entry_username.get()
    password = entry_password.get()
    if username == "user" and password == "password":
        label_login_status.config(text="로그인 성공")
        entry_word.config(state=tk.NORMAL)
        search_button.config(state=tk.NORMAL)
    else:
        label_login_status.config(text="로그인 실패")

# 단어 사전 (단어: 의미)
word_dict = {}

# CSV 파일에서 단어 읽어오기

with open('words.csv', newline='', encoding='utf-8-sig') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        word_dict[row[0]] = row[1]


# Tkinter 창 생성
root = tk.Tk()
root.title("영어 단어장")

# 로그인 프레임
login_frame = tk.Frame(root)
login_frame.grid(row=0, column=0, columnspan=2)

label_username = tk.Label(login_frame, text="사용자 이름:")
label_username.grid(row=0, column=0)

entry_username = tk.Entry(login_frame)
entry_username.grid(row=0, column=1)

label_password = tk.Label(login_frame, text="비밀번호:")
label_password.grid(row=1, column=0)

entry_password = tk.Entry(login_frame, show="*")
entry_password.grid(row=1, column=1)

login_button = tk.Button(login_frame, text="로그인", command=login)
login_button.grid(row=2, columnspan=2)

label_login_status = tk.Label(login_frame, text="")
label_login_status.grid(row=3, columnspan=2)

# 단어 입력 필드
label_word = tk.Label(root, text="단어:")
label_word.grid(row=1, column=0)

entry_word = tk.Entry(root, state=tk.DISABLED)  # 로그인 전에는 비활성화 상태로 설정
entry_word.grid(row=1, column=1)

# 검색 버튼
search_button = tk.Button(root, text="검색", command=search_word, state=tk.DISABLED)  # 로그인 전에는 비활성화 상태로 설정
search_button.grid(row=1, column=2)

# 단어 의미 표시 레이블
label_meaning = tk.Label(root, text="")
label_meaning.grid(row=2, column=0, columnspan=3)

root.mainloop()
