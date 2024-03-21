import requests
from employeeTable import employeeTable


db_connection_string = "postgresql://x_clients_user:x7ngHjC1h08a85bELNifgKmqZa8KIR40@dpg-cn1542en7f5s73fdrigg-a.frankfurt-postgres.render.com/x_clients_xxet"

sql = employeeTable(db_connection_string)

def test_create_new_employee_sql():
    name = "ООО ПулковоСтар"
    description = "У нас делаеют дела"
    sql.create_company(name, description)
    company_id = sql.get_max_id_company()
    sql.create_employee(
        is_active = True,
        create_timestamp = '2024-03-21 14:00:00.564 +0300', 
        change_timestamp = '2024-03-21 14:00:00.564 +0300',
        first_name = 'Иван',
        last_name  ='Исфаилов',
        middle_name  ='Иванович',
        phone  = '89764356688',
        email  = 'datch@example.com',
        avatar_url  = 'https://ya.ru/',
        company_id = company_id
    )
    employee_id = sql.get_employee_max_id()
    assert sql.get_company()[-1]["name"] == "ООО ПулковоСтар"
    assert sql.get_company()[-1]["description"] == "У нас делаеют дела"
    assert sql.get_employee()[-1]["first_name"] == 'Иван'
    assert sql.get_employee()[-1]["last_name"] == 'Исфаилов'
    assert sql.get_employee()[-1]["middle_name"] == 'Иванович'
    assert sql.get_employee()[-1]["phone"] == '89764356688'
    assert sql.get_employee()[-1]["email"] == 'datch@example.com'
    assert sql.get_employee()[-1]["avatar_url"] == 'https://ya.ru/'
    sql.delete_employee(employee_id)
    sql.delete_company(company_id)




    
def test_update_employee():
    name = "ООО Палочка"
    description = "Доставка деревьев"
    sql.create_company(name, description)
    company_id = sql.get_max_id_company()
    sql.create_employee(
        is_active = True,
        create_timestamp = '2024-03-21 15:00:00.564 +0300', 
        change_timestamp = '2024-03-21 15:00:00.564 +0300',
        first_name = 'Александр',
        last_name  ='Романов',
        middle_name  ='Петрович',
        phone  = '89008762134',
        email  = 'may@example.com',
        avatar_url  = 'https://ya.ru/',
        company_id = company_id
    )
    sql.change_employee(
        is_active = False,
        last_name = 'Иванов',
        phone = '79007653289',
        email = 'kratos@example.com',
        avatar_url = 'https://www.youtube.com/',
        company_id = company_id
    )
    employee_id = sql.get_employee_max_id()
    assert sql.get_company()[-1]["name"] == "ООО Палочка"
    assert sql.get_company()[-1]["description"] == "Доставка деревьев"
    assert sql.get_employee()[-1]["last_name"] == 'Иванов'
    assert sql.get_employee()[-1]["phone"] == '79007653289'
    assert sql.get_employee()[-1]["email"] == 'kratos@example.com'
    assert sql.get_employee()[-1]["avatar_url"] == 'https://www.youtube.com/'
    sql.delete_employee(employee_id)
    sql.delete_company(company_id)

   

