print('------ if구문 ------')

score = 88
if score >= 80:
    # print('성적은 A+입니다.')
    grade = 'A'
elif score >= 70:
    # print('성적은 B입니다.')
    grade = 'B'
elif score >= 60:
    # print('성적은 c입니다.')
    grade = 'C'
else:
    # print('성적은 F입니다.')
    grade = 'F'

print(f'이 학생의 성적은 {grade}입니다.')

month = 7
if month in [12, 1, 2]:
    season = '겨울'
elif month in [3, 4, 5]:
    season = '봄'
elif month in [6, 7, 8]:
    season = '여름'
else:
    season = '가을'

print(f'{month}월은 {season}입니다.')


