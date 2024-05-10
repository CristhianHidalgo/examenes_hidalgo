
import requests as rq

var_res = rq.get("https://jsonplaceholder.typicode.com/users")

var_json = var_res.json()

# print(var_json)

usuario_6 = var_json[5]
usuario_8 = var_json[7]

usuario_6["nombre"] = "Cristhian"
usuario_6["edad"] = 23

usuario_8["nombre"] = "Jefferson"
usuario_8["edad"] = 28

if usuario_6["edad"] > usuario_8["edad"]:
    print(f"{usuario_6["nombre"]} es mayor que {usuario_8["nombre"]}")
elif usuario_6["edad"] < usuario_8["edad"]:
    print(f"{usuario_8["nombre"]} es mayor que {usuario_6["nombre"]}")
else:
    print(f"{usuario_8["nombre"]} tiene la misma edad que "
          f"{usuario_6["nombre"]}")
