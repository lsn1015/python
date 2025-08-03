class EmployeeManage:
    employees = {}

    def __init__(self, name, workNo, dept, salary):
        self.name = name
        self.workNo = workNo
        self.dept = dept
        self.salary = salary

        EmployeeManage.employees[self.workNo] = {
            'Name': self.name,
            'Work No': self.workNo,
            'Department': self.dept,
            'Monthly payment': self.salary
        }
        print(f'新员工{self.name}的信息已添加成功')

    @classmethod
    def add_employees(cls):
        name = input('请输入员工姓名: ')
        workNo = input('请输入员工工号: ')
        dept = input('请输入员工部门: ')
        salary = input('请输入员工月薪: ')
        for workNo in EmployeeManage.employees.keys():
            return cls(name, workNo, dept, salary)
        else:
            print(f'该员工编号已存在！')

    @classmethod
    def show_all(cls):
        print("\n当前所有员工信息： ")
        for workNo, info in cls.employees.items():
            print(f"工号：{workNo},姓名：{info['Name']}部门: {info['Department']}, 月薪: {info['Monthly payment']}")

# 测试代码
if __name__ == "__main__":
    while True:
        print("\n欢迎使用员工管理系统")
        print("1. 添加员工")
        print("2. 删除员工")
        print("3. 显示所有员工")
        print("4. 退出")

        choice = input("请选择（1-4）进行操作： ")

        if choice == '1':
            emp = EmployeeManage.add_employees()
        elif choice == '2':
            workNo = input("请输入要删除的员工工号: ")
            if workNo in EmployeeManage.employees:
                del EmployeeManage.employees[workNo]
                print(f'该员工信息已删除。')
            else:
                print("该员工不存在！")
        elif choice == '3':
            EmployeeManage.show_all()
        elif choice == '4':
            print("感谢使用员工管理系统！")
            break
        else:
            print("无效输入，请重新选择！")
