from application.Controllers.EmployeeController import show_employees, get_employee_data
import json


def app(environ, start_response):
    path = environ.get("PATH_INFO")
    print(path)
    if path.endswith("/"):
        path = path[:-1]
    
    # home
    if path == "": # index / root of the web app
        data = show_employees(environ)
        data = data.encode("utf-8")
        # print(type(json.dumps(get_employee_data())))

    # employee data endpoint
    elif path.endswith("/employees"):
        data = json.dumps(get_employee_data()) #convert list to json string
        start_response("200 OK", [
            ("Content-Type", "text/json"),
            ("Content-Length", str(len(data)))
        ])
        return [bytes(data, 'utf-8')]

    # can display a 404
    else:
        data = show_employees(environ)
        data = data.encode("utf-8")
        
    start_response(
        f"200 OK", [
            ("Content-Type", "text/html"),
            ("Content-Length", str(len(data)))
        ]
    )
    return iter([data])

