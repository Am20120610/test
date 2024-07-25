تخزين المهام
tasks = []

# وظيفة لإضافة مهمة
def add_task(task):
    tasks.append(task)
    print(f"تمت إضافة المهمة: {task}")

# وظيفة لحذف مهمة
def delete_task(task):
    if task in tasks:
        tasks.remove(task)
        print(f"تم حذف المهمة: {task}")
    else:
        print(f"المهمة {task} غير موجودة")

# وظيفة لعرض جميع المهام
def show_tasks():
    if tasks:
        print("المهام الحالية:")
        for task in tasks:
            print(f"- {task}")
    else:
        print("لا توجد مهام")

# القائمة الرئيسية
while True:
    print("\nاختر عملية:")
    print("1. إضافة مهمة")
    print("2. حذف مهمة")
    print("3. عرض المهام")
    print("4. خروج")
    
    choice = input("أدخل الخيار (1/2/3/4): ")

    if choice == '1':
        task = input("أدخل المهمة: ")
        add_task(task)
    elif choice == '2':
        task = input("أدخل المهمة المراد حذفها: ")
        delete_task(task)
    elif choice == '3':
        show_tasks()
    elif choice == '4':
        break
    else:
        print("خيار غير صالح، حاول مرة أخرى.")
