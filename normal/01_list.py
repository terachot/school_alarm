quest = ['ตีไข่', 'ตั้งกระทะ', 'เจียวไข่']

for i in quest:
    print(i)

quest[1] = 'ใส่น้ำปลา'
print(quest[1])

quest.append('ใส่จาน')
print(quest)

quest.insert(1, 'ตั้งกระทะ')
print(quest)

quest.remove('ใส่น้ำปลา')
print(quest)

# Tuple ค่าเปลี่ยนแปลงไม่ได้
quests = ('ขุดดิน', 'หว่านพืช', 'รดน้ำ')

# Dictionary
quests1 = {'001': 'เก็บผลไม้', '002': 'ตกปลา', '003': 'หาของ'}
print(len(quests1))
quests1['004'] = 'ลงดันเจี้ยน'
quests1.pop('002')
print(quests1)