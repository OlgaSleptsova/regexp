from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
with open("phonebook_raw.csv", encoding="utf-8") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)

import re

PATTERN_TEL =r'(\+7|8)?\s*\((\d+)\)\s*(\d+)[-\s]*(\d+)[-\s]*(\d+)\s?[(]?(доб.)?\s?(\d+)[)]?'
TEL_SUB = r'+7(\2)-\3-\4-\5 \6\7'

new_contacts = []
for item in contacts_list:
  contact_fullname = " ".join(item[:3]).split(" ")

  cont_result = [contact_fullname[0], contact_fullname[1], contact_fullname[2], item[3], item[4],
                 re.sub(PATTERN_TEL, TEL_SUB, item[5]),item[6]]


  new_contacts.append(cont_result)





my_new_contacts ={}
for x in new_contacts:

  if (x[0],x[1]) in my_new_contacts.keys() :



    new_ct= list (zip(my_new_contacts[x[0],x[1]],x[3:]))

    contact =[]
    for y in new_ct:
      for r in y:
        if r not in contact and r != "":
          contact.append(r)
    # print(contact)

    my_new_contacts[x[0],x[1]]=contact
  else:
    my_new_contacts[x[0],x[1]]=x[2:]


new_contacts2=[]
for v,n in my_new_contacts.items():
  w=list(v)
  for n1 in n:
    w.append(n1)

  new_contacts2.append(w)












# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w", encoding="utf-8") as f:
  datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(new_contacts2)