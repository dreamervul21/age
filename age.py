driving = input('請問你有沒有開過車？')
if driving != '有' and driving !='沒有':
    print('請輸入有或沒有')
    raise SystemExit

age = input('請問你的年齡？')
age = int(age)
if driving == '有':
	if age >= 18:
		print('通過測驗了')
	else:
		print('無照駕駛？！！')
elif driving == '沒有':
	if age >= 18:
		print('可以去考囉')
	else:
		print('很好,再幾年就能考')
else:
	print('請輸入有或沒有')