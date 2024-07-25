# قائمة لتخزين جهات الاتصال
contacts = []

# وظيفة لإضافة جهة اتصال جديدة
def add_contact(name, phone):
    contact = {"name": name, "phone": phone}
    contacts.append(contact)
    print(f"تمت إضافة جهة الاتصال: {name}")

# وظيفة لعرض جميع جهات الاتصال
def show_contacts():
    if contacts:
        print("جهات الاتصال:")
        for contact in contacts:
            print(f"الاسم: {contact['name']}, رقم الهاتف: {contact['phone']}")
    else:
        print("لا توجد جهات اتصال")

# وظيفة لحذف جهة اتصال
def delete_contact(name):
    global contacts
    contacts = [contact for contact in contacts if contact["name"] != name]
    print(f"تم حذف جهة الاتصال: {name}")

# القائمة الرئيسية
while True:
    print("\nاختر عملية:")
    print("1. إضافة جهة اتصال")
    print("2. عرض جهات الاتصال")
    print("3. حذف جهة اتصال")
    print("4. خروج")

    choice = input("أدخل الخيار (1/2/3/4): ")

    if choice == '1':
        name = input("أدخل الاسم: ")
        phone = input("أدخل رقم الهاتف: ")
        add_contact(name, phone)
    elif choice == '2':
        show_contacts()
    elif choice == '3':
        name = input("أدخل الاسم المراد حذفه: ")
        delete_contact(name)
    elif choice == '4':
        break
    else:
        print("خيار غير صالح، حاول مرة أخرى.")
    print ("hi")
        
